import unittest

import pandas as pd

from sources.raw import load_raw_categories
from sources.raw import load_raw_items
from sources.raw import load_raw_sales_train
from sources.raw import load_raw_shops
from sources.raw import load_raw_test
from sources.raw import load_raw_test_merged
from sources.raw import load_raw_train_merged


class RawTestCase(unittest.TestCase):

    def test_load_raw_sales_train(self):
        raw_data_df = load_raw_sales_train(nrows=10)
        self.assertIsNotNone(raw_data_df)
        self.assertEqual(type(raw_data_df), pd.DataFrame)
        self.assertGreater(raw_data_df.shape[0], 0)

    def test_load_raw_items(self):
        raw_data_df = load_raw_items()
        self.assertIsNotNone(raw_data_df)
        self.assertEqual(type(raw_data_df), pd.DataFrame)
        self.assertGreater(raw_data_df.shape[0], 0)

    def test_load_raw_categories(self):
        raw_data_df = load_raw_categories()
        self.assertIsNotNone(raw_data_df)
        self.assertEqual(type(raw_data_df), pd.DataFrame)
        self.assertGreater(raw_data_df.shape[0], 0)

    def test_load_raw_shops(self):
        raw_data_df = load_raw_shops()
        self.assertIsNotNone(raw_data_df)
        self.assertEqual(type(raw_data_df), pd.DataFrame)
        self.assertGreater(raw_data_df.shape[0], 0)

    def test_load_raw_test(self):
        raw_data_df = load_raw_test()
        self.assertIsNotNone(raw_data_df)
        self.assertEqual(type(raw_data_df), pd.DataFrame)
        self.assertGreater(raw_data_df.shape[0], 0)

    def test_load_train_merged(self):
        raw_data_df = load_raw_train_merged(nrows=1000)
        self.assertIsNotNone(raw_data_df)
        self.assertEqual(type(raw_data_df), pd.DataFrame)
        self.assertGreater(raw_data_df.shape[0], 0)

    def test_load_test_merged(self):
        raw_data_df = load_raw_test_merged()
        self.assertIsNotNone(raw_data_df)
        self.assertEqual(type(raw_data_df), pd.DataFrame)
        self.assertGreater(raw_data_df.shape[0], 0)


if __name__ == '__main__':
    unittest.main()
