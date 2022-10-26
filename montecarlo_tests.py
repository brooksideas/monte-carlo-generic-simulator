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
        self.die_analyzer = Analyzer(self.die_game)
        self.coin_analyzer = Analyzer(self.coin_game)

    def tearDown(self):
        """Garbage collection process to free up memory"""
        self.number_die = None
        self.coin_die = None
        self.die_game = None
        self.coin_game = None
        self.die_analyzer = None
        self.coin_analyzer = None

    def test_create_number_die(self):
        """ Testing Integer number Die Object creation"""

        die_list = [1, 2, 3, 4, 5, 6]
        actual = Die(die_list)
        self.assertIsInstance(actual, Die)

    def test_create_string_die(self):
        """ Testing String Die Object creation"""

        coin_list = ['Heads', 'Tails']
        actual = Die(coin_list)
        self.assertIsInstance(actual, Die)

    def test_create_float_die(self):
        """Testing Float Die creation"""

        float_die_list = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        actual = Die(float_die_list)
        self.assertIsInstance(actual, Die)

    def test_change_weight_int_die(self):
        """ Test the change weight method for integer"""

        self.number_die.change_weight(2, 5)
        actual = self.number_die.faces_weights_df.iloc[1, 1:][0]
        expected = 5.0
        self.assertEqual(actual, expected)

    def test_change_weight_string_die(self):
        """Test the change weight method for string"""
        self.coin_die.change_weight('Tails', 4)
        # actual = self.coin_die.faces_weights_df['weights'][:-1][0]
        actual = self.coin_die.faces_weights_df
        actual = (actual[actual['faces'] == 'Tails'])['weights'][0]
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
        self.game = None
        self.assertCountEqual(actual.dice, dice)
        self.assertIsInstance(actual, Game)

    def test_create_game_string_die(self):
        """Create a Game Object from the given dice object , expected an instantiated Die Object list passed"""
        dice = []
        dice.extend([self.coin_die, self.coin_die])
        self.game = Game(dice)
        actual = self.game
        self.game = None
        self.assertCountEqual(actual.dice, dice)
        self.assertIsInstance(actual, Game)

    def test_play_game_number_die(self):
        """Play a games with the number faced die"""
        actual = self.die_game.play(10)
        expected_length = 10
        expected_shape = (10, 2)
        self.assertEqual(len(actual), expected_length)
        self.assertEqual(actual.shape, expected_shape)

    def test_play_game_string_die(self):
        """Play a games with the string faced die"""
        actual = self.coin_game.play(10)
        expected_length = 10
        expected_shape = (10, 2)
        self.assertEqual(len(actual), expected_length)
        self.assertEqual(actual.shape, expected_shape)

    def test_show_game_number_die(self):
        """Show the correct game play result output """
        actual = self.die_game.show(self.die_game.play(10), 1)
        expected_length = 10
        expected_shape = (10, 2)
        expected_class_type = pd.DataFrame()
        self.assertIn('Die 1', actual.columns)
        self.assertIn('Die 2', actual.columns)
        self.assertEqual(len(actual), expected_length)
        self.assertEqual(actual.shape, expected_shape)
        self.assertTrue(type(actual), expected_class_type)

    def test_show_game_string_die(self):
        """Show the correct game play result output """
        actual = self.coin_game.show(self.coin_game.play(10), 1)
        expected_length = 10
        expected_shape = (10, 2)
        expected_class_type = pd.DataFrame()
        self.assertIn('Die 1', actual.columns)
        self.assertIn('Die 2', actual.columns)
        self.assertEqual(len(actual), expected_length)
        self.assertEqual(actual.shape, expected_shape)
        self.assertTrue(type(actual), expected_class_type)

    def test_create_analyzer_number_die(self):
        """Test created Analyzer class is correct and infers the datatype from the Game Object"""
        actual = Analyzer(self.die_game)
        expected_dataframe_data_type = type(self.die_game.dice[0].faces[1])
        self.assertIsInstance(actual, Analyzer)
        self.assertTrue(actual.game_df_data_type, expected_dataframe_data_type)

    def test_create_analyzer_string_die(self):
        """Test created Analyzer class is correct and infers the datatype from the Game Object"""
        actual = Analyzer(self.coin_game)
        expected_dataframe_data_type = type(self.coin_game.dice[0].faces[1])
        self.assertIsInstance(actual, Analyzer)
        self.assertTrue(actual.game_df_data_type, expected_dataframe_data_type)

    def test_face_count_number_die(self):
        """Test if the die face count dataframe is correct and has the proper Header construction"""
        actual = self.die_analyzer.face_count()
        expected_list = len(self.die_analyzer.face_list)
        expected_dataframe_data_type = self.die_analyzer.face_count_df
        self.assertEqual(actual.empty, expected_dataframe_data_type.empty)
        self.assertEqual(len(actual), expected_list)

    def test_face_count_string_die(self):
        """Test if the coin face count dataframe is correct and has the proper Header construction"""
        actual = self.coin_analyzer.face_count()
        expected_list = len(self.coin_analyzer.face_list)
        expected_dataframe_data_type = self.coin_analyzer.face_count_df
        self.assertEqual(actual.empty, expected_dataframe_data_type.empty)
        self.assertEqual(len(actual), expected_list)

    def test_jackpot_number_die(self):
        """ Test the Jackpot method returns a count of strict type integer"""
        actual = self.die_analyzer.jackpot()
        expected_list = len(self.die_analyzer.jackpot_list)
        expected_data_frame = len(self.die_analyzer.jackpot_results_df)
        self.assertIsInstance(actual, int)
        self.assertEqual(actual, expected_list)
        self.assertEqual(actual, expected_data_frame)

    def test_jackpot_string_die(self):
        """ Test the Jackpot method returns a count of strict type integer"""
        actual = self.coin_analyzer.jackpot()
        expected_list = len(self.coin_analyzer.jackpot_list)
        expected_data_frame = len(self.coin_analyzer.jackpot_results_df)
        self.assertIsInstance(actual, int)
        self.assertEqual(actual, expected_list)
        self.assertEqual(actual, expected_data_frame)


if __name__ == '__main__':
    unittest.main(verbosity=3)
