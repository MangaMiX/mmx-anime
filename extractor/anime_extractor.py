import logging

from bs4 import BeautifulSoup

from utils.http_utils import HttpUtils

ANIME_URL_ = 'https://www.nautiljon.com/classements/tendance/anime/'


class AnimeExtractor:

    def __init__(self):
        self.logger = logging.getLogger(f'{__name__}.{__class__.__name__}')

    async def get_animes(self) -> list[str]:
        result = []
        status, response = await HttpUtils.send(method='GET', url=ANIME_URL_)
        if status != 200:
            self.logger.error(f'Failed to get_animes. Status: {status}, response: {response}')
            return result
        bs = BeautifulSoup(response, 'html.parser')
        table = bs.find("table", attrs={"class": "classements"})
        for td in table.find_all('td', attrs={"class": "vtop left"}):
            a = td.find("a", recursive=False)
            result.append(a.get('title'))
        self.logger.info(f'Found {len(result)} animes for url: {ANIME_URL_}')
        return result
