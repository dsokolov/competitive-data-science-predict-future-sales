import pandas as pd

import dataset_generation.feature_processors as f


def generate_dataset(raw_df, observation_days, prediction_days):
    feature_processors = [
        f.feature_sold_count_sum
    ]
    features = collect_features(raw_df, feature_processors, observation_days)
    labels = collect_labels(raw_df, prediction_days)
    dataset = features.merge(labels, how='inner', on=['ts', 'shop_id', 'item_category_id', 'item_id'])
    return dataset


def store_dataset(df: pd.DataFrame):
    name = "datasets/dataset_1.csv"
    df.to_csv(name, index=False)


def collect_features(df, feature_processors, observation_days=30):
    start_ts = df['date'].min()
    finish_ts = df['date'].max()
    print('Colling features from {} to {}'.format(start_ts, finish_ts))

    columns = ['ts', 'shop_id', 'item_category_id', 'item_id', 'sold_count_sum']
    data = {
        'ts': [],
        'shop_id': [],
        'item_category_id': [],
        'item_id': [],
        'sold_count_sum': []
    }

    while True:
        end_ts = start_ts + pd.Timedelta(days=observation_days)
        if end_ts > finish_ts:
            break

        observation_df = df[(start_ts <= df['date']) & (df['date'] < finish_ts)]
        print('{} - {}: {}'.format(start_ts, finish_ts, observation_df.shape))

        keys_df = observation_df[['shop_id', 'item_category_id', 'item_id']].drop_duplicates()

        for index, keys in keys_df.iterrows():
            shop_id = keys['shop_id']
            item_category_id = keys['item_category_id']
            item_id = keys['item_id']

            temp_df = observation_df[
                (observation_df['shop_id'] == shop_id) &
                (observation_df['item_category_id'] == item_category_id) &
                (observation_df['item_id'] == item_id)]

            data['ts'].append(end_ts)
            data['shop_id'].append(shop_id)
            data['item_category_id'].append(item_category_id)
            data['item_id'].append(item_id)

            data['sold_count_sum'] = temp_df['item_cnt_day'].sum()

        start_ts += pd.Timedelta(days=1)

    result_df = pd.DataFrame(columns=columns, data=data)
    return result_df


def collect_labels(df, prediction_days=30):
    start_ts = df['date'].min()
    finish_ts = df['date'].max()
    print('Colling labels from {} to {}'.format(start_ts, finish_ts))

    columns = ['ts', 'shop_id', 'item_category_id', 'item_id', 'label']
    data = {
        'ts': [],
        'shop_id': [],
        'item_category_id': [],
        'item_id': [],
        'label': []
    }

    while True:
        end_ts = start_ts + pd.Timedelta(days=prediction_days)
        if end_ts > finish_ts:
            break

        prediction_df = df[(start_ts <= df['date']) & (df['date'] <= finish_ts)]
        print('{} - {}: {}'.format(start_ts, finish_ts, prediction_df.shape))

        keys_df = prediction_df[['shop_id', 'item_category_id', 'item_id']].drop_duplicates()

        for index, keys in keys_df.iterrows():
            shop_id = keys['shop_id']
            item_category_id = keys['item_category_id']
            item_id = keys['item_id']

            temp_df = prediction_df[
                (prediction_df['shop_id'] == shop_id) &
                (prediction_df['item_category_id'] == item_category_id) &
                (prediction_df['item_id'] == item_id)]

            data['ts'].append(start_ts)
            data['shop_id'].append(shop_id)
            data['item_category_id'].append(item_category_id)
            data['item_id'].append(item_id)

            data['label'] = temp_df['item_cnt_day'].sum()

        start_ts += pd.Timedelta(days=1)

    result_df = pd.DataFrame(columns=columns, data=data)
    return result_df
