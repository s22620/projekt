import unittest
import pandas as pd
from src.data_analysis import DataAnalysis

class TestDataAnalysis(unittest.TestCase):
    def setUp(self):
        data = {
            'experience_level': ['SE', 'MI', 'EN', 'SE'],
            'salary_in_usd': [100000, 120000, 90000, 150000],
            'job_title': ['Data Engineer', 'Data Scientist', 'Data Analyst', 'AI Engineer']
        }
        self.df = pd.DataFrame(data)
        self.analysis = DataAnalysis(self.df)

    def test_basic_statistics(self):
        stats = self.analysis.basic_statistics()
        self.assertEqual(stats.loc['count', 'salary_in_usd'], 4)
        self.assertEqual(stats.loc['mean', 'salary_in_usd'], 115000)

    def test_filter_data(self):
        filtered_data = self.analysis.filter_data('job_title', 'Data Engineer')
        self.assertEqual(len(filtered_data), 1)
        self.assertEqual(filtered_data.iloc[0]['job_title'], 'Data Engineer')

    def test_convert_categorical_to_numeric(self):
        self.analysis.convert_categorical_to_numeric('experience_level')
        self.assertTrue(pd.api.types.is_numeric_dtype(self.analysis.data['experience_level']))

    def test_sort_data(self):
        sorted_data = self.analysis.sort_data('salary_in_usd', ascending=False)
        self.assertEqual(sorted_data.iloc[0]['salary_in_usd'], 150000)
        self.assertEqual(sorted_data.iloc[-1]['salary_in_usd'], 90000)

if __name__ == '__main__':
    unittest.main()
