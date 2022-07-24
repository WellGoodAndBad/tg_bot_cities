import os

import environs

env = environs.Env()

TG_TOKEN = env('TG_TOKEN')
MONGO_DSN_TEMPLATE = "mongodb://test_user:test_password@mongodb:27017/test_db"

URL_CITIES = 'https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B8%D0%B5_' \
             '%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D1%91%D0%BD%D0%BD%D1%8B%D0%B5_%D0%BF%D1%83%D0%BD%D0%BA%' \
             'D1%82%D1%8B_%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B9_%D0%BE%D0%' \
             'B1%D0%BB%D0%B0%D1%81%D1%82%D0%B8'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'