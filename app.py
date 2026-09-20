import os
from flask import Flask, render_template_string, abort

app = Flask(__name__)

TELEGRAM_USER = "vip_abdulvohidov"
INSTAGRAM_USER = "_abhvdv11"

# Barcha xizmatlar ro'yxati
SERVICES = [
    {
        "title": "Figma: Logotip & Brending",
        "category": "Dizayn Xizmati",
        "badge_class": "badge-figma",
        "icon": "fa-bezier-curve",
        "desc": "Kompaniya, Telegram kanallar va bizneslar uchun zamonaviy vektor logotiplar, favicon va firma uslubini noldan chizish.",
        "order_msg": "Salom, menga logotip va brending xizmati kerak edi."
    },
    {
        "title": "Figma: Sayt & Ilova UI/UX Dizayni",
        "category": "Dizayn Xizmati",
        "badge_class": "badge-figma",
        "icon": "fa-mobile-screen-button",
        "desc": "Zamonaviy veb-saytlar, mobil ilovalar va lending sahifalar uchun Auto Layout asosida moslashuvchan interfeys dizayni.",
        "order_msg": "Salom, menga veb-sayt yoki mobil ilova dizayni kerak edi."
    },
    {
        "title": "Telegram Stars Savdo Boti",
        "category": "Bot Xizmati",
        "badge_class": "badge-tg",
        "icon": "fa-star",
        "desc": "Telegram Stars valyutasi orqali raqamli mahsulotlar, obunalar yoki yulduzlar savdosi uchun avtomatlashtirilgan xavfsiz bot.",
        "order_msg": "Salom, menga Telegram Stars savdo boti kerak edi."
    },
    {
        "title": "Kino & Seriallar Boti",
        "category": "Bot Xizmati",
        "badge_class": "badge-tg",
        "icon": "fa-film",
        "desc": "Kinolar kodi bo'yicha qidiruv, majburiy kanalga a'zolik (obuna tekshirish), katta kino bazasiga ega tezkor bot.",
        "order_msg": "Salom, menga Kino bot yaratish xizmati kerak edi."
    },
    {
        "title": "SMM & Nakrutka Boti",
        "category": "Bot Xizmati",
        "badge_class": "badge-tg",
        "icon": "fa-chart-line",
        "desc": "Telegram, Instagram va TikTok uchun obunachi, layk va ko'rishlar buyurtma qilish va hisob to'ldirish tizimli bot.",
        "order_msg": "Salom, menga SMM nakrutka boti kerak edi."
    },
    {
        "title": "Telegram Bot Builder (Konstruktor)",
        "category": "Bot Xizmati",
        "badge_class": "badge-tg",
        "icon": "fa-cubes",
        "desc": "Foydalanuvchilar o'zlarining shaxsiy botlarini hech qanday kodsiz yaratishi va boshqarishi uchun konstruktor bot.",
        "order_msg": "Salom, menga Bot Builder tizimi kerak edi."
    },
    {
        "title": "VIP Kanal & Avto-to'lov Boti",
        "category": "Bot Xizmati",
        "badge_class": "badge-tg",
        "icon": "fa-money-bill-wave",
        "desc": "Yopiq Telegram guruh va kanallarga oylik pullik obunalarni qabul qilish (Click, Payme) va muddati tugagach avtomatik chiqarish.",
        "order_msg": "Salom, menga pullik VIP kanal uchun avto-to'lov boti kerak edi."
    },
    {
        "title": "Internet Magazin (E-Commerce) Boti",
        "category": "Bot Xizmati",
        "badge_class": "badge-tg",
        "icon": "fa-cart-shopping",
        "desc": "Tovarlar katalogi, savatcha (korzina), yetkazib berish manzili va to'lov integratsiyasiga ega to'liq do'kon boti.",
        "order_msg": "Salom, menga Telegram do'kon boti kerak edi."
    }
]

