# [Gamepy: some python code for game theory...](./index.html)

This contains some code for a growing number of game theoretical subjects (clicking on each of the packages goes to some short documentation as well as a link to the code):

- Cooperative Game Theory:
    - [Shap.py](./Shappy/Shappy.html) (a library to calculate the shapley value for a cooperative game)
- Non Cooperative Game Theory:
    - [Abm.py](./Abm/Abm.html) (a library to simulate a population of strategies in an evolutionary context)
    - [lrs_nash.py](./lrs_nash/lrs_nash.html) (a library that solves a normal form game using the awesome [lrs](http://cgm.cs.mcgill.ca/~avis/C/lrs.html) library made by David Avis)
- Matching Games:
    - [Gale_Shapley.py](./Gale_Shapley/Gale_Shapley.html) (a library to solve matching games using the extended gale shapley algorithm)

The code is all available on github and I'm sure can be improved a lot (for example the current communication with lrs is very clumsy). I'll be continuing to work on this here and there when I have time.

# License Information

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0](http://creativecommons.org/licenses/by-sa/3.0/us/) license.  You are free to:

* Share: copy, distribute, and transmit the work,
* Remix: adapt the work

Under the following conditions:

* Attribution: You must attribute the work in the manner specified by the author or licensor (but not in any way that suggests that they endorse you or your use of the work).
* Share Alike: If you alter, transform, or build upon this work, you may distribute the resulting work only under the same or similar license to this one.

When attributing this work, please include me.

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
