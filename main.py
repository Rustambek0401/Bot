import os
import telebot
from dotenv import load_dotenv
data = load_dotenv()

BOT_TOKEN = os.getenv('bot_token')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['boshla', 'salom'])
def send_welcome(message):
    bot.reply_to(message, f"{message.from_user}")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "salom Rustam qandaysan bolakay")

if __name__ == "__main__":
    bot.infinity_polling()
