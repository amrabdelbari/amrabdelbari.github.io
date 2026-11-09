# Site text in English, Arabic and Turkish. Paper titles and venues stay in English (in build.py).

_GH = "https://github.com/amro2021/"

def _cards(t):
    """t: dict of per-language strings for the six project cards."""
    return [
        dict(art="radar", title=t["pcl_t"], pill=t["research"], pillc="warn", p=t["pcl_p"], tags=["SDR", "FPGA", "DSP", "ADS-B"]),
        dict(art="qr", title="QR Lab", pill=t["live"], pillc="good", p=t["qr_p"], tags=["JavaScript", "WebCrypto", "Capacitor"],
             links=[(t["open"], "https://amro2021.github.io/qr-transfer/"), (t["code"], _GH + "qr-transfer")]),
        dict(art="p2p", title="MDANetwork", pill=t["prototype"], pillc="acc", p=t["mda_p"], tags=["Python", "P2P", "NAT traversal"],
             links=[(t["code"], _GH + "MDANetPro")]),
        dict(art="track", title="FlyDetectandTrack", pill=t["vision"], pillc="", p=t["fly_p"], tags=["OpenCV", "Kalman", "Tracking"],
             links=[(t["code"], _GH + "FlyDetectandTrack")]),
        dict(art="npu", title=t["npu_t"], pill=t["design"], pillc="warn", p=t["npu_p"], tags=["Verilog", "Nios V", t["quant"]]),
        dict(art="ecg", title="HomecareBot", pill=t["bot"], pillc="", p=t["home_p"], tags=["Python", "Telegram API"],
             links=[(t["code"], _GH + "HomecareBot")]),
    ]


