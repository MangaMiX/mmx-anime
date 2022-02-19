import asyncio
import logging
from logging import config
import os
import platform

from extractor.anime_extractor import AnimeExtractor

config.fileConfig(os.path.join(os.getcwd(), 'log.conf'))
logger = logging.getLogger(f'{__name__}')

async def run():
    anime_extractor = AnimeExtractor()
    animes = await anime_extractor.get_animes()
    # await asyncio.gather(*[elasticsearch_injector.inject(anime) for anime in animes])

if __name__ == '__main__':
    if platform.system().lower().find('windows') != -1:  # For windows compatibility
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(run())
