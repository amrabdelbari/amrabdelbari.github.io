"""Work experience, certificates and skills, in English, Arabic and Turkish.
Dates are (year, month); end=None means the role is ongoing."""

NOW = (2026, 11)

# track: acad | ind | teach | early
ROLES = [
    dict(start=(2025, 9), end=None, track="acad", tags=["Leadership", "Curriculum", "AI & Informatics"],
         en=("Head of Information Systems Engineering Department", "Near East University", "Nicosia",
             ["Leading the department, and part of the effort to establish the new Faculty of AI and Informatics.",
              "First appointed to the Data Analytics Department (Feb 2025), then moved to Information Systems to match my focus on AI applications, robotics and systems."]),
         ar=("رئيس قسم هندسة نظم المعلومات", "جامعة الشرق الأدنى", "نيقوسيا",
             ["قيادة القسم، والمشاركة في تأسيس كلية الذكاء الاصطناعي والمعلوماتية الجديدة.",
              "عُيّنت أولًا في قسم تحليل البيانات (فبراير 2025)، ثم انتقلت إلى نظم المعلومات بما يتوافق مع تخصصي في تطبيقات الذكاء الاصطناعي والروبوتات والأنظمة."]),
         tr=("Bilişim Sistemleri Mühendisliği Bölüm Başkanı", "Yakın Doğu Üniversitesi", "Lefkoşa",
             ["Bölümü yönetiyor ve yeni Yapay Zekâ ve Bilişim Fakültesi'nin kuruluş çalışmalarında yer alıyorum.",
              "Önce Veri Analitiği Bölümü'ne atandım (Şubat 2025), ardından yapay zekâ uygulamaları, robotik ve sistemler odağıma uygun olarak Bilişim Sistemleri'ne geçtim."])),
    dict(start=(2024, 9), end=None, track="acad", tags=["Wireless", "NOMA", "OTFS", "GenAI"],
         en=("Assistant Professor", "Near East University", "Nicosia",
             ["Mentor real-world student projects in AI and software engineering, such as AI for cybersecurity, a calorie-counting app and an AI chess game.",
              "Research the mathematical analysis of modulation and multiple access: 64-QAM, NOMA, OTFS and Massive MIMO.",
              "Teach students to apply generative AI to robotics, logic design, speech processing and software testing."]),
         ar=("أستاذ مساعد", "جامعة الشرق الأدنى", "نيقوسيا",
             ["الإشراف على مشاريع طلابية واقعية في الذكاء الاصطناعي وهندسة البرمجيات، مثل الذكاء الاصطناعي للأمن السيبراني، وتطبيق لحساب السعرات، ولعبة شطرنج بالذكاء الاصطناعي.",
              "البحث في التحليل الرياضي لتقنيات التضمين والنفاذ المتعدد: 64-QAM وNOMA وOTFS وMassive MIMO.",
              "تعليم الطلاب توظيف الذكاء الاصطناعي التوليدي في الروبوتات وتصميم الدوائر المنطقية ومعالجة الكلام واختبار البرمجيات."]),
         tr=("Dr. Öğretim Üyesi", "Yakın Doğu Üniversitesi", "Lefkoşa",
             ["Yapay zekâ ve yazılım mühendisliğinde gerçek dünya öğrenci projelerine mentorluk: siber güvenlikte yapay zekâ, kalori sayma uygulaması, yapay zekâlı satranç oyunu gibi.",
              "Modülasyon ve çoklu erişim tekniklerinin matematiksel analizi üzerine araştırma: 64-QAM, NOMA, OTFS ve Massive MIMO.",
              "Öğrencilere üretken yapay zekâyı robotik, lojik tasarım, konuşma işleme ve yazılım testinde kullanmayı öğretiyorum."])),
    dict(start=(2023, 7), end=(2024, 10), track="ind", tags=["ESP32", "NVIDIA Jetson", "Firmware", "Architecture"],
         en=("Head of Software Engineering", "RoboLabs", "Istanbul",
             ["Led firmware for the robot subsystems (ESP) and the main controllers (NVIDIA Jetson).",
              "Owned the software architecture and system design, managed the team's workload, and coordinated with the hardware and other departments."]),
         ar=("رئيس هندسة البرمجيات", "RoboLabs", "إسطنبول",
             ["قيادة تطوير البرمجيات الثابتة للأنظمة الفرعية للروبوت (ESP) ووحدات التحكم الرئيسية (NVIDIA Jetson).",
              "مسؤول عن معمارية البرمجيات وتصميم النظام، وإدارة عبء عمل الفريق، والتنسيق مع فريق العتاد والأقسام الأخرى."]),
         tr=("Yazılım Mühendisliği Müdürü", "RoboLabs", "İstanbul",
             ["Robot alt sistemleri (ESP) ve ana kontrolcüler (NVIDIA Jetson) için gömülü yazılım geliştirmeyi yönettim.",
              "Yazılım mimarisinden ve sistem tasarımından sorumluydum; ekibin iş yükünü yönetip donanım ve diğer departmanlarla koordinasyon sağladım."])),
    dict(start=(2023, 9), end=(2024, 8), track="acad", tags=["Programming", "Algorithms", "AI agents"],
         en=("Lecturer", "Near East University", "Nicosia",
             ["Taught programming, object-oriented programming, algorithms, and AI agents and reasoning in the AI Engineering Department and the AI and Robotics Institute.",
              "Taught software requirements to graduate students, and researched AI for wireless communications, signal processing, robotics and financial markets."]),
         ar=("محاضر", "جامعة الشرق الأدنى", "نيقوسيا",
             ["تدريس البرمجة، والبرمجة كائنية التوجه، والخوارزميات، والوكلاء الأذكياء والاستدلال في قسم هندسة الذكاء الاصطناعي ومعهد الذكاء الاصطناعي والروبوتات.",
              "تدريس متطلبات البرمجيات لطلاب الدراسات العليا، والبحث في تطبيقات الذكاء الاصطناعي في الاتصالات اللاسلكية ومعالجة الإشارات والروبوتات والأسواق المالية."]),
         tr=("Öğretim Görevlisi", "Yakın Doğu Üniversitesi", "Lefkoşa",
             ["Yapay Zekâ Mühendisliği Bölümü ile Yapay Zekâ ve Robotik Enstitüsü'nde programlama, nesne yönelimli programlama, algoritmalar ve yapay zekâ ajanları ve akıl yürütme dersleri verdim.",
              "Lisansüstü öğrencilere yazılım gereksinimleri dersi verdim; kablosuz haberleşme, sinyal işleme, robotik ve finansal piyasalarda yapay zekâ üzerine araştırma yaptım."])),
    dict(start=(2022, 7), end=(2023, 6), track="ind", tags=["Robotics", "Control", "Embedded", "UV-C"],
         en=("Software Engineer", "RoboLabs", "Istanbul",
             ["Built the control software for C-bot UV-C disinfection robots, with autonomous, manual, timed and QR-following modes.",
              "Worked across the battery, UV-C and motion subsystems, and fixed control and communication design problems."]),
         ar=("مهندس برمجيات", "RoboLabs", "إسطنبول",
             ["تطوير برمجيات التحكم لروبوتات التعقيم C-bot بالأشعة فوق البنفسجية، بأنماط ذاتية ويدوية ومؤقتة وتتبّع رموز QR.",
              "العمل على أنظمة البطارية والأشعة فوق البنفسجية والحركة، وحل مشكلات في تصميم التحكم والاتصال."]),
         tr=("Yazılım Mühendisi", "RoboLabs", "İstanbul",
             ["C-bot UV-C dezenfeksiyon robotlarının kontrol yazılımını geliştirdim: otonom, manuel, zamanlı ve QR takip modları.",
              "Batarya, UV-C ve hareket alt sistemlerinde çalıştım; kontrol ve haberleşme tasarım sorunlarını çözdüm."])),
    dict(start=(2022, 3), end=None, track="teach", tags=["Electronics", "Signals", "Wireless", "Online"],
         en=("Online Lecturer", "Course Khana", "Istanbul · remote",
             ["Teach undergraduate electrical, electronic and computer engineering: Electronics I and II, Signal Processing, Wireless Communications, Digital System Design and Communication Circuits.",
              "Run live classes on Zoom with digital whiteboards."]),
         ar=("محاضر عبر الإنترنت", "Course Khana", "إسطنبول · عن بُعد",
             ["تدريس مقررات الهندسة الكهربائية والإلكترونية وهندسة الحاسوب للمرحلة الجامعية: الإلكترونيات 1 و2، ومعالجة الإشارات، والاتصالات اللاسلكية، وتصميم الأنظمة الرقمية، ودوائر الاتصالات.",
              "تقديم محاضرات مباشرة عبر Zoom باستخدام السبورات الرقمية."]),
         tr=("Çevrim İçi Eğitmen", "Course Khana", "İstanbul · uzaktan",
             ["Lisans düzeyinde elektrik, elektronik ve bilgisayar mühendisliği dersleri veriyorum: Elektronik I ve II, Sinyal İşleme, Kablosuz Haberleşme, Sayısal Sistem Tasarımı ve Haberleşme Devreleri.",
              "Dersleri Zoom üzerinden dijital tahtalarla canlı yürütüyorum."])),
    dict(start=(2021, 9), end=(2022, 10), track="ind", tags=["Python", "C/C++", "MATLAB", "Quant"],
         en=("Co-founder & Quantitative Developer", "Oxyinance Technologies", "Istanbul",
             ["Built automated trading systems for stocks, FX and crypto, driven by mathematical and AI models.",
              "Designed fundamental and technical strategies and implemented them in Python, C/C++ and MATLAB."]),
         ar=("شريك مؤسس ومطوّر كمّي", "Oxyinance Technologies", "إسطنبول",
             ["بناء أنظمة تداول آلية للأسهم والعملات الأجنبية والعملات المشفرة، تعتمد على نماذج رياضية ونماذج ذكاء اصطناعي.",
              "تصميم استراتيجيات أساسية وفنية وتنفيذها بلغات Python وC/C++ وMATLAB."]),
         tr=("Kurucu Ortak ve Kantitatif Geliştirici", "Oxyinance Technologies", "İstanbul",
             ["Hisse senedi, döviz ve kripto için matematiksel ve yapay zekâ modellerine dayalı otomatik alım satım sistemleri geliştirdim.",
              "Temel ve teknik stratejiler tasarlayıp Python, C/C++ ve MATLAB ile uyguladım."])),
    dict(start=(2019, 2), end=(2021, 8), track="acad", tags=["DOA", "Array processing", "NOMA", "MIMO"],
         en=("Research Assistant", "Near East University", "Nicosia",
             ["Taught undergraduate courses and labs in electronics, AI, signal processing and computer vision.",
              "Researched array signal processing, DOA estimation, NOMA and MIMO, publishing in IEEE and Springer venues.",
              "Reviewed MSc and PhD theses, and built the university's official LaTeX thesis template."]),
         ar=("مساعد باحث", "جامعة الشرق الأدنى", "نيقوسيا",
             ["تدريس مقررات ومعامل جامعية في الإلكترونيات والذكاء الاصطناعي ومعالجة الإشارات والرؤية الحاسوبية.",
              "البحث في معالجة إشارات المصفوفات وتقدير اتجاه الوصول وNOMA وMIMO، مع النشر في منصات IEEE وSpringer.",
              "مراجعة رسائل الماجستير والدكتوراه، وإعداد قالب LaTeX الرسمي للرسائل الجامعية في الجامعة."]),
         tr=("Araştırma Görevlisi", "Yakın Doğu Üniversitesi", "Lefkoşa",
             ["Elektronik, yapay zekâ, sinyal işleme ve bilgisayarlı görü alanlarında lisans dersleri ve laboratuvarları yürüttüm.",
              "Dizi sinyal işleme, DOA kestirimi, NOMA ve MIMO üzerine araştırma yaptım; IEEE ve Springer yayınları çıkardım.",
              "Yüksek lisans ve doktora tezlerini inceledim; üniversitenin resmî LaTeX tez şablonunu hazırladım."])),
    dict(start=(2015, 7), end=(2015, 8), track="early", tags=["Site engineering"],
         en=("Electrical Engineer", "Construction project", "Doha, Qatar",
             ["Managed the electrical works from civil and electrical drawings, supervising three teams of workers."]),
         ar=("مهندس كهرباء", "مشروع إنشائي", "الدوحة، قطر",
             ["إدارة الأعمال الكهربائية وفق المخططات المدنية والكهربائية، والإشراف على ثلاثة فرق عمل."]),
         tr=("Elektrik Mühendisi", "İnşaat projesi", "Doha, Katar",
             ["İnşaat ve elektrik projelerine göre elektrik işlerini yönettim; üç işçi ekibini denetledim."])),
    dict(start=(2010, 7), end=(2011, 2), track="early", tags=["Web", "ICDL"],
         en=("Web Designer & ICDL Examiner", "Synergy Sohag Center", "Sohag, Egypt",
             ["Designed and built the websites of a training centre for business development, Microsoft Office and programming.",
              "Official ICDL examiner under a Ministry of Education contract."]),
         ar=("مصمم مواقع وممتحن ICDL", "مركز سينرجي سوهاج", "سوهاج، مصر",
             ["تصميم وبرمجة مواقع مركز تدريب في تطوير الأعمال وMicrosoft Office والبرمجة.",
              "ممتحن ICDL رسمي ضمن عقد مع وزارة التربية والتعليم."]),
         tr=("Web Tasarımcısı ve ICDL Sınav Görevlisi", "Synergy Sohag Center", "Sohag, Mısır",
             ["İş geliştirme, Microsoft Office ve programlama eğitimleri veren bir merkezin web sitelerini tasarlayıp geliştirdim.",
              "Millî Eğitim Bakanlığı sözleşmesi kapsamında resmî ICDL sınav görevlisiydim."])),
]

