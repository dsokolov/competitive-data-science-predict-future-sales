from os.path import abspath
from os.path import dirname
from os.path import join
from os.path import pardir

import pandas as pd

DATA_PATH = join(dirname(abspath(__file__)), pardir, 'data')


def load_raw_sales_train(nrows=None):
    file_name = join(DATA_PATH, 'sales_train_v2.csv')
    dtypes = {
        'shop_id': 'uint8',
        'item_id': 'uint16',
        'date_block_num': 'uint16',
        'item_price': 'float32',
        'item_cnt_day': 'float32'
    }
    df = pd.read_csv(file_name, dtype=dtypes,
                     parse_dates=['date'], date_parser=lambda x: pd.datetime.strptime(x, "%d.%m.%Y"),
                     nrows=nrows
                     )
    return df


def load_raw_items():
    file_name = join(DATA_PATH, 'items.csv')
    df = pd.read_csv(file_name, dtype={'item_id': 'uint16', 'item_category_id': 'uint16'})
    return df


def load_raw_categories():
    file_name = join(DATA_PATH, 'item_categories.csv')
    df = pd.read_csv(file_name, dtype={'item_category_id': 'uint16'})
    return df


def load_raw_shops():
    file_name = join(DATA_PATH, 'shops.csv')
    df = pd.read_csv(file_name, dtype={'shop_id': 'uint8'})
    return df


def load_raw_test():
    file_name = join(DATA_PATH, 'test.csv')
    df = pd.read_csv(file_name, dtype={'ID': 'uint32', 'shop_id': 'uint8', 'item_id': 'uint16'})
    return df


def load_raw_train_merged(nrows=None):
    sales_df = load_raw_sales_train(nrows)
    shops_df = load_raw_shops()
    items_df = load_raw_items()
    categories_df = load_raw_categories()
    result = sales_df.merge(shops_df, how='left', on='shop_id')
    result = result.merge(items_df, how='left', on='item_id')
    result = result.merge(categories_df, how='left', on='item_category_id')
    result['shop_name'] = result['shop_name'].astype('category')
    result['item_name'] = result['item_name'].astype('category')
    result['item_category_name'] = result['item_category_name'].astype('category')
    return result


def load_raw_test_merged():
    sales_df = load_raw_test()
    shops_df = load_raw_shops()
    items_df = load_raw_items()
    categories_df = load_raw_categories()
    result = sales_df.merge(shops_df, how='left', on='shop_id')
    result = result.merge(items_df, how='left', on='item_id')
    result = result.merge(categories_df, how='left', on='item_category_id')
    result['shop_name'] = result['shop_name'].astype('category')
    result['item_name'] = result['item_name'].astype('category')
    result['item_category_name'] = result['item_category_name'].astype('category')
    return result
