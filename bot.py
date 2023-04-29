from telegram.ext import Updater,CallbackContext
from telegram import ReplyKeyboardMarkup, ReplyMarkup ,InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, Update
from db import DB

db = DB("db.json")


class Samtuit:
    def __init__(self) -> None:
        self.chat_id = None
    
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
            reply_markup = ReplyKeyboardMarkup([["Murojat qoldirish"]], resize_keyboard=True)
            bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)
    
    def qurey(self, update:Update,context:CallbackContext):
        bot = context.bot
        chat_id = int(update.message.chat_id)
        text = "Siz keimg murojat qoldirmoqchisiz?"
        jobs = db.get_all_jobs()
        keyboard = []
        for job in jobs:
            keyboard.append([InlineKeyboardButton(job['job_name'], callback_data=f"chat_id__{job['chat_id']}")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)

    def psot_job(self,update:Update,context:CallbackContext):
        query = update.callback_query
        chat_id = int(query.message.chat_id)
        data = query.data
        job_id = data.split("__")[1]
        self.chat_id = job_id
        text = "Sizning murojatingizni qabul \nqilishga tayyormiz😊, surovingizni yozing📨"
        query.edit_message_text(text=text)