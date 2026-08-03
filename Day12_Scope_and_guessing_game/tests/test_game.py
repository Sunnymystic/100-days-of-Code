import unittest

from the_number_guessing_game import get_attempts_for_difficulty, check_guess


class TestGameHelpers(unittest.TestCase):
    def test_get_attempts_easy(self):
        self.assertEqual(get_attempts_for_difficulty('easy'), 10)

    def test_get_attempts_hard(self):
        self.assertEqual(get_attempts_for_difficulty('hard'), 5)

    def test_check_guess_low(self):
        self.assertEqual(check_guess(3, 10), 'low')

    def test_check_guess_high(self):
        self.assertEqual(check_guess(15, 10), 'high')

    def test_check_guess_correct(self):
        self.assertEqual(check_guess(10, 10), 'correct')


if __name__ == '__main__':
    unittest.main()
