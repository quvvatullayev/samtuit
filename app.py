from telegram.ext import CallbackQueryHandler, Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, Bot
from bot import Samtuit
from flask import Flask, request


app = Flask(__name__)
bot = Samtuit()
TOKEN = "5677023630:AAGdskZAvZwdRix213Ho28QaN-NZVcQtuU8"

@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello World!"

@app.route("/start", methods=["GET", "POST"])
def start():
    updater = Updater(token=TOKEN, use_context=True)
    update = Update.de_json(request.get_json(force=True), updater.bot)

    updater.dispatcher.add_handler(CommandHandler("start", bot.start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text("Murojat qoldirish"), bot.qurey))
    updater.dispatcher.add_handler(MessageHandler(Filters.text("Job qo'shish📥"), bot.add_job))
    updater.dispatcher.add_handler(MessageHandler(Filters.text("Job o'chirish📤"), bot.delete_job))
    updater.dispatcher.add_handler(MessageHandler(Filters.text("admin qo'shish📥"), bot.add_admin))
    updater.dispatcher.add_handler(MessageHandler(Filters.text("admin o'chirish📤"), bot.delete_admin))
    updater.dispatcher.add_handler(CallbackQueryHandler(bot.psot_job, pattern="chat_id__"))
    updater.dispatcher.add_handler(CallbackQueryHandler(bot.get_request, pattern="request_"))
    updater.dispatcher.add_handler(CallbackQueryHandler(bot.get_notrequest, pattern="notrequest_"))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, bot.post))
    updater.dispatcher.process_update(update = update)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
