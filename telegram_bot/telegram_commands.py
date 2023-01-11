from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram_bot.message_templates import start_command_message


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=start_command_message)


async def cardDeals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="hehe, auntie not ready yet lah. come again tomorrow")
