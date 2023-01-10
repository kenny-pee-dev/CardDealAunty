import asyncio
import telegram
from requests_html import HTMLSession
from const import TELEGRAM_BOT_API_TOKEN, CHAT_IDS_DEV, CHAT_IDS


async def main():
    bot = telegram.Bot(TELEGRAM_BOT_API_TOKEN)
    async with bot:
        for chat_id in CHAT_IDS_DEV:
            await bot.send_message(text='Testing message', chat_id=chat_id)


if __name__ == '__main__':
    asyncio.run(main())
