# [Gamepy: some python code for game theory...](../index.html)

## Gale_Shapley.py

Gale_Shapley contains some code to calculate a stable matching for the stable matching problem. Here's a great video describing the stable matching problem and the Gale Shapley algorithm:

<iframe width="560" height="315" src="http://www.youtube.com/embed/w1leqkpDaRw" frameborder="0" allowfullscreen></iframe>

The implementation in Gale_Shapley.py is actually the *extended Gale Shapley algorithm* a description of which can be found in introductory sections of [this paper](http://www.sciencedirect.com/science/article/pii/0166218X9200179P) by Steven Irving.

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

I have almost implemented the SUPER and STRONG algorithms of Irving's paper which return super and strong matchings (if they exist) for matching games where indifference is allowed.
