import os

ES_HOST = os.getenv('ES_HOST', 'http://localhost:9200')
ES_USER = os.getenv('ES_USER', 'elastic')
ES_PASSWORD = os.getenv('ES_PASSWORD', 'dzNIt6zKlFN5ynoOlnsD')
ES_INDEX = os.getenv('ES_INDEX', 'mangamix')
MMX_ANIME_URL = os.getenv('MMX_ANIME_URL', 'https://myanimelist.net/topanime.php')
MMX_EXTRACT_LIMIT = int(os.getenv('MMX_EXTRACT_LIMIT')) if os.getenv('MMX_EXTRACT_LIMIT') else None
MMX_SEARCH_SIZE = int(os.getenv('MMX_SEARCH_SIZE', '50'))
MMX_ANIMES = os.getenv('MMX_ANIMES').split(',') if os.getenv('MMX_ANIMES') else []
