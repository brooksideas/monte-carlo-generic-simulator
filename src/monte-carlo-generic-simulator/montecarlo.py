import random as rd
from itertools import combinations, product

import numpy as np
import pandas as pd


class Die:
    '''
    PURPOSE:
    A class accepts variety of random variables associated with stochastic
    processes and rolls/runs and returns a list of outcomes

    ATTRIBUTES:
    Takes an list of faces

    METHODS:
    __init__::Return a dataframe with faces and weights column
    change_weight:: Changes the weight of a single side/face.
    roll_die:: Roll/Run the die one or more times
    show_state:: Display the current set of the faces and weights
    -------------------------------------------------------------------------
    '''

    def __init__(self, faces):
        '''
        PURPOSE:
        Initializes private dataframe containing faces and weights respectively

        INPUTS:
        Takes a List of faces ([<int> | <str> | <float>])

        OUTPUTS:
        Return a dataframe with faces and weights column (DataFrame(<int> | <str> | <float>))
        '''
        self.faces = list(set(faces))  # The faces must be unique
        self.weights = np.ones(len(faces))  # Initialize the weight to 1.0
        self.faces_weights_df = pd.DataFrame(self.faces, columns=['faces'])
        self.faces_weights_df = self.faces_weights_df.assign(weights=self.weights)

    # Change the weight of a single side
    def change_weight(self, face_value, new_weight):
        '''
        PURPOSE:
        Change the weight of a single side/face

        INPUTS:
        Takes two arguments face value (<int> | <str> | <float>) to be changed and the new weight (<int> | <str> | <float>)

        OUTPUTS:
        Assigns a dataframe with faces and the newly assigned weights (DataFrame(<int> | <str> | <float>))
        '''
        # face passed must be valid
        is_face_valid = (lambda face_value: face_value in self.faces)
        if (not is_face_valid(face_value)): return "Error:The face passed is invalid."
        # Weight passed must be valid
        is_weight_valid = isinstance(new_weight, float) | isinstance(new_weight, int) | isinstance(new_weight, bool)
        if (not is_weight_valid): return "Error:The Weight passed is invalid."
        self.faces_weights_df.iloc[self.faces.index(face_value), [1]] = new_weight

    # Roll the die one or more times
    def roll_die(self, number_of_rolls=1):
        '''
        PURPOSE:
        Roll the die one or more times

        INPUTS:
        Takes one argument which is Number of rolls (<int>)

        OUTPUTS:
        Return a list of outcomes similar to the face types ([<int> | <str> | <float>]).
        '''
        return [rd.choice(self.faces) for roll in range(number_of_rolls)]

    # Show the user the die’s current set of faces and weights
    def show_state(self):
        '''
        PURPOSE:
        Show the die’s current set of faces and weights(could be changed by change_weight)

        INPUTS:
        Takes no argument

        OUTPUTS:
        Returns the dataframe according to the face types (DataFrame(<int> | <str> | <float>)).
        '''
        return self.faces_weights_df


class Game:
    '''
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
    '''

    def __init__(self, dice):
        '''
        PURPOSE:
        Initializes dice object which is inherited from the Die Class

        INPUTS:
        Takes one argument which is a List of Dice Objects ([<int> | <str> | <float>])

        OUTPUTS:
        Assigns internal dice variable for use in multiple areas (DataFrame(<int> | <str> | <float>))
        '''
        # Take the list of dice
        self.dice = dice
        self.cols = []
        self.play_df = pd.DataFrame()
        self.number_of_rolls = 0
        self.play_result_df_list = []

        # Rolls the Dice

    def play(self, number_of_rolls):
        '''
        PURPOSE:
        Rolls the Dice using the inherited roll_die method from the Die class

        INPUTS:
        Takes one parameter to specify how many times the dice should be rolled.(<int>)

        OUTPUTS:
        Saves the result of the play to a private dataframe of shape N rolls by M dice. (DataFrame(<int> | <str> | <float>))
        '''
        # assign and make the Number of rolls accessible
        self.number_of_rolls = number_of_rolls

        # Iterate through the list of dice and perform the same operations
        for roll in self.dice:
            self.cols = [str(die) for die in roll.faces]
            # Roll the dice X number of times extract the results
            roll_results = [roll for roll in roll.roll_die(self.number_of_rolls)]
            # Create a single dimension list with similar results populate across the horizontal list
            roll_data = np.array([np.full((1, len(roll.faces)), roll_result)[0] for roll_result in roll_results])
            index = [i for i in range(1, len(roll_data) + 1)]
            # Create the play Dataframe from the roll_data , index and columns
            self.play_df = pd.DataFrame(roll_data,
                                        index=index,
                                        columns=self.cols)
            self.play_df.index.name = 'roll number'
            return self.play_df

    # Display the Dice results
    # Default df return form is Wide = 1 and Narrow option is 2
    def show(self, play_result_df, df_form=1):
        '''
        PURPOSE:
        Show the results of the most recent play.

        INPUTS:
        Takes two arguments the play dataframe (DataFrame(<int> | <str> | <float>)) and df_form (<int>) that means the default Wide = 1 and Narrow option is 2 as parameters

        OUTPUTS:
        Display the result of the play result as a dataframe of shape N rolls by M dice.(DataFrame(<int> | <str> | <float>))
        '''
        if df_form != 1 and df_form != 2:
            return print("Error:The dataframe display format option can only be Wide(value 1) or Narrow(value 2).")

        self.play_result_df_list.append(play_result_df)
        if df_form == 1:
            return play_result_df
        else:
            return pd.melt(play_result_df, value_vars=self.cols, var_name='die number', value_name='face rolled',
                           ignore_index=False)


