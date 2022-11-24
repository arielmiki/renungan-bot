import telebot
import os
from view import DefaultView
from fetcher import ODBFetcher
from datetime import datetime

bot = telebot.TeleBot(os.environ["BOT_TOKEN"], parse_mode=None)
default_view = DefaultView()
odb_fetcher = ODBFetcher()

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Send `/today` for get daily devotional", parse_mode='Markdown')


@bot.message_handler(commands=['today'])
def send_today_devotion(message):
    devotion = odb_fetcher.get_devotion("id", datetime.now())
    md = default_view.get_markdown(devotion)
    print(md)
    bot.reply_to(message, md,  parse_mode="Markdown")

bot.infinity_polling()
