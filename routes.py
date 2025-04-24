from flask import Blueprint, render_template, request, redirect, url_for, session
from app import db
from models import User, Question, Score

main = Blueprint('main', __name__)
@main.app_context_processor
def inject_score_data():
    user_id = session.get('user_id')
    if not user_id:
        return {}

    user = User.query.get(user_id)
    score_data = Score.query.filter_by(user_id=user.id).first()
    latest_score = score_data.latest_score if score_data else 0
    highest_score = score_data.highest_score if score_data else 0
    top_score = db.session.query(db.func.max(Score.highest_score)).scalar()

    return {
        "latest_score": latest_score,
        "highest_score": highest_score,
        "top_score": top_score
    }

@main.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        if not username:
            return render_template('home.html', error="Kullanıcı adı gerekli!")

        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()

        session['user_id'] = user.id
        return redirect(url_for('main.select_topic'))

    return render_template('home.html')

@main.route('/select_topic', methods=['GET', 'POST'])
def select_topic():
    topics = db.session.query(Question.topic).distinct().all()
    topic_list = [t[0] for t in topics]
    if request.method == 'POST':
        session['topic'] = request.form.get('topic')
        return redirect(url_for('main.quiz'))
    return render_template('select_topic.html', topics=topic_list)

@main.route('/quiz', methods=['GET', 'POST'])
def quiz():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('main.home'))

    topic = session.get('topic')
    if not topic:
        return redirect(url_for('main.home'))

    # Oturumda başlatılmamışsa sıfırla
    if 'question_ids' not in session:
        questions = Question.query.filter_by(topic=topic).all()
        session['question_ids'] = [q.id for q in questions]
        session['question_index'] = 0
        session['score'] = 0

    question_ids = session['question_ids']
    index = session['question_index']

    # Tüm sorular bitti mi?
    if index >= len(question_ids):
        user = User.query.get(user_id)
        score = session['score']

        existing_score = Score.query.filter_by(user_id=user.id).first()
        if existing_score:
            existing_score.latest_score = score
            existing_score.highest_score = max(score, existing_score.highest_score)
        else:
            new_score = Score(user_id=user.id, latest_score=score, highest_score=score)
            db.session.add(new_score)

        db.session.commit()
        session['latest_score'] = score

        # Temizle
        session.pop('question_index')
        session.pop('question_ids')
        session.pop('score')

        return redirect(url_for('main.result'))

    # Şu anki soru
    question = Question.query.get(question_ids[index])
    error = None

    if request.method == 'POST':
        selected = request.form.get('answer')
        if not selected:
            error = "Lütfen soruyu cevaplayınız."
        else:
            if selected == question.correct_option:
                session['score'] += 1
            session['question_index'] += 1
            return redirect(url_for('main.quiz'))

    return render_template('quiz.html', question=question, error=error, index=index + 1, total=len(question_ids))



@main.route('/result')
def result():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('main.home'))

    user = User.query.get(user_id)
    score_data = Score.query.filter_by(user_id=user.id).first()
    latest_score = score_data.latest_score if score_data else 0
    highest_score = score_data.highest_score if score_data else 0
    top_score = db.session.query(db.func.max(Score.highest_score)).scalar()

    return render_template('result.html', latest_score=latest_score, highest_score=highest_score, top_score=top_score)


