import asyncio
import logging
from logging import config
import os
import platform

from mangamix.anime_extractor import AnimeExtractor
from mangamix.mangasearch import Mangasearch
from mangamix.settings import MMX_ANIMES

config.fileConfig(os.path.join(os.getcwd(), 'log.conf'))
logger = logging.getLogger(f'{__name__}')


async def run():
    anime_extractor = AnimeExtractor()
    mangasearch = Mangasearch()
    found_anime = True
    while found_anime:
        await asyncio.sleep(2)
        if len(MMX_ANIMES) > 0:
            await mangasearch.index(MMX_ANIMES)
            found_anime = False
        else:
            animes = await anime_extractor.get_next_animes()
            if len(animes) > 0:
                await mangasearch.index(animes)
            else:
                found_anime = False

if __name__ == '__main__':
    if platform.system().lower().find('windows') != -1:  # For windows compatibility
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(run())
