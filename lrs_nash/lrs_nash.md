# [Gamepy: some python code for game theory...](../index.html)

## lrs_nash.py

lrs_nash.py contains some code that is a basic wrapper for the `nash.c` and `setupnash.c` files that come with the **excellent** [lrs](http://cgm.cs.mcgill.ca/~avis/C/lrs.html) package which allows for the computation of Nash equilibria in 2 player normal form games. To use this program you need lrs on your machine, the download instructions are pretty good on the [lrs website](http://cgm.cs.mcgill.ca/~avis/C/lrs.html) but I'll include some further instructions at the end of this page.

Here's a little video discussing mixed strategies in 2 player normal form games (in this I video actually use [sagemath](http://sagemath.org/) to solve some simple algebraic equations to obtain the equilibria):

<iframe width="560" height="315" src="http://www.youtube.com/embed/poYucyX7-gE" frameborder="0" allowfullscreen></iframe>

## Usage

Create a normal form game instance by passing two lists representing the bi matrices:


~~~~{.python}
Normal_Form_Game(row_matrix=LIST, col_matrix=LIST)
~~~~

Here's an example:

~~~~{.python}
import lrs_nash
row_matrix = [[3, 3], [2, 5], [0, 6]]
col_matrix = [[3, 2], [2, 6], [3, 1]]
g = lrs_nash.Normal_Form_Game(row_matrix, col_matrix)
~~~~

To solve the game we use the `solve` method:

~~~~{.python}
g.solve()
~~~~

The attribute `equilibria` now contains all the equilibria objects which have the following attributes:

- `row_strategy_distribution`
- `col_strtegy_distribution`
- `row_utility`
- `col_utility`

So one way of view all the equilibria would be the following:

~~~~{.python}
for e in g.equilibria:
    print e
    print "\tRow player plays:", e.row_strategy_distribution, "with utility:", e.row_utility
    print "\tCol player plays:", e.col_strategy_distribution, "with utility:", e.col_utility
~~~~

The output of which would be:

~~~~{.python}
<__main__.Normal_Form_Equilibria instance at 0x1004c7830>
    Row player plays: [0.8, 0.2, 0] with utility: 3
    Col player plays: [0.6666666666666666, 0.3333333333333333] with utility: 2.8
<__main__.Normal_Form_Equilibria instance at 0x1004c7878>
    Row player plays: [0, 0.3333333333333333, 0.6666666666666666] with utility: 4
    Col player plays: [0.3333333333333333, 0.6666666666666666] with utility: 2.66666666667
<__main__.Normal_Form_Equilibria instance at 0x1004c78c0>
    Row player plays: [1, 0, 0] with utility: 3
    Col player plays: [1, 0] with utility: 3
~~~~

## Comments and issues

This program communicates with the lrs library through the writing of physical files. The names of those files are randomly chosen and they are deleted when the game is solved. An immediate improvement of the code would be bypass the writing of physical files. As soon as I learn a bit more about c and the subprocess python module I'll fix that.

### Installing lrs

Downloading and installing the lrs library is very straightforward (steps 1-5 are in fact the same as those shown [here](http://cgm.cs.mcgill.ca/~avis/C/lrslib/USERGUIDE.html#Installation%20Section)):

1. Go to the [lrs download page](http://cgm.cs.mcgill.ca/~avis/C/lrslib/)
2. Download the `tar.gz` file.
3. Navigate to the file and unpack it (we'll assume it's `lrslib-034.tar.gz` but the numbers might vary):

~~~~{.bash}
gunzip lrslib-043.tar.gz
tar xvf lrslib-043.tar
~~~~

4. Go to the newly created directory:

~~~~{.bash}
cd lrslib-043
~~~~

5. Make all the binaries:

~~~~{.bash}
make all
~~~~

6. Copy all those files to a directory that is in your PATH (so that python can talk to it). I choose to put them in `/usr/local/bin`.

~~~~{.bash}
cp * /usr/local/bin
~~~~

**It does not matter where you put the lrs library files but for lrs_nash.py to work you need `nash` and `setupnash` to be in a directory that is in your PATH.**

## Github repo

The github repo for lrs_nash.py can be found [here](https://github.com/drvinceknight/Gamepy/tree/master/lrs_nash).

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
