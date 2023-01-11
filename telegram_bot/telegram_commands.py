from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.constants import ParseMode
from telegram_bot.message_templates import start_command_message
from api.card_deals_api import getMoneySmartCardDeals
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.parser import *

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=start_command_message)


async def moneysmart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    money_smart_deals = getMoneySmartCardDeals()
    for deal in money_smart_deals:
      clean_caption = BeautifulSoup(deal['campaign']['snippet_text'], "lxml").text
      apply_link = f"https://iss.moneysmart.sg/credit_cards/{deal['slug']}/email-capture?campaign_id={deal['campaign']['id']}&category_slug=best-credit-cards&channel_slug=credit_cards&locale=en&product_slug={deal['slug']}&provider_slugs%5B%5D=-1"
      message = f"<b>{deal['name']}</b>\n\n{clean_caption}\n\n<b>Promotion start:</b> {parse(deal['campaign']['promotion_start'])}\n\n<b>Promotion end:</b> {parse(deal['campaign']['promotion_end'])}\n\n<b>Apply here:</b> {apply_link}"
      await context.bot.send_photo(chat_id=update.effective_chat.id, parse_mode=ParseMode.HTML, photo=deal['campaign']['image'] , caption=message)
