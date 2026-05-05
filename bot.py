import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Termux Eğitim Botuna Hoş Geldin!")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "/start - Başlat\n/termux - Bilgi")

@bot.message_handler(commands=['termux'])
def termux(message):
    bot.reply_to(message, "📲 Termux komutları:\n\npkg update && pkg upgrade")

print("Bot çalışıyor...")
bot.infinity_polling()
