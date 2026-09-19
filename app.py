from flask import Flask, render_template_string, request, jsonify, abort
from google import genai

app = Flask(__name__)

# Siz olgan tayyor Gemini API kaliti
GEMINI_API_KEY = "AQ.Ab8RN6Kr3ubGfWdFlflpLRKLJd3vcmlZvCwuJ2FBZpXEgUrt_g"

# Sizning Telegram va Instagram profilingiz (@ belgisiz)
TELEGRAM_USER = "vip_abdulvohidov"
INSTAGRAM_USER = "_abhvdv11"

ai_client = genai.Client(api_key=GEMINI_API_KEY)

DARSLIKLAR = {
    "python-asoslari": {
        "sarlavha": "1. Python Asoslari: Sintaksis va Turlar",
        "kategoriya": "Python",
        "vaqt": "5 daqiqa",
        "tavsif": "Dasturlash sintaksisi, matnlar, sonlar va mantiqiy amallar bilan ishlash.",
        "matn": """
            <h3>O'zgaruvchilar bilan ishlash</h3>
            <pre><code>ism = "Abubakr"
yosh = 19
narx = 45.5
status = True</code></pre>
            <p>Foydalanuvchi kiritgan ma'lumotni qabul qilish: <code>qiymat = input('Yozing: ')</code></p>
        """
    },
    "python-shartlar-va-sikllar": {
        "sarlavha": "2. Shartlar va Sikllar (if / for / while)",
        "kategoriya": "Python",
        "vaqt": "7 daqiqa",
        "tavsif": "Qarorlar qabul qilish va jarayonlarni avtomatlashtirish.",
        "matn": """
            <h3>If / Else tekshiruvi</h3>
            <pre><code>ball = 85
if ball >= 70:
    print("Muvaffaqiyatli topshirdingiz!")
else:
    print("Qayta harakat qiling.")</code></pre>
            <h3>For sikli orqali takrorlash</h3>
            <pre><code>for qadam in range(1, 6):
    print(f"Amal: {qadam}")</code></pre>
        """
    },
    "telegram-bot-yaratish": {
        "sarlavha": "3. Python'da Telegram Bot Dasturlash",
        "kategoriya": "Bot Development",
        "vaqt": "10 daqiqa",
        "tavsif": "Inline tugmalar, menyular va xabarlarni qabul qiluvchi bot mantig'i.",
        "matn": """
            <h3>Kutubxona: python-telegram-bot</h3>
            <pre><code>from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tugmalar = [
        [InlineKeyboardButton("Telegram Lichka ✈️", url="https://t.me/vip_abdulvohidov")],
        [InlineKeyboardButton("Instagram 📷", url="https://instagram.com/_abhvdv11")]
    ]
    await update.message.reply_text("Xush kelibsiz!", reply_markup=InlineKeyboardMarkup(tugmalar))

app = ApplicationBuilder().token("BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()</code></pre>
        """
    },
    "ai-prompt-muhandisligi": {
        "sarlavha": "4. Sun'iy Intellekt: Professional Promptlar",
        "kategoriya": "Sun'iy Intellekt",
        "vaqt": "8 daqiqa",
        "tavsif": "ChatGPT va Gemini'dan xatosiz kod va aniq natija olish sirlari.",
        "matn": """
            <h3>Dasturlash uchun eng samarali prompt strukturasi</h3>
            <pre><code>"Sen senior Python dasturchisisan. Menga Flask yordamida AI chat vidjeti yaratish kodini yozib ber. Kod tushunarli, zamonaviy usulda va izohlar bilan bo'lsin."</code></pre>
            <h3>Xatolikni tekshirish buyrug'i</h3>
            <pre><code>"Ushbu koddagi muammoni top va optimal yechimini ko'rsat: [KODINGIZ]"</code></pre>
        """
    },
    "ai-video-reels-promptlar": {
        "sarlavha": "5. Reels va TikTok uchun AI 3D Video Yaratish",
        "kategoriya": "AI Video",
        "vaqt": "6 daqiqa",
        "tavsif": "Sun'iy intellekt orqali vertikal animatsion videolar yaratish.",
        "matn": """
            <h3>Kinematik 3D Animatsiya Prompti (9:16)</h3>
            <pre><code>Cinematic 3D animation, Pixar style, vertical video 9:16, modern developer working on laptop with glowing neon elements, high detail, Unreal Engine 5 render, vibrant colors, smooth camera motion.</code></pre>
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
        
        .navbar-wrap { background: #1e293b; border-bottom: 1px solid #334155; }
        header { padding: 18px 20px; display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; }
        .logo { font-size: 22px; font-weight: 800; color: #38bdf8; text-decoration: none; }
        
        .social-buttons { display: flex; gap: 10px; }
        .btn-link { display: inline-flex; align-items: center; padding: 9px 16px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 14px; color: white; transition: 0.2s; }
        .btn-tg { background: #0284c7; }
        .btn-tg:hover { background: #0369a1; }
        .btn-insta { background: linear-gradient(45deg, #f09433, #dc2743, #bc1888); }
        .btn-insta:hover { opacity: 0.9; }

        .container { max-width: 1200px; margin: 30px auto; padding: 0 15px; display: grid; grid-template-columns: 2.5fr 1.2fr; gap: 30px; }
        
        .card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 22px; margin-bottom: 22px; }
        .card-tag { display: inline-block; background: #0284c7; color: white; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: bold; margin-bottom: 10px; }
        .card-title { font-size: 20px; margin: 0 0 10px 0; }
        .card-title a { color: #f8fafc; text-decoration: none; }
        .card-title a:hover { color: #38bdf8; }
        .card-desc { color: #94a3b8; line-height: 1.6; margin-bottom: 15px; font-size: 15px; }
        .read-btn { display: inline-block; background: #0284c7; color: white; padding: 8px 16px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 13px; }
        
        .sidebar-panel { display: flex; flex-direction: column; gap: 25px; }
        .side-box { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 20px; }
        .side-title { font-size: 16px; font-weight: bold; color: #f8fafc; margin-bottom: 12px; }

        /* AI Chat Vidjeti */
        .chat-widget { background: #1e293b; border: 1px solid #38bdf8; border-radius: 12px; padding: 18px; display: flex; flex-direction: column; height: 420px; }
        .chat-box { flex: 1; overflow-y: auto; background: #090d16; border-radius: 8px; padding: 12px; font-size: 13px; line-height: 1.5; border: 1px solid #334155; display: flex; flex-direction: column; gap: 8px; }
        .msg { padding: 8px 12px; border-radius: 8px; max-width: 85%; }
        .user-msg { background: #0284c7; align-self: flex-end; color: white; }
        .ai-msg { background: #334155; align-self: flex-start; color: #f8fafc; }
        .input-row { display: flex; gap: 8px; margin-top: 12px; }
        .input-row input { flex: 1; padding: 10px; border-radius: 6px; border: 1px solid #334155; background: #090d16; color: white; outline: none; }
        .input-row button { background: #38bdf8; color: #0b1120; border: none; border-radius: 6px; padding: 10px 14px; font-weight: bold; cursor: pointer; }

        pre { background: #090d16; padding: 12px; border-radius: 8px; overflow-x: auto; border: 1px solid #334155; }
        code { color: #38bdf8; font-family: Consolas, monospace; }
    </style>
</head>
<body>

<div class="navbar-wrap">
    <header>
        <a href="/" class="logo">⚡ AI & PYTHON PORTAL</a>
        <div class="social-buttons">
            <a href="https://t.me/{{ tg_user }}" target="_blank" class="btn-link btn-tg">✈️ Telegram Lichka</a>
            <a href="https://instagram.com/{{ insta_user }}" target="_blank" class="btn-link btn-insta">📷 Instagram</a>
        </div>
    </header>
</div>

<div class="container">
    <main>
        {% if maqola %}
            <article class="card">
                <a href="/" style="color: #38bdf8; text-decoration: none; font-size: 14px; font-weight: bold;">← Darsliklar ro'yxatiga qaytish</a>
                <div style="margin-top: 15px;"><span class="card-tag">{{ maqola.kategoriya }}</span></div>
                <h1 style="font-size: 26px; margin: 15px 0;">{{ maqola.sarlavha }}</h1>
                <div style="line-height: 1.8; color: #cbd5e1;">{{ maqola.matn|safe }}</div>
            </article>
        {% else %}
            {% for kalit, dars in darslar.items() %}
            <article class="card">
                <span class="card-tag">{{ dars.kategoriya }}</span>
                <h2 class="card-title"><a href="/dars/{{ kalit }}">{{ dars.sarlavha }}</a></h2>
                <p class="card-desc">{{ dars.tavsif }}</p>
                <a href="/dars/{{ kalit }}" class="read-btn">Darsni Boshlash →</a>
            </article>
            {% endfor %}
        {% endif %}
    </main>

    <aside class="sidebar-panel">
        <div class="side-box">
            <div class="side-title">Menga Bog'lanish</div>
            <p style="color: #94a3b8; font-size: 13px; line-height: 1.5; margin-bottom: 15px;">Bot yaratish, sayt yasash yoki savollar bo'yicha to'g'ridan-to'g'ri yozishingiz mumkin:</p>
            <div style="display: flex; flex-direction: column; gap: 10px;">
                <a href="https://t.me/{{ tg_user }}" target="_blank" class="btn-link btn-tg" style="justify-content: center;">✈️ Telegram orqali yozish</a>
                <a href="https://instagram.com/{{ insta_user }}" target="_blank" class="btn-link btn-insta" style="justify-content: center;">📷 Instagram profilim</a>
            </div>
        </div>

        <div class="chat-widget">
            <div class="side-title" style="color: #38bdf8; margin: 0 0 10px 0;">🤖 Gemini AI Yordamchi</div>
            <div class="chat-box" id="chatBox">
                <div class="msg ai-msg">Salom! Dasturlash yoki AI haqida savolingiz bo'lsa, marhamat yozing!</div>
            </div>
            <div class="input-row">
                <input type="text" id="userInput" placeholder="Savol yozing..." onkeypress="if(event.key==='Enter') savolBer()">
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
        yuklanmoqda.innerText = 'AI o\\'ylamoqda...';
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
            yuklanmoqda.innerText = "Xatolik yuz berdi.";
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
        # Sun'iy intellektga har doim faqat o'zbek tilida javob berishini qat'iy buyuramiz
        buyruq = (
            "Sen foydali AI yordamchisisan. Foydalanuvchi qanday yozishidan qat'i nazar, "
            "har doim faqat sof o'zbek tilida, samimiy va tushunarli qilib javob ber. "
            "O'zbekcha so'zlashuv iboralarini (masalan: 'nma gap', 'qalesan', 'salom') to'g'ri tushun "
            "va do'stona, aniq o'zbekcha javob qaytar.\n\n"
            f"Foydalanuvchi: {savol}"
        )
        response = ai_client.models.generate_content(
            model='gemini-3.6-flash',
            contents=buyruq
        )
        return jsonify({"javob": response.text})
    except Exception as e:
        return jsonify({"javob": f"Xatolik: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)