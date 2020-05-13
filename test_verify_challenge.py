import unittest
from five_challenge import FizzBuzz

class VerifyChallenge(unittest.TestCase):


    def test_only_3_multiples(self):
        
        _input = [3, 9, 12, 18, 21, 24, 27]
        expected_result = (
            "Fizz\n"
            "Fizz\n"
            "Fizz\n"
            "Fizz\n"
            "Fizz\n"
            "Fizz\n"
            "Fizz\n"
            "..............................................................\n"
            "Resumo\n"
            "7 Fizz\n"
            "0 Buzz\n"
            "0 FizzBuzz\n"
            "..............................................................\n"
        )
        result = FizzBuzz(_input)

        self.assertEqual(expected_result, result)
    

    def test_only_5_multiples(self):

        _input = [5, 10, 20, 25, 35, 40, 50]
        expected_result = (
            "Buzz\n"
            "Buzz\n"
            "Buzz\n"
            "Buzz\n"
            "Buzz\n"
            "Buzz\n"
            "Buzz\n"
            "..............................................................\n"
            "Resumo\n"
            "0 Fizz\n"
            "7 Buzz\n"
            "0 FizzBuzz\n"
            "..............................................................\n"
        )
        result = FizzBuzz(_input)

        self.assertEqual(expected_result, result)


    def test_3_and_5_multiples(self):

        _input = [15, 30, 45, 60, 75, 90, 105]
        expected_result = (
            "FizzBuzz\n"
            "FizzBuzz\n"
            "FizzBuzz\n"
            "FizzBuzz\n"
            "FizzBuzz\n"
            "FizzBuzz\n"
            "FizzBuzz\n"
            "..............................................................\n"
            "Resumo\n"
            "0 Fizz\n"
            "0 Buzz\n"
            "7 FizzBuzz\n"
            "..............................................................\n"
        )
        result = FizzBuzz(_input)

        self.assertEqual(expected_result, result)


    def test_without_multiples(self):

        _input = [1, 2, 4, 7, 8, 11, 13]
        expected_result = (
            "1\n"
            "2\n"
            "4\n"
            "7\n"
            "8\n"
            "11\n"
            "13\n"
            "..............................................................\n"
            "Resumo\n"
            "0 Fizz\n"
            "0 Buzz\n"
            "0 FizzBuzz\n"
            "..............................................................\n"
        )
        result = FizzBuzz(_input)

        self.assertEqual(expected_result, result)


    def test_mixed_numbers(self):

        _input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        expected_result = (
            "1\n"
            "2\n"
            "Fizz\n"
            "4\n"
            "Buzz\n"
            "Fizz\n"
            "7\n"
            "8\n"
            "Fizz\n"
            "Buzz\n"
            "11\n"
            "Fizz\n"
            "13\n"
            "14\n"
            "FizzBuzz\n"
            "..............................................................\n"
            "Resumo\n"
            "4 Fizz\n"
            "2 Buzz\n"
            "1 FizzBuzz\n"
            "..............................................................\n"
        )
        result = FizzBuzz(_input)

        self.assertEqual(expected_result, result)