import aiohttp
from bs4 import BeautifulSoup

import mongo
import settings


async def parse_data() -> None:
    headers = {
        'User-Agent': settings.USER_AGENT
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(settings.URL_CITIES) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            tables = soup.find_all("table", {"class": "standard"})
            insert_values = []
            for tbl in tables:
                trs = tbl.find_all("tr")
                for tr in trs:
                    if len((tds := tr.find_all("td"))) == 0:
                        continue
                    dict_values = {
                        "city": tds[1].text.lower(),
                        "population": tds[4].text,
                        "url": f"https://ru.wikipedia.org{tds[1].a['href']}"
                    }
                    insert_values.append(dict_values)
            await mongo.insert(insert_values)

