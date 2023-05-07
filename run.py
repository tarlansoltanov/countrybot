import asyncio
import logging

from countrybot import bot

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')
    
    logging.info('Starting bot...')
    logging.info('Press Ctrl + C to stop bot.')

    asyncio.run(bot.polling())
