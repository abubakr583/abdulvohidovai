import os
from flask import Flask, render_template_string, abort

app = Flask(__name__)

TELEGRAM_USER = "vip_abdulvohidov"
INSTAGRAM_USER = "_abhvdv11"

LESSONS = {
    # 1-BLOK: SCRATCH DARSLIKLARI
    "scratch-intro": {
        "title": "1. Scratch Asoslari: Vizual Bloklar va Spritelar",
        "category": "Scratch",
        "time": "10 daqiqa",
        "badge_class": "badge-scratch",
        "desc": "Dasturlash mantig'iga kirish: Sprite (qahramonlar), sahna va rangli bloklar bilan ishlash.",
        "content": """
<h3>1. Scratch nima va u kimlar uchun?</h3>
<p>Scratch — MIT universiteti tomonidan yaratilgan vizual blokli dasturlash muhiti. Bu yerda sintaksis xatolari bo'lmaydi, mantiq esa to'liq professional dasturlash kabi ishlaydi.</p>

<h3>2. Asosiy bloklar turlari:</h3>
<ul>
    <li><strong>Motion (Harakat - Ko'k):</strong> Qahramonni harakatlantirish (masalan: 10 qadam oldinga, 15 gradus burilish).</li>
    <li><strong>Looks (Ko'rinish - Binafsharang):</strong> Matn chiqarish ("Salom!"), kostyumni almashtirish, o'lchamni o'zgartirish.</li>
    <li><strong>Events (Hodisalar - Sariq):</strong> O'yinni boshlash kaliti: <code>Yashil bayroqcha bosilganda</code>, <code>Probel tugmasi bosilganda</code>.</li>
    <li><strong>Control (Boshqaruv - To'q sariq):</strong> Sikllar va shartlar: <code>Forever (Har doim)</code>, <code>Repeat (Takrorlash)</code>, <code>If...then</code>.</li>
</ul>

<h3>3. Birinchi sodda animatsiya:</h3>
<p>Mushukchani harakatlantirish kodi:</p>
<pre><code>[Qachonki Yashil Bayroq bosilsa]
[Har doim takrorla]:
    [10 qadam yur]
    [Keyingi kostyumga o't]
    [Agar chetga tegsa, orqaga qayt]</code></pre>
"""
    },
    "scratch-variables-game": {
        "title": "2. Scratch'da O'zgaruvchilar va Birinchi O'yin",
        "category": "Scratch",
        "time": "15 daqiqa",
        "badge_class": "badge-scratch",
        "desc": "O'yinlarda ochko hisoblash (Score), jonlar (Lives) va to'qnashuvlarni (Sensors) tekshirish.",
        "content": """
<h3>1. O'zgaruvchi (Variable) nima?</h3>
<p>O'yindagi har qanday raqamli natija — bu o'zgaruvchi. Masalan, olma tutganda ochko ko'payishi yoki to'siqqa tekkanda jon kamayishi.</p>

<h3>2. Olma Tutish (Catch the Apple) o'yini algoritmi:</h3>
<ol>
    <li>Savat (Bowl) spriteni yarating va uni sichqoncha koordinatasi bo'yicha harakatlantiring.</li>
    <li>Olma (Apple) spriteni tepadan pastga qulatish:</li>
</ol>
<pre><code>[Qachonki Yashil Bayroq bosilsa]
[Hisob = 0 qilib belgilansin]
[Har doim takrorla]:
    [y o'qini -5 ga o'zgartir (pastga tushish)]
    [Agar Savatga tegsa]:
        [Hisobni +1 ga oshir]
        [x: tasodifiy (-200 dan 200 gacha), y: 160 ga bor]</code></pre>
<p>Mana shu mantiq barcha zamonaviy o'yinlar fundamentidir!</p>
"""
    },

    # 2-BLOK: PYTHON ASOSLARI
    "python-intro": {
        "title": "3. Python Sintaksisi va Data Types",
        "category": "Python Asoslari",
        "time": "10 daqiqa",
        "badge_class": "badge-python",
        "desc": "O'zgaruvchilar, asosiy turlar: int, float, str, bool va f-string bilan ishlash.",
        "content": """
<h3>1. Dinamik tiplash va o'zgaruvchilar</h3>
<p>Pythonda ma'lumot turlari avtomatik aniqlanadi:</p>
<pre><code>ism = "Abdulvohidov"   # str (matn)
yosh = 20               # int (butun son)
ball = 94.5             # float (o'nlik son)
status = True           # bool (True/False)

print(f"Talaba: {ism}, Bali: {ball}")</code></pre>
<p>Matn va sonlarni birlashtirishda doimo <code>f-string</code> dan foydalaning.</p>
"""
    },
    "python-conditions": {
        "title": "4. Shart Operatorlari: if, elif, else",
        "category": "Python Asoslari",
        "time": "12 daqiqa",
        "badge_class": "badge-python",
        "desc": "Mantiqiy ifodalar, taqqoslash operatorlari (==, !=, >, <) va shartli boshqaruv.",
        "content": """
<h3>1. Shartlar orqali tekshirish</h3>
<pre><code>yosh = 18

if yosh >= 18:
    print("Xush kelibsiz! Kirishga ruxsat.")
elif yosh >= 16:
    print("Faqat ota-ona ruxsati bilan.")
else:
    print("Hali erta, kirish taqiqlanadi.")</code></pre>
<p>Python bloklarni ajratish uchun jingalak qavslar o'rniga <strong>bo'shliq (Indentation - 4 ta probel)</strong> ishlatadi.</p>
"""
    },
    "python-loops": {
        "title": "5. Sikllar: for va while",
        "category": "Python Asoslari",
        "time": "12 daqiqa",
        "badge_class": "badge-python",
        "desc": "Qayta takrorlanuvchi jarayonlar, range funksiyasi, break va continue amallari.",
        "content": """
<h3>1. for sikli:</h3>
<pre><code># 1 dan 10 gacha bo'lgan toq sonlarni chiqarish:
for son in range(1, 11, 2):
    print(f"Toq son: {son}")</code></pre>

<h3>2. while sikli va to'xtatish:</h3>
<pre><code>qadam = 0
while True:
    qadam += 1
    if qadam == 5:
        print("To'xtatildi!")
        break</code></pre>
"""
    },
    "python-lists": {
        "title": "6. Ro'yxatlar (Lists) va Tuple",
        "category": "Python Asoslari",
        "time": "14 daqiqa",
        "badge_class": "badge-python",
        "desc": "Indekslash, slicing, element qo'shish (append), o'chirish (pop, remove) va saralash.",
        "content": """
<h3>1. Ro'yxat metodlari</h3>
<pre><code>kurslar = ["Python", "Scratch", "Figma"]

kurslar.append("Telegram Bot")  # Oxiriga qo'shish
kurslar.insert(1, "Django")     # 1-indeksga qo'shish
kurslar.remove("Scratch")       # O'chirish

print(kurslar[0])     # Python
print(kurslar[-1])    # Eng oxirgi element
print(len(kurslar))   # Elementlar soni</code></pre>
"""
    },
    "python-dicts": {
        "title": "7. Lug'atlar (Dictionaries) va To'plamlar (Sets)",
        "category": "Python Asoslari",
        "time": "15 daqiqa",
        "badge_class": "badge-python",
        "desc": "Key-Value arxitekturasi, tezkor qidiruv, takrorlanmas to'plamlar bilan ishlash.",
        "content": """
<h3>1. Lug'atlar (dict)</h3>
<pre><code>developer = {
    "username": "vip_abdulvohidov",
    "stack": ["Python", "Flask", "aiogram"],
    "active": True
}

# Xavfsiz qiymat olish:
stack = developer.get("stack")
developer["tajriba"] = "2 yil"

print(developer.keys())    # Barcha kalitlar
print(developer.values())  # Barcha qiymatlar</code></pre>
"""
    },
    "python-functions": {
        "title": "8. Funksiyalar: def, return, *args, **kwargs",
        "category": "Python Ilg'or",
        "time": "15 daqiqa",
        "badge_class": "badge-python",
        "desc": "Kodni toza va modulli yozish, nomaqbul takrorlanishlarni bartaraf etish.",
        "content": """
<h3>1. Mukammal funksiya namunasi:</h3>
<pre><code>def hisobla_chegirma(narx, foiz=10):
    chegirma = narx * (foiz / 100)
    yakuniy = narx - chegirma
    return yakuniy

print(hisobla_chegirma(100000, 20)) # 80000.0</code></pre>
"""
    },
    "python-oop": {
        "title": "9. OOP: Obyektga Yo'naltirilgan Dasturlash",
        "category": "Python Ilg'or",
        "time": "18 daqiqa",
        "badge_class": "badge-python",
        "desc": "Class, __init__ konstruktori, Object, Meros olish (Inheritance) va Encapsulation.",
        "content": """
<h3>1. Class va Object</h3>
<pre><code>class Foydalanuvchi:
    def __init__(self, ism, status):
        self.ism = ism
        self.status = status

    def info(self):
        return f"{self.ism} - {self.status}"

admin = Foydalanuvchi("Abubakr", "Administrator")
print(admin.info())</code></pre>
"""
    },
    "python-files-errors": {
        "title": "10. Fayllar bilan ishlash va Try-Except",
        "category": "Python Ilg'or",
        "time": "14 daqiqa",
        "badge_class": "badge-python",
        "desc": "TXT/JSON fayllarni o'qish va yozish, xatoliklarni (Exception handling) to'g'ri ushlash.",
        "content": """
<h3>1. Xatolarni xavfsiz ushlash:</h3>
<pre><code>try:
    son = int("salom")
except ValueError as e:
    print(f"Xatolik yuz berdi: {e}")
finally:
    print("Tekshiruv yakunlandi.")</code></pre>

<h3>2. Faylga yozish va o'qish:</h3>
<pre><code>with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Yangi foydalanuvchi kirdi\\n")</code></pre>
"""
    },

    # 3-BLOK: TELEGRAM BOTLAR
    "tgbot-setup": {
        "title": "11. aiogram 3: Bot Arxitekturasi va Sozlash",
        "category": "Telegram Bot",
        "time": "15 daqiqa",
        "badge_class": "badge-tg",
        "desc": "BotFather orqali token olish, aiogram 3 kutubxonasini o'rnatish va asinxron ishga tushirish.",
        "content": """
<h3>1. Zamonaviy aiogram 3 kodi:</h3>
<pre><code>import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

bot = Bot(token="TOKENINGIZ")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(msg: types.Message):
    await msg.answer(f"Salom, {msg.from_user.first_name}! Botimizga xush kelibsiz!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())</code></pre>
"""
    },
    "tgbot-keyboards": {
        "title": "12. Inline va Reply Tugmalar (Keyboards)",
        "category": "Telegram Bot",
        "time": "16 daqiqa",
        "badge_class": "badge-tg",
        "desc": "Foydalanuvchi uchun qulay menyu, InlineKeyboardMarkup va callback query hodisalarini ushlash.",
        "content": """
<h3>1. Inline Tugmalar yasash:</h3>
<pre><code>from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tugmalar = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒 Kurslar", callback_data="courses")],
    [InlineKeyboardButton(text="📞 Bog'lanish", url="https://t.me/vip_abdulvohidov")]
])</code></pre>
"""
    },
    "tgbot-database": {
        "title": "13. Botga SQLite Ma'lumotlar Bazasini Ulanish",
        "category": "Telegram Bot",
        "time": "18 daqiqa",
        "badge_class": "badge-tg",
        "desc": "Foydalanuvchilar ID sini bazada saqlash, takroriy ro'yxatdan o'tishni tekshirish va xabar yuborish.",
        "content": """
<h3>1. SQLite bilan ishlash:</h3>
<pre><code>import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users (
    telegram_id INTEGER PRIMARY KEY,
    ism TEXT
)''')
conn.commit()</code></pre>
"""
    },
    "tgbot-payments": {
        "title": "14. Telegram Stars va To'lov Tizimlari",
        "category": "Telegram Bot",
        "time": "20 daqiqa",
        "badge_class": "badge-tg",
        "desc": "Telegram Stars orqali raqamli mahsulot va kurslarni bot orqali avtomatik sotish.",
        "content": """
<h3>1. Telegram Stars invoices yaratish:</h3>
<p>Telegram Stars orqali to'lov qabul qilishda vositachisiz to'g'ridan-to'g'ri Telegram platformasi xizmatidan foydalaniladi.</p>
<pre><code>from aiogram.types import LabeledPrice

prices = [LabeledPrice(label="Python Darslik", amount=50)] # 50 Telegram Stars</code></pre>
"""
    },

    # 4-BLOK: FIGMA & UI/UX DIZAYN
    "figma-intro": {
        "title": "15. Figma Asoslari: Ishchi Maydon va Frame'lar",
        "category": "Figma UI/UX",
        "time": "12 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Interfeys, Frame (F), Shape (R, O), Pen tool va to'g'ri loyiha strukturasini qurish.",
        "content": """
<h3>1. Nega dasturchiga Figma kerak?</h3>
<p>Sayt yoki ilovani kodlashdan oldin uning barcha elementlari (rangi, joylashuvi, o'lchamlari) Figmada loyihalanadi.</p>
<h3>2. Standart Frame o'lchamlari:</h3>
<ul>
    <li>Desktop: 1440 x 1024 px</li>
    <li>Mobile (iPhone 15 Pro): 393 x 852 px</li>
</ul>
"""
    },
    "figma-autolayout": {
        "title": "16. Auto Layout (Shift + A) Sehri",
        "category": "Figma UI/UX",
        "time": "16 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Elementlarni responsive qilish, padding, gap va moslashuvchan tugmalar yaratish.",
        "content": """
<h3>1. Auto Layout qanday ishlaydi?</h3>
<p>Har qanday matnni tanlab <strong>Shift + A</strong> tugmasini bosing. U avtomatik tarzda moslashuvchan konteynerga aylanadi. Matn ko'payganda ramka ham o'zi kengayadi!</p>
"""
    },
    "figma-components": {
        "title": "17. Komponentlar va Variantlar (Ctrl + Alt + K)",
        "category": "Figma UI/UX",
        "time": "15 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Qayta ishlatiluvchi Master Komponentlar, Hover holatlari va dizayn tizimi (Design System).",
        "content": """
<h3>1. Master Component nima?</h3>
<p>Bitta Master tugma yaratib, undan 50 ta nusxa (Instance) olsangiz, asosiy tugmaning rangini o'zgartirganingizda qolgan 50 tasi bir lahzada yangilanadi.</p>
"""
    },
    "figma-typography-colors": {
        "title": "18. Tipografika, Ranglar va Qorong'u (Dark) Mavzu",
        "category": "Figma UI/UX",
        "time": "14 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Kontrast qoidalari, neon ranglar palitrasi, Google Fonts (Space Grotesk, Inter) integratsiyasi.",
        "content": """
<h3>1. Dark Theme siri:</h3>
<p>Hech qachon toza qora (#000000) ishlatmang! To'q ko'k yoki kulrang fonlar (#070d1e, #0f172a) neon elementlarni yanada jozibador qiladi.</p>
"""
    },
    "figma-prototyping": {
        "title": "19. Prototip Yasash va Animatsiyalar",
        "category": "Figma UI/UX",
        "time": "16 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Sahifalarni bir-biriga bog'lash, Smart Animate, tugmalarning bosilish effektlari.",
        "content": """
<h3>1. Smart Animate imkoniyati:</h3>
<p>Prototype bo'limiga o'tib, tugmani boshqa sahifaga tortasiz. Transition turiga <strong>Smart Animate</strong> qo'ysangiz, elementlar silliq siljiydi.</p>
"""
    },
    "figma-to-code": {
        "title": "20. Figma'dan Toza CSS va HTML Kodga O'tkazish",
        "category": "Figma to Web",
        "time": "18 daqiqa",
        "badge_class": "badge-figma",
        "desc": "Dev Mode, box-shadow, linear-gradient, SVG ikonkalar va loyihani to'liq kodga ko'chirish.",
        "content": """
<h3>1. Dizaynni kodga o'girish amaliyoti:</h3>
<p>Figma Dev Mode sizga tayyor CSS kodlarni beradi:</p>
<pre><code>/* Neon Tugma CSS */
background: linear-gradient(90deg, #00f2fe 0%, #4facfe 100%);
box-shadow: 0px 0px 24px rgba(0, 242, 254, 0.7);
border-radius: 12px;
color: #070d1e;
font-weight: bold;</code></pre>
<p>Shunday qilib dizayn to'g'ridan-to'g'ri veb-saytga aylanadi!</p>
"""
    }
}

# ASOSIY SAHIFA
INDEX_TEMPLATE = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abdulvohidov Academy | Python, Scratch, Figma</title>
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
    </style>
</head>
<body class="py-4">
    <div class="container">
        <header class="d-flex justify-content-between align-items-center mb-5 flex-wrap gap-3 pb-3 border-bottom border-secondary border-opacity-25">
            <div>
                <h2 class="header-title mb-1">⚡ ABDULVOHIDOV ACADEMY</h2>
                <p class="text-secondary small mb-0">Scratch, Python & Figma — 20 ta Professional Amaliy Dars</p>
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
                <div class="profile-card mb-4 sticky-top" style="top: 20px;">
                    <div class="mb-3">
                        <i class="fas fa-laptop-code fa-4x text-info"></i>
                    </div>
                    <h4 class="fw-bold mb-1">Abdulvohidov</h4>
                    <p class="text-secondary small mb-3">Full-Stack & UI/UX Mentor</p>
                    <p class="small text-light">Scratch orqali mantiqni, Python orqali backend va botlarni, hamda Figma orqali chiroyli dizayn yaratishni to'liq o'rganing.</p>
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

# KATTA DARSLIK SAHIFASI
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
        code { color: #00f2fe; }
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
