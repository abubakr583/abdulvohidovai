import os
from flask import Flask, render_template_string, abort

app = Flask(__name__)

TELEGRAM_USER = "vip_abdulvohidov"
INSTAGRAM_USER = "_abhvdv11"

# Barcha darsliklar bazasi (kengaytirilgan va batafsil)
LESSONS = {
    "python-intro": {
        "title": "1. Python Asoslari, O'zgaruvchilar va Ma'lumot Turlari",
        "category": "Python Asoslari",
        "time": "10 daqiqa",
        "badge_class": "badge-python",
        "desc": "Dasturlash sintaksisi, o'zgaruvchilarni e'lon qilish, data types va xotirada saqlanishi.",
        "content": """
<h3>1. Python nima va nega u ommabop?</h3>
<p>Python — o'qilishi oson, sintaksisi toza va kuchli imkoniyatlarga ega yuqori darajali dasturlash tili. U veb-ishlanmalar (Flask, Django), sun'iy intellekt, ma'lumotlar tahlili va Telegram botlar yaratishda yetakchi hisoblanadi.</p>

<h3>2. O'zgaruvchilar (Variables)</h3>
<p>O'zgaruvchi — bu kompyuter xotirasidagi ma'lumot saqlanadigan quticha. Pythonda uning turini oldindan yozish shart emas (dinamik tiplash):</p>
<pre><code># O'zgaruvchilarni e'lon qilish
ism = "Abubakr"          # str (matn)
yosh = 20                # int (butun son)
narx = 49.99             # float (o'nlik son)
talabami = True          # bool (mantiqiy: True yoki False)

print(f"Salom, mening ismim {ism}, yoshim {yosh}da.")</code></pre>

<h3>3. Ma'lumot turlarini tekshirish va o'zgartirish</h3>
<p>Qaysi turdagi ma'lumot ekanligini <code>type()</code> orqali bilib olish mumkin:</p>
<pre><code>x = "150"
print(type(x))  # <class 'str'>

# Matnni butun songa aylantirish (Type Casting):
son_x = int(x)
print(son_x + 50)  # Natija: 200</code></pre>

<h3>Vazifa:</h3>
<p>O'zingizning ismingiz, kasbingiz va haftalik o'qish soatingizni o'zgaruvchilarda saqlang va f-string yordamida ekranga chiqaring.</p>
"""
    },
    "python-conditions": {
        "title": "2. Shart Operatorlari va Sikllar (if, for, while)",
        "category": "Python Asoslari",
        "time": "15 daqiqa",
        "badge_class": "badge-python",
        "desc": "Mantiqiy shartlar (if/elif/else), takrorlanuvchi amallar, break va continue tushunchalari.",
        "content": """
<h3>1. Shart operatorlari (if, elif, else)</h3>
<p>Kod oqimini mantiqiy tekshiruvlar asosida boshqarish:</p>
<pre><code>ball = 85

if ball >= 90:
    print("A'lo (A)")
elif ball >= 75:
    print("Yaxshi (B)")
elif ball >= 60:
    print("Qoniqarli (C)")
else:
    print("Imtihondan yiqildi")</code></pre>

<h3>2. Sikllar: for va while</h3>
<p><strong>for</strong> — ro'yxat, matn yoki berilgan oraliq bo'ylab takrorlash uchun ishlatiladi:</p>
<pre><code># 1 dan 5 gacha sonlarni chiqarish
for son in range(1, 6):
    print(f"Hozirgi qadam: {son}")</code></pre>

<p><strong>while</strong> — berilgan shart rost bo'lib turguncha to'xtovsiz aylanadi:</p>
<pre><code>hisoblagich = 3
while hisoblagich > 0:
    print(f"Boshlanishiga {hisoblagich} soniya qoldi...")
    hisoblagich -= 1
print("Start!")</code></pre>

<h3>3. break va continue</h3>
<ul>
    <li><code>break</code> — siklni majburan to'xtatadi.</li>
    <li><code>continue</code> — joriy qadamni tashlab o'tib, keyingi aylanaga o'tadi.</li>
</ul>
"""
    },
    "python-lists-dicts": {
        "title": "3. Ro'yxatlar va Lug'atlar (Lists & Dictionaries)",
        "category": "Ma'lumotlar Tuzilmasi",
        "time": "12 daqiqa",
        "badge_class": "badge-python",
        "desc": "Katta ma'lumotlar bilan ishlash: indexlar, metodlar (append, pop), kalit-qiymat munosabatlari.",
        "content": """
<h3>1. Ro'yxatlar (List)</h3>
<p>Ro'yxat kvadrat qavslar <code>[]</code> ichida saqlanadi va tartiblangan bo'ladi:</p>
<pre><code>tillari = ["Python", "JavaScript", "C++"]

# Yangi element qo'shish
tillari.append("Go")

# Elementni indeks orqali olish (0 dan boshlanadi)
print(tillari[0])  # Python

# O'chirish
tillari.remove("C++")
print(tillari)  # ['Python', 'JavaScript', 'Go']</code></pre>

<h3>2. Lug'atlar (Dictionary)</h3>
<p>Lug'atlar kalit va qiymat (Key-Value) ko'rinishida saqlanadi. Ma'lumotlarni aniq identsifikator bilan topish uchun ideal vosita:</p>
<pre><code>user = {
    "id": 101,
    "ism": "Abdulvohidov",
    "kasb": "Backend Dasturchi",
    "loyihalar": ["Telegram Bot", "Veb Portal"]
}

# Qiymatlarni olish va yangilash
print(user["ism"])
user["kasb"] = "Full Stack Engineer"
print(user.get("kasb"))</code></pre>
"""
    },
    "python-functions": {
        "title": "4. Funksiyalar va Modulli Dasturlash (def, lambda)",
        "category": "Python Ilg'or",
        "time": "14 daqiqa",
        "badge_class": "badge-python",
        "desc": "Qayta ishlatiluvchi toza kod yozish, argumentlar, return qiymatlari va nomaqbul xatolarni oldini olish.",
        "content": """
<h3>1. Funksiya nima?</h3>
<p>Bir xil kodni qayta-qayta yozmaslik uchun ma'lum bir mantiqni bitta nom ostida jamlash.</p>
<pre><code>def hisobla_bonus(oylik, foiz=10):
    bonus = oylik * (foiz / 100)
    jami = oylik + bonus
    return jami

daromad = hisobla_bonus(5000000, 15)
print(f"Jami to'lanadigan summa: {daromad} so'm")</code></pre>

<h3>2. Args va Kwargs (*args, **kwargs)</h3>
<p>Cheksiz miqdordagi argumentlarni qabul qilish usuli:</p>
<pre><code>def jamla(*sonlar):
    return sum(sonlar)

print(jamla(10, 20, 30, 40))  # Natija: 100</code></pre>
"""
    },
    "telegram-bot": {
        "title": "5. Python'da Professional Telegram Bot Yaratish",
        "category": "Telegram Dev",
        "time": "20 daqiqa",
        "badge_class": "badge-tg",
        "desc": "aiogram 3 orqali tezkor bot, inline tugmalar, callback query va buyruqlarni boshqarish.",
        "content": """
<h3>1. Tayyorgarlik va BotFather</h3>
<p>Telegramda <code>@BotFather</code> ga o'tib <code>/newbot</code> buyrug'i orqali yangi bot va API Token oling.</p>
<pre><code>pip install aiogram</code></pre>

<h3>2. aiogram orqali bot arxitekturasi</h3>
<pre><code>import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "BOT_TOKENINGIZNI_YOZING"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}! Botga xush kelibsiz!")

async def main():
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())</code></pre>
"""
    },
    "figma-basics": {
        "title": "6. Figma Asoslari: Interfeys, Frame va Asosiy Uskunalar",
        "category": "Figma Dizayn",
        "time": "15 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Figma vositalari (Frame, Pen, Shape), o'lchamlar, Desktop va Mobile maketlarini to'g'ri qurish.",
        "content": """
<h3>1. Nega dasturchiga Figma kerak?</h3>
<p>Zamonaviy IT sohasida dasturchi dizaynni tushunishi shart. Figma veb-saytlar va mobil ilovalar dizaynini yaratuvchi brauzerga asoslangan eng kuchli grafik vositadir.</p>

<h3>2. Asosiy hotkeylar (Tezkor tugmalar)</h3>
<ul>
    <li><strong>F (Frame)</strong> — Yangi ramka ochish (Desktop: 1440x1024, iPhone 15: 393x852).</li>
    <li><strong>R (Rectangle)</strong> — Tugma yoki kartochka uchun to'rtburchak chizish.</li>
    <li><strong>T (Text)</strong> — Matn yozish.</li>
    <li><strong>V (Move)</strong> — Oddiy tanlash va siljitish kursoriga qaytish.</li>
    <li><strong>Space (probel) + Sichqoncha</strong> — Ishchi maydon bo'ylab erkin harakatlanish.</li>
</ul>

<h3>3. Grid (Kataklar) tizimi</h3>
<p>Sayt elementlari toza turishi uchun Frame ustiga bosib, o'ng tomondan <strong>Layout Grid</strong> qo'shing:</p>
<p>Veb-saytlar uchun standart: <strong>Columns -> Count: 12, Margin: 80, Gutter: 24</strong>.</p>
"""
    },
    "figma-autolayout": {
        "title": "7. Figma Auto Layout va Komponentlar (Shift + A)",
        "category": "Figma Professional",
        "time": "18 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Moslashuvchan (responsive) tugmalar, kartalar yasash, variantlar va Master Komponentlar.",
        "content": """
<h3>1. Auto Layout siri nima?</h3>
<p>Oddiy chizilgan to'rtburchak ichiga matn yozilsa va matn cho'zilsa, to'rtburchak kichik qolib ketadi. <strong>Auto Layout</strong> esa CSS'dagi <code>flexbox</code> kabi ishlaydi — matn cho'zilishi bilan tugma ham avtomatik kattalashadi!</p>

<h3>2. Auto Layout yasash qadamlari:</h3>
<ol>
    <li>Matn yozing: masalan "Darsni Boshlash".</li>
    <li>Klaviaturada <strong>Shift + A</strong> bosing.</li>
    <li>O'ng tomonda Auto Layout paneli ochiladi:
        <ul>
            <li>Horizontal padding: 24px (yon tomonlar masofasi)</li>
            <li>Vertical padding: 12px (tepa va pastki masofa)</li>
            <li>Corner radius: 10px (burchaklarni yumaloqlash)</li>
            <li>Fill: Tugmaga rang berish (masalan neon ko'k: #00f2fe)</li>
        </ul>
    </li>
</ol>

<h3>3. Komponentlar (Ctrl + Alt + K)</h3>
<p>Bir marta chizilgan elementni (masalan tugma) <strong>Component</strong> qilib qo'ysangiz, saytning 100 ta joyida ishlatsangiz ham, asosiy komponent rangini o'zgartirganingizda 100 ta tugma ham bir onda o'zgaradi!</p>
"""
    },
    "figma-to-code": {
        "title": "8. Figma Dizaynni Toza HTML & CSS Kodga O'tkazish",
        "category": "Figma Frontend",
        "time": "16 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Dev Mode imkoniyatlari, ranglar palitrasi, shriftlar, padding va soyalarni (box-shadow) CSS'ga ko'chirish.",
        "content": """
<h3>1. Dev Mode (Dasturchi rejimi)</h3>
<p>Figma yuqori o'ng burchagida <code>&lt;/&gt;</code> belgisini yoqish orqali Dev Mode rejimiga o'tiladi. Istalgan element bosilganda uning aniq CSS qatorlari ko'rinadi:</p>

<h3>2. Neon tugma kodi qanday olinadi?</h3>
<p>Figma'da Effect -> Drop Shadow beriladi:</p>
<pre><code>/* Figma generatsiya qiladigan CSS */
background: linear-gradient(90deg, #00f2fe 0%, #4facfe 100%);
border-radius: 12px;
box-shadow: 0px 0px 20px rgba(0, 242, 254, 0.7);
color: #070d1e;
font-weight: 700;
padding: 12px 28px;</code></pre>

<h3>3. Dasturchi uchun oltin qoidalar:</h3>
<ul>
    <li>Elementlar orasidagi masofani bilish uchun <strong>Alt (Option)</strong> tugmasini bosib turing.</li>
    <li>Rasmlar va ikonkalar sifatini yo'qotmaslik uchun ularni faqat <strong>SVG</strong> formatda eksport qiling.</li>
</ul>
"""
    }
}

