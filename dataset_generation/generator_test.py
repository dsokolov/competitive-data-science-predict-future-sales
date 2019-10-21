import unittest
from sources.raw import load_raw_train_merged
from dataset_generation.generator import generate_dataset

class GeneratorTestCase(unittest.TestCase):

    def test_generate_dataset(self):
        raw_df = load_raw_train_merged(nrows=1000)
        dataset_df = generate_dataset(raw_df, 5, 2)
        print(dataset_df.head(10))


if __name__ == '__main__':
    unittest.main()