EN = dict(
    lang_label="EN", dir="ltr",
    name="Amr Abdelbari", fullname="Dr. Amr Abdelbari", initials="AA",
    title="Amr Abdelbari — UAV simulation, radar & wireless systems",
    description="Dr. Amr Abdelbari — Assistant Professor and Head of Information Systems Engineering at Near East University, Nicosia, Cyprus. UAV competition simulation, passive radar, NOMA/MIMO wireless research.",
    og_desc="Builder of the Virtual UAV Engagement Arena: ArduPilot SITL, referee engine, 100-team scale, radar & EW league.",
    otw="open to work", otw_title="Open to roles in robotics, UAV simulation and defence software",
    nav_arena="UAV Arena", nav_projects="Projects", nav_research="Research", nav_about="About", nav_contact="Contact",
    kicker="Engineer · Educator · Nicosia, Cyprus",
    h1="I build systems that <span>fly, sense and score</span> themselves.",
    lede="Assistant Professor and <strong>Head of Information Systems Engineering</strong> at Near East University, with an electrical-engineering background. "
         "I build <strong>UAV competition simulators</strong> on real autopilots, <strong>passive radar</strong> from SDR and FPGA hardware, "
         "and research <strong>NOMA / MIMO</strong> wireless links.",
    cta_arena="See the UAV Arena →", cta_research="Publications",
    arena_aria="Live arena simulation", arena_live="Arena · live", running="RUNNING",
    arena_title="Virtual UAV Engagement Arena", arena_sub="Flagship project · 2026",
    arena_h3="A virtual Fighting UAV competition, run on real ArduPilot autopilots.",
    arena_p="A competition platform for fixed-wing UAV teams, modelled on the TEKNOFEST Fighting UAV format. "
            "Teams score by holding an opponent in their camera's hit zone, finishing a QR dive task, avoiding penalties "
            "and landing safely. Every aircraft is a real <b>ArduPlane SITL</b> autopilot, flown by the team's own code or by "
            "hand from a <b>3D browser cockpit</b>, and an <b>automatic referee</b> scores every match from ground truth. "
            "Guests watch in 3D from one link.",
    feats=[
        "<b>Referee engine</b>: lock-on validation (≥ 4 s window, ≥ 90 % in-zone, no gap &gt; 0.3 s), geofence, telemetry watchdog, false-claim and collision penalties, warn / freeze / eject.",
        "<b>Four rulebooks</b>: standard, TEKNOFEST mode, a defence scenario, and a standalone league.",
        "<b>League mode</b>: fog of war, ground radar, hidden SAM sites, GPS and comms jamming, on-board ECM, and an unattended season runner that publishes standings and 3D replays.",
        "<b>Per-aircraft camera images</b> streamed to each team, with recorded evidence clips for every lock-on review.",
        "<b>Fair play</b>: per-team tokens, rate limits, server-side time, and an isolated MAVLink port for each team.",
        "<b>Multi-autopilot</b>: ArduPilot and PX4 airframes, homologated before a match, spread across several computers.",
    ],
    stats=[
        ("100", "teams in one match: about twice the last TEKNOFEST final (42)"),
        ("2.7 ms", "per referee tick for 100 aircraft (all 9,900 camera/target pairs) against a 50 ms budget"),
        ("~12k", "lines of Python: server, referee, starter teams, scripts and tests"),
        ("5 Hz", "telemetry from every team, each reply carrying all the other aircraft"),
    ],
    rehearsal="Rehearsal results · 25 Oct 2026", th_setup="Setup", th_outcome="Outcome",
    rows=[
        ("1", "Two identical hunters", "Collided at 23.7 s, both out"),
        ("3", "Hunter vs patrol, 10 min", "11 valid locks; final score 135 – 3"),
        ("4", "Fly-out vs false-claim team", "Ejected after 30 s / after 5 false claims"),
        ("5", "Telemetry dropped at 60 s", "Warned at 5 s, ejected at 30 s"),
        ("6", "ArduPlane SITL, 3 runs", "Valid locks every run; staggered landings fixed approach collisions"),
    ],
    lessons=[
        ("The first merge is the most dangerous moment", "With identical code, both aircraft pointed at each other within 20 s of take-off. Teams need a deconfliction rule before they need a lock-on algorithm."),
        ("Equal aircraft circle forever", "Points come from asymmetry: slowing down to out-turn (ω = g·tan φ / V), using altitude, or extending and re-engaging."),
        ("Evasion is worth as much as attack", "A predictable target gave up 11 locks in 10 minutes. Being locked costs −2, against +10 for the attacker."),
    ],
    proj_title="More projects", proj_sub="Hardware, signals and software",
    cards=_cards(dict(
        research="research", live="live", prototype="prototype", vision="vision", design="in design", bot="bot",
        open="Open", code="Code", quant="Quantisation",
        pcl_t="Passive FM radar (PCL)",
        pcl_p="A passive coherent location system that detects aircraft using FM broadcast stations as illuminators. It uses RTL-SDR receivers, a DE10-Lite FPGA, cross-ambiguity processing with direct-path cancellation in Python, and ADS-B ground truth for validation. Next step: a coherent multi-channel array.",
        qr_p="Screen-to-camera communication between phones: fountain-coded file transfer, colour and spatial multiplexing, a NOMA-style layered broadcast with SIC, encrypted per-group quizzes, and end-to-end encrypted QR chat (ECDH + AES-GCM). It also ships as an offline Android app, and was field-tested with 20+ students.",
        mda_p="A true peer-to-peer networking and chat system: nodes talk directly, with no central relay, across different networks. It runs on desktop and web, and a native Kotlin Android client is planned.",
        fly_p="Live insect tracking with persistent IDs, using OpenCV detection, a Kalman filter per track and Hungarian assignment on IoU. It draws fading motion trails and a live HUD.",
        npu_t="FPGA NPU (DE10-Lite)",
        npu_p="An educational INT8 systolic-array accelerator on a MAX 10 FPGA with a Nios V soft core, benchmarking quantised LeNet/MNIST inference against software.",
        home_p="A Telegram assistant that supports patients recovering at home after open-heart surgery, with symptom-monitoring alerts and care guidance.",
    )),
    res_title="Research", res_sub="Signal processing · DOA estimation · Massive MIMO · NOMA · 5G scheduling",
    neu_page="NEU staff page",
    pub_journal="Journal articles", pub_conf="Conference papers", pub_thesis="Theses", pub_prep="In preparation and ongoing",
    thesis_phd="PhD thesis, Electrical and Electronics Engineering, Near East University",
    thesis_msc="MSc thesis, Electrical and Electronics Engineering, Near East University",
    prep=[
        ("In preparation", "MIMO-NOMA power allocation and symbolic detection", "With F. Al-Turjman. For IntechOpen's AI, Computer Science and Robotics Technology journal."),
        ("In preparation", "Probability of error for NOMA in Rayleigh fading for IoT in civil engineering", "With B. Bilgehan and F. Al-Turjman."),
        ("In preparation", "A unified BER derivation for BPSK, 16-QAM and 64-QAM", "With B. Bilgehan and F. Al-Turjman."),
        ("Ongoing", "Distributed passive coherent location", "Multi-node FM passive radar for aircraft detection: bistatic geometry, CAF processing, and ADS-B validated detection statistics."),
    ],
    about_title="About", bg_title="Background",
    bg='<p style="margin-top:0">I\'m an electrical engineer turned systems builder. I am Assistant Professor and Head of the Information Systems Engineering Department at Near East University in Nicosia, Cyprus, where I split my time between teaching, research and department leadership. Before that I was Head of Software Engineering at RoboLabs, building embedded systems and ROS 2 control architectures for autonomous robots.</p>'
       '<p>My work sits where <b>software, signals and autonomy</b> meet: autopilot-in-the-loop simulation, radar signal processing, wireless link analysis, and tools I can put in front of a real classroom the next morning.</p>'
       '<p style="margin-bottom:0">I\'m looking for engineering roles in <b>robotics, UAV and simulation, and defence software</b>.</p>',
    edu_title="Education",
    edu=[("2021", "PhD, Electrical and Electronics Engineering, Near East University"),
         ("2018", "MSc, Electrical and Electronics Engineering, Near East University"),
         ("2014", "BSc, Electrical and Electronics Engineering, Sohag University, Egypt")],
    teach_title="Teaching · Fall 2026",
    courses=[
        ("AIE401", "Introduction to Robotics: simulation-first robotics for 4th-year AI students"),
        ("AII452", "AI Applications: real-world projects for 4th-year students"),
        ("AII020", "System Analysis and Design: design and agile practice"),
        ("AII108", "Object-Oriented Programming in Python"),
        ("—", "Engineering Ethics: dual-use and safety-critical case studies"),
    ],
    footer_loc="Nicosia, Cyprus", email="Email",
    arena_js=dict(start="Match started · 4 teams airborne", lock="{a} lock on {b}  +10", attack="attack", evade="evade"),
)


