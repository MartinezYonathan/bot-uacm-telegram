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
import random

TOKEN = os.getenv("TOKEN")
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()

def start_handler(update, context):
    logger.info("User {} started bot".format(update.effective_user["id"]))
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hola! soy el bot de la uacm")

def random_handler(update, context):
    number = random.randint(0, 10)
    logger.info("User {} randomed number {}".format(update.effective_user["id"], number))
    update.message.reply_text("Random number: {}".format(number))

dispatcher.add_handler(CommandHandler("start", start_handler))
dispatcher.add_handler(CommandHandler("random", random_handler))

def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text[::-1])


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
