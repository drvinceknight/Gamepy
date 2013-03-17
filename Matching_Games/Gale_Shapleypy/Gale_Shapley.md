# [Gamepy: some python code for game theory...](../index.html)

## Gale_Shapley.py

Gale_Shapley contains some code to calculate a stable matching for the stable matching problem. Here's a great video describing the stable matching problem and the Gale Shapley algorithm:

<iframe width="560" height="315" src="http://www.youtube.com/embed/w1leqkpDaRw" frameborder="0" allowfullscreen></iframe>

The implementation in Gale_Shapley.py is actually the *extended Gale Shapley algorithm* a description of which can be found in introductory sections of [this paper](http://www.sciencedirect.com/science/article/pii/0166218X9200179P) by Steven Irving.

## Usage


### As a library

Create a matching game instance by passing two dictionaries representing the preferences of the suitors and reviewers:

~~~~{.python}
Matching_Game(suitor_preferences=DICTIONARY, reviewer_preferences=DICTIONARY)
~~~~

Here's an example (using the same preferences as for the video above):

~~~~{.python}
import Gale_Shapley
suitr_pref = {'J': ['A', 'D', 'C', 'B'], 'K': ['A', 'B', 'C', 'D'], 'L': ['B', 'D', 'C', 'A'], 'M': ['C', 'A', 'B', 'D']}
reviewr_pref = {'A': ['L', 'J', 'K', 'M'], 'B': ['J', 'M', 'L', 'K'], 'C': ['K', 'M', 'L', 'J'], 'D': ['M', 'K', 'J', 'L']}
g = Gale_Shapley.Matching_Game(suitr_pref, reviewr_pref)
~~~~

We run the extended Gale Shapley algorithm using the `solve` method:

~~~~{.python}
g.solve()
~~~~

To view the obtained stable matching we view the `stable_matching` attribute:

~~~~{.python}
g.stable_matching
~~~~

Which returns:

~~~~{.python}
{'K': 'C', 'J': 'A', 'M': 'B', 'L': 'D'}
~~~~

We can also view the matching that would be obtained if the suitors and reviewers swapped roles:

~~~~{.python}
g.invert_solve()
g.inverted_stable_matching
~~~~

Which returns:

~~~~{.python}
{'A': 'L', 'C': 'K', 'B': 'J', 'D': 'M'}
~~~~

### As a script

The library is coded so that it can be directly run on a csv file containing the preferences of suitors and reviewers (this allows you to run it on larger instances of matching games although you might prefer to write your own script to do this using Gale_Shapley as a library).

As an example consider the file schedule.csv:

~~~~{.csv}
A,Mon,Wed,Tue,Thu,Fri,Sat,Sun
C,Mon,Fri,Wed,Tue,Thu,Sat,Sun
B,Tue,Wed,Fri,Thu,Mon,Sat,Sun
D,Tue,Wed,Thu,Fri,Mon,Sat,Sun
E,Mon,Tue,Thu,Fri,Wed,Sat,Sun
F,Fri,Thu,Wed,Mon,Tue,Sat,Sun
G,Thu,Mon,Tue,Wed,Fri,Sat,Sun

Mon,G,D,B,A,C,E,F
Tue,G,B,A,C,E,F,D
Wed,G,A,C,E,F,D,B
Thu,A,C,E,F,D,G,B
Fri,E,C,F,D,G,B,A
Sat,E,F,G,D,B,A,C
Sun,A,D,G,B,F,C,E
~~~~

We can run the extended Gale Shapley algorithm on this file using:

~~~~{.bash}
python Gale_Shapley.py schedule.csv
~~~~

Which returns:

~~~~{.bash}
Stable matching:
    {'A': 'Wed', 'C': 'Fri', 'B': 'Tue', 'E': 'Thu', 'D': 'Sun', 'G': 'Mon', 'F': 'Sat'}
Inverted stable matching:
    {'Wed': 'A', 'Sun': 'D', 'Fri': 'E', 'Tue': 'B', 'Mon': 'G', 'Thu': 'C', 'Sat': 'F'}
~~~~

(Note that if no csv file is passed but the python file is run from the command line the basic example shown above will be run.)

## Comments and issues

I have almost implemented the SUPER and STRONG algorithms of [Irving's paper](http://www.sciencedirect.com/science/article/pii/0166218X9200179P) which return super and strong matchings (if they exist) for matching games where indifference is allowed.
