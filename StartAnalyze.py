import pandas as pd
import numpy as np
import sys
import os

import time
from tqdm import tqdm
import multiprocessing

from Utilities import Consts, CalcHelper

# Set print for pandas
pd.set_option("display.max_rows", 999)
pd.set_option("display.max_columns", 999)
pd.set_option('display.max_colwidth', -1)


def calc_person(x, y):
    return np.corrcoef(x, y)[1, 0]


def score_function(x, y_max, y_min, feature_name):
    """
    Norm the data and calculate the pearson corr between x y_max and x y_min.
    :param x: feature data
    :param y_max: the max price change
    :param y_min: the min price change
    :param feature_name: the feature name
    :return:
    """
    # Norm the feature
    if Consts.NORM_DATA:
        x = CalcHelper.normalize(x)
    max_corr = calc_person(x, y_max)
    min_corr = calc_person(x, y_min)

    return {
        Consts.FEATURE_NAME_COLUMN: feature_name,
        Consts.CORR_RES_MAX_CHANGE: max_corr,
        Consts.CORR_RES_MIN_CHANGE: min_corr,
    }


def start_run():
    """
    The main function that compute
    :return:
    """
    print("Loading Data")
    # Load the features
    df = pd.read_csv(Consts.ACC_DATA_PATH, compression='gzip').set_index([Consts.COIN_SYMBOL_COLUMN, Consts.TIME_COLUMN])
    if 'Date UTC' in df.columns:
        df.drop('Date UTC', axis=1, inplace=True)
    df.sort_index(inplace=True)

    # Smooth the data with sliding window algorithm
    df = CalcHelper.smooth_all_df(df)

    df_btc_price_change = pd.read_csv(Consts.BTC_PRICE_CHANGE_FILE, compression='gzip') \
        .set_index([Consts.COIN_SYMBOL_COLUMN, Consts.TIME_COLUMN]).loc[df.index]

    if df_btc_price_change.shape[0] != df.shape[0]:
        print("It seems that the price changes does not match the data from ACC, contact ACC for help.")
        quit(1)

    print("Total number of features {}".format(df.shape[1]))
    print("Total number of hours {}".format(df.shape[0]))

    # Compare ACC Data with random samples
    print("Create random samples and calculating Pearson corr and normalize the data")
    rand_scores = []
    num_of_digits = len(str(df.shape[1]))
    for i in range(df.shape[1]):
        prng = np.random.RandomState()
        rand_test = prng.random_sample(df.shape[0])
        score_rand_test = score_function(pd.Series(rand_test),
                                         df_btc_price_change[Consts.BTC_PRICE_CHANGE_MAX_NAME],
                                         df_btc_price_change[Consts.BTC_PRICE_CHANGE_MIN_NAME],
                                         'RANDOM-{}'.format(str(i).zfill(num_of_digits))
                                         )
        rand_scores.append(score_rand_test)
    rand_scores_df = pd.DataFrame(rand_scores)

    print("Start calculating Pearson corr and normalize the data")
    score_results_for_each_feature = []
    for feature_name in df.columns.tolist():
        feature_score = score_function(df[feature_name],
                                       df_btc_price_change[Consts.BTC_PRICE_CHANGE_MAX_NAME],
                                       df_btc_price_change[Consts.BTC_PRICE_CHANGE_MIN_NAME],
                                       feature_name)
        score_results_for_each_feature.append(feature_score)

    # Load results to DataFrame
    corr_df = pd.DataFrame(score_results_for_each_feature)

    # Use sleep to pretty print logs
    time.sleep(1)
    print()
    print_info_str = 'Random Pearson correlation results'
    print_sep(len(print_info_str))
    print(print_info_str)
    print_sep(len(print_info_str))
    print_best_corr(rand_scores_df)
    time.sleep(3)
    print()
    print_info_str = 'ACC Data Pearson correlation results'
    print_sep(len(print_info_str))
    print(print_info_str)
    print_sep(len(print_info_str))
    print_best_corr(corr_df)


def print_sep(sep_len=40):
    print('-' * sep_len)


def print_best_corr(df):
    """
    Print highest corr in the DataFrame
    :param df:
    :return:
    """
    for column_print in [Consts.CORR_RES_MAX_CHANGE, Consts.CORR_RES_MIN_CHANGE]:
        df['abs_req'] = np.abs(df[column_print])
        df.sort_values('abs_req', inplace=True, ascending=False)
        print("#------------------------------ {} ------------------------------#\n".format(column_print))
        print(df[[Consts.FEATURE_NAME_COLUMN, column_print]].head(10))
        print()


if __name__ == "__main__":
    if not os.path.isfile(Consts.ACC_DATA_PATH):
        print('Fail to find {}, please visit {} downloaded the file and move it into the Data folder.'
              .format(Consts.ACC_DATA_PATH, Consts.ACC_WEBSITE),
              file=sys.stderr)
        quit(1)

    start_run()
