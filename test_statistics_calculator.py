"""Tests for the statistics calculator."""

import unittest

from statistics_calculator import calculate_statistics, parse_numbers


class StatisticsCalculatorTests(unittest.TestCase):
    def test_calculates_mean_median_and_single_mode(self):
        result = calculate_statistics([2, 4, 4, 6, 8])

        self.assertEqual(result["mean"], 4.8)
        self.assertEqual(result["median"], 4)
        self.assertEqual(result["modes"], [4])

    def test_handles_even_number_of_values(self):
        result = calculate_statistics([1, 2, 3, 4])

        self.assertEqual(result["mean"], 2.5)
        self.assertEqual(result["median"], 2.5)

    def test_reports_multiple_modes(self):
        result = calculate_statistics([1, 1, 2, 2, 3])

        self.assertEqual(result["modes"], [1, 2])

    def test_supports_decimal_and_negative_values(self):
        result = calculate_statistics([-1.5, 2.5, 2.5])

        self.assertAlmostEqual(result["mean"], 1.1666666666666667)
        self.assertEqual(result["median"], 2.5)
        self.assertEqual(result["modes"], [2.5])

    def test_rejects_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_statistics([])

    def test_parses_numeric_strings(self):
        self.assertEqual(parse_numbers(["1", "2.5", "-3"]), [1.0, 2.5, -3.0])

    def test_rejects_invalid_values(self):
        with self.assertRaises(ValueError):
            parse_numbers(["1", "hello", "3"])


if __name__ == "__main__":
    unittest.main()
