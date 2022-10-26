import random as rd
from itertools import product

import numpy as np
import pandas as pd


class Die:
    """
    PURPOSE:
    A class accepts variety of random variables associated with stochastic
    processes and rolls/runs and returns a list of outcomes

    ATTRIBUTES:
    Takes a list of faces

    METHODS:
    __init__::Return a dataframe with faces and weights column
    change_weight:: Changes the weight of a single side/face.
    roll_die:: Roll/Run the die one or more times
    show_state:: Display the current set of the faces and weights
    -------------------------------------------------------------------------
    """

    def __init__(self, faces):
        """
        PURPOSE:
        Initializes private dataframe containing faces and weights respectively

        INPUTS:
        Takes a List of faces ([<int> | <str> | <float>])

        OUTPUTS:
        Return a dataframe with faces and weights column (DataFrame(<int> | <str> | <float>))
        """
        self.faces = list(set(faces))  # The faces must be unique
        self.weights = np.ones(len(faces))  # Initialize the weight to 1.0
        self.faces_weights_df = pd.DataFrame(self.faces, columns=['faces'])
        self.faces_weights_df = self.faces_weights_df.assign(weights=self.weights)

    # Change the weight of a single side
    def change_weight(self, face_value, new_weight):
        """
        PURPOSE:
        Change the weight of a single side/face

        INPUTS: Takes two arguments face value (<int> | <str> | <float>) to be changed and the new weight (<int> |
        <str> | <float>)

        OUTPUTS:
        Assigns a dataframe with faces and the newly assigned weights (DataFrame(<int> | <str> | <float>))
        """
        # face passed must be valid
        is_face_valid = (lambda face_values: face_values in self.faces)
        if not is_face_valid(face_value):
            return "Error:The face passed is invalid."
        # Weight passed must be valid
        is_weight_valid = isinstance(new_weight, float) | isinstance(new_weight, int) | isinstance(new_weight, bool)
        if not is_weight_valid:
            return "Error:The Weight passed is invalid."
        self.faces_weights_df.iloc[self.faces.index(face_value), [1]] = new_weight

    # Roll the die one or more times
    def roll_die(self, number_of_rolls=1):
        """
        PURPOSE:
        Roll the die one or more times

        INPUTS:
        Takes one argument which is Number of rolls (<int>)

        OUTPUTS:
        Return a list of outcomes similar to the face types ([<int> | <str> | <float>]).
        """
        return [rd.choice(self.faces) for _ in range(number_of_rolls)]

    # Show the user the die’s current set of faces and weights
    def show_state(self):
        """
        PURPOSE:
        Show the die’s current set of faces and weights(could be changed by change_weight)

        INPUTS:
        Takes no argument

        OUTPUTS:
        Returns the dataframe according to the face types (DataFrame(<int> | <str> | <float>)).
        """
        return self.faces_weights_df


