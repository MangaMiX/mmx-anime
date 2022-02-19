import logging
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk

from mangamix.settings import ES_INDEX, ES_HOST, ES_USER, ES_PASSWORD


class ElasticsearchInjector:

    def __init__(self):
        self.logger = logging.getLogger(f'{__name__}.{__class__.__name__}')
        self.es = AsyncElasticsearch(hosts=ES_HOST, http_auth=(ES_USER, ES_PASSWORD))

    async def index(self, animes: list[str]):
        self.logger.debug(f'Start indexing {animes}')
        await async_bulk(self.es, self.__gendata(animes))

    @staticmethod
    async def __gendata(animes: list[str]):
        for anime in animes:
            yield {
                "_index": ES_INDEX,
                "test": anime
            }