# 20 ta darslik bazasi
LESSONS = {
    "scratch-intro": {
        "title": "1. Scratch Asoslari: Vizual Bloklar va Spritelar",
        "category": "Scratch",
        "time": "10 daqiqa",
        "badge_class": "badge-scratch",
        "desc": "Dasturlash mantig'iga kirish: Sprite, sahna va rangli bloklar bilan ishlash.",
        "content": "<h3>Scratch nima?</h3><p>Scratch — blokli dasturlash tili bo'lib, algoritmik fikrlashni shakllantirish uchun dunyodagi eng zo'r platformadir.</p>"
    },
    "scratch-variables-game": {
        "title": "2. Scratch'da O'zgaruvchilar va Birinchi O'yin",
        "category": "Scratch",
        "time": "15 daqiqa",
        "badge_class": "badge-scratch",
        "desc": "O'yinlarda ochko hisoblash (Score), jonlar va sensorlar.",
        "content": "<h3>O'zgaruvchilar</h3><p>O'yinda ochko, vaqt va jonlarni saqlash mexanizmlari.</p>"
    },
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
        "content": "<h3>Fayllar bilan ishlash</h3><pre><code>with open('data.txt', 'w') as f:\\n    f.write('Salom')</code></pre>"
    },
    "tgbot-setup": {
        "title": "11. aiogram 3: Bot Arxitekturasi",
        "category": "Telegram Bot",
        "time": "15 daqiqa",
        "badge_class": "badge-tg",
        "desc": "aiogram 3 o'rnatish, dispatcher va asinxron arxitektura.",
        "content": "<h3>aiogram 3</h3><p>Zamonaviy asinxron Telegram botlar poydevori.</p>"
    },
    "tgbot-keyboards": {
        "title": "12. Inline va Reply Tugmalar",
        "category": "Telegram Bot",
        "time": "16 daqiqa",
        "badge_class": "badge-tg",
        "desc": "Tugmali menyular, callback_data va havolalar ulash.",
        "content": "<h3>Inline Tugmalar</h3><p>Foydalanuvchi qulayligi uchun klaviaturalar.</p>"
    },
    "tgbot-database": {
        "title": "13. Botga SQLite Bazasini Ulanish",
        "category": "Telegram Bot",
        "time": "18 daqiqa",
        "badge_class": "badge-tg",
        "desc": "Foydalanuvchilarni saqlash va tekshirish tizimi.",
        "content": "<h3>SQLite Baza</h3><pre><code>CREATE TABLE users (id INT, ism TEXT)</code></pre>"
    },
    "tgbot-payments": {
        "title": "14. Telegram Stars va To'lovlar",
        "category": "Telegram Bot",
        "time": "20 daqiqa",
        "badge_class": "badge-tg",
        "desc": "Bot orqali avtomatlashtirilgan to'lovlarni qabul qilish.",
        "content": "<h3>To'lovlar</h3><p>Telegram Stars orqali tezkor savdo tizimi.</p>"
    },
    "figma-intro": {
        "title": "15. Figma Asoslari va Frame'lar",
        "category": "Figma UI/UX",
        "time": "12 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Interfeys, Frame (F), Shape va loyiha strukturasini qurish.",
        "content": "<h3>Figma Vositalari</h3><p>Desktop va Mobile o'lchamlari bilan to'g'ri ishlash.</p>"
    },
    "figma-autolayout": {
        "title": "16. Auto Layout (Shift + A) Sehri",
        "category": "Figma UI/UX",
        "time": "16 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Elementlarni responsive qilish va moslashuvchan tugmalar.",
        "content": "<h3>Auto Layout</h3><p>Har qanday elementni moslashuvchan konteynerga aylantirish.</p>"
    },
    "figma-components": {
        "title": "17. Komponentlar va Variantlar",
        "category": "Figma UI/UX",
        "time": "15 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Master Komponentlar va yagona dizayn tizimi.",
        "content": "<h3>Komponentlar</h3><p>Bitta o'zgartirish bilan butun loyihani yangilash.</p>"
    },
    "figma-typography-colors": {
        "title": "18. Tipografika va Qorong'u Mavzu",
        "category": "Figma UI/UX",
        "time": "14 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Kontrast qoidalari, neon ranglar va to'g'ri shriftlar.",
        "content": "<h3>Ranglar Tanlash</h3><p>Ko'zni charchatmaydigan qorong'u rejim dizayni.</p>"
    },
    "figma-prototyping": {
        "title": "19. Prototip Yasash va Smart Animate",
        "category": "Figma UI/UX",
        "time": "16 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Sahifalarni o'zaro bog'lash va animatsiyalar.",
        "content": "<h3>Prototip</h3><p>Dizaynni bosiladigan va jonli ko'rinishga keltirish.</p>"
    },
    "figma-to-code": {
        "title": "20. Figma'dan Toza CSS Kodga O'tkazish",
        "category": "Figma to Web",
        "time": "18 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Dev Mode, box-shadow va dizaynni kodga ko'chirish.",
        "content": "<h3>Dev Mode</h3><p>Figma elementlarini brauzer uchun CSS ga aylantirish.</p>"
    }
}

