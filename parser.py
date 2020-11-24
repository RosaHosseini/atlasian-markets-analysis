import numpy as np
import pandas as pd

from repository import save_in_csv, fetch_markets_place, fetch_market_reviews, fetch_market_price
from utils.constansts import MARKET_PLACE_PATH
from utils.limited_thread import LimitedThread

"""
Here we parse json data
    
in main function :
    we scrape data from Atlasian Market Place page and save it in a csv file
"""


def parse_market_hit(hit: dict) -> pd.Series:
    """
    Parse a json format of a market data and save it in a pandas series (return a row of table)
    """
    name = hit['name']
    release_date = hit['releaseDate']

    vendor_obj = hit['vendor']
    vendor_name = vendor_obj['name']
    is_top_vendor = bool(vendor_obj['isTopVendor'])
    is_atlasian = bool(vendor_obj['isAtlassian'])

    rating_obj = hit['ratings']
    rating_stars = rating_obj['avgStars']
    rating_num = rating_obj['numRatings']
    rating_score = rating_obj['ratingsScore']

    dist_obj = hit['distribution']
    try:
        active_installs = dist_obj['activeInstalls']
    except KeyError:
        active_installs = 0
    downloads = dist_obj['downloads']
    delta_installs = dist_obj['deltaInstalls']
    bundled = bool(dist_obj['bundled'])

    version_obj = hit['version']
    canonical_version = bool(version_obj['canonicalVersion'])
    latest_of_hosting_version = bool(version_obj['latestOfHosting'])
    plugin_system_version = version_obj['pluginSystemVersion']
    version = version_obj['name']
    build_number = version_obj['buildNumber']
    stable_version = bool(version_obj['stable'])
    supported = bool(version_obj['supported'])
    paid = bool(version_obj['paid'])
    remotable = bool(version_obj['remotable'])
    free_remotable = bool(version_obj['freeRemotable'])
    marketplace_type = version_obj['marketplaceType']
    v_license = version_obj['license']

    desc = hit['_highlightResult']['tagLine']['value']

    deployment_obj = hit['deployments']
    deployment_cloud = bool(deployment_obj.__contains__('cloud'))
    deployment_server = bool(deployment_obj.__contains__('server'))
    deployment_data_center = bool(deployment_obj.__contains__('dataCenter'))

    return pd.Series({
        "market_name": name,
        "vendor_name": vendor_name,
        "is_top_vendor": is_top_vendor,
        "is_vendor_atlasian": is_atlasian,
        "release_date": release_date,
        "rating_stars": rating_stars,
        "rating_num": rating_num,
        "rating_score": rating_score,
        "active_installs": active_installs,
        "downloads": downloads,
        "delta_installs": delta_installs,
        # "bundled": bundled,
        "version": version,
        "version_build_number": build_number,
        # "stable_version": stable_version,
        # "version_paid": paid,
        # "supported_version": supported,
        # "canonical_version": canonical_version,
        # "latest_of_hosting_version": latest_of_hosting_version,
        "plugin_system_version": plugin_system_version,
        # "remotable_version": remotable,
        # "free_remotable_version": free_remotable,
        "marketplace_type": marketplace_type,
        "license": v_license,
        "description": desc,
        "deployment_cloud": deployment_cloud,
        "deployment_server": deployment_server,
        "deployment_data_center": deployment_data_center
    })


def parse_market_reviews(data: dict, host) -> pd.Series:
    """
    Parse a json format of a reviews data and save it in a pandas series
    """
    stars = np.empty(5)
    review_list = data['reviews']
    for i, review_obj in enumerate(review_list):
        if i >= 5:
            break
        stars[i] = review_obj['stars']
    return pd.Series({f"{host}_review_rate1": int(stars[0]),
                      f"{host}_review_rate2": int(stars[1]),
                      f"{host}_review_rate3": int(stars[2]),
                      f"{host}_review_rate4": int(stars[3]),
                      f"{host}_review_rate5": int(stars[4])
                      })


def parse_market_price(data: dict, host) -> pd.Series:
    """
    Parse a json format of a prices data and save it in a pandas series
    """
    items = data['items']
    prices = []
    for i, item in enumerate(items):
        prices.append(item["amount"])
    prices = np.array(prices)
    return pd.Series({
        f"{host}_min_price": np.min(prices),
        f"{host}_max_price": np.max(prices),
        f"{host}_avg_price": np.mean(prices).astype(int)
    })


def scrap_market_page(add_on, deployments) -> pd.Series:
    """
    Scrape the market page and save data in series
    """
    series_reviews = pd.Series()
    series_price = pd.Series()
    for host in deployments:
        reviews_data = fetch_market_reviews(add_on, host)
        if reviews_data is not None:
            series_reviews = series_reviews.append(parse_market_reviews(reviews_data, host))

        price_data = fetch_market_price(host, add_on)
        if price_data is not None:
            series_price = series_price.append(parse_market_price(price_data, host))
    return series_price.append(series_reviews)


def scrape_market_place_page() -> pd.DataFrame:
    """
    Scrape the markets-place-Atlasian page and return it in a dataframe
    """

    def get_market(m_hit, lock=None):
        row = parse_market_hit(m_hit)
        print(f"fetch market data {m_hit['name']}")
        market = scrap_market_page(m_hit['addonKey'], m_hit['deployments'])
        row = row.append(market)[row.keys().tolist() + market.keys().tolist()]

        lock.acquire()
        nonlocal df
        df = df.append(row, ignore_index=True)
        lock.release()

    thread_pool = LimitedThread(30)
    df = pd.DataFrame()  # for saving result table

    # get first page of markets_place
    data = fetch_markets_place(0)
    if data is None:
        return pd.DataFrame()
    for hit in data['results'][0]['hits']:
        thread_pool.insert_thread(get_market, [hit])

    # get other pages of markets_place
    page_count = data['results'][0]['nbPages']
    for i in range(1, page_count):
        data = fetch_markets_place(i)
        if data is None:
            continue
        for hit in data['results'][0]['hits']:
            thread_pool.insert_thread(get_market, [hit])

    thread_pool.wait_to_end()
    return df


if __name__ == "__main__":
    result = scrape_market_place_page()
    print(len(result))
    save_in_csv(MARKET_PLACE_PATH, result)
