from telegram.ext import CallbackQueryHandler, Updater, CommandHandler, MessageHandler
from telegram import Update
from bot import Samtuit

bot = Samtuit()

TOKEN = "5567524975:AAHzn2G8Ws6IgE_XRjuW3LTGv2eUtsiXL8E"
updater = Updater(token=TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler("start", bot.start))

updater.start_polling()
updater.idle()