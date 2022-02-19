import asyncio
import logging
from logging import config
import os
import platform

from mangamix.anime_extractor import AnimeExtractor
from mangamix.elasticsearch_injector import ElasticsearchInjector

config.fileConfig(os.path.join(os.getcwd(), 'log.conf'))
logger = logging.getLogger(f'{__name__}')


async def run():
    anime_extractor = AnimeExtractor()
    animes = await anime_extractor.get_animes()
    elasticsearch_injector = ElasticsearchInjector()
    await elasticsearch_injector.index(animes)

if __name__ == '__main__':
    if platform.system().lower().find('windows') != -1:  # For windows compatibility
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(run())
