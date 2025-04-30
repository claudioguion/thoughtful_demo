# thoughtful_demo

This demo was built for the take home assignment for ThoughtfulAI Python Developer role.

This is a package classifier built using only standard libraries from Python 3.10+ so it doesn't
require any extra instalation.

The sort function definition is the same as in the problem description, so that the arguments are:
 - width:float
 - height:float
 - length:float
 - mass: float

The output of the function will be a string, classifying the package into one of these categories:
 - STANDARD
 - SPECIAL
 - REJECTED

At the top of the file, the configurations are declared as global constants (for maintainability).

I also included a TEST config (currently set to True), because I wanted to showcase the functionality
of the feature using the doctest module. The config can be set to FALSE in order turn off the testmods
for manual testing.
