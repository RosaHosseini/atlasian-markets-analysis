import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from market_place import MarketPlace
from utils import constansts

"""
Here we analyse the number of active installs and which features can be effective 
"""

markets = MarketPlace()


def plot_installs():
    x = markets.df['market_name']
    y = markets.df['active_installs']

    plt.title("distribution of active installs")
    plt.ylabel("active installs")

    plt.yscale("log")
    plt.bar(x, y, color=constansts.green)
    plt.show()


def plot_installs_dist():
    installs = markets.df['active_installs'].tolist()
    y = [int(i / 100) for i in installs]
    labels = [0] + (np.unique(y) * 5000).tolist()
    ax = sns.displot(data=y)
    ax.set_titles("distribution of markets based on active-installs")
    ax.set_xlabels("#_active_installs")
    ax.set_ylabels("frequency")
    ax.set(xticklabels=labels)
    plt.show()


def plot_dist_base_max_price():
    temp_df = pd.DataFrame()
    temp_df['max_price'] = markets.retrieve_max_price()
    temp_df['install_range'] = (markets.df['active_installs'] / 100).astype(int)
    temp_df = temp_df[temp_df['max_price'] >= 0]  # remove null data
    ax = sns.boxplot(x="#_active_installs", y="max_price", data=temp_df)
    labels = (np.unique(temp_df['install_range']) * 100).tolist()
    ax.set_xticklabels(labels, rotation=45)
    plt.show()


def plot_dist_base_avg_price():
    temp_df = pd.DataFrame()
    temp_df['avg_price'] = markets.retrieve_avg_price().astype(int)
    temp_df = temp_df[temp_df['avg_price'] >= 0]  # remove null data
    temp_df['install_range'] = (markets.df['active_installs'] / 100).astype(int)
    ax = sns.boxplot(x="#_active_installs", y="avg_price", data=temp_df)
    labels = (np.unique(temp_df['install_range']) * 100).tolist()
    ax.set_xticklabels(labels, rotation=45)
    plt.show()


def plot_dist_base_min_price():
    temp_df = pd.DataFrame()
    temp_df['min_price'] = markets.retrieve_min_price()
    temp_df['install_range'] = (markets.df['active_installs'] / 100).astype(int)
    temp_df = temp_df[temp_df['min_price'] >= 0]  # remove null data
    ax = sns.boxplot(x="install_range", y="min_price", data=temp_df)
    labels = (np.unique(temp_df['install_range']) * 100).tolist()
    ax.set_xticklabels(labels, rotation=45)
    plt.show()


def compare_parameters():
    temp_df = markets.df[
        ['#_active_installs', 'deployment_cloud', 'deployment_data_center', 'deployment_server', 'rating_num',
         'rating_score', 'rating_stars', 'release_date']].astype(int)
    temp_df['version_number'] = markets.retrieve_version_number().astype(int)
    temp_df['avg_price'] = markets.retrieve_avg_price()
    temp_df['max_price'] = markets.retrieve_max_price()
    temp_df['min_price'] = markets.retrieve_min_price()
    temp_df['is_free'] = markets.retrieve_market_type_numeric()
    temp_df['last_reviews_score'] = markets.retrieve_avg_last_reviews_rate().astype(int)
    temp_df.to_csv("temp.csv")
    corr = temp_df.apply(lambda x: x.factorize()[0]).corr()
    sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True)
    plt.show()


if __name__ == "__main__":
    plot_installs_dist()
    plot_dist_base_min_price()
    plot_dist_base_avg_price()
    plot_dist_base_max_price()
    compare_parameters()