class Game:
    """
    PURPOSE:
    A class to roll one or more dice of the same kind one or more times.
    Inherits methods from Die class to perform the simulations

    ATTRIBUTES:
    Takes a list of similarly defined dice (Die Objects/instances).

    METHODS:
    __init__:: Instantiate a similar Die Objects.
    play:: Rolls the Dice using the inherited roll_die method from the Die class
    show:: Display the results of the most recent play
    -------------------------------------------------------------------------
    """

    def __init__(self, dice):
        """
        PURPOSE:
        Initializes dice object which is inherited from the Die Class

        INPUTS:
        Takes one argument which is a List of Dice Objects ([<int> | <str> | <float>])

        OUTPUTS:
        Assigns internal dice variable for use in multiple areas (DataFrame(<int> | <str> | <float>))
        """
        # Take the list of dice
        self.dice = dice
        self.cols = []
        self.columns = []
        self.play_df = pd.DataFrame()
        self.number_of_rolls = 0
        self.play_result_df_list = []

    # Rolls the Dice
    def play(self, number_of_rolls):
        """
        PURPOSE:
        Rolls the Dice using the inherited roll_die method from the Die class

        INPUTS:
        Takes one parameter to specify how many times the dice should be rolled.(<int>)

        OUTPUTS: Saves the result of the play to a private dataframe of shape N rolls by M dice. (DataFrame(<int> |
        <str> | <float>))
        """
        # assign and make the Number of rolls accessible
        self.number_of_rolls = number_of_rolls
        self.play_result_df_list = []
        roll_data = []
        # Filter out the Die for M Column
        self.columns = ["Die " + str(index + 1) for index, dice in enumerate(self.dice)]
        # Pull out the Cols temporary
        for roll in self.dice:
            self.cols = [str(die) for die in roll.faces]

        # Iterate through the list of dice and perform the same operations
        for roll in range(self.number_of_rolls):
            each_roll_results = []
            for d in self.dice:
                # Roll the dice Once append the results in temporary list for use
                each_roll_results.append(d.roll_die(1)[0])
            roll_data.append(each_roll_results)

            # Create a single dimension list with similar results populate across the horizontal list
        index = [i for i in range(1, len(roll_data) + 1)]
        # Create the play Dataframe from the roll_data , index and columns
        self.play_df = pd.DataFrame(roll_data,
                                    index=index,
                                    columns=self.columns)
        self.play_df.index.name = 'roll number'
        return self.play_df

    # Display the Dice results
    # Default df return form is Wide = 1 and Narrow option is 2
    def show(self, play_result_df, df_form=1):
        """
        PURPOSE:
        Show the results of the most recent play.

        INPUTS: Takes two arguments the play dataframe (DataFrame(<int> | <str> | <float>)) and df_form (<int>) that
        means the default Wide = 1 and Narrow option is 2 as parameters

        OUTPUTS: Display the result of the play result as a dataframe of shape N rolls by M dice.(DataFrame(<int> |
        <str> | <float>))
        """
        if df_form != 1 and df_form != 2:
            return print("Error:The dataframe display format option can only be Wide(value 1) or Narrow(value 2).")

        self.play_result_df_list.append(play_result_df)

        if df_form == 1:
            return play_result_df
        else:
            return pd.melt(play_result_df, value_vars=self.cols, var_name='die number', value_name='face rolled',
                           ignore_index=False)


