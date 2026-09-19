import os
from flask import Flask, render_template_string, request, jsonify
from google import genai

app = Flask(__name__)

GEMINI_API_KEY = os.getenv("AQ.Ab8RN6Lf7SBvhTpNIy0vLImLlUlrylsVMfYYGrcfIMXRYAN6JA", "")

client = None
if GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)

TELEGRAM_USER = "vip_abdulvohidov"
INSTAGRAM_USER = "_abhvdv11"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI & Python Ta'lim Portali</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { background-color: #0b1329; color: #ffffff; font-family: 'Segoe UI', sans-serif; min-height: 100vh; }
        .header-title { color: #38bdf8; font-weight: 800; }
        .lesson-card { background-color: #111e38; border: 1px solid #1e293b; border-radius: 12px; padding: 24px; margin-bottom: 20px; }
        .lesson-badge { background-color: #0284c7; font-size: 0.85rem; border-radius: 6px; padding: 4px 10px; }
        .chat-container { background-color: #111e38; border: 1px solid #0284c7; border-radius: 14px; padding: 20px; height: 520px; display: flex; flex-direction: column; }
        .chat-box { flex-grow: 1; overflow-y: auto; border: 1px solid #1e293b; border-radius: 8px; background-color: #0b1329; padding: 12px; margin-bottom: 12px; }
        .chat-msg { margin-bottom: 10px; padding: 8px 12px; border-radius: 8px; font-size: 0.95rem; max-width: 85%; word-wrap: break-word; }
        .msg-bot { background-color: #1e293b; color: #e2e8f0; align-self: flex-start; margin-right: auto; }
        .msg-user { background-color: #0284c7; color: #ffffff; align-self: flex-end; margin-left: auto; }
        .btn-social-tg { background-color: #0284c7; color: white; font-weight: bold; }
        .btn-social-ig { background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); color: white; font-weight: bold; }
    </style>
</head>
<body class="py-4">
    <div class="container">
        <div class="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
            <h2 class="header-title mb-0">⚡ AI & PYTHON PORTAL</h2>
            <div class="d-flex gap-2">
                <a href="https://t.me/{{ tg_user }}" target="_blank" class="btn btn-social-tg btn-sm px-3"><i class="fab fa-telegram"></i> Telegram</a>
                <a href="https://instagram.com/{{ ig_user }}" target="_blank" class="btn btn-social-ig btn-sm px-3"><i class="fab fa-instagram"></i> Instagram</a>
            </div>
        </div>

        <div class="row">
            <div class="col-lg-7">
                <div class="lesson-card">
                    <span class="badge lesson-badge mb-2">Python Asoslari</span>
                    <h5 class="text-white mt-2">1. Python Asoslari: O'zgaruvchilar va Ma'lumot Turlari</h5>
                    <p class="text-secondary small">Dasturlash sintaksisi, o'zgaruvchilar, int, float, str va bool turlari.</p>
                </div>
                <div class="lesson-card">
                    <span class="badge lesson-badge mb-2">Python Asoslari</span>
                    <h5 class="text-white mt-2">2. Shart Operatorlari va Sikllar (if, for, while)</h5>
                    <p class="text-secondary small">Mantiqiy shartlar orqali tekshirish va for, while yordamida takrorlanuvchi amallar.</p>
                </div>
                <div class="lesson-card">
                    <span class="badge lesson-badge mb-2">Python Asoslari</span>
                    <h5 class="text-white mt-2">3. Ro'yxatlar va Lug'atlar (Lists & Dictionaries)</h5>
                    <p class="text-secondary small">Bir nechta ma'lumotlarni tartibli saqlash va kalit-qiymat ko'rinishida boshqarish.</p>
                </div>
            </div>

            <div class="col-lg-5">
                <div class="chat-container">
                    <h6 class="text-white mb-2"><i class="fas fa-robot text-info"></i> Gemini AI Maslahatchi</h6>
                    <div class="chat-box d-flex flex-column" id="chatBox">
                        <div class="chat-msg msg-bot">Assalomu alaykum! Python yoki AI bo'yicha qanday savolingiz bor?</div>
                    </div>
                    <div class="input-group">
                        <input type="text" id="userInput" class="form-control bg-dark text-white border-secondary" placeholder="Savolingizni yozing..." onkeypress="if(event.key==='Enter') sendMessage()">
                        <button class="btn btn-info text-white fw-bold px-3" onclick="sendMessage()">Yuborish</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        async function sendMessage() {
            const input = document.getElementById('userInput');
            const text = input.value.trim();
            if (!text) return;

            const chatBox = document.getElementById('chatBox');
            chatBox.innerHTML += `<div class="chat-msg msg-user">${text}</div>`;
            input.value = '';
            chatBox.scrollTop = chatBox.scrollHeight;

            const loadingId = 'loading-' + Date.now();
            chatBox.innerHTML += `<div class="chat-msg msg-bot" id="${loadingId}">Javob yozilmoqda...</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;

            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: text})
                });
                const data = await response.json();
                document.getElementById(loadingId).remove();
                if (data.reply) {
                    chatBox.innerHTML += `<div class="chat-msg msg-bot">${data.reply}</div>`;
                } else {
                    chatBox.innerHTML += `<div class="chat-msg msg-bot text-danger">Xatolik: ${data.error}</div>`;
                }
            } catch (err) {
                document.getElementById(loadingId).remove();
                chatBox.innerHTML += `<div class="chat-msg msg-bot text-danger">Server xatosi</div>`;
            }
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, tg_user=TELEGRAM_USER, ig_user=INSTAGRAM_USER)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_msg = data.get("message", "").strip()

    if not user_msg:
        return jsonify({"error": "Bo'sh xabar"}), 400
    if not client:
        return jsonify({"error": "Kalit topilmadi"}), 500

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_msg,
        )
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
