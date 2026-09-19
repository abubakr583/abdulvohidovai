from flask import Flask, render_template_string, request, jsonify, abort
from google import genai

app = Flask(__name__)

# Gemini API kaliti
GEMINI_API_KEY = "AQ.Ab8RN6Kr3ubGfWdFlflpLRKLJd3vcmlZvCwuJ2FBZpXEgUrt_g"

# Aloqa profillari
TELEGRAM_USER = "vip_abdulvohidov"
INSTAGRAM_USER = "_abhvdv11"

ai_client = genai.Client(api_key=GEMINI_API_KEY)

DARSLIKLAR = {
    "python-asoslari": {
        "sarlavha": "1. Python Asoslari: O'zgaruvchilar va Ma'lumot Turlari",
        "kategoriya": "Python Asoslari",
        "vaqt": "5 daqiqa",
        "tavsif": "Dasturlash sintaksisi, o'zgaruvchilar, int, float, str va bool turlari.",
        "matn": """
            <h3>Python'da o'zgaruvchilar qanday e'lon qilinadi?</h3>
            <p>Pythonda boshqa tillardek ma'lumot turini qo'lda ko'rsatish shart emas. Qiymat berilganda tur avtomatik belgilanadi.</p>
            <pre><code>ism = "Abubakr"        # str (matn)
yosh = 19              # int (butun son)
balans = 150000.50     # float (o'nlik son)
talabami = True        # bool (rost yoki yolg'on)</code></pre>

            <h3>Foydalanuvchidan ma'lumot olish</h3>
            <p><code>input()</code> funksiyasi konsoldan ma'lumot qabul qiladi va uni matn ko'rinishida saqlaydi:</p>
            <pre><code>ismingiz = input("Ismingiz nima? ")
print(f"Salom, {ismingiz}! Xush kelibsiz.")</code></pre>
        """
    },
    "python-shartlar-va-sikllar": {
        "sarlavha": "2. Shart Operatorlari va Sikllar (if, for, while)",
        "kategoriya": "Python Asoslari",
        "vaqt": "7 daqiqa",
        "tavsif": "Mantiqiy shartlar orqali tekshirish va for, while yordamida takrorlanuvchi amallar.",
        "matn": """
            <h3>If-Elif-Else bilan mantiqiy qarorlar</h3>
            <pre><code>ball = 85

if ball >= 90:
    print("Baho: 5 (A'lo)")
elif ball >= 70:
    print("Baho: 4 (Yaxshi)")
else:
    print("Qayta topshirish kerak")</code></pre>

            <h3>For va While sikli</h3>
            <pre><code># 1 dan 5 gacha sanash
for son in range(1, 6):
    print(f"Sanoq: {son}")

# While bilan shart bajarilguncha aylanish
hisob = 3
while hisob > 0:
    print(f"Boshlanishiga: {hisob}")
    hisob -= 1
print("Start!")</code></pre>
        """
    },
    "python-royxatlar-lugatlar": {
        "sarlavha": "3. Ro'yxatlar va Lug'atlar (Lists & Dictionaries)",
        "kategoriya": "Python Asoslari",
        "vaqt": "8 daqiqa",
        "tavsif": "Bir nechta ma'lumotlarni tartibli saqlash va kalit-qiymat ko'rinishida boshqarish.",
        "matn": """
            <h3>List (Ro'yxat) bilan ishlash</h3>
            <pre><code>dasturchilar = ["Abubakr", "Ali", "Vali"]
dasturchilar.append("Javohir")  # Ro'yxatga yangi qo'shish
print(dasturchilar[0])         # Birinchi element: Abubakr</code></pre>

            <h3>Dictionary (Lug'at) tuzilmasi</h3>
            <pre><code>foydalanuvchi = {
    "username": "vip_abdulvohidov",
    "stars": 250,
    "admin": True
}
print(foydalanuvchi["stars"])  # 250 chiqadi</code></pre>
        """
    },
    "python-funksiyalar-modullar": {
        "sarlavha": "4. Funksiyalar va Modullar (def va import)",
        "kategoriya": "Python Asoslari",
        "vaqt": "6 daqiqa",
        "tavsif": "Kodni toza, ixcham qilish va qayta ishlatiluvchi funksiyalar yaratish.",
        "matn": """
            <h3>Funksiya yaratish</h3>
            <pre><code>def hisobla_foyda(narx, foiz):
    jami = narx + (narx * foiz / 100)
    return jami

natija = hisobla_foyda(100000, 15)
print(f"Yakuniy narx: {natija} so'm")</code></pre>
            <p>O'z kodingizni qismlarga bo'lish uchun modullardan (boshqa fayllardan) foydalaning: <code>from utils import hisobla_foyda</code></p>
        """
    },
    "python-xatoliklar-try-except": {
        "sarlavha": "5. Xatolarni Tutish (Try - Except)",
        "kategoriya": "Python Asoslari",
        "vaqt": "6 daqiqa",
        "tavsif": "Dastur kutilmaganda to'xtab qolmasligi uchun istisnolarni (Exception) to'g'ri boshqarish.",
        "matn": """
            <h3>Nega Try-Except kerak?</h3>
            <p>Agar foydalanuvchi son o'rniga harf yozsa yoki fayl topilmasa, dastur qulab tushmaydi.</p>
            <pre><code>try:
    yosh = int(input("Yoshingizni kiriting: "))
    print(f"Keyingi yili {yosh + 1} ga kirasiz.")
except ValueError:
    print("Iltimos, faqat butun son kiriting!")
except Exception as xato:
    print(f"Noma'lum xatolik: {xato}")</code></pre>
        """
    },
    "python-fayllar-bilan-ishlash": {
        "sarlavha": "6. Fayllar bilan Ishlash (O'qish va Yozish)",
        "kategoriya": "Python Asoslari",
        "vaqt": "7 daqiqa",
        "tavsif": "TXT, JSON fayllarga ma'lumot yozish va undan o'qib olish.",
        "matn": """
            <h3>Faylga matn yozish va saqlash</h3>
            <pre><code>with open("log.txt", "a", encoding="utf-8") as fayl:
    fayl.write("Foydalanuvchi tizimga kirdi\\n")</code></pre>

            <h3>Faylni o'qish</h3>
            <pre><code>with open("log.txt", "r", encoding="utf-8") as fayl:
    matn = fayl.read()
    print(matn)</code></pre>
        """
    },
    "telegram-bot-yaratish": {
        "sarlavha": "7. Python'da Telegram Bot: Tuzilma va Xabarlar",
        "kategoriya": "Telegram Bot",
        "vaqt": "10 daqiqa",
        "tavsif": "Aiogram va python-telegram-bot yordamida ilk botni ishga tushirish.",
        "matn": """
            <h3>Oddiy javob qaytaruvchi bot arxitekturasi</h3>
            <pre><code>from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! Botimizga xush kelibsiz!")

app = ApplicationBuilder().token("BOT_TOKEN_SHU_YERGA").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()</code></pre>
        """
    },
    "telegram-bot-inline-buttons": {
        "sarlavha": "8. Telegram Bot: Inline Tugmalar va Callback",
        "kategoriya": "Telegram Bot",
        "vaqt": "9 daqiqa",
        "tavsif": "Xabar ostidagi tugmalar, bosilganda sahifani almashtirish va harakatlarni tutish.",
        "matn": """
            <h3>Inline Tugmalar Strukturasi</h3>
            <pre><code>from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackQueryHandler, ContextTypes

async def menyu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tugmalar = [
        [InlineKeyboardButton("⭐ Stars Narxlari", callback_data="stars_narx")],
        [InlineKeyboardButton("👨‍💻 Admin bilan aloqa", url="https://t.me/vip_abdulvohidov")]
    ]
    markup = InlineKeyboardMarkup(tugmalar)
    await update.message.reply_text("Bo'limni tanlang:", reply_markup=markup)

async def tugma_bosildi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "stars_narx":
        await query.edit_message_text("100 Stars = 25 000 so'm\\n500 Stars = 115 000 so'm")</code></pre>
        """
    },
    "telegram-bot-stars-tolov": {
        "sarlavha": "9. Telegram Botda Do'kon va To'lov Tizimi",
        "kategoriya": "Telegram Bot",
        "vaqt": "11 daqiqa",
        "tavsif": "Telegram Stars sotish, chek qabul qilish va adminga buyurtmani yuborish mantig'i.",
        "matn": """
            <h3>Buyurtma va To'lovni Tekshirish Jarayoni</h3>
            <p>1. Foydalanuvchi xarid qilmoqchi bo'lgan Stars miqdorini tanlaydi.<br>
            2. Bot to'lov uchun karta raqami yoki havolani beradi.<br>
            3. Foydalanuvchi chek (skrinshot) yuborgach, bot admin guruhiga tasdiqlash tugmasi bilan yo'naltiradi:</p>
            <pre><code>ADMIN_ID = 123456789  # Sizning Telegram ID

async def chek_qabul(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    rasm_id = update.message.photo[-1].file_id
    
    # Adminga yuborish
    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=rasm_id,
        caption=f"Yangi to'lov! Foydalanuvchi: @{user.username} (ID: {user.id})"
    )
    await update.message.reply_text("Chekingiz adminga yuborildi, tez orada tasdiqlanadi!")</code></pre>
        """
    },
    "ai-gemini-integratsiya": {
        "sarlavha": "10. Gemini AI API bilan Bot va Saytga Sun'iy Intellekt Qo'shish",
        "kategoriya": "Sun'iy Intellekt",
        "vaqt": "8 daqiqa",
        "tavsif": "Gemini API orqali dasturlash, matn yaratish va avtomatlashtirish.",
        "matn": """
            <h3>Gemini 2.5 Flash bilan so'rov yuborish</h3>
            <pre><code>from google import genai

client = genai.Client(api_key="API_KALITINGIZ")

javob = client.models.generate_content(
    model='gemini-2.5-flash',
    contents="Python dasturlash tilining eng katta 3 ta afzalligini aytib ber."
)
print(javob.text)</code></pre>
        """
    },
    "ai-video-reels-promptlar": {
        "sarlavha": "11. Reels va TikTok uchun 3D AI Video Promptlari",
        "kategoriya": "AI Video",
        "vaqt": "6 daqiqa",
        "tavsif": "Sun'iy intellekt orqali 9:16 vertikal kinematik 3D animatsiyalar generatsiya qilish.",
        "matn": """
            <h3>Eng yaxshi natija beruvchi tayyor prompt</h3>
            <pre><code>Cinematic 3D animation, Pixar style, vertical video 9:16, modern developer working on laptop with glowing neon elements, high detail, Unreal Engine 5 render, vibrant colors, smooth camera motion, hyper realistic lighting, 4k resolution.</code></pre>
            <p>Ushbu promptni Kling AI, Luma Dream Machine yoki Runway kabi video generatorlarga kiritib yuqori sifatli roliklar olishingiz mumkin.</p>
        """
    },
    "server-render-pythonanywhere": {
        "sarlavha": "12. Loyihalarni Bulutga Joylash: Render va PythonAnywhere",
        "kategoriya": "DevOps & Cloud",
        "vaqt": "9 daqiqa",
        "tavsif": "Yozgan kodlaringiz kompyuter o'chsa ham 24/7 internetda to'xtovsiz ishlashi uchun qo'llanma.",
        "matn": """
            <h3>Asosiy Deploy Fayllari</h3>
            <p>Har bir Flask yoki Web loyiha bulutda ishlashi uchun 3 ta asosiy fayl kerak bo'ladi:</p>
            <ul>
                <li><strong>app.py:</strong> Asosiy server dasturi kodi.</li>
                <li><strong>requirements.txt:</strong> Server o'rnatishi kerak bo'lgan kutubxonalar ro'yxati (flask, gunicorn, google-genai).</li>
                <li><strong>Procfile:</strong> Server qaysi buyruq bilan ishga tushishini bildiruvchi fayl (<code>web: gunicorn app:app</code>).</li>
            </ul>
        """
    }
}

