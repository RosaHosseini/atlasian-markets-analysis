import numpy as np
import pandas as pd

from repository import read_from_csv
from utils.constansts import MARKET_PLACE_PATH

"""
This class reads data from market_place.csv
and retrieves different features of it
"""


class MarketPlace:
    def __init__(self):
        self.df = read_from_csv(MARKET_PLACE_PATH)
        if len(self.df) == 0:
            raise Exception("market_place.csv file is empty")

    def retrieve_max_price(self) -> np.array:
        """
        :return: max price of all deployments
        """
        max_price = []
        for index, row in self.df.iterrows():
            _max_price = None
            if row['cloud_max_price'] >= 0:
                _max_price = row['cloud_max_price']
            if row['server_max_price'] >= 0:
                if _max_price is None or _max_price < row['server_max_price']:
                    _max_price = row['server_max_price']
            if row['dataCenter_max_price'] >= 0:
                if _max_price is None or _max_price < row['dataCenter_max_price']:
                    _max_price = row['dataCenter_max_price']
            max_price.append(_max_price)
        return np.array(max_price)

    def retrieve_min_price(self) -> np.array:
        """
        :return: min price of all deployments
        """
        min_price = []
        for index, row in self.df.iterrows():

            _min_price = None
            if row['cloud_min_price'] >= 0:
                _min_price = row['cloud_min_price']
            if row['server_min_price'] >= 0:
                if _min_price is None or _min_price > row['server_min_price']:
                    _min_price = row['server_min_price']
            if row['dataCenter_min_price'] >= 0:
                if _min_price is None or _min_price > row['dataCenter_min_price']:
                    _min_price = row['dataCenter_min_price']

            min_price.append(_min_price)

        return np.array(min_price)

    def retrieve_avg_price(self) -> np.array:
        """
        :return: avg price of all deployments
        """
        avg_price = []
        for index, row in self.df.iterrows():
            try:
                temp = 0
                count = 0
                if row['cloud_avg_price'] >= 0:
                    temp += row['cloud_avg_price']
                    count += 1
                if row['server_avg_price'] >= 0:
                    temp += row['server_avg_price']
                    count += 1
                if row['dataCenter_avg_price'] >= 0:
                    temp += row['dataCenter_avg_price']
                    count += 1
                _avg_price = temp / count
            except ZeroDivisionError:
                _avg_price = None
            avg_price.append(_avg_price)
        return np.array(avg_price)

    def retrieve_avg_last_reviews_rate(self) -> np.array:
        """
        :return: average stars that 5 last reviewers of each deployment rated that market
        """
        sums = np.zeros(len(self.df))
        count = np.zeros(len(self.df))
        for key in self.df.columns:
            if key.__contains__("review_rate"):
                for i, row in self.df.iterrows():
                    if row[key] >= 0:
                        sums[i] += row[key]
                        count[i] += 1
        avg = pd.DataFrame(sums / count)
        avg.replace([np.inf, -np.inf, np.NAN], 0)
        return avg

    def retrieve_version_number(self) -> np.array:
        """
        Reformat version string to version number
        """
        return self.df['version'].str.split(".", n=1, expand=True)[0]

    def retrieve_market_type_numeric(self) -> np.array:
        """
        Reformat market type to integer numbers
        """
        m = self.df['marketplace_type'].tolist()
        numeric_list = []
        for m_type in m:
            if m_type == "Free":
                numeric_list.append(1)
            elif m_type == "Paid via Atlassian":
                numeric_list.append(2)
            else:
                numeric_list.append(3)
        return np.array(numeric_list)
