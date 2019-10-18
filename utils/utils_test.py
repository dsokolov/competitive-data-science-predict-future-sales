import unittest

import pandas as pd

from utils.utils import load_raw_categories
from utils.utils import load_raw_items
from utils.utils import load_raw_sales_train


class UtilsTestCase(unittest.TestCase):

    def test_load_raw_sales_train(self):
        raw_data_df = load_raw_sales_train()
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


if __name__ == '__main__':
    unittest.main()
