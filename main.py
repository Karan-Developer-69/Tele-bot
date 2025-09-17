# Install requirement first:
# pip install python-telegram-bot==20.3

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# --- यहाँ अपना Telegram Bot Token डालें ---
BOT_TOKEN = "8498725048:AAG9Fzmk5qZh-ahyvjPrS0dLAkcDOFKAgVo"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "👋 नमस्ते!\n\n"
        "मैं *Cyber Security & Ethical Hacking Training Bot* हूँ।\n\n"
        "📌 आप यहाँ से सीख सकते हैं:\n"
        "1. Cyber Security का बेसिक ज्ञान\n"
        "2. Ethical Hacking का Introduction\n"
        "3. Termux और Kali Linux की बेसिक Training\n"
        "4. Legal Cyber Security Services\n\n"
        "👉 शुरू करने के लिए /help लिखें।"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "🔐 *Available Commands:*\n\n"
        "/start - Bot शुरू करें\n"
        "/help - सभी commands देखें\n"
        "/training - Cyber Security Training Topics\n"
        "/service - हमारी Legal Services जानकारी\n"
        "/contact - संपर्क जानकारी"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

# /training command
async def training(update: Update, context: ContextTypes.DEFAULT_TYPE):
    training_text = (
        "🎓 *Cyber Security & Ethical Hacking Training Topics:*\n\n"
        "1️⃣ Networking Basics\n"
        "2️⃣ Linux & Termux Basics\n"
        "3️⃣ Ethical Hacking Introduction\n"
        "4️⃣ Web Security Basics\n"
        "5️⃣ Malware Analysis (Basics)\n"
        "6️⃣ Penetration Testing Overview\n\n"
        "⚠️ *ध्यान दें:* ये सिर्फ Educational Purpose के लिए है।"
    )
    await update.message.reply_text(training_text, parse_mode="Markdown")

# /service command
async def service(update: Update, context: ContextTypes.DEFAULT_TYPE):
    service_text = (
        "💼 *Legal Cyber Security Services:*\n\n"
        "✔️ Website Security Audit\n"
        "✔️ Android Security Awareness\n"
        "✔️ Data Privacy Guidance\n"
        "✔️ Penetration Testing (Legal)\n\n"
        "👉 अधिक जानकारी के लिए /contact लिखें।"
    )
    await update.message.reply_text(service_text, parse_mode="Markdown")

# /contact command
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact_text = (
        "📧 *संपर्क जानकारी:*\n\n"
        "Email: your-email@example.com\n"
        "Telegram: @YourUsername\n"
        "Website: https://yourwebsite.com\n\n"
        "⚡ Ethical Hacking = सिर्फ Learning और Security Purpose"
    )
    await update.message.reply_text(contact_text, parse_mode="Markdown")


def main():
    # Application बनाओ
    app = Application.builder().token(BOT_TOKEN).build()

    # Command Handlers जोड़ो
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("training", training))
    app.add_handler(CommandHandler("service", service))
    app.add_handler(CommandHandler("contact", contact))

    # Bot चलाओ
    print("✅ Bot चल रहा है...")
    app.run_polling()

if __name__ == "__main__":
    main()
