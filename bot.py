# !/usr/bin/env python
# pylint: disable=W0603
"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see rawapibot.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os

TOKEN = os.getenv("TOKEN")
print(TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Здравствуй, братан!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text[::-1])


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
