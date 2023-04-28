from telegram.ext import Updater,CallbackContext
from telegram import ReplyKeyboardMarkup, ReplyMarkup ,InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, Update
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
            text = "Botimizga xush kelibsiz\n Hozircha sizga murojat yo'q ✅"
            bot.send_message(chat_id=chat_id, text=text)

        else:
            text = "Botimizga xush kelibsiz\n Sizning murojatlaringizga javob berish\n uchun hodimlarimiz hamisha tayyor 🥰"
            jobs = db.get_all_jobs()
            keyboard = []
            for job in jobs:
                keyboard.append([job["job_name"]])
            
            reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)