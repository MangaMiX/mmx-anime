import logging

from bs4 import BeautifulSoup

from mangamix.settings import MMX_ANIME_URL, MMX_EXTRACT_LIMIT, MMX_SEARCH_SIZE
from utils.http_utils import HttpUtils


class AnimeExtractor:

    def __init__(self, start_index=-MMX_SEARCH_SIZE):
        self.logger = logging.getLogger(f'{__name__}.{__class__.__name__}')
        self.num = start_index

    async def get_next_animes(self) -> (int, list[str]):
        result = []
        url = f'{MMX_ANIME_URL}{self.get_anime_index()}/'
        if self.num < MMX_EXTRACT_LIMIT:
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
        return result

    def get_anime_index(self):
        self.num += MMX_SEARCH_SIZE
        return self.num
