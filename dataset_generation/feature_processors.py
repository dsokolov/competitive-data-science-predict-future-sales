def sold_count_sum(df):
    v = df['item_cnt_day'].sum()
    return v


feature_sold_count_sum = {
    'column_name': 'sold_count_sum',
    'processor': sold_count_sum
}
