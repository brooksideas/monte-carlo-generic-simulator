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
        self.number_die = Die(die_list)
        self.coin_die = Die(coin_list)

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

    # Test the change weight method for integer
    def test_change_weight_int_die(self):
        self.number_die.change_weight(2, 5)
        actual = self.number_die.faces_weights_df.iloc[1, 1:][0]
        expected = 5.0
        self.assertEqual(actual, expected)

    # Test the change weight method for string
    def test_change_weight_string_die(self):
        self.coin_die.change_weight('Heads', 4)
        actual = self.coin_die.faces_weights_df.iloc[0, 1:][0]
        expected = 4.0
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=3)
