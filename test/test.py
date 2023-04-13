import unittest
import task
import pandas

file_details = pandas.read_csv('orders.csv')

class Testrevenue(unittest.TestCase):
     
    def test_revenue_by_each_month(self):
        self.assertEqual(task.revenue_by_each_month(file_details), {'jan': 4750, 'mar': 1000})

    def test_revenue_by_each_product(self):
        self.assertEqual(task.revenue_by_each_product(file_details), {'prod_name1': 2000, 'prod_name2': 1500, 'prod_name3': 2250})
    
    def test_revenue_by_each_customer(self):
        self.assertEqual(task.revenue_by_each_customer(file_details), {'cus_1': 4250, 'cus_2': 500, 'cus_3': 1000})


if __name__ == '__main__':
    unittest.main()