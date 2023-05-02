from telegram import Update, Bot
TOKEN = "5567524975:AAHzn2G8Ws6IgE_XRjuW3LTGv2eUtsiXL8E"
bot = Bot(token=TOKEN)

url = "https://tuit.pythonanywhere.com/start"
# webhook info
print(bot.get_webhook_info())
# set webhook
print(bot.set_webhook(url=url))