HTML_SHABLON = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI & Python Ta'lim Portali</title>
    <style>
        * { box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; background: #0b1120; color: #f8fafc; }
        
        .navbar-wrap { background: #1e293b; border-bottom: 1px solid #334155; position: sticky; top: 0; z-index: 100; }
        header { padding: 16px 20px; display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; }
        .logo { font-size: 20px; font-weight: 800; color: #38bdf8; text-decoration: none; letter-spacing: 0.5px; }
        
        .social-buttons { display: flex; gap: 10px; }
        .btn-link { display: inline-flex; align-items: center; padding: 8px 14px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 13px; color: white; transition: 0.2s; }
        .btn-tg { background: #0284c7; }
        .btn-tg:hover { background: #0369a1; }
        .btn-insta { background: linear-gradient(45deg, #f09433, #dc2743, #bc1888); }
        .btn-insta:hover { opacity: 0.9; }

        .container { max-width: 1200px; margin: 25px auto; padding: 0 15px; display: grid; grid-template-columns: 2.5fr 1.2fr; gap: 25px; }
        
        .card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 22px; margin-bottom: 20px; }
        .card-tag { display: inline-block; background: #0284c7; color: white; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: bold; margin-bottom: 10px; }
        .card-time { font-size: 12px; color: #94a3b8; margin-left: 8px; }
        .card-title { font-size: 20px; margin: 0 0 10px 0; }
        .card-title a { color: #f8fafc; text-decoration: none; }
        .card-title a:hover { color: #38bdf8; }
        .card-desc { color: #94a3b8; line-height: 1.6; margin-bottom: 15px; font-size: 14px; }
        .read-btn { display: inline-block; background: #0284c7; color: white; padding: 8px 16px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 13px; transition: 0.2s; }
        .read-btn:hover { background: #0369a1; }
        
        .sidebar-panel { display: flex; flex-direction: column; gap: 20px; }
        .side-box { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 20px; }
        .side-title { font-size: 16px; font-weight: bold; color: #f8fafc; margin-bottom: 12px; }

        .chat-widget { background: #1e293b; border: 1px solid #38bdf8; border-radius: 12px; padding: 18px; display: flex; flex-direction: column; height: 440px; }
        .chat-box { flex: 1; overflow-y: auto; background: #090d16; border-radius: 8px; padding: 12px; font-size: 13px; line-height: 1.5; border: 1px solid #334155; display: flex; flex-direction: column; gap: 8px; }
        .msg { padding: 8px 12px; border-radius: 8px; max-width: 85%; }
        .user-msg { background: #0284c7; align-self: flex-end; color: white; }
        .ai-msg { background: #334155; align-self: flex-start; color: #f8fafc; }
        .input-row { display: flex; gap: 8px; margin-top: 12px; }
        .input-row input { flex: 1; padding: 10px; border-radius: 6px; border: 1px solid #334155; background: #090d16; color: white; outline: none; }
        .input-row button { background: #38bdf8; color: #0b1120; border: none; border-radius: 6px; padding: 10px 14px; font-weight: bold; cursor: pointer; }

        pre { background: #090d16; padding: 14px; border-radius: 8px; overflow-x: auto; border: 1px solid #334155; }
        code { color: #38bdf8; font-family: Consolas, monospace; font-size: 13px; }
        
        @media (max-width: 850px) {
            .container { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>

<div class="navbar-wrap">
    <header>
        <a href="/" class="logo">⚡ AI & PYTHON PORTAL</a>
        <div class="social-buttons">
            <a href="https://t.me/{{ tg_user }}" target="_blank" class="btn-link btn-tg">✈️ Telegram</a>
            <a href="https://instagram.com/{{ insta_user }}" target="_blank" class="btn-link btn-insta">📷 Instagram</a>
        </div>
    </header>
</div>

<div class="container">
    <main>
        {% if maqola %}
            <article class="card">
                <a href="/" style="color: #38bdf8; text-decoration: none; font-size: 14px; font-weight: bold;">← Barcha darslarga qaytish</a>
                <div style="margin-top: 15px;">
                    <span class="card-tag">{{ maqola.kategoriya }}</span>
                    <span class="card-time">⏱ {{ maqola.vaqt }}</span>
                </div>
                <h1 style="font-size: 24px; margin: 15px 0;">{{ maqola.sarlavha }}</h1>
                <div style="line-height: 1.8; color: #cbd5e1;">{{ maqola.matn|safe }}</div>
            </article>
        {% else %}
            <div style="margin-bottom: 20px;">
                <h2 style="font-size: 22px; margin: 0 0 5px 0;">Amaliy Darslar To'plami</h2>
                <p style="color: #94a3b8; font-size: 14px; margin: 0;">Noldan boshlab to'liq amaliyotgacha bo'lgan darsliklar</p>
            </div>
            {% for kalit, dars in darslar.items() %}
            <article class="card">
                <div>
                    <span class="card-tag">{{ dars.kategoriya }}</span>
                    <span class="card-time">⏱ {{ dars.vaqt }}</span>
                </div>
                <h3 class="card-title"><a href="/dars/{{ kalit }}">{{ dars.sarlavha }}</a></h3>
                <p class="card-desc">{{ dars.tavsif }}</p>
                <a href="/dars/{{ kalit }}" class="read-btn">Darsni O'qish →</a>
            </article>
            {% endfor %}
        {% endif %}
    </main>

    <aside class="sidebar-panel">
        <div class="side-box">
            <div class="side-title">Bog'lanish</div>
            <p style="color: #94a3b8; font-size: 13px; line-height: 1.5; margin-bottom: 15px;">
                Savollar, hamkorlik yoki bot buyurtmalari uchun bevosita yozishingiz mumkin:
            </p>
            <div style="display: flex; flex-direction: column; gap: 10px;">
                <a href="https://t.me/{{ tg_user }}" target="_blank" class="btn-link btn-tg" style="justify-content: center;">✈️ Telegram Lichka</a>
                <a href="https://instagram.com/{{ insta_user }}" target="_blank" class="btn-link btn-insta" style="justify-content: center;">📷 Instagram Profilim</a>
            </div>
        </div>

        <div class="chat-widget">
            <div class="side-title" style="color: #38bdf8; margin: 0 0 10px 0;">🤖 Gemini AI Maslahatchi</div>
            <div class="chat-box" id="chatBox">
                <div class="msg ai-msg">Assalomu alaykum! Python, Telegram botlar yoki AI bo'yicha qanday savolingiz bor?</div>
            </div>
            <div class="input-row">
                <input type="text" id="userInput" placeholder="Savolingizni yozing..." onkeypress="if(event.key==='Enter') savolBer()">
                <button onclick="savolBer()">Yuborish</button>
            </div>
        </div>
    </aside>
</div>

<script>
    async function savolBer() {
        const input = document.getElementById('userInput');
        const box = document.getElementById('chatBox');
        const text = input.value.trim();
        if (!text) return;

        box.innerHTML += `<div class="msg user-msg">${text}</div>`;
        input.value = '';
        box.scrollTop = box.scrollHeight;

        const yuklanmoqda = document.createElement('div');
        yuklanmoqda.className = 'msg ai-msg';
        yuklanmoqda.innerText = 'AI yozmoqda...';
        box.appendChild(yuklanmoqda);
        box.scrollTop = box.scrollHeight;

        try {
            const res = await fetch('/api/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ savol: text })
            });
            const data = await res.json();
            yuklanmoqda.innerText = data.javob;
        } catch (e) {
            yuklanmoqda.innerText = "Xatolik yuz berdi. Qayta urinib ko'ring.";
        }
        box.scrollTop = box.scrollHeight;
    }
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_SHABLON, darslar=DARSLIKLAR, maqola=None, tg_user=TELEGRAM_USER, insta_user=INSTAGRAM_USER)

@app.route('/dars/<dars_nomi>')
def dars_sahifasi(dars_nomi):
    if dars_nomi not in DARSLIKLAR:
        abort(404)
    return render_template_string(HTML_SHABLON, darslar=DARSLIKLAR, maqola=DARSLIKLAR[dars_nomi], tg_user=TELEGRAM_USER, insta_user=INSTAGRAM_USER)

@app.route('/api/chat', methods=['POST'])
def chat():
    malumot = request.get_json()
    savol = malumot.get('savol', '')
    try:
        buyruq = (
            "Sen foydali AI yordamchisisan. Foydalanuvchi qanday yozishidan qat'i nazar, "
            "har doim faqat sof o'zbek tilida, samimiy va tushunarli qilib javob ber. "
            "O'zbekcha so'zlashuv iboralarini to'g'ri tushun va do'stona, aniq javob qaytar.\n\n"
            f"Foydalanuvchi: {savol}"
        )
        response = ai_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=buyruq
        )
        return jsonify({"javob": response.text})
    except Exception as e:
        return jsonify({"javob": f"Xatolik: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)