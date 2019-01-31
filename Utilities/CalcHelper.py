from Utilities import Consts


def smooth_all_df(df, window_size=Consts.WINDOW_SIZE):
    """

    :param df:
    :type df: pd.DataFrame
    :param window_size:
    :return:
    """
    print("Start smooth data")
    if window_size == 1:
        return df
    rolling = df.rolling(window=window_size)
    rolling_mean = rolling.mean()
    df = rolling_mean[window_size - 1:]
    return df


def normalize(data):
    _min = data.values.min(axis=0)
    _max = data.values.max(axis=0)
    _min_max = _max - _min
    if _min_max == 0:
        _min_max = 1
    only_features = (data.values - _min) / _min_max
    return only_features
