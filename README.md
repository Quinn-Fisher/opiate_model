# opiate_model

https://github.com/Quinn-Fisher/opiate_model


Compartment model for prescription opiate addiction for our mathematical modelling class (APM348) at UofT.

Most of the files in this repo are us just messing around/testing how the model behaves and creating plots. The most important files for the model are opiate_functions.py and timed_finctions.py which defines the system of differential equations as well as a couple of cost functions and the lockdown implementation and tracking functions. It also has some example parameters and initial conditions written out referenced from a paper.


### opiate_functions.py

This section sets up the model and some default parameters and initial values. It defines the compartments/differential equations 

### timed_functions.py

This section defines addiction outbreak functions and prescription lockdown functions. Ultimately, we are testing the effectiveness of tartgetted prescription lockdowns on brief but rapid rises in addiction rates (for example, during COVID). We also define a function that loops over a range of time of intervention as well as magnitude of intervention that outputs an array of cost. This function is evaluated and plotted in timed_prescription_results.py