class Analyzer:
    """
    PURPOSE:
    A class to take the results of a single game and compute statistical properties about it.

    ATTRIBUTES:

    METHODS: __init__:: Instantiate a Game Objects from the Game Class and infers the data type of the die faces.
    face counts per roll, i.e. the number of times a given face appeared in each roll. For example, if a roll of five
    dice has all sixes, then the counts for this roll would be 6 for the face value '6' and 0 for the other faces.
    jackpot count, i.e. how many times a roll resulted in all faces being the same, e.g. six ones for a six-sided
    die. combo count, i.e. how many combination types of faces were rolled and their counts. permutation count,
    i.e. how may sequence types were rolled and their counts.
    -------------------------------------------------------------------------
    """

    def __init__(self, game):
        """
        PURPOSE:
        Initializes the game object which is inherited from the Game Class

        INPUTS:
        Takes one argument which is a Game Object

        OUTPUTS:
        Assigns Game Object for internal use , Game dataframe type (<int> | <str> | <float>),
        Result of the Game played([<int> | <str> | <float>])
        """
        self.game = game
        # Infers the data type of the die faces
        self.game_df_data_type = type(game.dice[0].faces[1])
        self.game_result = game.play_result_df_list
        self.game_result_df = game.play_df
        # Face count
        self.face_count_df = pd.DataFrame()
        self.face_list = []
        # Jackpot
        self.jackpot_list = []
        self.jackpot_results_df = pd.DataFrame()
        self.jackpot_results_df.index.name = ''
        self.jack_pot_indices = []
        # Combination
        self.combination_list = []
        self.combination_df = pd.DataFrame()
        # Permutation
        self.permutation_list = []
        self.permutation_df = pd.DataFrame()

        # Method to compute how many times a given face is rolled in each event

    def face_count(self):
        """
        PURPOSE:
        Method to compute how many times a given face is rolled in each event

        INPUTS:
        Takes no argument

        OUTPUTS:
        Returns the Face Count dataframe according to the initial dice face type (DataFrame(<int> | <str> | <float>))
        """
        index = [i for i in range(1, self.game.number_of_rolls + 1)]
        self.face_count_df = pd.DataFrame(index=index, columns=self.game.cols)
        self.face_count_df.index.name = 'roll number'
        self.face_list = np.zeros(len(self.game.cols),
                                  dtype=int)  # Hold the face value and increment when new similar value is found.
        # Uses Game Cols Structure Copy

        for index, row in self.game_result_df.iterrows():
            for col in self.game.columns:
                self.face_list[self.game.cols.index(str(row[col]))] = self.face_list[
                                                                          self.game.cols.index(str(row[col]))] + 1

                # Append the new face counts to the dataframe
            self.face_count_df.loc[index] = self.face_list
            self.face_list = np.zeros(len(self.game.cols), dtype=int)  # Flush the temporary list

        return self.face_count_df

    # Method to compute how many times the game resulted in all faces being identical
    def jackpot(self):
        """
        PURPOSE:
        Method to compute how many times the game resulted in all faces being identical

        INPUTS:
        Takes no argument

        OUTPUTS:
        Returns the count of how many times the game resulted in all faces being identical
        You can also access the Jackpot Dataframe using <Class Analyzer>.jackpot_results_df
        """
        self.jackpot_results_df = pd.DataFrame(columns=self.game.cols)
        self.jackpot_results_df.index.name = 'roll number'
        self.jack_pot_indices = []
        self.jackpot_list = np.zeros(len(self.game.cols),
                                     dtype=int)  # Hold the face value and increment when new similar value is found.
        # Uses Game Cols Structure Copy

        for index, row in self.game_result_df.iterrows():
            for col in self.game.columns:
                self.jackpot_list[self.game.cols.index(str(row[col]))] = self.jackpot_list[
                                                                             self.game.cols.index(str(row[col]))] + 1
                # Save the index only if all values result in similar faces, which is equal to number of cols
            if len(self.game.dice) in self.jackpot_list:
                self.jackpot_list[self.jackpot_list != len(self.game.dice)] = 0
                # Append the Index for the dataframe
                self.jack_pot_indices.append(index + 1)
                # Append the new face counts to the jackpot_results dataframe
                self.jackpot_results_df.loc[index] = self.jackpot_list

            self.jackpot_list = np.zeros(len(self.game.cols), dtype=int)

        return len(self.jackpot_results_df.index)

        # Combo method to compute the distinct/unique combinations of faces rolled, along with their counts

    # Count is always 1 because the specific combination only occurs Once
    def combo(self):
        """
        PURPOSE:
        Method to compute the distinct/unique combinations of faces rolled, along with their counts

        INPUTS:
        Takes no argument

        OUTPUTS: Returns the count of how many times the Game could result in distinct/unique combinations of faces
        when dice is played/rolled You can also access the full combination multi-columned Dataframe using <Class
        Analyzer>.combination_df or access the corresponding <Class Analyzer>.combination_list

        """

        # The faces that have been rolled by the dice game
        face_combination_rolled = []

        # The combination List of rolled dice with the respective count

        # Check if the face has been rolled during the Game; and form a List[(tuples)]
        die_faces_rolled = []
        for index, row in self.game_result_df.iterrows():
            for col in self.game.columns:
                current_die_face = row[col]
                die_faces_rolled.append(current_die_face)
            face_combination_rolled.append(tuple(die_faces_rolled + [0]))  # Initialize with zero append
            die_faces_rolled = []  # flush the list

        # Check all possible values similarly to the permutation given below
        check_face_presence = []
        for index, row in self.game_result_df.iterrows():
            for col in self.game.columns:
                # Check the type of Dataframe type to conditionally pass casting
                if self.game_df_data_type == int:
                    if row[col] not in check_face_presence:
                        check_face_presence.append(row[col])
                elif self.game_df_data_type == str:
                    if str(row[col]) not in check_face_presence:
                        check_face_presence.append(row[col])
                elif self.game_df_data_type == float:
                    if row[col] not in check_face_presence:
                        check_face_presence.append(row[col])

        # Loop through the results array and add to the face_combo_list only if not present
        # Extract only the Unique values
        face_combo_list = list(set(check_face_presence))

        # Sort the values
        face_combo_list.sort(key=self.game_df_data_type)

        # Perform the combination  of unique values and store it in self.permutation_df for public access
        # initializing the range with the Number of Dice rolled
        # using list comprehension to formulate all distinct permutation s of the elements
        combo_list = [list(face_combo_list) for _ in range(len(self.game.dice))]

        # using product() to get permutations
        self.combination_list = list(product(*combo_list))

        # Instantiate with 0 append to all values
        self.combination_list = [tuple(list(tup) + [0]) for tup in self.combination_list]

        # Construct the count for the combinations given
        for passed in face_combination_rolled:
            for index, tup in enumerate(self.combination_list):
                if tup[:-1] == passed[:-1]:
                    combination_increase = list(tup[-1:])[0] + 1
                    self.combination_list[index] = self.combination_list[index][:-1] + (combination_increase,)

        # Construct the combination  tuples indices
        combination_indices_list = [tuple([i] * len(self.combination_list)) for i in range(len(self.combination_list))]

        # Construct the Index name
        combination_indices_name_list = ["roll_number " + str(index + 1) for index in range(len(self.combination_list))]

        # Create Row Level MultiIndex
        combination_index = pd.MultiIndex.from_tuples(combination_indices_list, names=combination_indices_name_list)

        # Create Column Level MultiIndex
        cols = pd.MultiIndex.from_tuples(self.combination_list)
        # Create Data for the MultiIndex table
        data = [[1 for _ in range(len(self.combination_list))] for _ in range(len(self.combination_list))]
        # Construct the permutation  Dataframe
        self.combination_df = pd.DataFrame(data, columns=cols, index=combination_index)
        pd.set_option('display.max_rows', None)

        # Return the count of all the unique combinations from the game
        return len(list(set(face_combination_rolled)))

    # Permutation order matters , so we will have to look through all the possible values
    def permutation(self):
        """
        PURPOSE:
        Method to compute how may sequence types were rolled and their counts

        INPUTS:
        Takes no argument

        OUTPUTS:
        Returns the count of all the possible combinations of faces present when dice is played/rolled
        You can also access the permutation multi-columned Dataframe using <Class Analyzer>.permutation_df
        """

        # Check if the face has been rolled during the Game , checking presence
        check_face_presence = []
        for index, row in self.game_result_df.iterrows():
            for col in self.game.columns:
                # Check the type of Dataframe type to conditionally pass casting
                if self.game_df_data_type == int:
                    if row[col] not in check_face_presence:
                        check_face_presence.append(row[col])
                elif self.game_df_data_type == str:
                    if str(row[col]) not in check_face_presence:
                        check_face_presence.append(row[col])
                elif self.game_df_data_type == float:
                    if row[col] not in check_face_presence:
                        check_face_presence.append(row[col])

        # Loop through the results array and add to the face_permutation_list only if not present
        # Extract only the Unique values
        face_permutation_list = list(set(check_face_presence))

        # Sort the values
        face_permutation_list.sort(key=self.game_df_data_type)

        # Perform the permutation  of unique values and store it in self.permutation_df for public access
        # initializing the range with the Number of Dice rolled
        # using list comprehension to formulate all distinct permutation s of the elements
        perm_list = [list(face_permutation_list) for _ in range(len(self.game.dice))]

        # using product() to get permutation s
        self.permutation_list = list(product(*perm_list))

        # Construct the permutation  tuples indices
        permutation_indices_list = [tuple([i] * len(self.permutation_list)) for i in range(len(self.permutation_list))]

        # Construct the Index name
        permutation_indices_name_list = ["roll_number " + str(index + 1) for index in range(len(self.permutation_list))]

        # Create Row Level MultiIndex
        permutation_index = pd.MultiIndex.from_tuples(permutation_indices_list, names=permutation_indices_name_list)

        # Create Column Level MultiIndex
        cols = pd.MultiIndex.from_tuples(self.permutation_list)

        # Create Data for the MultiIndex table
        data = [[1 for _ in range(len(self.permutation_list))] for _ in range(len(self.permutation_list))]
        # Construct the permutation  Dataframe
        self.permutation_df = pd.DataFrame(data, columns=cols, index=permutation_index)
        pd.set_option('display.max_rows', None)
        return len(self.permutation_list)