AR = dict(
    lang_label="عربي", dir="rtl",
    name="عمرو عبد الباري", fullname="د. عمرو عبد الباري", initials="ع",
    title="عمرو عبد الباري — محاكاة الطائرات المسيّرة والرادار والأنظمة اللاسلكية",
    description="د. عمرو عبد الباري — أستاذ مساعد ورئيس قسم هندسة نظم المعلومات في جامعة الشرق الأدنى، نيقوسيا، قبرص. محاكاة مسابقات الطائرات المسيّرة، الرادار السلبي، وأبحاث الاتصالات اللاسلكية NOMA/MIMO.",
    og_desc="مطوّر ساحة الاشتباك الافتراضية للطائرات المسيّرة: ArduPilot SITL، محرّك تحكيم آلي، 100 فريق في مباراة واحدة، ودوري للرادار والحرب الإلكترونية.",
    otw="متاح للعمل", otw_title="متاح لوظائف في الروبوتات ومحاكاة الطائرات المسيّرة وبرمجيات الدفاع",
    nav_arena="ساحة المسيّرات", nav_projects="المشاريع", nav_research="الأبحاث", nav_about="نبذة", nav_contact="تواصل",
    kicker="مهندس · أكاديمي · نيقوسيا، قبرص",
    h1="أبني أنظمة <span>تطير وتستشعر وتُقيّم</span> نفسها بنفسها.",
    lede="أستاذ مساعد و<strong>رئيس قسم هندسة نظم المعلومات</strong> في جامعة الشرق الأدنى، بخلفية في الهندسة الكهربائية. "
         "أطوّر <strong>محاكيات لمسابقات الطائرات المسيّرة</strong> تعمل على طيارات آلية حقيقية، و<strong>رادارًا سلبيًا</strong> باستخدام أجهزة SDR وFPGA، "
         "وأبحث في روابط الاتصال اللاسلكي <strong>NOMA / MIMO</strong>.",
    cta_arena="← شاهد ساحة المسيّرات", cta_research="المنشورات",
    arena_aria="محاكاة حيّة للساحة", arena_live="الساحة · مباشر", running="قيد التشغيل",
    arena_title="ساحة الاشتباك الافتراضية للطائرات المسيّرة", arena_sub="المشروع الرئيسي · 2026",
    arena_h3="مسابقة افتراضية لقتال الطائرات المسيّرة، تعمل على طيارات ArduPilot آلية حقيقية.",
    arena_p="منصّة مسابقات لفرق الطائرات المسيّرة ثابتة الجناح، مبنية على نموذج مسابقة «Savaşan İHA» في مهرجان تكنوفست (TEKNOFEST). "
            "تحصد الفرق النقاط بإبقاء الخصم داخل منطقة الإصابة في كاميرتها، وإنجاز مهمة الانقضاض على رمز QR، وتجنّب المخالفات، "
            "والهبوط الآمن. كل طائرة هي طيار آلي حقيقي <b>ArduPlane SITL</b>، يقودها كود الفريق نفسه أو يقودها يدويًا من "
            "<b>قمرة قيادة ثلاثية الأبعاد في المتصفح</b>، ويقوم <b>حَكَم آلي</b> باحتساب نتيجة كل مباراة من البيانات الفعلية. "
            "ويتابع الضيوف المباراة بالأبعاد الثلاثية عبر رابط واحد.",
    feats=[
        "<b>محرّك التحكيم</b>: التحقق من الإقفال على الهدف (نافذة ≥ 4 ثوانٍ، ≥ 90% داخل المنطقة، دون انقطاع &gt; 0.3 ثانية)، سياج جغرافي، مراقبة انقطاع البيانات، عقوبات الادعاء الكاذب والتصادم، ثم إنذار / تجميد / إقصاء.",
        "<b>أربع لوائح قواعد</b>: القياسية، ونمط TEKNOFEST، وسيناريو دفاعي، ودوري مستقل.",
        "<b>نمط الدوري</b>: ضباب الحرب، رادار أرضي، مواقع صواريخ أرض-جو مخفية، تشويش على GPS والاتصالات، إجراءات إلكترونية مضادة على متن الطائرة، ومشغّل موسم آلي ينشر الترتيب وإعادات ثلاثية الأبعاد.",
        "<b>صور كاميرا لكل طائرة</b> تُبثّ إلى كل فريق، مع مقاطع أدلّة مسجّلة لمراجعة كل عملية إقفال.",
        "<b>اللعب النظيف</b>: رموز دخول لكل فريق، وحدود للطلبات، وتوقيت من جهة الخادم، ومنفذ MAVLink معزول لكل فريق.",
        "<b>تعدد الطيارات الآلية</b>: طائرات ArduPilot وPX4 تُعتمد قبل المباراة، وتتوزع على عدة حواسيب.",
    ],
    stats=[
        ("100", "فريق في مباراة واحدة: نحو ضعف نهائي TEKNOFEST الأخير (42)"),
        ("2.7 ms", "لكل دورة تحكيم مع 100 طائرة (جميع أزواج الكاميرا/الهدف البالغة 9,900) مقابل ميزانية 50 ms"),
        ("~12k", "سطر Python: الخادم، والحَكَم، والفرق التجريبية، والسكربتات، والاختبارات"),
        ("5 Hz", "بيانات طيران من كل فريق، وكل رد يحمل مواقع جميع الطائرات الأخرى"),
    ],
    rehearsal="نتائج التجارب · 25 أكتوبر 2026", th_setup="الإعداد", th_outcome="النتيجة",
    rows=[
        ("1", "صيّادان متطابقان", "تصادما عند 23.7 ثانية، وخرج كلاهما"),
        ("3", "صيّاد مقابل دورية، 10 دقائق", "11 إقفالًا صحيحًا؛ النتيجة النهائية 135 – 3"),
        ("4", "فريق يخرج من السياج مقابل فريق يدّعي كذبًا", "إقصاء بعد 30 ثانية / بعد 5 ادعاءات كاذبة"),
        ("5", "انقطاع البيانات عند 60 ثانية", "إنذار عند 5 ثوانٍ، وإقصاء عند 30 ثانية"),
        ("6", "ArduPlane SITL، ثلاث جولات", "إقفالات صحيحة في كل جولة؛ وحلّ الهبوط المتدرّج مشكلة التصادم أثناء الاقتراب"),
    ],
    lessons=[
        ("أول التقاء هو أخطر لحظة", "مع كود متطابق، اتجهت الطائرتان نحو بعضهما خلال 20 ثانية من الإقلاع. تحتاج الفرق إلى قاعدة لتجنّب التصادم قبل خوارزمية الإقفال."),
        ("الطائرات المتكافئة تدور إلى الأبد", "النقاط تأتي من عدم التماثل: الإبطاء للالتفاف بشكل أضيق (ω = g·tan φ / V)، أو استغلال الارتفاع، أو الابتعاد ثم العودة للاشتباك."),
        ("المراوغة تساوي الهجوم قيمةً", "هدف يمكن التنبؤ بحركته تعرّض لـ 11 إقفالًا في 10 دقائق. الإقفال عليك يكلّف −2، مقابل +10 للمهاجم."),
    ],
    proj_title="مشاريع أخرى", proj_sub="عتاد، وإشارات، وبرمجيات",
    cards=_cards(dict(
        research="بحث", live="منشور", prototype="نموذج أولي", vision="رؤية حاسوبية", design="قيد التصميم", bot="بوت",
        open="فتح", code="الكود", quant="التكميم",
        pcl_t="رادار FM سلبي (PCL)",
        pcl_p="نظام تحديد موقع متماسك سلبي يكشف الطائرات باستخدام محطات البث FM كمصادر إضاءة. يستخدم مستقبلات RTL-SDR، ولوحة FPGA من نوع DE10-Lite، ومعالجة الالتباس المتقاطع مع إلغاء المسار المباشر بلغة Python، وبيانات ADS-B كمرجع للتحقق. الخطوة التالية: مصفوفة متماسكة متعددة القنوات.",
        qr_p="اتصال من الشاشة إلى الكاميرا بين الهواتف: نقل ملفات بترميز النافورة، وتعدد إرسال لوني ومكاني، وبثّ طبقي بأسلوب NOMA مع SIC، واختبارات مشفّرة لكل مجموعة، ودردشة QR مشفّرة من طرف إلى طرف (ECDH + AES-GCM). يتوفر أيضًا كتطبيق Android يعمل دون إنترنت، وجُرّب ميدانيًا مع أكثر من 20 طالبًا.",
        mda_p="نظام شبكات ودردشة نظير-إلى-نظير حقيقي: تتواصل العُقد مباشرةً دون خادم وسيط مركزي، وعبر شبكات مختلفة. يعمل على الحاسوب والويب، ومن المخطط إصدار عميل Android أصلي بلغة Kotlin.",
        fly_p="تتبّع حيّ للحشرات بمعرّفات ثابتة، باستخدام الكشف عبر OpenCV، ومرشّح كالمان لكل مسار، والتعيين المجري (Hungarian) على IoU. يرسم آثار حركة متلاشية وشاشة معلومات حيّة.",
        npu_t="معالج عصبي على FPGA (DE10-Lite)",
        npu_p="مسرّع تعليمي بمصفوفة انقباضية INT8 على FPGA من نوع MAX 10 مع معالج Nios V مرن، لقياس أداء استدلال LeNet/MNIST المكمَّم مقارنةً بالبرمجيات.",
        home_p="مساعد على Telegram يدعم المرضى المتعافين في المنزل بعد جراحة القلب المفتوح، مع تنبيهات لمراقبة الأعراض وإرشادات للرعاية.",
    )),
    res_title="الأبحاث", res_sub="معالجة الإشارات · تقدير اتجاه الوصول (DOA) · Massive MIMO · NOMA · جدولة شبكات 5G",
    neu_page="صفحتي في جامعة الشرق الأدنى",
    pub_journal="مقالات في مجلات علمية", pub_conf="أوراق مؤتمرات", pub_thesis="الرسائل العلمية", pub_prep="قيد الإعداد وأعمال جارية",
    thesis_phd="أطروحة الدكتوراه، الهندسة الكهربائية والإلكترونية، جامعة الشرق الأدنى",
    thesis_msc="رسالة الماجستير، الهندسة الكهربائية والإلكترونية، جامعة الشرق الأدنى",
    prep=[
        ("قيد الإعداد", "توزيع القدرة والكشف الرمزي في أنظمة MIMO-NOMA", "مع F. Al-Turjman. لمجلة IntechOpen للذكاء الاصطناعي وعلوم الحاسوب وتقنيات الروبوت."),
        ("قيد الإعداد", "احتمال الخطأ في NOMA ضمن خفوت رايلي لإنترنت الأشياء في الهندسة المدنية", "مع B. Bilgehan وF. Al-Turjman."),
        ("قيد الإعداد", "اشتقاق موحّد لمعدل الخطأ في البتات (BER) لـ BPSK و16-QAM و64-QAM", "مع B. Bilgehan وF. Al-Turjman."),
        ("جارٍ", "تحديد الموقع المتماسك السلبي الموزّع", "رادار FM سلبي متعدد العُقد لكشف الطائرات: الهندسة ثنائية الموقع، ومعالجة CAF، وإحصاءات كشف مُتحقَّق منها ببيانات ADS-B."),
    ],
    about_title="نبذة", bg_title="الخلفية",
    bg='<p style="margin-top:0">أنا مهندس كهرباء تحوّل إلى بناء الأنظمة. أعمل أستاذًا مساعدًا ورئيسًا لقسم هندسة نظم المعلومات في جامعة الشرق الأدنى في نيقوسيا، قبرص، وأوزّع وقتي بين التدريس والبحث وإدارة القسم. قبل ذلك كنت رئيس هندسة البرمجيات في RoboLabs، حيث طوّرت أنظمة مدمجة وبُنى تحكّم مبنية على ROS 2 للروبوتات ذاتية التشغيل.</p>'
       '<p>يقع عملي حيث تلتقي <b>البرمجيات والإشارات والأنظمة الذاتية</b>: محاكاة بوجود الطيار الآلي في الحلقة، ومعالجة إشارات الرادار، وتحليل روابط الاتصال اللاسلكي، وأدوات أستطيع أن أضعها أمام طلابي في الصباح التالي.</p>'
       '<p style="margin-bottom:0">أبحث عن وظائف هندسية في <b>الروبوتات، والطائرات المسيّرة والمحاكاة، وبرمجيات الدفاع</b>.</p>',
    edu_title="التعليم",
    edu=[("2021", "دكتوراه في الهندسة الكهربائية والإلكترونية، جامعة الشرق الأدنى"),
         ("2018", "ماجستير في الهندسة الكهربائية والإلكترونية، جامعة الشرق الأدنى"),
         ("2014", "بكالوريوس الهندسة الكهربائية والإلكترونية، جامعة سوهاج، مصر")],
    teach_title="التدريس · خريف 2026",
    courses=[
        ("AIE401", "مقدمة في الروبوتات: روبوتات تبدأ بالمحاكاة لطلاب السنة الرابعة في الذكاء الاصطناعي"),
        ("AII452", "تطبيقات الذكاء الاصطناعي: مشاريع واقعية لطلاب السنة الرابعة"),
        ("AII020", "تحليل وتصميم النظم: التصميم والممارسات الرشيقة (Agile)"),
        ("AII108", "البرمجة كائنية التوجه بلغة Python"),
        ("—", "أخلاقيات الهندسة: دراسات حالة في الاستخدام المزدوج والأنظمة الحرجة للسلامة"),
    ],
    footer_loc="نيقوسيا، قبرص", email="البريد الإلكتروني",
    arena_js=dict(start="Match started · 4 teams airborne", lock="{a} lock on {b}  +10", attack="attack", evade="evade"),
)


