from telegram.ext import Updater,CallbackContext
from telegram import ReplyKeyboardMarkup, ReplyMarkup ,InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, Update
from db import DB

db = DB("db.json")


class Samtuit:
    def __init__(self) -> None:
        self.job_id = None
        self.user_id = None
        self.user_text = None
    
    def start(self,update:Update,context:CallbackContext):
        bot = context.bot
        chat_id = int(update.message.chat_id)
        job = db.get_job(chat_id)
        admin = db.get_admin(chat_id)
        
        if admin:
            text = "Botimizga xush kelibsiz\n Siz bot adminlaridan birisiz ✅"
            bot.send_message(chat_id=chat_id, text=text)

            keyboard = [
                [KeyboardButton("Job qo'shish📥"), KeyboardButton("Job o'chirish📤")],
                [KeyboardButton("admin qo'shish📥"), KeyboardButton("admin o'chirish📤")]
            ]

            reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            bot.send_message(chat_id=chat_id, text="Kerakli bo'limni tanlang", reply_markup=reply_markup)


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
        self.job_id = int(job_id)
        text = "Sizning murojatingizni qabul \nqilishga tayyormiz😊, surovingizni yozing📨"
        query.edit_message_text(text=text)

    def post(self,update:Update,context:CallbackContext):
        bot = context.bot
        chat_id = int(update.message.chat_id)
        text = update.message.text
        job_id = self.job_id
        jobs = db.search_job(str(chat_id))
        admin = db.get_admin(chat_id)

        if "admin_name:" in text and 'delet_admin_name:' not in text and (admin or chat_id == 677038439):
            text = text.split('\n')
            admin_chat_id = text[1].split(':')[1]
            admin_name = text[0].split(':')[1]
            db.add_admin(admin_chat_id, admin_name)
            text = "Admin qo'shildi ✅"
            bot.send_message(chat_id=chat_id, text=text)
        
        elif "job_name:" in text and 'delet_job_name:' not in text and (admin or chat_id == 677038439):
            text = text.split('\n')
            job_name = text[0].split(':')[1]
            job_chat_id = text[1].split(':')[1]
            db.add_job(job_name, job_chat_id)
            text = "Job qo'shildi ✅"
            bot.send_message(chat_id=chat_id, text=text)
            "Sizning javobingiz yuborildi😊"

        elif "delet_job_name:" in text and (admin or chat_id == 677038439):
            text = text.split('\n')
            job_name = text[0].split(':')[1]
            print(job_name)
            db.delete_job(job_name)
            text = "Job o'chirildi ✅"
            bot.send_message(chat_id=chat_id, text=text)

        elif "delet_admin_name:" in text and (admin or chat_id == 677038439):
            # delete_admin_name:ogabek
            text = text.split(':')
            admin_name = text[1]
            db.delete_admin(admin_name)
            text = "Admin o'chirildi ✅"
            bot.send_message(chat_id=chat_id, text=text)


        elif jobs:
            text1 = f"Sizning javobingiz yuborildi😊\n\n\Sizga berilgan savol:{self.user_text}\n\nSizning javob:{text}"
            bot.send_message(chat_id=chat_id, text=text1)
            text = f"Savolingiz:{self.user_text}\n\nJavob:{text}"
            bot.send_message(chat_id=self.user_id, text=text)

        else:
            self.user_text = text
            text = f'Sizga yangi murojat kelib tushdi:\n\n' + text
            keyboard = [
                    [
                        InlineKeyboardButton(text="javob bersh", callback_data=f'request_{chat_id}'), 
                        InlineKeyboardButton(text='rad etish', callback_data=f"notrequest_{chat_id}")
                    ]
                ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            bot.send_message(chat_id=job_id, text=text, reply_markup = reply_markup)
            text_main = update.message.text
            text = f"Sizning savolingiz:{text_main}\n\nSizning murojatingiz muvaffaqiyatli jo'natildi😊,\n javobni kuting"
            bot.send_message(chat_id=chat_id, text=text)

    def get_request(self,update:Update,context:CallbackContext):
        query = update.callback_query
        chat_id = query.message.chat_id
        data = query.data
        user_id = data.split('_')[1]
        self.user_id = user_id

        text = f"Savol:{self.user_text}\n\nJavobni yozing😊"
        query.edit_message_text(text=text, reply_markup=None)

    def get_notrequest(self,update:Update,context:CallbackContext):
        query = update.callback_query
        data = query.data
        user_id = data.split('_')[1]
        self.user_id = None
        text = "Murojat rad etildi 😊"
        query.edit_message_text(text=text, reply_markup=None)

    def add_job(self,update:Update,context:CallbackContext):
        bot = context.bot
        chat_id = int(update.message.chat_id)
        text = """Job nomini kiriting\nNamuna : \njob_name:hisobchi\nchat_id:123456789\n"""
        bot.send_message(chat_id=chat_id, text=text)

    def add_admin(self,update:Update,context:CallbackContext):
        bot = context.bot
        chat_id = int(update.message.chat_id)
        text = """Admin nomini kiriting\nNamuna : \nadmin_name:ogabek\nchat_id:123456789\n"""
        bot.send_message(chat_id=chat_id, text=text)

    def delete_job(self,update:Update,context:CallbackContext):
        bot = context.bot
        chat_id = int(update.message.chat_id)
        text = """Job nomini kiriting\nNamuna : \ndelet_job_name:hisobchi\n"""
        bot.send_message(chat_id=chat_id, text=text)

    def delete_admin(self,update:Update,context:CallbackContext):
        bot = context.bot
        chat_id = int(update.message.chat_id)
        text = """Admin nomini kiriting\nNamuna : \ndelet_admin_name:ogabek\n"""
        bot.send_message(chat_id=chat_id, text=text)