class Analyzer:
    '''
    PURPOSE:
    A class to take the results of a single game and compute statistical properties about it.

    ATTRIBUTES:

    METHODS:
    __init__:: Instantiate a Game Objects from the Game Class and infers the data type of the die faces.
    face counts per roll, i.e. the number of times a given face appeared in each roll. For example, if a roll of five dice has all sixes, then the counts for this roll would be 6 for the face value '6' and 0 for the other faces.
    jackpot count, i.e. how many times a roll resulted in all faces being the same, e.g. six ones for a six-sided die.
    combo count, i.e. how many combination types of faces were rolled and their counts.
    permutation count, i.e. how may sequence types were rolled and their counts.
    -------------------------------------------------------------------------
    '''

    def __init__(self, game):
        '''
        PURPOSE:
        Initializes the game object which is inherited from the Game Class

        INPUTS:
        Takes one argument which is a Game Object

        OUTPUTS:
        Assigns Game Object for internal use , Game dataframe type (<int> | <str> | <float>), Result of the Game played([<int> | <str> | <float>])
        '''
        self.game = game
        # Infers the data type of the die faces
        self.game_df_data_type = type(game.dice[0].faces[1])
        self.game_result = game.play_result_df_list
        # Face count
        self.face_count_df = pd.DataFrame()
        self.face_list = []
        # Jackpot
        self.jackpot_list = []
        self.jackpot_results_df = pd.DataFrame()
        self.jackpot_results_df.index.name = ''
        self.jack_pot_indices = []
        # Combination
        self.combination_df = pd.DataFrame()
        # Permutation
        self.permutation_df = pd.DataFrame()

        # Method to compute how many times a given face is rolled in each event

    def face_count(self):
        '''
        PURPOSE:
        Method to compute how many times a given face is rolled in each event

        INPUTS:
        Takes no argument

        OUTPUTS:
        Returns the Face Count dataframe according to the initial dice face type (DataFrame(<int> | <str> | <float>))
        '''
        index = [i for i in range(1, self.game.number_of_rolls + 1)]
        self.face_count_df = pd.DataFrame(index=index, columns=self.game.cols)
        self.face_count_df.index.name = 'roll number'
        # Iterate through the resulting list array and extract each parallel value to match and increment properly
        for parallel_index in range(self.game.number_of_rolls):
            start = 0
            self.face_list = np.zeros(len(self.game.cols),
                                      dtype=int)  # Hold the face value and increment when new similar value is found uses Game Cols Structure Copy
            while start < len(self.game_result):
                self.face_list[
                    self.game.cols.index(str(self.game_result[start].iloc[parallel_index][self.game.cols[0]]))] = \
                    self.face_list[
                        self.game.cols.index(str(self.game_result[start].iloc[parallel_index][self.game.cols[0]]))] + 1
                start += 1
            # Append the new face counts to the dataframe
            self.face_count_df.loc[parallel_index + 1] = self.face_list

        return self.face_count_df

    # Method to compute how many times the game resulted in all faces being identical
    def jackpot(self):
        '''
        PURPOSE:
        Method to compute how many times the game resulted in all faces being identical

        INPUTS:
        Takes no argument

        OUTPUTS:
        Returns the count of how many times the game resulted in all faces being identical
        You can also access the List of Jackpot Dataframe indices using <Class Analyzer>.jack_pot_indices
        '''
        self.jackpot_results_df = pd.DataFrame(columns=self.game.cols)
        self.jackpot_results_df.index.name = 'roll number'
        self.jack_pot_indices = []
        # Iterate through the resulting list array and extract each parallel value to match and increment properly
        for parallel_index in range(self.game.number_of_rolls):
            start = 0
            # Hold the face value and increment when new similar value is found uses Game Cols Structure Copy
            self.jackpot_list = np.zeros(len(self.game.cols), dtype=int)
            while start < len(self.game_result):
                self.jackpot_list[
                    self.game.cols.index(str(self.game_result[start].iloc[parallel_index][self.game.cols[0]]))] = \
                    self.jackpot_list[
                        self.game.cols.index(str(self.game_result[start].iloc[parallel_index][self.game.cols[0]]))] + 1
                start += 1
                # Save the index only if all values result in similar faces
                if len(self.game.dice) in self.jackpot_list:
                    # Append the Index for the dataframe
                    self.jack_pot_indices.append(parallel_index + 1)
                    # Append the new face counts to the jackpot_results dataframe
                    self.jackpot_results_df.loc[parallel_index + 1] = self.jackpot_list

        return len(self.jack_pot_indices)

        # Combo method to compute the distinct/unique combinations of faces rolled, along with their counts

    # Count is always 1 because the specific combination only occurs Once
    def combo(self):
        '''
        PURPOSE:
        Method to compute the distinct/unique combinations of faces rolled, along with their counts

        INPUTS:
        Takes no argument

        OUTPUTS:
        Returns the count of how many times the Game could result in distinct/unique combinations of faces when dice is played/rolled
        You can also access the combination multi-columned Dataframe using <Class Analyzer>.combination_df
        '''
        # Loop through the results array and add to the face_combination_list only if not present
        face_combination_list = []

        # Check if the face has been rolled during the Game , checking presence
        for roll in self.game_result:
            for i in self.game.cols:
                # Check the type of Dataframe type to conditionally pass casting
                if self.game_df_data_type == int:
                    check_face_presence = (roll.loc[roll[self.game.cols[0]] == int(i)])
                elif self.game_df_data_type == str:
                    check_face_presence = (roll.loc[roll[self.game.cols[0]] == i])
                else:
                    check_face_presence = (roll.loc[roll[self.game.cols[0]] == float(i)])
                # Append to the present list if this face has been rolled during the Game
                if not check_face_presence.empty: face_combination_list.append(i)

        # Extract only the Unique values
        face_combination_list = list(set(face_combination_list))

        # Sort the values
        face_combination_list.sort(key=self.game_df_data_type)

        # Perform the Combination of unique values and store it in self.combination_df for public access
        combination_list = []
        # If the List type of str the different combinations reseambles the permutation
        if self.game_df_data_type == str:
            # using list comprehension to formulate all distinct combinations of the elements
            combo_list = [list(face_combination_list) for _ in range(len(self.game.dice))]
            # using product() to get Combinations
            combination_list = list(product(*combo_list))
        else:
            combination_list = list(combinations(face_combination_list, len(self.game.dice)))

        # Construct the combination tuples indices
        combination_indices_list = [tuple([i] * len(combination_list)) for i in range(len(combination_list))]

        # Construct the Index name
        combination_indices_name_list = ["roll_number " + str(index + 1) for index in range(len(combination_list))]

        # Create Row Level MultiIndex
        combination_index = pd.MultiIndex.from_tuples(combination_indices_list, names=combination_indices_name_list)

        # Create Column Level MultiIndex
        cols = pd.MultiIndex.from_tuples(combination_list)

        # Create Data for the MultiIndex table
        data = [[1 for i in range(len(combination_list))] for i in range(len(combination_list))]

        # Construct the Combination Dataframe
        self.combination_df = pd.DataFrame(data, columns=cols, index=combination_index)
        return len(combination_list)

    # Permutation order matters , so we will have to look through all the possible values
    def permutation(self):
        '''
        PURPOSE:
        Method to compute how may sequence types were rolled and their counts

        INPUTS:
        Takes no argument

        OUTPUTS:
        Returns the count of all the possible combinations of faces present when dice is played/rolled
        You can also access the permutation multi-columned Dataframe using <Class Analyzer>.permutation_df
        '''
        # Loop through the results array and add to the face_permutation_list only if not present
        face_permutation_list = []

        # Check if the face has been rolled during the Game , checking presence
        for roll in self.game_result:
            for i in self.game.cols:
                # Check the type of Dataframe type to conditionally pass casting
                if self.game_df_data_type == int:
                    check_face_presence = (roll.loc[roll[self.game.cols[0]] == int(i)])
                elif self.game_df_data_type == str:
                    check_face_presence = (roll.loc[roll[self.game.cols[0]] == i])
                else:
                    check_face_presence = (roll.loc[roll[self.game.cols[0]] == float(i)])
                # Append to the present list if this face has been rolled during the Game
                if not check_face_presence.empty: face_permutation_list.append(i)

        # Extract only the Unique values
        face_permutation_list = list(set(face_permutation_list))

        # Sort the values
        face_permutation_list.sort(key=self.game_df_data_type)

        # Perform the permutation  of unique values and store it in self.permutation_df for public access
        # initializing the range with the Number of Dice rolled
        # using list comprehension to formulate all distinct permutation s of the elements
        perm_list = [list(face_permutation_list) for _ in range(len(self.game.dice))]

        # using product() to get permutation s
        permutation_list = list(product(*perm_list))

        # Construct the permutation  tuples indices
        permutation_indices_list = [tuple([i] * len(permutation_list)) for i in range(len(permutation_list))]

        # Construct the Index name
        permutation_indices_name_list = ["roll_number " + str(index + 1) for index in range(len(permutation_list))]

        # Create Row Level MultiIndex
        permutation_index = pd.MultiIndex.from_tuples(permutation_indices_list, names=permutation_indices_name_list)

        # Create Column Level MultiIndex
        cols = pd.MultiIndex.from_tuples(permutation_list)

        # Create Data for the MultiIndex table
        data = [[1 for i in range(len(permutation_list))] for i in range(len(permutation_list))]

        # Construct the permutation  Dataframe
        self.permutation_df = pd.DataFrame(data, columns=cols, index=permutation_index)
        return len(permutation_list)
