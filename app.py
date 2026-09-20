import os
from flask import Flask, render_template_string, abort

app = Flask(__name__)

TELEGRAM_USER = "vip_abdulvohidov"
INSTAGRAM_USER = "_abhvdv11"

# 20 ta to'liq darsliklar bazasi
LESSONS = {
    # 1. SCRATCH
    "scratch-intro": {
        "title": "1. Scratch Asoslari: Vizual Bloklar va Spritelar",
        "category": "Scratch",
        "time": "10 daqiqa",
        "badge_class": "badge-scratch",
        "desc": "Dasturlash mantig'iga kirish: Sprite, sahna va rangli bloklar bilan ishlash.",
        "content": "<h3>Scratch nima?</h3><p>Scratch — blokli vizual dasturlash tili bo'lib, o'yinlar yaratish orqali algoritmik fikrlashni o'rgatadi.</p>"
    },
    "scratch-variables-game": {
        "title": "2. Scratch'da O'zgaruvchilar va Birinchi O'yin",
        "category": "Scratch",
        "time": "15 daqiqa",
        "badge_class": "badge-scratch",
        "desc": "O'yinlarda ochko hisoblash (Score), jonlar va sensorlar.",
        "content": "<h3>O'yin Mantig'i</h3><p>Ochkolar yig'ish va to'siqlarga tekkanda o'yinni boshqarish algoritmi.</p>"
    },

    # 2. PYTHON ASOSLARI
    "python-intro": {
        "title": "3. Python Sintaksisi va Data Types",
        "category": "Python Asoslari",
        "time": "10 daqiqa",
        "badge_class": "badge-python",
        "desc": "O'zgaruvchilar, int, float, str, bool va f-string bilan ishlash.",
        "content": "<h3>Python Asoslari</h3><pre><code>ism = 'Abdulvohidov'\\nprint(f'Salom, {ism}')</code></pre>"
    },
    "python-conditions": {
        "title": "4. Shart Operatorlari: if, elif, else",
        "category": "Python Asoslari",
        "time": "12 daqiqa",
        "badge_class": "badge-python",
        "desc": "Mantiqiy ifodalar va shartli tarmoqlanish.",
        "content": "<h3>Shartlar</h3><pre><code>if ball > 80:\\n    print('A')</code></pre>"
    },
    "python-loops": {
        "title": "5. Sikllar: for va while",
        "category": "Python Asoslari",
        "time": "12 daqiqa",
        "badge_class": "badge-python",
        "desc": "Takrorlanuvchi jarayonlar, range va break/continue.",
        "content": "<h3>Sikllar</h3><pre><code>for i in range(5):\\n    print(i)</code></pre>"
    },
    "python-lists": {
        "title": "6. Ro'yxatlar (Lists) va Tuple",
        "category": "Python Asoslari",
        "time": "14 daqiqa",
        "badge_class": "badge-python",
        "desc": "Indekslash, metodlar: append, remove, pop, sort.",
        "content": "<h3>Ro'yxatlar</h3><pre><code>mevalar = ['olma', 'banan']\\nmevalar.append('uzum')</code></pre>"
    },
    "python-dicts": {
        "title": "7. Lug'atlar (Dictionaries) va Sets",
        "category": "Python Asoslari",
        "time": "15 daqiqa",
        "badge_class": "badge-python",
        "desc": "Key-Value arxitekturasi va tezkor ma'lumotlar bilan ishlash.",
        "content": "<h3>Lug'atlar</h3><pre><code>user = {'ism': 'Ali', 'yosh': 20}</code></pre>"
    },
    "python-functions": {
        "title": "8. Funksiyalar: def, return, *args",
        "category": "Python Ilg'or",
        "time": "15 daqiqa",
        "badge_class": "badge-python",
        "desc": "Toza kod yozish, argumentlar va return qiymatlari.",
        "content": "<h3>Funksiyalar</h3><pre><code>def kvadrat(x):\\n    return x**2</code></pre>"
    },
    "python-oop": {
        "title": "9. OOP: Obyektga Yo'naltirilgan Dasturlash",
        "category": "Python Ilg'or",
        "time": "18 daqiqa",
        "badge_class": "badge-python",
        "desc": "Class, Object, konstruktor (__init__) va meros olish.",
        "content": "<h3>OOP Asoslari</h3><pre><code>class Bot:\\n    def __init__(self, token):\\n        self.token = token</code></pre>"
    },
    "python-files-errors": {
        "title": "10. Fayllar va Try-Except",
        "category": "Python Ilg'or",
        "time": "14 daqiqa",
        "badge_class": "badge-python",
        "desc": "Fayllarga yozish va xatoliklarni xavfsiz boshqarish.",
        "content": "<h3>Fayllar</h3><pre><code>with open('data.txt', 'w') as f:\\n    f.write('Salom')</code></pre>"
    },

    # 3. TELEGRAM BOTLAR
    "tgbot-setup": {
        "title": "11. aiogram 3: Bot Arxitekturasi",
        "category": "Telegram Bot",
        "time": "15 daqiqa",
        "badge_class": "badge-tg",
        "desc": "aiogram 3 o'rnatish, dispatcher va asinxron arxitektura.",
        "content": "<h3>aiogram 3</h3><p>Zamonaviy tezkor Telegram botlar asosi.</p>"
    },
    "tgbot-keyboards": {
        "title": "12. Inline va Reply Tugmalar",
        "category": "Telegram Bot",
        "time": "16 daqiqa",
        "badge_class": "badge-tg",
        "desc": "Tugmali menyular, callback_data va havolalar ulash.",
        "content": "<h3>Inline Keyboards</h3><p>Tugmali interfeys yaratish tartibi.</p>"
    },
    "tgbot-database": {
        "title": "13. Botga SQLite Bazasini Ulanish",
        "category": "Telegram Bot",
        "time": "18 daqiqa",
        "badge_class": "badge-tg",
        "desc": "Foydalanuvchilarni saqlash va tekshirish tizimi.",
        "content": "<h3>SQLite</h3><pre><code>CREATE TABLE users (id INT, ism TEXT)</code></pre>"
    },
    "tgbot-payments": {
        "title": "14. Telegram Stars va To'lovlar",
        "category": "Telegram Bot",
        "time": "20 daqiqa",
        "badge_class": "badge-tg",
        "desc": "Bot orqali avtomatlashtirilgan to'lovlarni qabul qilish.",
        "content": "<h3>To'lovlar</h3><p>Telegram Stars orqali tezkor savdo qilish usuli.</p>"
    },

    # 4. FIGMA UI/UX
    "figma-intro": {
        "title": "15. Figma Asoslari va Frame'lar",
        "category": "Figma UI/UX",
        "time": "12 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Interfeys, Frame (F), Shape va loyiha strukturasini qurish.",
        "content": "<h3>Figma Asoslari</h3><p>Desktop va Mobile ramkalar bilan ishlash.</p>"
    },
    "figma-autolayout": {
        "title": "16. Auto Layout (Shift + A) Sehri",
        "category": "Figma UI/UX",
        "time": "16 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Elementlarni responsive qilish va moslashuvchan tugmalar.",
        "content": "<h3>Auto Layout</h3><p>Elementlarni avtomatik cho'ziluvchan qilish siri.</p>"
    },
    "figma-components": {
        "title": "17. Komponentlar va Variantlar",
        "category": "Figma UI/UX",
        "time": "15 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Master Komponentlar va yagona dizayn tizimi.",
        "content": "<h3>Komponentlar</h3><p>Bitta o'zgartirish bilan butun dizaynni boshqarish.</p>"
    },
    "figma-typography-colors": {
        "title": "18. Tipografika va Qorong'u Mavzu",
        "category": "Figma UI/UX",
        "time": "14 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Kontrast qoidalari, neon ranglar va to'g'ri shriftlar.",
        "content": "<h3>Ranglar</h3><p>Zamonaviy Dark Theme yaratish qoidalari.</p>"
    },
    "figma-prototyping": {
        "title": "19. Prototip Yasash va Smart Animate",
        "category": "Figma UI/UX",
        "time": "16 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Sahifalarni o'zaro bog'lash va animatsiyalar.",
        "content": "<h3>Prototip</h3><p>Dizaynni bosiladigan va jonli holatga keltirish.</p>"
    },
    "figma-to-code": {
        "title": "20. Figma'dan Toza CSS Kodga O'tkazish",
        "category": "Figma to Web",
        "time": "18 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Dev Mode, box-shadow va dizaynni kodga ko'chirish.",
        "content": "<h3>CSS Eksport</h3><p>Figma elementlarini brauzer kodiga aylantirish.</p>"
    }
}