TR = dict(
    lang_label="TR", dir="ltr",
    name="Amr Abdelbari", fullname="Dr. Öğr. Üyesi Amr Abdelbari", initials="AA",
    title="Amr Abdelbari — İHA simülasyonu, radar ve kablosuz sistemler",
    description="Dr. Öğr. Üyesi Amr Abdelbari — Yakın Doğu Üniversitesi Bilişim Sistemleri Mühendisliği Bölüm Başkanı, Lefkoşa, Kıbrıs. İHA yarışma simülasyonu, pasif radar, NOMA/MIMO kablosuz haberleşme araştırmaları.",
    og_desc="Sanal İHA Angajman Arenası'nın geliştiricisi: ArduPilot SITL, otomatik hakem motoru, 100 takım ölçeği, radar ve EH ligi.",
    otw="iş tekliflerine açık", otw_title="Robotik, İHA simülasyonu ve savunma yazılımı alanlarındaki pozisyonlara açık",
    nav_arena="İHA Arenası", nav_projects="Projeler", nav_research="Araştırma", nav_about="Hakkımda", nav_contact="İletişim",
    kicker="Mühendis · Eğitimci · Lefkoşa, Kıbrıs",
    h1="Kendi kendine <span>uçan, algılayan ve puanlayan</span> sistemler geliştiriyorum.",
    lede="Elektrik mühendisliği kökenli bir Dr. Öğretim Üyesi ve Yakın Doğu Üniversitesi'nde <strong>Bilişim Sistemleri Mühendisliği Bölüm Başkanı</strong>yım. "
         "Gerçek otopilotlar üzerinde çalışan <strong>İHA yarışma simülatörleri</strong>, SDR ve FPGA donanımıyla <strong>pasif radar</strong> geliştiriyor; "
         "<strong>NOMA / MIMO</strong> kablosuz bağlantıları üzerine araştırma yapıyorum.",
    cta_arena="İHA Arenası'nı incele →", cta_research="Yayınlar",
    arena_aria="Canlı arena simülasyonu", arena_live="Arena · canlı", running="ÇALIŞIYOR",
    arena_title="Sanal İHA Angajman Arenası", arena_sub="Ana proje · 2026",
    arena_h3="Gerçek ArduPilot otopilotlarıyla koşan sanal bir Savaşan İHA yarışması.",
    arena_p="Sabit kanatlı İHA takımları için, TEKNOFEST Savaşan İHA formatını örnek alan bir yarışma platformu. "
            "Takımlar rakibi kameralarının vuruş alanında tutarak, QR dalış görevini tamamlayarak, cezalardan kaçınarak "
            "ve güvenli iniş yaparak puan toplar. Her uçak gerçek bir <b>ArduPlane SITL</b> otopilotudur; takımın kendi koduyla ya da "
            "<b>tarayıcıdaki 3B kokpitten</b> elle uçurulur ve <b>otomatik hakem</b> her maçı gerçek konum verisinden puanlar. "
            "İzleyiciler tek bir bağlantıdan 3B olarak takip eder.",
    feats=[
        "<b>Hakem motoru</b>: kilitlenme doğrulaması (≥ 4 sn pencere, ≥ %90 alan içinde, 0,3 sn'den uzun kesinti yok), coğrafi sınır, telemetri bekçisi, asılsız iddia ve çarpışma cezaları, uyarı / dondurma / ihraç.",
        "<b>Dört kural seti</b>: standart, TEKNOFEST modu, bir savunma senaryosu ve bağımsız bir lig.",
        "<b>Lig modu</b>: savaş sisi, yer radarı, gizli SAM mevzileri, GPS ve haberleşme karıştırma, uçak üstü ECM ve sıralamaları ile 3B tekrarları yayınlayan insansız bir sezon yürütücüsü.",
        "<b>Her uçağa ait kamera görüntüleri</b> takımlara aktarılır; her kilitlenme incelemesi için kanıt klipleri kaydedilir.",
        "<b>Adil oyun</b>: takım başına anahtar, istek sınırları, sunucu tarafı zaman ve her takıma ayrı MAVLink portu.",
        "<b>Çoklu otopilot</b>: maç öncesi homologasyondan geçen ArduPilot ve PX4 uçakları, birden çok bilgisayara dağıtılmış olarak.",
    ],
    stats=[
        ("100", "takım tek maçta: son TEKNOFEST finalinin (42) yaklaşık iki katı"),
        ("2,7 ms", "100 uçak için hakem döngüsü başına (9.900 kamera/hedef çiftinin tamamı), 50 ms bütçeye karşı"),
        ("~12 bin", "satır Python: sunucu, hakem, örnek takımlar, betikler ve testler"),
        ("5 Hz", "her takımdan telemetri; her yanıt diğer tüm uçakları içerir"),
    ],
    rehearsal="Prova sonuçları · 25 Ekim 2026", th_setup="Kurulum", th_outcome="Sonuç",
    rows=[
        ("1", "İki özdeş avcı", "23,7. saniyede çarpıştılar, ikisi de elendi"),
        ("3", "Avcı - devriye, 10 dk", "11 geçerli kilitlenme; final skoru 135 – 3"),
        ("4", "Sınır dışına uçan - asılsız iddia eden takım", "30 sn sonra / 5 asılsız iddiadan sonra ihraç"),
        ("5", "60. saniyede telemetri kesildi", "5. saniyede uyarı, 30. saniyede ihraç"),
        ("6", "ArduPlane SITL, 3 koşu", "Her koşuda geçerli kilitlenme; kademeli iniş, yaklaşma çarpışmalarını çözdü"),
    ],
    lessons=[
        ("İlk karşılaşma en tehlikeli an", "Aynı kodla iki uçak kalkıştan sonraki 20 saniye içinde birbirine yöneldi. Takımların kilitlenme algoritmasından önce çatışma önleme kuralına ihtiyacı var."),
        ("Eşit uçaklar sonsuza dek döner", "Puan asimetriden gelir: daha dar dönmek için yavaşlamak (ω = g·tan φ / V), irtifayı kullanmak ya da uzaklaşıp yeniden angaje olmak."),
        ("Kaçış, saldırı kadar değerli", "Hareketi tahmin edilebilen bir hedef 10 dakikada 11 kez kilitlendi. Kilitlenmek −2, saldırana ise +10 puan."),
    ],
    proj_title="Diğer projeler", proj_sub="Donanım, sinyal ve yazılım",
    cards=_cards(dict(
        research="araştırma", live="yayında", prototype="prototip", vision="görüntü işleme", design="tasarımda", bot="bot",
        open="Aç", code="Kod", quant="Nicemleme",
        pcl_t="Pasif FM radar (PCL)",
        pcl_p="FM yayın istasyonlarını aydınlatıcı olarak kullanıp uçakları tespit eden pasif koherent konumlama sistemi. RTL-SDR alıcılar, DE10-Lite FPGA, Python'da doğrudan yol bastırmalı çapraz belirsizlik işleme ve doğrulama için ADS-B referans verisi kullanır. Sonraki adım: koherent çok kanallı dizi.",
        qr_p="Telefonlar arasında ekrandan kameraya iletişim: fountain kodlu dosya aktarımı, renk ve uzamsal çoğullama, SIC'li NOMA tarzı katmanlı yayın, gruba özel şifreli sınavlar ve uçtan uca şifreli QR sohbet (ECDH + AES-GCM). Çevrimdışı Android uygulaması olarak da sunulur ve 20'den fazla öğrenciyle sahada denendi.",
        mda_p="Gerçek eşler arası (P2P) ağ ve sohbet sistemi: düğümler merkezi bir aktarıcı olmadan, farklı ağlar üzerinden doğrudan konuşur. Masaüstünde ve web'de çalışır; yerel bir Kotlin Android istemcisi planlanıyor.",
        fly_p="Kalıcı kimliklerle canlı böcek takibi: OpenCV ile tespit, her iz için Kalman filtresi ve IoU üzerinde Macar (Hungarian) eşleştirme. Solan hareket izleri ve canlı bir HUD çizer.",
        npu_t="FPGA NPU (DE10-Lite)",
        npu_p="MAX 10 FPGA üzerinde Nios V soft çekirdekli, eğitim amaçlı INT8 sistolik dizi hızlandırıcısı; nicemlenmiş LeNet/MNIST çıkarımını yazılıma karşı kıyaslar.",
        home_p="Açık kalp ameliyatı sonrası evde iyileşen hastaları destekleyen, belirti izleme uyarıları ve bakım rehberliği sunan bir Telegram asistanı.",
    )),
    res_title="Araştırma", res_sub="Sinyal işleme · DOA kestirimi · Massive MIMO · NOMA · 5G çizelgeleme",
    neu_page="YDÜ personel sayfası",
    pub_journal="Dergi makaleleri", pub_conf="Konferans bildirileri", pub_thesis="Tezler", pub_prep="Hazırlık aşamasında ve devam eden",
    thesis_phd="Doktora tezi, Elektrik ve Elektronik Mühendisliği, Yakın Doğu Üniversitesi",
    thesis_msc="Yüksek lisans tezi, Elektrik ve Elektronik Mühendisliği, Yakın Doğu Üniversitesi",
    prep=[
        ("Hazırlanıyor", "MIMO-NOMA'da güç tahsisi ve sembolik sezim", "F. Al-Turjman ile. IntechOpen'ın Yapay Zekâ, Bilgisayar Bilimi ve Robotik Teknolojisi dergisi için."),
        ("Hazırlanıyor", "İnşaat mühendisliğinde IoT için Rayleigh sönümlemeli kanalda NOMA hata olasılığı", "B. Bilgehan ve F. Al-Turjman ile."),
        ("Hazırlanıyor", "BPSK, 16-QAM ve 64-QAM için birleşik BER türetimi", "B. Bilgehan ve F. Al-Turjman ile."),
        ("Devam ediyor", "Dağıtık pasif koherent konumlama", "Uçak tespiti için çok düğümlü FM pasif radar: bistatik geometri, CAF işleme ve ADS-B ile doğrulanmış tespit istatistikleri."),
    ],
    about_title="Hakkımda", bg_title="Özgeçmiş",
    bg='<p style="margin-top:0">Sistem geliştiriciliğine yönelmiş bir elektrik mühendisiyim. Lefkoşa\'daki Yakın Doğu Üniversitesi\'nde Dr. Öğretim Üyesi ve Bilişim Sistemleri Mühendisliği Bölüm Başkanı olarak zamanımı eğitim, araştırma ve bölüm yönetimi arasında paylaştırıyorum. Daha önce RoboLabs\'ta Yazılım Mühendisliği Müdürü olarak otonom robotlar için gömülü sistemler ve ROS 2 tabanlı kontrol mimarileri geliştirdim.</p>'
       '<p>Çalışmalarım <b>yazılım, sinyal ve otonominin</b> kesiştiği noktada: döngüde otopilotlu simülasyon, radar sinyal işleme, kablosuz bağlantı analizi ve ertesi sabah gerçek bir sınıfta kullanabileceğim araçlar.</p>'
       '<p style="margin-bottom:0"><b>Robotik, İHA ve simülasyon ile savunma yazılımı</b> alanlarında mühendislik pozisyonları arıyorum.</p>',
    edu_title="Eğitim",
    edu=[("2021", "Doktora, Elektrik ve Elektronik Mühendisliği, Yakın Doğu Üniversitesi"),
         ("2018", "Yüksek Lisans, Elektrik ve Elektronik Mühendisliği, Yakın Doğu Üniversitesi"),
         ("2014", "Lisans, Elektrik ve Elektronik Mühendisliği, Sohag Üniversitesi, Mısır")],
    teach_title="Dersler · Güz 2026",
    courses=[
        ("AIE401", "Robotiğe Giriş: 4. sınıf yapay zekâ öğrencileri için simülasyon öncelikli robotik"),
        ("AII452", "Yapay Zekâ Uygulamaları: 4. sınıf öğrencileri için gerçek dünya projeleri"),
        ("AII020", "Sistem Analizi ve Tasarımı: tasarım ve çevik (agile) uygulamalar"),
        ("AII108", "Python ile Nesne Yönelimli Programlama"),
        ("—", "Mühendislik Etiği: çift kullanımlı ve emniyet kritik vaka çalışmaları"),
    ],
    footer_loc="Lefkoşa, Kıbrıs", email="E-posta",
    arena_js=dict(start="Maç başladı · 4 takım havada", lock="{a} → {b} kilitlendi  +10", attack="saldırı", evade="kaçış"),
)