CERTS = [
    ("2025", "AI Product Manager", "IBM"),
    ("2025", "AI Product Manager", "Microsoft"),
    ("2025", "FPGA Softcore Processors and IP Acquisition", "University of Colorado Boulder"),
    ("2025", "Hardware Description Languages for FPGA Design", "University of Colorado Boulder"),
    ("2024", "Google AI Essentials", "Google"),
    ("2023", "ROS 2 Nav2 with SLAM and Navigation", "Udemy"),
    ("2023", "ROS 2 for Beginners (Foxy, Humble)", "Udemy"),
]

SKILLS = [("Python", 5), ("MATLAB", 5), ("ROS 2", 4), ("VHDL", 4), ("C++", 3)]

TEXT = {
    "en": dict(
        nav="Experience", title="Experience", sub="16 years across academia, industry and teaching",
        tracks={"all": "All", "acad": "Academia", "ind": "Industry", "teach": "Teaching", "early": "Early career"},
        present="Present",
        months="Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(),
        summary=[("2010", "first job, in Sohag"), ("7+", "years teaching at university level"),
                 ("3+", "years in industry R&D"), ("2", "engineering teams led or co-founded")],
        certs="Certificates", skills="Skills", langs="Languages",
        skill_levels={5: "expert", 4: "skilled", 3: "experienced"},
        languages=[("Arabic", "native"), ("English", "fluent"), ("Turkish", "elementary")],
    ),
    "ar": dict(
        nav="الخبرات", title="الخبرات العملية", sub="16 عامًا بين الأكاديميا والصناعة والتدريس",
        tracks={"all": "الكل", "acad": "أكاديمي", "ind": "صناعي", "teach": "تدريس", "early": "بداية المسيرة"},
        present="حتى الآن",
        months="يناير فبراير مارس أبريل مايو يونيو يوليو أغسطس سبتمبر أكتوبر نوفمبر ديسمبر".split(),
        summary=[("2010", "أول وظيفة، في سوهاج"), ("7+", "سنوات من التدريس الجامعي"),
                 ("3+", "سنوات في البحث والتطوير الصناعي"), ("2", "فريقان هندسيان قدتهما أو شاركت في تأسيسهما")],
        certs="الشهادات", skills="المهارات", langs="اللغات",
        skill_levels={5: "خبير", 4: "متمكّن", 3: "متمرّس"},
        languages=[("العربية", "اللغة الأم"), ("الإنجليزية", "بطلاقة"), ("التركية", "مستوى مبتدئ")],
    ),
    "tr": dict(
        nav="Deneyim", title="İş deneyimi", sub="Akademi, sanayi ve eğitimde 16 yıl",
        tracks={"all": "Tümü", "acad": "Akademi", "ind": "Sanayi", "teach": "Eğitmenlik", "early": "Kariyer başı"},
        present="Halen",
        months="Oca Şub Mar Nis May Haz Tem Ağu Eyl Eki Kas Ara".split(),
        summary=[("2010", "ilk iş, Sohag'da"), ("7+", "yıl üniversite düzeyinde eğitim"),
                 ("3+", "yıl sanayide Ar-Ge"), ("2", "yönettiğim ya da kurduğum mühendislik ekibi")],
        certs="Sertifikalar", skills="Beceriler", langs="Diller",
        skill_levels={5: "uzman", 4: "yetkin", 3: "deneyimli"},
        languages=[("Arapça", "ana dil"), ("İngilizce", "akıcı"), ("Türkçe", "başlangıç")],
    ),
}


def duration(code, start, end):
    end = end or NOW
    n = (end[0] - start[0]) * 12 + (end[1] - start[1]) + 1
    y, m = divmod(n, 12)
    if code == "en":
        parts = ([f"{y} yr" + ("s" if y > 1 else "")] if y else []) + ([f"{m} mo" + ("s" if m > 1 else "")] if m else [])
        return " ".join(parts)
    if code == "tr":
        return " ".join(([f"{y} yıl"] if y else []) + ([f"{m} ay"] if m else []))
    def ar_years(k):
        return {1: "سنة", 2: "سنتان"}.get(k, f"{k} سنوات")
    def ar_months(k):
        return {1: "شهر", 2: "شهران"}.get(k, f"{k} أشهر" if k <= 10 else f"{k} شهرًا")
    return " و".join(([ar_years(y)] if y else []) + ([ar_months(m)] if m else []))


def date_range(code, start, end):
    T = TEXT[code]
    f = lambda d: f"{T['months'][d[1]-1]} {d[0]}"
    return f"{f(start)} – {f(end) if end else T['present']}"
