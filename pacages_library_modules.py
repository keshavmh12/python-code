#A module = a Python file
# (.py) that contains functions, classes, or variables you want to reuse


import my_module

print(my_module.add(1,2))
print(my_module.mul(1,2))

#packages means collectio of modules my_module is also a packages bcz it also contain multiple function in ti

print(my_module.shout("keshav"))

#for import specific funcction from a pakages

print(my_module.add(1,2))

#built-in-modules

import math
print(math.sqrt(5))

import random
print(random.randint(1,10))

#external package :-External packages are third-party libraries (not built-in).
#pip is satand for pip installs packages

#An external package is not built into Python.

#It is created by other developers and shared so we can install and use it.

#Example: requests, numpy, pandas, flask, django



#🟢 6. Why use Modules & Packages?

#✅ Code reuse (don’t repeat yourself)
#✅ Easy to maintain (split into small files)
#✅ Organize large projects
#✅ Share code with others