# Arabic feed: keep the short log lines readable inside the left-to-right feed box.
AR["arena_js"] = dict(start="بدأت المباراة · 4 فرق في الجو", lock="{a} أقفل على {b}  +10", attack="هجوم", evade="مراوغة")


EN.update(
    email_me="Email me", contact_label="Get in touch",
    band=[("13", "peer-reviewed papers"), ("100", "teams in one UAV arena match"),
          ("12+", "years building hardware and software"), ("20+", "students field-testing QR Lab")],
    chart_title="Publications per year", journey_title="From Sohag to Nicosia",
    timeline=[
        ("2014", "BSc, Electrical & Electronics Eng.", "Sohag University, Egypt"),
        ("2018", "MSc, Electrical & Electronics Eng.", "Near East University"),
        ("2019", "Research Assistant", "Near East University"),
        ("2021", "PhD, Electrical & Electronics Eng.", "Near East University"),
        ("2021", "Co-founder & Quant Developer", "Oxyinance Technologies, Istanbul"),
        ("2022", "Software Engineer → Head of Software Engineering", "RoboLabs, Istanbul"),
        ("2023", "Lecturer", "Near East University"),
        ("2024", "Assistant Professor", "Near East University"),
        ("2025", "Head of Information Systems Engineering", "Near East University"),
    ],
)

