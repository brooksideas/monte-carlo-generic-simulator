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