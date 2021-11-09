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

#TOKEN = os.getenv("TOKEN")
TOKEN = "1596253229:AAGUFRYRC2uhgpbymVU3VXR_ckUw0sdgWBI"
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()


def start_handler(update, context):
    logger.info("User {} started bot".format(update.effective_user["id"]))

    user = update.message.from_user
    print('You talk with user {} and his user ID: {} '.format(
        user['username'], user['id']))

    saludos = f""" Hola {user['username']}! """
    saludo2 = f""" Esto es el bot de la uacm! """
    saludo3 = f""" Dime en que puedo ayudarte? """
    planteles = f""" /planteles """
    carreras = f""" /carreras """
    horarios = f""" /horarios """
    info = f""" /info """

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=saludos)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=saludo2)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=saludo3)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=planteles)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=carreras)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=horarios)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=info)


def random_handler(update, context):
    number = random.randint(0, 10)
    logger.info("User {} randomed number {}".format(
        update.effective_user["id"], number))
    update.message.reply_text("Random number: {}".format(number))


def planteles_handler(update, context):
    logger.info("User {} planteles ".format(
        update.effective_user["id"] ))

    update.message.reply_text("Plantel: Casa Libertad")
    update.message.reply_text("Plantel: Centro Histórico")
    update.message.reply_text("Plantel: Cuautepec")
    update.message.reply_text("Plantel: Del Valle")
    update.message.reply_text("Plantel: San Lorenzo Tezonco")


dispatcher.add_handler(CommandHandler("start", start_handler))
dispatcher.add_handler(CommandHandler("random", random_handler))
dispatcher.add_handler(CommandHandler("planteles", planteles_handler))


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text[::-1])


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
