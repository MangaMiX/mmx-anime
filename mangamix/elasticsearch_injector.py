import logging
import hashlib

import elastic_transport
import elasticsearch
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk

from mangamix.settings import ES_INDEX, ES_HOST, ES_USER, ES_PASSWORD


class ElasticsearchInjector:

    def __init__(self):
        self.logger = logging.getLogger(f'{__name__}.{__class__.__name__}')
        self.es = AsyncElasticsearch(hosts=ES_HOST, http_auth=(ES_USER, ES_PASSWORD), retry_on_timeout=True)

    async def index(self, animes: list[str]):
        self.logger.info(f'Try to index {len(animes)} animes')
        self.logger.debug(f'indexing {animes}')

        try:
            index_succeed, errors = await async_bulk(client=self.es, actions=self.__create_doc(animes),
                                                     raise_on_error=False)
            self.logger.info(f'Indexing succeed: {index_succeed}, indexing failed: {len(errors)}')
            for error in errors:
                self.logger.debug(error)
        except (elastic_transport.ConnectionError, elasticsearch.AuthenticationException) as e:
            self.logger.warning(e)

    @staticmethod
    async def __create_doc(animes: list[str]):
        for anime in animes:
            yield {
                "_index": ES_INDEX,
                "_id": ElasticsearchInjector.hash_name(anime),
                "_source": {'name': anime},
                "_op_type": 'create',
            }

    @staticmethod
    def hash_name(name: str):
        return hashlib.sha256(name.encode('utf-8')).hexdigest()
