import os
from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Render Environment Variables bo'limidan kalitni oladi
GEMINI_API_KEY = os.getenv("AQ.Ab8RN6Lf7SBvhTpNIy0vLImLlUlrylsVMfYYGrcfIMXRYAN6JA")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None

# Aloqa profillari
TELEGRAM_USER = "vip_abdulvohidov"
INSTAGRAM_USER = "_abhvdv11"

# Saytning HTML sahifasi
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI & Python Portal</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: #0b1329; color: #f8fafc; padding: 20px; }
        .header { display: flex; justify-content: space-between; align-items: center; padding-bottom: 20px; border-bottom: 1px solid #1e293b; max-width: 1200px; margin: 0 auto 30px auto; flex-wrap: wrap; gap: 15px; }
        .logo { font-size: 24px; font-weight: bold; color: #38bdf8; display: flex; align-items: center; gap: 8px; }
        .top-links { display: flex; gap: 10px; }
        .btn-link { padding: 8px 16px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 14px; color: white; display: inline-block; transition: 0.2s; }
        .btn-tg { background-color: #0284c7; }
        .btn-ig { background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); }
        .main-container { display: grid; grid-template-columns: 2fr 1fr; gap: 24px; max-width: 1200px; margin: 0 auto; }
        @media (max-width: 850px) { .main-container { grid-template-columns: 1fr; } }
        
        .card { background-color: #131d38; border: 1px solid #1e293b; border-radius: 12px; padding: 20px; margin-bottom: 20px; }
        .tag { display: inline-block; background-color: #0284c7; color: white; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: bold; margin-bottom: 12px; }
        .duration { color: #94a3b8; font-size: 12px; margin-left: 8px; }
        .card h3 { font-size: 18px; margin-bottom: 8px; color: #f1f5f9; }
        .card p { color: #94a3b8; font-size: 14px; line-height: 1.5; margin-bottom: 15px; }
        .btn-read { background-color: #0284c7; color: white; border: none; padding: 8px 14px; border-radius: 6px; font-size: 13px; font-weight: bold; cursor: pointer; }
        
        .chat-box { background-color: #131d38; border: 1px solid #1e293b; border-radius: 12px; padding: 18px; display: flex; flex-direction: column; height: 500px; }
        .chat-header { font-size: 16px; font-weight: bold; margin-bottom: 14px; color: #38bdf8; }
        .messages { flex-grow: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; padding-right: 5px; margin-bottom: 12px; }
        .msg { padding: 10px 14px; border-radius: 10px; font-size: 14px; line-height: 1.4; max-width: 85%; word-break: break-word; }
        .msg-bot { background-color: #1e293b; color: #f8fafc; align-self: flex-start; }
        .msg-user { background-color: #0284c7; color: white; align-self: flex-end; }
        .chat-input-area { display: flex; gap: 8px; }
        .chat-input-area input { flex-grow: 1; background-color: #0b1329; border: 1px solid #334155; color: white; padding: 10px 14px; border-radius: 8px; outline: none; }
        .chat-input-area button { background-color: #38bdf8; color: #0b1329; border: none; padding: 10px 16px; border-radius: 8px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>

    <div class="header">
        <div class="logo">⚡ AI & PYTHON PORTAL</div>
        <div class="top-links">
            <a href="https://t.me/{{ telegram_user }}" target="_blank" class="btn-link btn-tg">Telegram</a>
            <a href="https://instagram.com/{{ instagram_user }}" target="_blank" class="btn-link btn-ig">Instagram</a>
        </div>
    </div>

    <div class="main-container">
        <div>
            <div class="card">
                <span class="tag">Python Asoslari</span><span class="duration">⏱ 5 daqiqa</span>
                <h3>1. Python Asoslari: O'zgaruvchilar va Ma'lumot Turlari</h3>
                <p>Dasturlash sintaksisi, o'zgaruvchilar, int, float, str va bool turlari bo'yicha to'liq qo'llanma.</p>
                <button class="btn-read">Darsni O'qish →</button>
            </div>

            <div class="card">
                <span class="tag">Python Asoslari</span><span class="duration">⏱ 7 daqiqa</span>
                <h3>2. Shart Operatorlari va Sikllar (if, for, while)</h3>
                <p>Mantiqiy shartlar orqali tekshirish va for, while yordamida takrorlanuvchi amallar bajarish.</p>
                <button class="btn-read">Darsni O'qish →</button>
            </div>

            <div class="card">
                <span class="tag">Python Asoslari</span><span class="duration">⏱ 8 daqiqa</span>
                <h3>3. Ro'yxatlar va Lug'atlar (Lists & Dictionaries)</h3>
                <p>Bir nechta ma'lumotlarni tartibli saqlash va kalit-qiymat ko'rinishida boshqarish usullari.</p>
                <button class="btn-read">Darsni O'qish →</button>
            </div>
        </div>

        <div>
            <div class="card" style="margin-bottom: 15px; padding: 14px; display: flex; flex-direction: column; gap: 8px;">
                <a href="https://t.me/{{ telegram_user }}" target="_blank" class="btn-link btn-tg" style="text-align: center;">🚀 Telegram Lichka</a>
                <a href="https://instagram.com/{{ instagram_user }}" target="_blank" class="btn-link btn-ig" style="text-align: center;">📸 Instagram Profilim</a>
            </div>

            <div class="chat-box">
                <div class="chat-header">🤖 Gemini AI Maslahatchi</div>
                <div class="messages" id="chat-messages">
                    <div class="msg msg-bot">Assalomu alaykum! Python, Telegram botlar yoki AI bo'yicha qanday savolingiz bor?</div>
                </div>
                <form class="chat-input-area" id="chat-form" onsubmit="sendMessage(event)">
                    <input type="text" id="user-input" placeholder="Savolingizni yozing..." autocomplete="off" required>
                    <button type="submit" id="send-btn">Yuborish</button>
                </form>
            </div>
        </div>
    </div>

    <script>
        async function sendMessage(e) {
            e.preventDefault();
            const input = document.getElementById('user-input');
            const messages = document.getElementById('chat-messages');
            const sendBtn = document.getElementById('send-btn');
            const text = input.value.trim();
            if (!text) return;

            // Foydalanuvchi xabari
            messages.innerHTML += `<div class="msg msg-user">${text}</div>`;
            input.value = '';
            messages.scrollTop = messages.scrollHeight;

            sendBtn.disabled = true;
            sendBtn.innerText = '...';

            try {
                const res = await fetch('/api/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: text })
                });
                const data = await res.json();
                messages.innerHTML += `<div class="msg msg-bot">${data.response || data.error}</div>`;
            } catch (err) {
                messages.innerHTML += `<div class="msg msg-bot">Tarmoqda xatolik yuz berdi.</div>`;
            } finally {
                sendBtn.disabled = false;
                sendBtn.innerText = 'Yuborish';
                messages.scrollTop = messages.scrollHeight;
            }
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, telegram_user=TELEGRAM_USER, instagram_user=INSTAGRAM_USER)

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_msg = data.get("message", "")

    if not user_msg:
        return jsonify({"error": "Xabar bo'sh bo'lishi mumkin emas"}), 400

    if not model:
        return jsonify({"error": "Tizimda GEMINI_API_KEY sozlanmagan"}), 500

    try:
        response = model.generate_content(user_msg)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": f"Xatolik: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
