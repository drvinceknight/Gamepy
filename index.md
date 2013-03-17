# [Gamepy: some python code for game theory...](./index.html)

This contains some code for a growing number of game theoretical subjects (clicking on each of the packages goes to some short documentation as well as a link to the code):

- Cooperative Game Theory:
    - [Shap.py](./Cooperative_Games/Shappy.html) (a library to calculate the shapley value for a cooperative game)
- Non Cooperative Game Theory:
    - Abm.py (a library to simulate a population of strategies in an evolutionary context)
    - lrs_nash.py (a library that solves a normal form game using the lrs library)
- Matching Games:
    - [Gale_Shapley.py](./Matching_Games/Gale_Shapley.html) (a library to solve matching games using the extended gale shapley algorithm)

The code is all available on github and I'm sure can be improved a lot (for example the current communication with lrs is very clumsy). I'll be continuing to work on this here and there when I have time.


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
