from telegram.ext import Updater,CallbackContext
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, Update
from db import DB

db = DB("db.json")


class Samtuit:
    def start(self,update:Update,context:CallbackContext):
        bot = context.bot
        chat_id = int(update.message.chat_id)
        job = db.get_job(chat_id)
        admin = db.get_admin(chat_id)
        
        if admin:
            print(admin)
            text = "You are admin"
            bot.send_message(chat_id=chat_id, text=text)

        elif job:
            print(job)
            text = "You have a job"
            bot.send_message(chat_id=chat_id, text=text)

        else:
            print(chat_id)
            text = "user"
            bot.send_message(chat_id=chat_id, text=text)