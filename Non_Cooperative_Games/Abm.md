# [Gamepy: some python code for game theory...](../index.html)

## Abm.py

Abm.py contains some code to run agent based simulations of normal form games. This allows for nice visualisations of emergent behaviour in game theoretical contexts. The pseudo code for the main procedure in this file is given below:

~~~~{.pseudo}
Create row agents corresponding to row strategies
Create col agents corresponding to col strategies

for every generation:
    for every round of tournament:
        randomly dual row agents against col agents

    remove week agents
    reproduce strong agents (allowing for mutation)
~~~~

A great explanation of these sort of things is available in [this book](http://goo.gl/jDvY7) by Herbert Gintis.

## Usage
