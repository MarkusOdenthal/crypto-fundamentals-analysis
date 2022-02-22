"""
This module contains coinmarketcap api
"""

import pandas as pd
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json 
import os


def get_coins_coinmarketcap(start: int) -> pd.DataFrame:
    api_key = os.environ["API_KEY"]
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    parameters = {
        'listing_status': 'active,inactive,untracked',
        'start': start,
        'limit': 5000
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    return data
