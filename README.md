# Monte Carlo Simulator

***Monte Carlo Simulator for different board games such as Coin flips ,
Dice rolls , Roman Alphabet ,Card shuffle and many more.***

# Metadata

### Author: Brook Tarekegn Assefa

### Net UD: rnc3mm

### Project name: Monte Carlo Simulator

# Synopsis

### Installation

```commandline
pip install mcgs
```

### Importing

```python
from montecarlo import Die, Game, Analyzer 
```

### Creating fair dice objects  all of six sides with the faces 1 through 6

```python
from montecarlo import Die

fair_die_faces = [1, 2, 3, 4, 5, 6]
fair_die = Die(fair_die_faces)
```

### Create fair coin object with faces H and T

```python
from montecarlo import Die

coin_faces = ['H', 'T']
fair_coin = Die(coin_faces)
```

### Playing Games with two six sided dice

```python
from montecarlo import Die, Game

fair_die_faces = [1, 2, 3, 4, 5, 6]
fair_die = Die(fair_die_faces)

# Let us Play a game of 10 rolls with 2 fair dice 
dice = []
dice.extend([fair_die, fair_die])  # Playing a Two Fair dice 
dice_game = Game(dice)
dice_game.show(dice_game.play(10), 1)  # Displaying results in Wide Dataframe format (see API List Table)
```

### Playing Games with two coins

```python
from montecarlo import Die, Game

coin_faces = ['H', 'T']
fair_coin = Die(coin_faces)

# Let us Play a game of 10 rolls with 2 fair coins 
coins = []
coins.extend([fair_coin, fair_coin])
coin_game = Game(coins)
coin_game.show(coin_game.play(10), 1) 
```

### Analyzing games with two six sided dice

```python
from montecarlo import Die, Game, Analyzer

fair_die_faces = [1, 2, 3, 4, 5, 6]
fair_die = Die(fair_die_faces)

# Let us Play a game of 10 rolls with 2 fair dice 
# This is similar for Coins as well
dice = []
dice.extend([fair_die, fair_die])
dice_game = Game(dice)
dice_game.show(dice_game.play(10), 1)

# Let us now analyze the game
dice_analyzer = Analyzer(dice_game)

# Get the face count on each roll event 
dice_analyzer.face_count()

# Get how many times the game resulted in all faces being identical (jackpot)
dice_analyzer.jackpot()

# Compute the distinct/unique combinations of faces rolled along with their counts
dice_analyzer.combo()

# Compute how may sequence types were rolled and their counts
dice_analyzer.permutation()
```

# API description

### Class Table

| Class Name |                                                                                                                             Method Name                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Attributes |
|:-----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Die        |                       <table>  <thead>  <tr>  <th> Methods</th>  </tr>  </thead>  <tbody>  <tr>  <td>__init__</td>  </tr> <tr>  <td>change_weight</td> </tr> <tr><td>roll_die</td> </tr> <tr> <td>show_state</td> </tr>   </tbody>  </table>                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <table>  <thead>  <tr>  <th> Attributes </th>   <th> Description</th> </tr>  </thead>  <tbody>  <tr>  <td>faces</td>  <td>Sides of the dice</td>  </tr>    <tr>  <td>weights</td>  <td>Value of assigned to a face</td>  </tr> <tr>  <td>faces_weights_df</td>  <td>Dataframe of faces and weights</td>  </tr>  </tbody>  </table> |
| Game       |                                              <table>  <thead>  <tr>  <th> Methods</th>  </tr>  </thead>  <tbody>  <tr>  <td>__init__</td>  </tr> <tr>  <td>play</td> </tr> <tr><td>show</td> </tr>  </tbody>  </table>                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      <table>  <thead>  <tr>  <th> Attributes </th>   <th> Description</th> </tr>  </thead>  <tbody>  <tr>  <td>dice</td>  <td>Die Object List passed from Die class</td>  </tr>    <tr>  <td>cols/columns</td>  <td>Headers of the play result dataframe</td>  </tr> <tr>  <td>play_df</td>  <td>Play result dataframe shape N rolls by M dice </td>  </tr>  <tr> <td> number_of_rolls</td>  <td> The number of times games/rolls played </td> </tr> <tr> <td>play_result_df_list</td>  <td> List form of the play result </td> </tr>  </tbody>  </table> | 
| Analyzer   | <table>  <thead>  <tr>  <th> Methods</th>  </tr>  </thead>  <tbody>  <tr>  <td>__init__</td>  </tr> <tr>  <td>face_count</td> </tr> <tr><td>show</td> </tr> <tr><td>jackpot</td> </tr> <tr><td>combo</td> </tr> <tr> <td> permutation</td></tr>  </tbody>  </table> | <table>  <thead>  <tr>  <th> Attributes </th>   <th> Description</th> </tr>  </thead>  <tbody>  <tr>  <td>game</td>  <td>Game Object passed from Game Class</td>  </tr>    <tr>  <td>game_df_data_type</td>  <td>Holds the primitive type of the Dataframe</td>  </tr> <tr>  <td>game_result / game_result_df </td>  <td> Game result Dataframe shape N rolls by M dice played </td>  </tr>  <tr> <td> face_count_df</td>  <td> Face Count result Dataframe shape N rolls by M die faces </td> </tr> <tr> <td>face_list</td>  <td> List form of the face count result </td> </tr> <tr> <td> jackpot_results_df </td> <td> Jackpot result Dataframe shape N of Jackpots rolls by M die faces</td> </tr> <tr> <td> jackpot_list</td> <td> List form of the jackpot result</td> </tr><tr> <td> jack_pot_indices </td> <td> Index values of where the Jackpot occurred in result Dataframe</td> </tr><tr> <td> combination_df</td> <td> Combination result as multi-columned Dataframe shape X of N rolls by Y die faces with Z number of occurrence.</td> </tr><tr> <td>combination_list </td> <td> Tuple zipped List form of the Combination result</td> </tr><tr> <td> permutation_df</td> <td>Permutation result as multi-columned Dataframe shape X of N rolls by Y die faces with Z number of occurrence. </td> </tr><tr> <td>permutation_list</td> <td>	Tuple zipped List form of the Permutation result</td> </tr> </tbody>  </table> |

