from flask import Flask, request, abort
from mongoengine import NotUniqueError
from telebot.types import Update, ReplyKeyboardMarkup, KeyboardButton
from .config import TOKEN, WEBHOOK_URI
from telebot import TeleBot
import time

from shop.bot import constants
from shop.models.shop_models import User

app = Flask(__name__)
bot = TeleBot(TOKEN)


@app.route(WEBHOOK_URI, methods=['POST'])
def handle_webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    abort(403)


@bot.message_handler(commands=['start'])
def handle_start(message):
    name = f', {message.from_user.first_name}' if getattr(message.from_user, 'first_name') else ''
    greetings = constants.GREETINGS.format(name)
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(n) for n in constants.START_KB.values()]
    kb.add(*buttons)
    bot.send_message(message.chat.id, greetings, reply_markup=kb)



