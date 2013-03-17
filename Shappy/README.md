# Gamepy: some python code for game theory...

## Shap.py

Shap.py contains some code to calculate the shapley value for a cooperative game.

## Usage

Create a cooperative game instance by passing a dictionary stating the coalition values:

~~~~{.python}
Coop_Game(player_list=LIST, characteristic_function=DICTIONARY)
~~~~

Here's an example:

~~~~{.python}
import Shap
player_list = ['A', 'B', 'C']
coalition_dictionary = {'A' : 3, 'B' : 4, 'C' : 3, 'A,B' : 4, 'B,C' : 4, 'A,C': 6, 'A,B,C' : 10}
g = Shap.Coop_Game(player_list, coalition_dictionary)
~~~~

We obtain the Shapley value using the `shapley` method:

~~~~{.python}
g.shapley()
~~~~

which returns:

~~~~{.python}
{'A': 3.5, 'C': 3.5, 'B': 3.0}
~~~~

## Comments and issues

Currently there is a check function that makes sure the characteristic function is valid (i.e. that the player list concurs).
