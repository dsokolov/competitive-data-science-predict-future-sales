from os.path import abspath
from os.path import dirname
from os.path import join
from os.path import pardir

import pandas as pd

DATA_PATH = join(dirname(abspath(__file__)), pardir, 'data')


def load_raw_sales_train():
    file_name = join(DATA_PATH, 'sales_train_v2.csv')
    dateparser = lambda x: pd.datetime.strptime(x, "%d.%m.%Y")
    df = pd.read_csv(file_name, parse_dates=['date'], date_parser=dateparser)
    df['shop_id'] = df['shop_id'].astype('uint16')
    df['item_id'] = df['item_id'].astype('uint16')
    df['date_block_num'] = df['date_block_num'].astype('uint16')
    df['item_price'] = df['item_price'].astype('float32')
    df['item_cnt_day'] = df['item_cnt_day'].astype('float32')
    return df


def load_raw_items():
    file_name = join(DATA_PATH, 'items.csv')
    df = pd.read_csv(file_name)
    df['item_id'] = df['item_id'].astype('uint16')
    df['item_category_id'] = df['item_category_id'].astype('uint16')
    return df


def load_raw_categories():
    file_name = join(DATA_PATH, 'item_categories.csv')
    df = pd.read_csv(file_name)
    df['item_category_id'] = df['item_category_id'].astype('uint16')
    return df
