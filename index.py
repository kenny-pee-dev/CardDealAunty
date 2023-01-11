from telegram_bot.telegram_commands import start, cardDeals
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram import Update
from requests_html import HTMLSession
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv()
    application = ApplicationBuilder().token(
        os.environ['TELEGRAM_BOT_API_TOKEN']).build()

    start_handler = CommandHandler('start', start)
    display_card_deals_handler = CommandHandler('hitmeup', cardDeals)

    application.add_handlers(handlers={
        0: [start_handler],
        1: [display_card_deals_handler]
    })
    print('Running CardAuntyBot!')
    application.run_polling()
