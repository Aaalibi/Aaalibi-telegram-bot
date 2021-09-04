# IMPORT
from telegram import update
from telegram.ext import *
import datetime
import requests

# VARIABILI GLOBALI
updater = Updater(token='1991659683:AAG6GnbLsi0qdrxgl00Nx8TyhMkNEPUeyqo', use_context=True)
dispatcher = updater.dispatcher

# LOGGING
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# COMANDI


def get_prices(update, context):
    coins = ["BTC", "ETH", "XRP", "LTC", "BCH", "ADA", "DOT", "LINK", "BNB", "XLM"]

    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["USD"]["PRICE"],
            "change_day": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["USD"]["CHANGEPCTHOUR"]
        }

    return data and context.bot.send_message(data)














def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def stop(update, context):
    updater.stop()

def time(update, context):
    todaytime = "Orario: " + datetime.time()
    context.bot.send_message(todaytime)



# REGISTRAZIONE COMANDI
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# START
updater.start_polling()
