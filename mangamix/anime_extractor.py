import logging

from bs4 import BeautifulSoup

from mangamix.settings import ANIME_URL
from utils.http_utils import HttpUtils


class AnimeExtractor:

    def __init__(self, start_index=-30):
        self.logger = logging.getLogger(f'{__name__}.{__class__.__name__}')
        self.num = start_index

    async def get_next_animes(self) -> (int, list[str]):
        result = []
        url = f'{ANIME_URL}{self.get_anime_index()}/'
        status, response = await HttpUtils.send(method='GET', url=url)
        if status == 200:
            bs = BeautifulSoup(response, 'html.parser')
            table = bs.find("table", attrs={"class": "classements"})
            for td in table.find_all('td', attrs={"class": "vtop left"}):
                a = td.find("a", recursive=False)
                result.append(a.get('title'))
            self.logger.info(f'Found {len(result)} animes for url: {url}')
        else:
            self.logger.error(f'Failed to get_animes for url {url}. Status: {status}, response: {response}')
        return status, result

    def get_anime_index(self):
        self.num += 30
        return self.num
