import os
from flask import Flask, render_template_string

app = Flask(__name__)

TELEGRAM_USER = "vip_abdulvohidov"
INSTAGRAM_USER = "_abhvdv11"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Dev Portal | Abdulvohidov</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- FontAwesome Ikonkalar -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-dark: #070d1e;
            --card-bg: #0f172a;
            --cyan-glow: #00f2fe;
            --purple-glow: #9d4edd;
        }

        body {
            background-color: var(--bg-dark);
            color: #f8fafc;
            font-family: 'Space Grotesk', sans-serif;
            min-height: 100vh;
            overflow-x: hidden;
        }

        /* Chiroyli fon nurlari */
        body::before {
            content: '';
            position: fixed;
            top: -20%;
            left: -10%;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(0, 242, 254, 0.15) 0%, rgba(0,0,0,0) 70%);
            z-index: -1;
        }
        body::after {
            content: '';
            position: fixed;
            bottom: -20%;
            right: -10%;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(157, 78, 221, 0.15) 0%, rgba(0,0,0,0) 70%);
            z-index: -1;
        }

        .header-title {
            background: linear-gradient(135deg, #00f2fe 0%, #4facfe 50%, #9d4edd 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        /* Neon ijtimoiy tarmoq tugmalari */
        .btn-telegram {
            background: #229ED9;
            color: #fff;
            font-weight: 600;
            border-radius: 12px;
            box-shadow: 0 0 15px rgba(34, 158, 217, 0.4);
            transition: all 0.3s ease;
        }
        .btn-telegram:hover {
            box-shadow: 0 0 25px rgba(34, 158, 217, 0.8);
            transform: translateY(-2px);
            color: #fff;
        }

        .btn-instagram {
            background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
            color: #fff;
            font-weight: 600;
            border-radius: 12px;
            box-shadow: 0 0 15px rgba(220, 39, 67, 0.4);
            transition: all 0.3s ease;
        }
        .btn-instagram:hover {
            box-shadow: 0 0 25px rgba(220, 39, 67, 0.8);
            transform: translateY(-2px);
            color: #fff;
        }

        /* Dars kartochkalari */
        .lesson-card {
            background: var(--card-bg);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 24px;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.35s ease;
            position: relative;
            overflow: hidden;
        }
        .lesson-card:hover {
            transform: translateY(-6px);
            border-color: rgba(0, 242, 254, 0.4);
            box-shadow: 0 10px 30px rgba(0, 242, 254, 0.15);
        }

        .badge-module {
            background: rgba(0, 242, 254, 0.1);
            color: #00f2fe;
            border: 1px solid rgba(0, 242, 254, 0.3);
            border-radius: 8px;
            padding: 6px 12px;
            font-size: 0.8rem;
            font-weight: 600;
        }

        /* YONIB VA YALTIRAB TURUVCHI TUGMA */
        .btn-glow {
            position: relative;
            background: linear-gradient(90deg, #00f2fe, #4facfe, #00f2fe);
            background-size: 200% auto;
            color: #070d1e;
            font-weight: 700;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            animation: glowingEffect 3s linear infinite;
            box-shadow: 0 0 20px rgba(0, 242, 254, 0.6);
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            text-align: center;
        }

        .btn-glow:hover {
            color: #070d1e;
            transform: scale(1.03);
            box-shadow: 0 0 30px rgba(0, 242, 254, 0.9);
        }

        @keyframes glowingEffect {
            0% {
                background-position: 0% 50%;
                box-shadow: 0 0 15px rgba(0, 242, 254, 0.5);
            }
            50% {
                background-position: 100% 50%;
                box-shadow: 0 0 28px rgba(0, 242, 254, 0.85);
            }
            100% {
                background-position: 0% 50%;
                box-shadow: 0 0 15px rgba(0, 242, 254, 0.5);
            }
        }

        /* Profil blok */
        .profile-card {
            background: linear-gradient(180deg, #0f172a 0%, #172554 100%);
            border: 1px solid rgba(0, 242, 254, 0.2);
            border-radius: 16px;
            padding: 24px;
            text-align: center;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
        }
    </style>
</head>
<body class="py-4">
    <div class="container">
        <!-- Yuqori menyu -->
        <header class="d-flex justify-content-between align-items-center mb-5 flex-wrap gap-3 pb-3 border-bottom border-secondary border-opacity-25">
            <div>
                <h2 class="header-title mb-1">⚡ PYTHON ACADEMY</h2>
                <p class="text-secondary small mb-0">Zamonaviy dasturlash darslari & Loyihalar</p>
            </div>
            <div class="d-flex gap-2">
                <a href="https://t.me/{{ tg_user }}" target="_blank" class="btn btn-telegram px-3 py-2">
                    <i class="fab fa-telegram me-1"></i> Telegram Kanal
                </a>
                <a href="https://instagram.com/{{ ig_user }}" target="_blank" class="btn btn-instagram px-3 py-2">
                    <i class="fab fa-instagram me-1"></i> Instagram
                </a>
            </div>
        </header>

        <div class="row g-4">
            <!-- Chap tomon: Darsliklar ro'yxati -->
            <div class="col-lg-8">
                <div class="row g-3">
                    
                    <!-- 1-Dars -->
                    <div class="col-md-6">
                        <div class="lesson-card">
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-3">
                                    <span class="badge-module">1-Modul</span>
                                    <span class="text-secondary small"><i class="far fa-clock"></i> 5 daqiqa</span>
                                </div>
                                <h5 class="fw-bold mb-2">O'zgaruvchilar va Data Types</h5>
                                <p class="text-secondary small mb-4">Python asosiy turlari: int, float, str, bool va f-stringlar bilan ishlash.</p>
                            </div>
                            <button class="btn btn-glow w-100" onclick="showModal('1. O\'zgaruvchilar va Ma\'lumot turlari', 'Python-da ma\\'lumotlar 4 ta asosiy turga bo\\'linadi: int (butun son), float (o\\'nlik son), str (matn) va bool (rost/yolg\\'on).\\n\\nMisol:\\nism = \\'Ali\\'\\nyosh = 20\\nbo\\'yi = 1.78\\ntalaba = True\\n\\nprint(f\\'{ism}ning yoshi {yosh}da\\')')">Darsni Boshlash &rarr;</button>
                        </div>
                    </div>

                    <!-- 2-Dars -->
                    <div class="col-md-6">
                        <div class="lesson-card">
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-3">
                                    <span class="badge-module">1-Modul</span>
                                    <span class="text-secondary small"><i class="far fa-clock"></i> 8 daqiqa</span>
                                </div>
                                <h5 class="fw-bold mb-2">Shartlar va Sikllar (if, for, while)</h5>
                                <p class="text-secondary small mb-4">Mantiqiy shartlar orqali kod oqimini boshqarish va sikllar yordamida takrorlash.</p>
                            </div>
                            <button class="btn btn-glow w-100" onclick="showModal('2. Shartlar va Sikllar', 'if, elif, else yordamida shartlarni tekshiramiz.\\n\\nfor va while yordamida amallarni qayta-qayta bajaramiz.\\n\\nMisol:\\nfor i in range(1, 6):\\n    print(f\\'Qadam: {i}\\')')">Darsni Boshlash &rarr;</button>
                        </div>
                    </div>

                    <!-- 3-Dars -->
                    <div class="col-md-6">
                        <div class="lesson-card">
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-3">
                                    <span class="badge-module">2-Modul</span>
                                    <span class="text-secondary small"><i class="far fa-clock"></i> 10 daqiqa</span>
                                </div>
                                <h5 class="fw-bold mb-2">Ro'yxat va Lug'atlar (List & Dict)</h5>
                                <p class="text-secondary small mb-4">Bir nechta ma'lumotlar to'plamini tartibli va kalit-qiymat ko'rinishida saqlash.</p>
                            </div>
                            <button class="btn btn-glow w-100" onclick="showModal('3. Ro\'yxat va Lug\'atlar', 'List (ro\\'yxat) — elementlar to\\'plami: mevalar = [\\'olma\\', \\'anor\\']\\nDict (lug\\'at) — kalit-qiymat juftligi: user = {\\'name\\': \\'Ali\\', \\'age\\': 22}')">Darsni Boshlash &rarr;</button>
                        </div>
                    </div>

                    <!-- 4-Dars -->
                    <div class="col-md-6">
                        <div class="lesson-card">
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-3">
                                    <span class="badge-module">2-Modul</span>
                                    <span class="text-secondary small"><i class="far fa-clock"></i> 12 daqiqa</span>
                                </div>
                                <h5 class="fw-bold mb-2">Funksiyalar (def & lambda)</h5>
                                <p class="text-secondary small mb-4">Kodni modulli qilish, qayta ishlatiluvchi funksiyalar va return qiymatlari.</p>
                            </div>
                            <button class="btn btn-glow w-100" onclick="showModal('4. Funksiyalar', 'def orqali o\\'z funksiyangizni yaratasiz.\\n\\nMisol:\\ndef salom_ber(ism):\\n    return f\\'Assalomu alaykum, {ism}!\\'\\n\\nprint(salom_ber(\\'Abubakr\\'))')">Darsni Boshlash &rarr;</button>
                        </div>
                    </div>

                    <!-- 5-Dars -->
                    <div class="col-md-6">
                        <div class="lesson-card">
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-3">
                                    <span class="badge-module">3-Modul</span>
                                    <span class="text-secondary small"><i class="far fa-clock"></i> 15 daqiqa</span>
                                </div>
                                <h5 class="fw-bold mb-2">OOP (Obyektga Yo'naltirilgan Dasturlash)</h5>
                                <p class="text-secondary small mb-4">Class, Object, __init__ konstruktori, meros olish va polimorfizm asoslari.</p>
                            </div>
                            <button class="btn btn-glow w-100" onclick="showModal('5. OOP Asoslari', 'Katta loyihalarni yaratishda obyektlar bilan ishlash juda muhim.\\n\\nMisol:\\nclass Bot:\\n    def __init__(self, token):\\n        self.token = token\\n\\n    def start(self):\\n        print(\\'Bot ishga tushdi\\')')">Darsni Boshlash &rarr;</button>
                        </div>
                    </div>

                    <!-- 6-Dars -->
                    <div class="col-md-6">
                        <div class="lesson-card">
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-3">
                                    <span class="badge-module">Amaliyot</span>
                                    <span class="text-secondary small"><i class="far fa-clock"></i> 20 daqiqa</span>
                                </div>
                                <h5 class="fw-bold mb-2">Telegram Bot Yaratish (aiogram)</h5>
                                <p class="text-secondary small mb-4">Python yordamida zamonaviy Telegram botlarni noldan yozish va serverga qo'yish.</p>
                            </div>
                            <button class="btn btn-glow w-100" onclick="showModal('6. Telegram Bot Yaratish', 'aiogram kutubxonasi orqali tugmali (inline), to\\'lovli yoki avtomatlashtirilgan botlarni yasashingiz mumkin!\\n\\npip install aiogram')">Darsni Boshlash &rarr;</button>
                        </div>
                    </div>

                </div>
            </div>

            <!-- O'ng tomon: Muallif profili va Aloqa -->
            <div class="col-lg-4">
                <div class="profile-card mb-4">
                    <div class="mb-3">
                        <i class="fas fa-user-astronaut fa-4x text-info"></i>
                    </div>
                    <h4 class="fw-bold mb-1">Abdulvohidov</h4>
                    <p class="text-secondary small mb-3">Python & Backend Dasturchi</p>
                    <p class="small text-light">Python orqali zamonaviy saytlar, kuchli Telegram botlar va avtomatlashtirilgan tizimlar yaratishni o'rganing.</p>
                    <hr class="border-secondary my-3">
                    <div class="d-grid gap-2">
                        <a href="https://t.me/{{ tg_user }}" target="_blank" class="btn btn-telegram py-2">
                            <i class="fab fa-telegram me-2"></i> Lichkaga yozish
                        </a>
                        <a href="https://instagram.com/{{ ig_user }}" target="_blank" class="btn btn-instagram py-2">
                            <i class="fab fa-instagram me-2"></i> Instagram profil
                        </a>
                    </div>
                </div>

                <div class="lesson-card text-center p-4">
                    <i class="fas fa-rocket fa-3x mb-3 text-warning"></i>
                    <h5 class="fw-bold">Yangi loyihalar</h5>
                    <p class="text-secondary small mb-0">Tez orada platformamizda yangi amaliy darslar va kodlar bazasi qo'shiladi.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Dars oynasi (Modal) -->
    <div class="modal fade" id="lessonModal" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content" style="background-color: #0f172a; color: #fff; border: 1px solid #00f2fe;">
                <div class="modal-header border-secondary">
                    <h5 class="modal-title fw-bold text-info" id="modalTitle"></h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <pre id="modalContent" style="white-space: pre-wrap; font-family: inherit; color: #cbd5e1; font-size: 0.95rem;"></pre>
                </div>
                <div class="modal-footer border-secondary">
                    <button type="button" class="btn btn-glow px-4" data-bs-dismiss="modal">Tushunarli</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        function showModal(title, text) {
            document.getElementById('modalTitle').innerText = title;
            document.getElementById('modalContent').innerText = text;
            const modal = new bootstrap.Modal(document.getElementById('lessonModal'));
            modal.show();
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, tg_user=TELEGRAM_USER, ig_user=INSTAGRAM_USER)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))                   
