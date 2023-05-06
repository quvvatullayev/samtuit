from telegram import Update, Bot
TOKEN = "5677023630:AAGdskZAvZwdRix213Ho28QaN-NZVcQtuU8"
bot = Bot(token=TOKEN)

url = "https://tuit.pythonanywhere.com/"
# webhook info
print(bot.get_webhook_info())
# set webhook
print(bot.set_webhook(url=url))