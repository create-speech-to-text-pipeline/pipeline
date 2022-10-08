import unittest
import sys, os
import io
import pandas as pd
sys.path.append(os.path.abspath(os.path.join('../airflow/dags')))

from scripts.dataloader import DataLoader

class TestDataLoader(unittest.TestCase):
     def test_read_csv(self):
        """Test the readcsv method"""
        filename = "../airflow/data/AmharicNewsDataset.csv"
        dataloader = DataLoader()
        pd = dataloader.read_csv(filename)
        col1 = pd.columns[0]
        self.assertEqual(col1, "headline")
        col1 = pd.columns[2]
        self.assertEqual(col1, "date")

if __name__ == '__main__':
    unittest.main()
