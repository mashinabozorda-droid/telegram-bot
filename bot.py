import telebot
import os

TOKEN = os.getenv("6673316226:AAFqXnQqvz6pXegT8VLMQ3axck0SFN40RZ4")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Salom {message.from_user.first_name}! Bot ishlayapti ✅"
    )

print("Bot ishga tushdi...")

bot.infinity_polling()