INDEX_TEMPLATE = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abdulvohidov Academy & Services</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-dark: #070d1e;
            --card-bg: #0f172a;
            --neon-blue: #00f2fe;
            --neon-figma: #ff7262;
            --neon-scratch: #f59e0b;
        }

        body {
            background-color: var(--bg-dark);
            color: #f8fafc;
            font-family: 'Space Grotesk', sans-serif;
            min-height: 100vh;
            overflow-x: hidden;
        }

        body::before {
            content: '';
            position: fixed;
            top: -20%;
            left: -10%;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(0, 242, 254, 0.12) 0%, rgba(0,0,0,0) 70%);
            z-index: -1;
        }
        body::after {
            content: '';
            position: fixed;
            bottom: -20%;
            right: -10%;
            width: 650px;
            height: 650px;
            background: radial-gradient(circle, rgba(157, 78, 221, 0.12) 0%, rgba(0,0,0,0) 70%);
            z-index: -1;
        }

        .header-title {
            background: linear-gradient(135deg, #00f2fe 0%, #4facfe 50%, #f59e0b 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .btn-telegram {
            background: #229ED9;
            color: #fff;
            font-weight: 600;
            border-radius: 12px;
            box-shadow: 0 0 15px rgba(34, 158, 217, 0.4);
            transition: 0.3s;
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
            transition: 0.3s;
        }
        .btn-instagram:hover {
            box-shadow: 0 0 25px rgba(220, 39, 67, 0.8);
            transform: translateY(-2px);
            color: #fff;
        }

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
        }
        .lesson-card:hover {
            transform: translateY(-6px);
            border-color: rgba(0, 242, 254, 0.4);
            box-shadow: 0 10px 30px rgba(0, 242, 254, 0.15);
        }

        .badge-scratch {
            background: rgba(245, 158, 11, 0.15);
            color: var(--neon-scratch);
            border: 1px solid rgba(245, 158, 11, 0.4);
            border-radius: 8px;
            padding: 5px 12px;
            font-size: 0.8rem;
            font-weight: 700;
        }
        .badge-python {
            background: rgba(0, 242, 254, 0.1);
            color: var(--neon-blue);
            border: 1px solid rgba(0, 242, 254, 0.3);
            border-radius: 8px;
            padding: 5px 12px;
            font-size: 0.8rem;
            font-weight: 600;
        }
        .badge-figma {
            background: rgba(255, 114, 98, 0.1);
            color: var(--neon-figma);
            border: 1px solid rgba(255, 114, 98, 0.3);
            border-radius: 8px;
            padding: 5px 12px;
            font-size: 0.8rem;
            font-weight: 600;
        }
        .badge-tg {
            background: rgba(34, 158, 217, 0.1);
            color: #229ED9;
            border: 1px solid rgba(34, 158, 217, 0.3);
            border-radius: 8px;
            padding: 5px 12px;
            font-size: 0.8rem;
            font-weight: 600;
        }

        .btn-glow {
            display: block;
            text-align: center;
            background: linear-gradient(90deg, #00f2fe, #4facfe, #00f2fe);
            background-size: 200% auto;
            color: #070d1e;
            font-weight: 700;
            text-decoration: none;
            border-radius: 10px;
            padding: 11px 20px;
            animation: glowingEffect 3s linear infinite;
            box-shadow: 0 0 18px rgba(0, 242, 254, 0.55);
            transition: all 0.3s ease;
        }
        .btn-glow:hover {
            color: #070d1e;
            transform: scale(1.02);
            box-shadow: 0 0 28px rgba(0, 242, 254, 0.85);
        }

        @keyframes glowingEffect {
            0% { background-position: 0% 50%; box-shadow: 0 0 15px rgba(0, 242, 254, 0.45); }
            50% { background-position: 100% 50%; box-shadow: 0 0 26px rgba(0, 242, 254, 0.8); }
            100% { background-position: 0% 50%; box-shadow: 0 0 15px rgba(0, 242, 254, 0.45); }
        }

        .profile-card {
            background: linear-gradient(180deg, #0f172a 0%, #172554 100%);
            border: 1px solid rgba(0, 242, 254, 0.2);
            border-radius: 16px;
            padding: 24px;
            text-align: center;
        }

        /* O'ng tomondagi yagona ixcham xizmatlar bloki */
        .services-unified-box {
            background: #0f172a;
            border: 1px solid rgba(16, 185, 129, 0.4);
            border-radius: 16px;
            padding: 22px;
            box-shadow: 0 10px 30px rgba(16, 185, 129, 0.15);
        }

        .btn-order-glow {
            display: block;
            text-align: center;
            background: linear-gradient(90deg, #10b981, #059669, #10b981);
            background-size: 200% auto;
            color: #ffffff;
            font-weight: 700;
            text-decoration: none;
            border-radius: 10px;
            padding: 12px 20px;
            box-shadow: 0 0 20px rgba(16, 185, 129, 0.6);
            transition: all 0.3s ease;
        }
        .btn-order-glow:hover {
            color: #ffffff;
            transform: scale(1.02);
            box-shadow: 0 0 30px rgba(16, 185, 129, 0.9);
        }
    </style>
</head>
<body class="py-4">
    <div class="container">
        <!-- HEADER -->
        <header class="d-flex justify-content-between align-items-center mb-5 flex-wrap gap-3 pb-3 border-bottom border-secondary border-opacity-25">
            <div>
                <h2 class="header-title mb-1">⚡ ABDULVOHIDOV ACADEMY & SERVICES</h2>
                <p class="text-secondary small mb-0">Professional Dasturlash Portali & IT Xizmatlari Markazi</p>
            </div>
            <div class="d-flex gap-2">
                <a href="https://t.me/{{ tg_user }}" target="_blank" class="btn btn-telegram px-3 py-2">
                    <i class="fab fa-telegram me-1"></i> Telegram
                </a>
                <a href="https://instagram.com/{{ ig_user }}" target="_blank" class="btn btn-instagram px-3 py-2">
                    <i class="fab fa-instagram me-1"></i> Instagram
                </a>
            </div>
        </header>

        <div class="row g-4">
            <!-- CHAP TOMON: BARCHA 20 TA DARSLIK -->
            <div class="col-lg-8">
                <div class="d-flex align-items-center gap-2 mb-4 pb-2 border-bottom border-secondary border-opacity-25">
                    <i class="fas fa-graduation-cap text-info fs-4"></i>
                    <h4 class="fw-bold mb-0 text-white">Barcha O'quv Darsliklari (20 ta Dars)</h4>
                </div>

                <div class="row g-3">
                    {% for key, item in lessons.items() %}
                    <div class="col-md-6">
                        <div class="lesson-card">
                            <div>
                                <div class="d-flex justify-content-between align-items-center mb-3">
                                    <span class="{{ item.badge_class }}">{{ item.category }}</span>
                                    <span class="text-secondary small"><i class="far fa-clock"></i> {{ item.time }}</span>
                                </div>
                                <h5 class="fw-bold mb-2">{{ item.title }}</h5>
                                <p class="text-secondary small mb-4">{{ item.desc }}</p>
                            </div>
                            <a href="/lesson/{{ key }}" class="btn-glow">Darsni O'qish &rarr;</a>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </div>

            <!-- O'NG TOMON: PROFIL VA HAMMASI BITTA JOYDA BO'LGAN XIZMATLAR BLOKI -->
            <div class="col-lg-4">
                <div class="profile-card mb-4">
                    <div class="mb-3">
                        <i class="fas fa-laptop-code fa-4x text-info"></i>
                    </div>
                    <h4 class="fw-bold mb-1">Abdulvohidov</h4>
                    <p class="text-secondary small mb-3">Full-Stack & UI/UX Developer</p>
                    <p class="small text-light">Python, Telegram Botlar, Scratch va Figma bo'yicha professional ta'lim va shaxsiy buyurtmalar.</p>
                    <hr class="border-secondary my-3">
                    <div class="d-grid gap-2">
                        <a href="https://t.me/{{ tg_user }}" target="_blank" class="btn btn-telegram py-2">
                            <i class="fab fa-telegram me-2"></i> Telegram Lichka
                        </a>
                        <a href="https://instagram.com/{{ ig_user }}" target="_blank" class="btn btn-instagram py-2">
                            <i class="fab fa-instagram me-2"></i> Instagram Profil
                        </a>
                    </div>
                </div>

                <!-- O'NG TOMONDAGI BO'SH JOYNI TO'LDIRUVCHI XIZMATLAR BLOKI -->
                <div class="services-unified-box sticky-top" style="top: 20px;">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <i class="fas fa-briefcase text-success fs-4"></i>
                        <h5 class="fw-bold mb-0 text-white">Xizmatlarimiz & Buyurtma</h5>
                    </div>
                    <p class="text-secondary small mb-3">Quyidagi xizmat turini tanlang va to'g'ridan-to'g'ri lichkaga buyurtma bering:</p>

                    <div class="mb-3">
                        <label class="small text-light mb-1 fw-bold">Xizmat turini tanlang:</label>
                        <select class="form-select bg-dark text-white border-secondary" id="serviceSelector" onchange="updateServiceInfo()">
                            <!-- Figma guruhi -->
                            <optgroup label="🎨 Figma & UI/UX Dizayn">
                                <option value="logo" data-desc="Kanal, brend yoki kompaniya uchun original vektor logotip va to'liq dizayn tayyorlash." data-msg="Assalomu alaykum, menga Figma'da Logotip / Rasm yaratish xizmati kerak edi.">Figma: Logotip & Rasm yaratish</option>
                                <option value="uiux" data-desc="Veb-sayt, lenta, lending yoki mobil ilovalar uchun zamonaviy interfeys chizish." data-msg="Assalomu alaykum, menga Sayt yoki Ilova dizayni kerak edi.">Figma: Veb-sayt & Ilova UI/UX</option>
                            </optgroup>
                            <!-- Bot guruhi -->
                            <optgroup label="🤖 Telegram Botlar">
                                <option value="kino" data-desc="Kinolar kodi bo'yicha qidiruv, majburiy kanal a'zoligi va tezkor kino yuklab beruvchi bot." data-msg="Assalomu alaykum, menga Kino bot yaratish xizmati kerak edi.">Kino & Seriallar Boti</option>
                                <option value="stars" data-desc="Telegram Stars xavfsiz savdosi va yulduzlar orqali to'lov qabul qiluvchi avtomat bot." data-msg="Assalomu alaykum, menga Telegram Stars savdo boti kerak edi.">Telegram Stars Savdo Boti</option>
                                <option value="smm" data-desc="Obunachi, layk, ko'rishlar buyurtmasi va hisob to'ldirish tizimli avtomat nakrutka boti." data-msg="Assalomu alaykum, menga SMM Nakrutka boti kerak edi.">SMM & Nakrutka Boti</option>
                                <option value="builder" data-desc="Foydalanuvchilar o'zlari uchun kodsiz bot yarata oladigan konstruktor platforma boti." data-msg="Assalomu alaykum, menga Telegram Bot Builder boti kerak edi.">Telegram Bot Builder</option>
                                <option value="vip" data-desc="Pullik kanallarga avtomatik obuna qabul qilish (Click, Payme) va muddatli chiqarish boti." data-msg="Assalomu alaykum, menga VIP kanal to'lov boti kerak edi.">VIP Kanal & Avto-to'lov Boti</option>
                                <option value="magazin" data-desc="Katalog, tovar savatchasi va yetkazib berish tizimiga ega e-commerce internet do'kon boti." data-msg="Assalomu alaykum, menga Telegram Do'kon boti kerak edi.">Internet Magazin (Do'kon) Boti</option>
                            </optgroup>
                        </select>
                    </div>

                    <!-- Tanlangan xizmat ta'rifi -->
                    <div class="p-3 mb-3 rounded" style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);">
                        <p class="small text-info mb-0" id="serviceDesc">Kanal, brend yoki kompaniya uchun original vektor logotip va to'liq dizayn tayyorlash.</p>
                    </div>

                    <a href="https://t.me/{{ tg_user }}?text=Assalomu alaykum, menga Figma'da Logotip / Rasm yaratish xizmati kerak edi." id="orderBtn" target="_blank" class="btn-order-glow w-100">
                        <i class="fab fa-telegram me-2"></i> Buyurtma Berish &rarr;
                    </a>
                </div>
            </div>
        </div>
    </div>

    <!-- Tanlangan xizmatni dinamik almashtirish skripti -->
    <script>
        function updateServiceInfo() {
            const selector = document.getElementById('serviceSelector');
            const selectedOption = selector.options[selector.selectedIndex];
            const desc = selectedOption.getAttribute('data-desc');
            const msg = encodeURIComponent(selectedOption.getAttribute('data-msg'));
            
            document.getElementById('serviceDesc').innerText = desc;
            document.getElementById('orderBtn').href = "https://t.me/{{ tg_user }}?text=" + msg;
        }
    </script>
</body>
</html>
"""

LESSON_PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ lesson.title }} | Academy</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body { background-color: #070d1e; color: #f8fafc; font-family: 'Space Grotesk', sans-serif; min-height: 100vh; }
        .content-box { background-color: #0f172a; border: 1px solid rgba(0, 242, 254, 0.25); border-radius: 18px; padding: 35px; box-shadow: 0 10px 40px rgba(0,0,0,0.5); margin-bottom: 50px; }
        pre { background-color: #040814; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 16px; color: #38bdf8; font-family: 'Consolas', monospace; font-size: 0.95rem; overflow-x: auto; }
        code { color: #00f2fe; }
        .btn-back { background: linear-gradient(90deg, #00f2fe, #4facfe); color: #070d1e; font-weight: bold; border-radius: 10px; padding: 10px 22px; text-decoration: none; display: inline-block; transition: 0.3s; }
        .btn-back:hover { color: #070d1e; transform: scale(1.03); box-shadow: 0 0 20px rgba(0, 242, 254, 0.6); }
        h3 { color: #38bdf8; margin-top: 25px; margin-bottom: 12px; font-weight: 700; }
        p, li { color: #cbd5e1; line-height: 1.7; font-size: 1.05rem; }
    </style>
</head>
<body class="py-4">
    <div class="container" style="max-width: 900px;">
        <div class="mb-4">
            <a href="/" class="btn-back"><i class="fas fa-arrow-left me-2"></i> Bosh sahifaga qaytish</a>
        </div>
        <div class="content-box">
            <div class="d-flex justify-content-between align-items-center flex-wrap gap-2 mb-3 pb-3 border-bottom border-secondary border-opacity-25">
                <span class="badge bg-info text-dark px-3 py-2 fw-bold">{{ lesson.category }}</span>
                <span class="text-secondary"><i class="far fa-clock"></i> O'rganish vaqti: {{ lesson.time }}</span>
            </div>
            <h1 class="fw-bold mb-4">{{ lesson.title }}</h1>
            <div class="lesson-details">
                {{ lesson.content | safe }}
            </div>
            <hr class="border-secondary my-4">
            <div class="d-flex justify-content-between align-items-center">
                <span class="text-secondary small">Muallif: Abdulvohidov</span>
                <a href="/" class="btn-back">Bosh sahifaga qaytish &rarr;</a>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(INDEX_TEMPLATE, lessons=LESSONS, tg_user=TELEGRAM_USER, ig_user=INSTAGRAM_USER)

@app.route("/lesson/<lesson_id>")
def lesson_page(lesson_id):
    lesson = LESSONS.get(lesson_id)
    if not lesson:
        abort(404)
    return render_template_string(LESSON_PAGE_TEMPLATE, lesson=lesson)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