### Method Table

| Method Name   |                                                      Description Docs |                                                                                                                                                                                                                                                                                                      Parameters |                                                                                                                                                                                                        Return values |                                                                                                                 Snapshots |
|:--------------|----------------------------------------------------------------------:|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|--------------------------------------------------------------------------------------------------------------------------:|
| change_weight |                               Change the weight of a single side/face | <table>  <thead>  <tr>  <th> Data types</th>  <th>Defaults</th>  </tr>  </thead>  <tbody>  <tr>  <td>Face Value **integer,string,float** </td> <td> **integer(1) <br/>string("") <br/>float (1.0)** </td></tr> <tr> <td>New Weight **integer,string,float** </td> <td> **1.0**</td> </tr>    </tbody>  </table> |                                                                                                                             Assigns a dataframe (integer,string or float ) with faces and the newly assigned weights | ![Changed Weights](https://user-images.githubusercontent.com/45931201/199298366-0ac1bdb0-d1a4-4f9c-8c02-ff20921b4f13.png) |
| roll_die      |                                        Roll the die one or more times |                                                                                                                               <table>  <thead>  <tr>  <th> Data types</th>  <th>Defaults</th>  </tr>  </thead>  <tbody>  <tr>  <td>Number of rolls **integer** </td> <td> **1** </td></tr>   </tbody>  </table> |                                                                                                                                  Return a list of outcomes similar to the face types      (integer,string or float ) |        ![Roll Die](https://user-images.githubusercontent.com/45931201/199302425-8c552f72-55ae-42d6-bc2e-b49e1b44c488.png) |
| show_state    |                       Show the die’s current set of faces and weights |                                                                                                                                                                                                                                                                                               Takes no argument |                                                                                                                                      Returns the dataframe according to the face types    (integer,string or float ) |      ![Show State](https://user-images.githubusercontent.com/45931201/199298366-0ac1bdb0-d1a4-4f9c-8c02-ff20921b4f13.png) |
| play          | Rolls the Dice using the inherited roll_die method from the Die class |                                                                                                                               <table>  <thead>  <tr>  <th> Data types</th>  <th>Defaults</th>  </tr>  </thead>  <tbody>  <tr>  <td>Number of Rolls **integer** </td> <td> **1** </td></tr>   </tbody>  </table> |                                                                                                                                           Returns the results of the play as a dataframe of shape N rolls by M dice. |       ![Play Game](https://user-images.githubusercontent.com/45931201/199354408-b1d7b93f-6eff-4928-8166-31974ca955d7.png) |
| show          |                              Show the results of the most recent play |                     <table>  <thead>  <tr>  <th> Data types</th>  <th>Defaults</th>  </tr>  </thead>  <tbody>  <tr>  <td>Play Result **DataFrame** </td> <td>  **pd.DataFrame()** </td></tr> <tr>  <td>DataFrame table Form <br/>**integer <br/> Wide (1) or Narrow(2)** </td> <td>  **1**   </tbody>  </table> |                                                                                                                               Display the result of the latest play result as a dataframe of shape N rolls by M dice |       ![Show Game](https://user-images.githubusercontent.com/45931201/200873022-d30d6f05-7bde-44d6-bb43-730786853a6a.png) |
| face_count    | Method to compute how many times a given face is rolled in each event |                                                                                                                                                                                                                                                                                               Takes no argument | Returns the count for each face displayed according to the initial dice face sides given as a dataframe of shape N rolls by M dice. ***See how the above row show dataframe is displayed by face_count dataframe.*** |      ![Face Count](https://user-images.githubusercontent.com/45931201/200873510-d66ca1b5-fe74-4f72-ae9c-df0659c99009.png) |
|
| roll_die      |                                        Roll the die one or more times |                                                                                     <table>  <thead>  <tr>  <th> Data types</th>  <th>Defaults</th>  </tr>  </thead>  <tbody>  <tr>  <td>face_value integer,string,float </td> <td> integer(1) <br/>string("") <br/>float (1.0) </td></tr>   </tbody>  </table> |                                                                                                                                                                                                                      |                                                                                                                           |
| roll_die      |                                        Roll the die one or more times |                                                                                     <table>  <thead>  <tr>  <th> Data types</th>  <th>Defaults</th>  </tr>  </thead>  <tbody>  <tr>  <td>face_value integer,string,float </td> <td> integer(1) <br/>string("") <br/>float (1.0) </td></tr>   </tbody>  </table> |                                                                                                                                                                                                                      |                                                                                                                           |
| roll_die      |                                        Roll the die one or more times |                                                                                     <table>  <thead>  <tr>  <th> Data types</th>  <th>Defaults</th>  </tr>  </thead>  <tbody>  <tr>  <td>face_value integer,string,float </td> <td> integer(1) <br/>string("") <br/>float (1.0) </td></tr>   </tbody>  </table> |                                                                                                                                                                                                                      |                                                                                                                           |
| roll_die      |                                        Roll the die one or more times |                                                                                     <table>  <thead>  <tr>  <th> Data types</th>  <th>Defaults</th>  </tr>  </thead>  <tbody>  <tr>  <td>face_value integer,string,float </td> <td> integer(1) <br/>string("") <br/>float (1.0) </td></tr>   </tbody>  </table> |                                                                                                                                                                                                                      |                                                                                                                           |
