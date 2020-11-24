import json
from typing import Optional

import pandas as pd
import requests

from utils import constansts

"""
    Here we perform IO jobs like writing and reading file or fetching data from network
"""


def get_request(url) -> requests.Response:
    """
    Get a url and return the response of the GET request if it succeed
    """
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response
    else:
        raise Exception(response.status_code)


def post_request(url: str, payload: str, headers: str) -> requests.Response:
    """
    Get a url and return the response of the POST request if it succeed
    """
    response = requests.post(url, timeout=10, headers=headers, data=payload)
    if response.status_code == 200:
        return response
    else:
        raise Exception(response.status_code)


def write_data(name: str, data) -> bool:
    """
    Write data in given file and return true, if it succeed otherwise false
    """
    try:
        f = open(name, 'w')
        f.write(data)
        return True
    except Exception as e:
        print(f"Error in writing data in file {name} with error:{e}")
        return False


def save_in_csv(name: str, df: pd.DataFrame) -> bool:
    """
    Write data frame in a csv file and return true, if it succeed otherwise false
    """
    try:
        df.to_csv(name)
        return True
    except Exception as e:
        print(f"Error in writing data in csv {name} with error:{e}")
        return False


def read_from_csv(name: str) -> pd.DataFrame:
    """
    Read data frame from a csv file and return it
    """
    try:
        df = pd.read_csv(name)
        return df
    except Exception as e:
        print(f"Error in reading data from {name} with error: {e}")
        return pd.DataFrame()


def fetch_markets_place(page_number: int) -> Optional[dict]:
    """
    Fetch data of market place, and return json data
    """
    try:
        payload = json.dumps(constansts.MARKET_PLACE_PARAMS(page_number))
        response = post_request(constansts.MARKET_PLACE_URL, payload, constansts.MARKET_PLACE_HEADER)
        # write_data("log/log.txt", response.text)  # log fetched data
        search_result = json.loads(response.text)
        return search_result
    except Exception as e:
        print(f"Error in fetch market_place with error: {e}")
        return None


def fetch_market_reviews(add_on: str, host: str) -> Optional[dict]:
    """
    Fetch 5 last reviewers rate of given market and host,
     and return json data
    """
    try:
        response = get_request(constansts.REVIEW_URL(add_on, host))
        # write_data(f"log/log_reviews_{plugin}_{host}.txt", response.text)  # log fetched data
        search_result = json.loads(response.text)
        return search_result
    except Exception:
        return None


def fetch_market_price(host: str, addon: str) -> Optional[dict]:
    """
    Fetch prices of given market and host, and return json data
    """
    try:
        response = get_request(constansts.PRICE_URL(host, addon))
        # write_data(f"log/log_price_{host}_{addon}.txt", response.text)  # log fetched data
        search_result = json.loads(response.text)
        return search_result
    except Exception as e:
        if e.args[0] == 404:
            return {
                "items": [
                    {"amount": 0}
                ]
            }
        print(f"Error in fetch price of market {addon},{host} with error: {e}")
        return None
