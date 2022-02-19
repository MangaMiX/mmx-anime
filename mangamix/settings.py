import os

ES_HOST = os.getenv('ES_HOST', 'http://localhost:9200')
ES_USER = os.getenv('ES_USER', 'elastic')
ES_PASSWORD = os.getenv('ES_PASSWORD', 'whlaib58SI-8RF9h1heP')
ES_INDEX = os.getenv('ES_INDEX', 'mangamix')
ANIME_URL = os.getenv('ANIME_URL', 'https://www.nautiljon.com/classements/tendance/anime/')