AR.update(
    email_me="راسلني", contact_label="تواصل معي",
    band=[("13", "ورقة علمية محكّمة"), ("100", "فريق في مباراة واحدة بساحة المسيّرات"),
          ("12+", "عامًا في بناء العتاد والبرمجيات"), ("20+", "طالبًا جرّبوا QR Lab ميدانيًا")],
    chart_title="المنشورات حسب السنة", journey_title="من سوهاج إلى نيقوسيا",
    timeline=[
        ("2014", "بكالوريوس الهندسة الكهربائية والإلكترونية", "جامعة سوهاج، مصر"),
        ("2018", "ماجستير الهندسة الكهربائية والإلكترونية", "جامعة الشرق الأدنى"),
        ("2019", "مساعد باحث", "جامعة الشرق الأدنى"),
        ("2021", "دكتوراه الهندسة الكهربائية والإلكترونية", "جامعة الشرق الأدنى"),
        ("2021", "شريك مؤسس ومطوّر كمّي", "Oxyinance Technologies، إسطنبول"),
        ("2022", "مهندس برمجيات ← رئيس هندسة البرمجيات", "RoboLabs، إسطنبول"),
        ("2023", "محاضر", "جامعة الشرق الأدنى"),
        ("2024", "أستاذ مساعد", "جامعة الشرق الأدنى"),
        ("2025", "رئيس قسم هندسة نظم المعلومات", "جامعة الشرق الأدنى"),
    ],
)

