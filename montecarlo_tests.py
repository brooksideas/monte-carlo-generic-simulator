###############################
# File name montecarlo_test.py#
###############################
import unittest
import pandas as pd
from montecarlo import Die, Game, Analyzer


class MonteCarloTestSuite(unittest.TestCase):
    def setUp(self):
        """Setup Die , Game and Analyzer before every single test"""

        die_list = [1, 2, 3, 4, 5, 6]
        coin_list = ['Heads', 'Tails']
        self.number_die = Die(die_list)
        self.coin_die = Die(coin_list)
        number_dice = []
        number_dice.extend([self.number_die, self.number_die])
        coin_dice = []
        coin_dice.extend([self.coin_die, self.coin_die])
        self.die_game = Game(number_dice)
        self.coin_game = Game(coin_dice)

    def tearDown(self):
        """Garbage collection process to free up memory"""
        self.number_die = None
        self.coin_die = None
        self.die_game = None
        self.coin_game = None

    def test_create_number_die(self):
        """ Testing Integer number Die Object creation"""

        die_list = [1, 2, 3, 4, 5, 6]
        self.die = Die(die_list)
        actual = type(self.die)
        expected = type(Die(die_list))
        # Manual Garbage collection here
        self.die = None
        self.assertTrue(actual, expected)

    def test_create_string_die(self):
        """ Testing String Die Object creation"""

        coin_list = ['Heads', 'Tails']
        self.die = Die(coin_list)
        actual = type(self.die)
        expected = type(Die(coin_list))
        self.assertTrue(actual, expected)

    def test_create_float_die(self):
        """Testing Float Die creation"""

        float_die_list = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        self.die = Die(float_die_list)
        actual = type(self.die)
        expected = type(Die(float_die_list))
        self.assertTrue(actual, expected)

    def test_change_weight_int_die(self):
        """ Test the change weight method for integer"""

        self.number_die.change_weight(2, 5)
        actual = self.number_die.faces_weights_df.iloc[1, 1:][0]
        expected = 5.0
        self.assertEqual(actual, expected)

    def test_change_weight_string_die(self):
        """Test the change weight method for string"""
        self.coin_die.change_weight('Tails', 4)
        actual = self.coin_die.faces_weights_df.iloc[1, 1:][0]
        expected = 4.0
        self.assertEqual(actual, expected)

    def test_incorrect_face__number_input_exception(self):
        """" Test error response when an incorrect face value is passed in string expecting a number"""

        actual = self.number_die.change_weight("2", 5)
        expected = "Error:The face passed is invalid."
        self.assertEqual(actual, expected)

    def test_incorrect_face_string_input_exception(self):
        """" Test error response when an incorrect face value is passed in number expecting a string"""

        actual = self.coin_die.change_weight(2, 5)
        expected = "Error:The face passed is invalid."
        self.assertEqual(actual, expected)

    def test_roll_number_die(self):
        """Test the number faced die being rolled expects a random 10 values"""
        actual = self.number_die.roll_die(10)
        expected = 10
        expected_class_type = []
        self.assertEqual(len(actual), expected)
        self.assertTrue(type(actual), type(expected_class_type))

    def test_roll_string_die(self):
        """Test the string faced die being rolled expects a random 10 values"""
        actual = self.coin_die.roll_die(10)
        expected = 10
        expected_class_type = []
        self.assertEqual(len(actual), expected)
        self.assertTrue(type(actual), type(expected_class_type))

    def test_show_number_die_state(self):
        """Test if the correct state is being displayed to the user, Shape , Length and Type"""
        actual = self.number_die.faces_weights_df
        expected_length = 6
        expected_shape = (6, 2)
        expected_class_type = pd.DataFrame()
        self.assertEqual(len(actual), expected_length)
        self.assertEqual(actual.shape, expected_shape)
        self.assertTrue(type(actual), expected_class_type)

    def test_show_string_die_state(self):
        """Test if the correct state is being displayed to the user, Shape , Length and Type"""
        actual = self.coin_die.faces_weights_df
        expected_length = 2
        expected_shape = (2, 2)
        expected_class_type = pd.DataFrame()
        self.assertEqual(len(actual), expected_length)
        self.assertEqual(actual.shape, expected_shape)
        self.assertTrue(type(actual), expected_class_type)

    def test_create_game_number_die(self):
        """Create a Game Object from the given dice object , expected an instantiated Die Object list passed"""
        dice = []
        dice.extend([self.number_die, self.number_die])
        self.game = Game(dice)
        actual = self.game
        expected_class_type = type(self.game)
        self.game = None
        self.assertCountEqual(actual.dice, dice)
        self.assertTrue(type(actual), expected_class_type)

    def test_create_game_string_die(self):
        """Create a Game Object from the given dice object , expected an instantiated Die Object list passed"""
        dice = []
        dice.extend([self.coin_die, self.coin_die])
        self.game = Game(dice)
        actual = self.game
        expected_class_type = type(self.game)
        self.game = None
        self.assertCountEqual(actual.dice, dice)
        self.assertTrue(type(actual), expected_class_type)

    def test_play_game_number_die(self):
        """Play a games with the number faced die"""


if __name__ == '__main__':
    unittest.main(verbosity=3)