# ASOSIY BOSH SAHIFA
INDEX_TEMPLATE = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python & Figma Academy | Abdulvohidov</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-dark: #070d1e;
            --card-bg: #0f172a;
            --neon-blue: #00f2fe;
            --neon-purple: #9d4edd;
            --neon-figma: #ff7262;
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
            width: 550px;
            height: 550px;
            background: radial-gradient(circle, rgba(0, 242, 254, 0.12) 0%, rgba(0,0,0,0) 70%);
            z-index: -1;
        }
        body::after {
            content: '';
            position: fixed;
            bottom: -20%;
            right: -10%;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(157, 78, 221, 0.12) 0%, rgba(0,0,0,0) 70%);
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

        .badge-python {
            background: rgba(0, 242, 254, 0.1);
            color: var(--neon-blue);
            border: 1px solid rgba(0, 242, 254, 0.3);
            border-radius: 8px;
            padding: 6px 12px;
            font-size: 0.8rem;
            font-weight: 600;
        }
        .badge-figma {
            background: rgba(255, 114, 98, 0.1);
            color: var(--neon-figma);
            border: 1px solid rgba(255, 114, 98, 0.3);
            border-radius: 8px;
            padding: 6px 12px;
            font-size: 0.8rem;
            font-weight: 600;
        }
        .badge-tg {
            background: rgba(34, 158, 217, 0.1);
            color: #229ED9;
            border: 1px solid rgba(34, 158, 217, 0.3);
            border-radius: 8px;
            padding: 6px 12px;
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
    </style>
</head>
<body class="py-4">
    <div class="container">
        <header class="d-flex justify-content-between align-items-center mb-5 flex-wrap gap-3 pb-3 border-bottom border-secondary border-opacity-25">
            <div>
                <h2 class="header-title mb-1">⚡ PYTHON & FIGMA ACADEMY</h2>
                <p class="text-secondary small mb-0">Professional Dasturlash va UI/UX Dizayn Kursi</p>
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
            <div class="col-lg-8">
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

            <div class="col-lg-4">
                <div class="profile-card mb-4">
                    <div class="mb-3">
                        <i class="fas fa-user-astronaut fa-4x text-info"></i>
                    </div>
                    <h4 class="fw-bold mb-1">Abdulvohidov</h4>
                    <p class="text-secondary small mb-3">Python & UI/UX Developer</p>
                    <p class="small text-light">Python orqali server dasturlari va botlar yaratishni, hamda Figma orqali zamonaviy IT dizaynlarini noldan yasashni o'rganing.</p>
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

                <div class="lesson-card text-center p-4">
                    <i class="fab fa-figma fa-3x mb-3 text-danger"></i>
                    <h5 class="fw-bold">Figma & Python Integratsiyasi</h5>
                    <p class="text-secondary small mb-0">Figma'da go'zal dizayn chizib, uni Flask yoki Bot orqali to'liq ishlaydigan loyihaga aylantirish ko'nikmasi.</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

# ALOHIDA KATTA TO'LIQ DARSLIK SAHIFASI
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
        body {
            background-color: #070d1e;
            color: #f8fafc;
            font-family: 'Space Grotesk', sans-serif;
            min-height: 100vh;
        }
        .content-box {
            background-color: #0f172a;
            border: 1px solid rgba(0, 242, 254, 0.25);
            border-radius: 18px;
            padding: 35px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);
            margin-bottom: 50px;
        }
        pre {
            background-color: #040814;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 16px;
            color: #38bdf8;
            font-family: 'Consolas', monospace;
            font-size: 0.95rem;
            overflow-x: auto;
        }
        code {
            color: #00f2fe;
        }
        .btn-back {
            background: linear-gradient(90deg, #00f2fe, #4facfe);
            color: #070d1e;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 22px;
            text-decoration: none;
            display: inline-block;
            transition: 0.3s;
        }
        .btn-back:hover {
            color: #070d1e;
            transform: scale(1.03);
            box-shadow: 0 0 20px rgba(0, 242, 254, 0.6);
        }
        h3 {
            color: #38bdf8;
            margin-top: 25px;
            margin-bottom: 12px;
            font-weight: 700;
        }
        p, li {
            color: #cbd5e1;
            line-height: 1.7;
            font-size: 1.05rem;
        }
    </style>
</head>
<body class="py-4">
    <div class="container" style="max-width: 900px;">
        <div class="mb-4">
            <a href="/" class="btn-back"><i class="fas fa-arrow-left me-2"></i> Barcha darslarga qaytish</a>
        </div>

        <div class="content-box">
            <div class="d-flex justify-content-between align-items-center flex-wrap gap-2 mb-3 pb-3 border-bottom border-secondary border-opacity-25">
                <span class="badge bg-info text-dark px-3 py-2 fw-bold">{{ lesson.category }}</span>
                <span class="text-secondary"><i class="far fa-clock"></i> O'rganish vaqti: {{ lesson.time }}</span>
            </div>
            
            <h1 class="fw-bold mb-4" style="color: #ffffff;">{{ lesson.title }}</h1>
            
            <div class="lesson-details">
                {{ lesson.content | safe }}
            </div>

            <hr class="border-secondary my-4">
            <div class="d-flex justify-content-between align-items-center">
                <span class="text-secondary small">Muallif: Abdulvohidov</span>
                <a href="/" class="btn-back">Keyingi dars &rarr;</a>
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
