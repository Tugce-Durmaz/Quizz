from app import create_app, db
from models import Question

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    questions = [
        Question(
    topic="Python ile sohbet botu otomasyonu",
    question_text="Discord.py kütüphanesi ne için kullanılır?",
    option_a="Veri analizi için",
    option_b="Görselleştirme için",
    option_c="Discord botları geliştirmek için",
    option_d="Web geliştirme için",
    correct_option="C"
),
Question(
    topic="Python ile sohbet botu otomasyonu",
    question_text="Discord botları için hangi kütüphane kullanılır?",
    option_a="Flask",
    option_b="Django",
    option_c="discord.py",
    option_d="requests",
    correct_option="C"
),
Question(
    topic="Python ile sohbet botu otomasyonu",
    question_text="discord.py kütüphanesinde bot komutları hangi decorator ile tanımlanır?",
    option_a="@app.route",
    option_b="@bot.command()",
    option_c="@app.command",
    option_d="@command.run",
    correct_option="B"
),
Question(
    topic="Python ile sohbet botu otomasyonu",
    question_text="Discord botu için kullanıcıdan mesaj almak için hangi fonksiyon kullanılır?",
    option_a="bot.receive()",
    option_b="bot.get_message()",
    option_c="bot.wait_for()",
    option_d="bot.listen()",
    correct_option="C"
),
Question(
    topic="Python ile sohbet botu otomasyonu",
    question_text="Discord botu için token nasıl alınır?",
    option_a="discord.com'dan alınır",
    option_b="bot.start() fonksiyonu ile",
    option_c="Bot oluşturulup token kısmı alınır",
    option_d="Token.py dosyasından",
    correct_option="C"
),

Question(
    topic="Python ile web geliştirme",
    question_text="Flask framework’ü hangi programlama dili ile kullanılır?",
    option_a="Java",
    option_b="Python",
    option_c="C++",
    option_d="JavaScript",
    correct_option="B"
),
Question(
    topic="Python ile web geliştirme",
    question_text="Flask hangi tür uygulamalar için uygundur?",
    option_a="Büyük ölçekli, çok kullanıcıya sahip uygulamalar",
    option_b="Web uygulamaları",
    option_c="Veritabanı yönetim sistemleri",
    option_d="Yapay zeka uygulamaları",
    correct_option="B"
),
Question(
    topic="Python ile web geliştirme",
    question_text="Flask’te hangi dosya, uygulamanın başlatılmasını sağlar?",
    option_a="main.py",
    option_b="app.py",
    option_c="run.py",
    option_d="init.py",
    correct_option="B"
),
Question(
    topic="Python ile web geliştirme",
    question_text="Flask'te veritabanı bağlantısını sağlayan kütüphane nedir?",
    option_a="Pandas",
    option_b="SQLAlchemy",
    option_c="Django ORM",
    option_d="Flask-DB",
    correct_option="B"
),
Question(
    topic="Python ile web geliştirme",
    question_text="Flask ile hangi tipte web sayfaları oluşturulabilir?",
    option_a="Sadece statik sayfalar",
    option_b="Dinamik web sayfaları",
    option_c="Sadece API'ler",
    option_d="Web uygulamaları ve API'ler",
    correct_option="D"
),

Question(
    topic="Python ile yapay zeka geliştirme",
    question_text="Yapay zeka modellerini eğitmek için en çok kullanılan Python kütüphanesi hangisidir?",
    option_a="Flask",
    option_b="NumPy",
    option_c="TensorFlow",
    option_d="Matplotlib",
    correct_option="C"
),
Question(
    topic="Python ile yapay zeka geliştirme",
    question_text="Yapay zeka için hangi kütüphane derin öğrenme ağlarını oluşturmak için kullanılır?",
    option_a="Pandas",
    option_b="TensorFlow",
    option_c="BeautifulSoup",
    option_d="SciPy",
    correct_option="B"
),
Question(
    topic="Python ile yapay zeka geliştirme",
    question_text="Scikit-learn kütüphanesi hangi amaçla kullanılır?",
    option_a="Veri görselleştirme",
    option_b="Yapay zeka eğitimi",
    option_c="İstatistiksel modelleme",
    option_d="Veri temizleme",
    correct_option="B"
),
Question(
    topic="Python ile yapay zeka geliştirme",
    question_text="Yapay zeka için model eğitirken kullanılan 'gradient descent' algoritması neyi optimize eder?",
    option_a="Modelin doğruluğunu",
    option_b="Modelin öğrenme hızını",
    option_c="Modelin parametrelerini",
    option_d="Veri kümesini",
    correct_option="C"
),
Question(
    topic="Python ile yapay zeka geliştirme",
    question_text="Veri ön işleme için hangi Python kütüphanesi yaygın olarak kullanılır?",
    option_a="NumPy",
    option_b="Pandas",
    option_c="TensorFlow",
    option_d="Keras",
    correct_option="B"
),

Question(
    topic="Bilgisayar görüşü",
    question_text="ImageAI kütüphanesi ne için kullanılır?",
    option_a="Ses tanıma için",
    option_b="Görüntü tanıma ve nesne tespiti için",
    option_c="Web geliştirme için",
    option_d="Metin analizi için",
    correct_option="B"
),
Question(
    topic="Bilgisayar görüşü",
    question_text="OpenCV kütüphanesinin en temel kullanımı nedir?",
    option_a="Veri analizi",
    option_b="Metin analizi",
    option_c="Görüntü işleme",
    option_d="Doğal dil işleme",
    correct_option="C"
),
Question(
    topic="Bilgisayar görüşü",
    question_text="OpenCV’de görüntü yüklemek için hangi fonksiyon kullanılır?",
    option_a="load_image()",
    option_b="cv2.imread()",
    option_c="cv2.load()",
    option_d="image.load()",
    correct_option="B"
),
Question(
    topic="Bilgisayar görüşü",
    question_text="Yüz tanıma uygulamaları için en çok hangi kütüphane kullanılır?",
    option_a="PIL",
    option_b="ImageAI",
    option_c="dlib",
    option_d="NumPy",
    correct_option="C"
),
Question(
    topic="Bilgisayar görüşü",
    question_text="Yüz tanıma için hangi yöntem kullanılır?",
    option_a="Hough dönüşümü",
    option_b="Haar Cascade sınıflandırıcıları",
    option_c="Bayes sınıflandırıcıları",
    option_d="Karar ağaçları",
    correct_option="B"
),

Question(
    topic="Doğal Dil İşleme",
    question_text="NLTK kütüphanesi ne işe yarar?",
    option_a="Veritabanı yönetimi",
    option_b="Web sunucusu başlatma",
    option_c="Doğal dil işleme görevleri",
    option_d="Grafik oluşturma",
    correct_option="C"
),
Question(
    topic="Doğal Dil İşleme",
    question_text="Hangi kütüphane doğal dil işleme (NLP) için yaygın olarak kullanılır?",
    option_a="NumPy",
    option_b="NLTK",
    option_c="TensorFlow",
    option_d="Pandas",
    correct_option="B"
),
Question(
    topic="Doğal Dil İşleme",
    question_text="NLTK'nin temel bileşenlerinden biri nedir?",
    option_a="Veri analizi araçları",
    option_b="Görüntü işleme araçları",
    option_c="Tokenization",
    option_d="Veritabanı yönetim araçları",
    correct_option="C"
),
Question(
    topic="Doğal Dil İşleme",
    question_text="Doğal dil işleme için hangi algoritma en yaygın kullanılanlardan biridir?",
    option_a="Gömülü dil modeli",
    option_b="Regresyon analizi",
    option_c="Nöral ağlar",
    option_d="Bağımlı sınıflandırıcılar",
    correct_option="C"
),
Question(
    topic="Doğal Dil İşleme",
    question_text="Tokenization işlemi nedir?",
    option_a="Metni sayısal verilere dönüştürme",
    option_b="Metni bölme ve kelimeleri ayrıştırma",
    option_c="Metni grafiklere dönüştürme",
    option_d="Veritabanı oluşturma",
    correct_option="B"
),
]


    db.session.bulk_save_objects(questions)
    db.session.commit()
    print("Veriler başarıyla eklendi!")

