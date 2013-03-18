# [Gamepy: some python code for game theory...](../index.html)

## Shap.py

Shap.py contains some code to calculate the shapley value for a cooperative game. Here's a video explaining the usage of the shapley value:

<iframe width="560" height="315" src="http://www.youtube.com/embed/aThG4YAFErw" frameborder="0" allowfullscreen></iframe>

(Note there is an error at 3:51)

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

## Github repo

The github repo for Shap.py can be found [here](https://github.com/drvinceknight/Gamepy/tree/master/Shappy).

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-38016329-2']);
  _gaq.push(['_setDomainName', 'github.com']);
  _gaq.push(['_setAllowLinker', true]);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
