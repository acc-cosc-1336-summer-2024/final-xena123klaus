import unittest
from io import StringIO
import sys
from src.question_a.question_a import Stock
from src.question_b.question_b import create_multiplication_table, display_multiplication_table
from src.question_c.question_c import Stock as StockC, stock_purchase_history
from src.question_d.question_d import get_statistics

class TestStock(unittest.TestCase):

    def test_stock_initialization(self):
        stock = Stock("MSFT", "Microsoft")
        self.assertEqual(stock.get_symbol(), "MSFT")
        self.assertEqual(stock.get_company_name(), "Microsoft")

    def test_create_multiplication_table(self):
        table = create_multiplication_table()
        expected_table = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
            [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],
            [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],
            [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
            [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],
            [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],
            [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],
            [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],
            [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        ]
        self.assertEqual(table, expected_table)

    def test_display_multiplication_table(self):
        table = create_multiplication_table()
        expected_output = (
            " 1  2  3  4  5  6  7  8  9 10\n"
            " 2  4  6  8 10 12 14 16 18 20\n"
            " 3  6  9 12 15 18 21 24 27 30\n"
            " 4  8 12 16 20 24 28 32 36 40\n"
            " 5 10 15 20 25 30 35 40 45 50\n"
            " 6 12 18 24 30 36 42 48 54 60\n"
            " 7 14 21 28 35 42 49 56 63 70\n"
            " 8 16 24 32 40 48 56 64 72 80\n"
            " 9 18 27 36 45 54 63 72 81 90\n"
            "10 20 30 40 50 60 70 80 90 100\n"
        )
        
        captured_output = StringIO()
        sys.stdout = captured_output
        display_multiplication_table(table)
        sys.stdout = sys.__stdout__  

        self.assertEqual(captured_output.getvalue(), expected_output)
       

    def test_question_c_stock_purchase_history(self):
        history = stock_purchase_history()
        expected_history = {
            "AAPL": "Apple Inc",
            "CAT": "Caterpillar",
            "EK": "Eastman Kodak",
            "GOOG": "Google",
            "MSFT": "Microsoft"
        }
        self.assertEqual(history, expected_history)

    def test_question_d_get_statistics(self):
        numbers = [10, 20, 30, 40, 50]
        lowest, highest, total, average = get_statistics(numbers)
        self.assertEqual(lowest, 10)
        self.assertEqual(highest, 50)
        self.assertEqual(total, 150)
        self.assertAlmostEqual(average, 30.0)

    def test_question_d_get_statistics_with_invalid_length(self):
        with self.assertRaises(ValueError):
            get_statistics([1, 2, 3])




