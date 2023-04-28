from telegram.ext import Updater,CallbackContext
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, Update
from db import DB

db = DB("db.json")


class Samtuit:
    def start(self,update:Update,context:CallbackContext):
        bot = context.bot
        chat_id = update.message.chat_id
        db.add_job(chat_id, "start")

        reply_markup = ReplyKeyboardMarkup([["/start"]], resize_keyboard=True)
        bot.send_message(chat_id=chat_id, text="Hello", reply_markup=reply_markup)