import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("Watch Now 🎬", url="https://t.me/yourlink")],
        [InlineKeyboardButton("Join Channel 🔔", url="https://t.me/yourchannel")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await context.bot.send_message(
        chat_id='@yourchannelusername',
        text="🔥 Frieren Hindi Dubbed Season 1\nEP 01–25",
        reply_markup=reply_markup
    )

    await update.message.reply_text("Post sent to channel ✅")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("post", post))
app.run_polling()
