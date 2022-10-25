##############################
# File name montecarlo_test.py#
##############################
import unittest
from montecarlo import Die, Game, Analyzer


class MonteCarloTestSuite(unittest.TestCase):
    # Setup before every single test
    def setUp(self):
        die_list = [1, 2, 3, 4, 5, 6]
        coin_list = ['Heads', 'Tails']
        number_die = Die(die_list)
        coin_die = Die(coin_list)

    def tearDown(self):
        # Garbage collection process
        self.number_die = None
        self.coin_die = None

    # Testing Integer number Die Object creation
    def test_create_number_die(self):
        die_list = [1, 2, 3, 4, 5, 6]
        die = Die(die_list)
        actual = type(die)
        expected = type(Die(die_list))
        self.assertTrue(actual, expected)

    # Testing String Die Object creation
    def test_create_string_die(self):
        coin_list = ['Heads', 'Tails']
        die = Die(coin_list)
        actual = type(die)
        expected = type(Die(coin_list))
        self.assertTrue(actual, expected)

    # Testing Float Die creation
    def test_create_float_die(self):
        float_die_list = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        die = Die(float_die_list)
        actual = type(die)
        expected = type(Die(float_die_list))
        self.assertTrue(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=3)