TR.update(
    email_me="E-posta gönder", contact_label="İletişime geçin",
    band=[("13", "hakemli yayın"), ("100", "takım tek bir İHA arena maçında"),
          ("12+", "yıl donanım ve yazılım geliştirme"), ("20+", "öğrenci QR Lab'i sahada denedi")],
    chart_title="Yıllara göre yayınlar", journey_title="Sohag'dan Lefkoşa'ya",
    timeline=[
        ("2014", "Lisans, Elektrik ve Elektronik Müh.", "Sohag Üniversitesi, Mısır"),
        ("2018", "Yüksek Lisans, Elektrik ve Elektronik Müh.", "Yakın Doğu Üniversitesi"),
        ("2019", "Araştırma Görevlisi", "Yakın Doğu Üniversitesi"),
        ("2021", "Doktora, Elektrik ve Elektronik Müh.", "Yakın Doğu Üniversitesi"),
        ("2021", "Kurucu Ortak ve Kantitatif Geliştirici", "Oxyinance Technologies, İstanbul"),
        ("2022", "Yazılım Mühendisi → Yazılım Mühendisliği Müdürü", "RoboLabs, İstanbul"),
        ("2023", "Öğretim Görevlisi", "Yakın Doğu Üniversitesi"),
        ("2024", "Dr. Öğretim Üyesi", "Yakın Doğu Üniversitesi"),
        ("2025", "Bilişim Sistemleri Mühendisliği Bölüm Başkanı", "Yakın Doğu Üniversitesi"),
    ],
)

LANGS = {"en": EN, "ar": AR, "tr": TR}
