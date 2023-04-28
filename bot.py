from telegram.ext import Updater,CallbackContext
from telegram import *

class Samtuit:
    def start(self,update:Update,context:CallbackContext):
        bot = context.bot
        chat_id = update.message.chat_id
        bot.send_message(chat_id=chat_id,text="안녕하세요")