INDEX_TEMPLATE = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abdulvohidov Academy & IT Services</title>
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

        .section-heading {
            font-size: 1.6rem;
            font-weight: 800;
            color: #38bdf8;
            border-bottom: 2px solid rgba(0, 242, 254, 0.2);
            padding-bottom: 10px;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            gap: 12px;
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

        .custom-card {
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
        .custom-card:hover {
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

        .btn-order {
            display: block;
            text-align: center;
            background: linear-gradient(90deg, #10b981, #059669, #10b981);
            background-size: 200% auto;
            color: #ffffff;
            font-weight: 700;
            text-decoration: none;
            border-radius: 10px;
            padding: 11px 20px;
            box-shadow: 0 0 18px rgba(16, 185, 129, 0.45);
            transition: all 0.3s ease;
        }
        .btn-order:hover {
            color: #ffffff;
            transform: scale(1.02);
            box-shadow: 0 0 28px rgba(16, 185, 129, 0.8);
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
    </style>
</head>
<body class="py-4">
    <div class="container">
        <!-- HEADER -->
        <header class="d-flex justify-content-between align-items-center mb-5 flex-wrap gap-3 pb-3 border-bottom border-secondary border-opacity-25">
            <div>
                <h2 class="header-title mb-1">⚡ ABDULVOHIDOV ACADEMY & SERVICES</h2>
                <p class="text-secondary small mb-0">Professional Ta'lim & Tayyor IT Xizmatlari</p>
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
            <!-- ASOSIY QISM (XIZMATLAR VA DARSLAR) -->
            <div class="col-lg-8">
                
                <!-- 1. XIZMATLAR BLOKI -->
                <div class="mb-5">
                    <div class="section-heading">
                        <i class="fas fa-briefcase text-info"></i>
                        <span>Bizning Xizmatlarimiz (Buyurtma Berish)</span>
                    </div>
                    <div class="row g-3">
                        {% for s in services %}
                        <div class="col-md-6">
                            <div class="custom-card">
                                <div>
                                    <div class="d-flex justify-content-between align-items-center mb-3">
                                        <span class="{{ s.badge_class }}">{{ s.category }}</span>
                                        <i class="fas {{ s.icon }} text-info fs-5"></i>
                                    </div>
                                    <h5 class="fw-bold mb-2">{{ s.title }}</h5>
                                    <p class="text-secondary small mb-4">{{ s.desc }}</p>
                                </div>
                                <a href="https://t.me/{{ tg_user }}?text={{ s.order_msg }}" target="_blank" class="btn-order">
                                    <i class="fab fa-telegram me-1"></i> Buyurtma berish &rarr;
                                </a>
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </div>

                <!-- 2. TA'LIM PORTALI (20 TA DARSLIK) -->
                <div>
                    <div class="section-heading">
                        <i class="fas fa-graduation-cap text-warning"></i>
                        <span>O'quv Darsliklari (20 ta Amaliy Dars)</span>
                    </div>
                    <div class="row g-3">
                        {% for key, item in lessons.items() %}
                        <div class="col-md-6">
                            <div class="custom-card">
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

            </div>

            <!-- O'NG TOMON: SHAXSIY PROFIL -->
            <div class="col-lg-4">
                <div class="profile-card mb-4 sticky-top" style="top: 20px;">
                    <div class="mb-3">
                        <i class="fas fa-laptop-code fa-4x text-info"></i>
                    </div>
                    <h4 class="fw-bold mb-1">Abdulvohidov</h4>
                    <p class="text-secondary small mb-3">Full-Stack & UI/UX Developer</p>
                    <p class="small text-light">Telegram botlar yaratish, Figma'da professional brending va veb-dasturlash bo'yicha buyurtmalarni qabul qilaman.</p>
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
            </div>
        </div>
    </div>
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
    return render_template_string(INDEX_TEMPLATE, services=SERVICES, lessons=LESSONS, tg_user=TELEGRAM_USER, ig_user=INSTAGRAM_USER)

@app.route("/lesson/<lesson_id>")
def lesson_page(lesson_id):
    lesson = LESSONS.get(lesson_id)
    if not lesson:
        abort(404)
    return render_template_string(LESSON_PAGE_TEMPLATE, lesson=lesson)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
