from telegram.ext import CallbackQueryHandler, Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update
from bot import Samtuit

bot = Samtuit()

TOKEN = "5567524975:AAHzn2G8Ws6IgE_XRjuW3LTGv2eUtsiXL8E"
updater = Updater(token=TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler("start", bot.start))
updater.dispatcher.add_handler(MessageHandler(Filters.text("Murojat qoldirish"), bot.qurey))
updater.dispatcher.add_handler(CallbackQueryHandler(bot.psot_job, pattern="chat_id__"))

updater.start_polling()
updater.idle()