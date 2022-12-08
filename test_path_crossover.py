import unittest
import csv


from path import CsvPath


class TestCsvPath(unittest.TestCase):

    def test_small_csvpath_crossover(self):
        path = CsvPath(2)
        filename = 'small_test_path.csv'

        with open(filename, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                x, y = float(row[0]), float(row[1])
                path.run(True, x, y)

        print(f"Lookahead is : {path.lookahead}")
    
    def test_big_csvpath_crossover(self):
        path = CsvPath(2)
        filename = 'big_test_path.csv'

        with open(filename, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                x, y = float(row[0]), float(row[1])
                path.run(True, x, y)

        print(f"Lookahead is : {path.lookahead}")

if __name__ == '__main__':
    test = TestCsvPath()
    test.test_small_csvpath_crossover()
    test.test_big_csvpath_crossover()