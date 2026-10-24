# Anchor for this module: [[mathematics-init-anchor|mathematics.__init__.py]]

#* Imports all available functions and class from [[#percent_class_anchor|percent_class.py]]
from .percent_class import (
    Percent,  
    # Link to source code: [[#Percent-anchor|Percent]]

    pct10,
    # Link to source code: [[#pct10-anchor|pct10]]

    pct20,
    # Link to source code: [[#pct20-anchor|pct20]]

    pct25,
    # Link to source code: [[#pct25-anchor|pct25]]

    pct30,
    # Link to source code: [[#pct30-anchor|pct30]]

    pct40,
    # Link to source code: [[#pct40-anchor|pct40]]

    pct50,
    # Link to source code: [[#pct50-anchor|pct50]]

    pct60,
    # Link to source code: [[#pct60-anchor|pct60]]

    pct70,
    # Link to source code: [[#pct70-anchor|pct70]]

    pct75,
    # Link to source code: [[#pct75-anchor|pct75]]

    pct80,
    # Link to source code: [[#pct80-anchor|pct80]]

    pct90,
    # Link to source code: [[#pct90-anchor|pct90]]
)

#* Imports all functions from [[#trigonometry-anchor|trigonometry.py]]
from .trigonometry import (
    asine, 
    # Link to source code: [[#asine-anchor|asine]]

    cosine,
    # Link to source code: [[#cosine-anchor|cosine]]

    sine,          
    # Link to source code: [[#sine-anchor|sine]]
)


#* Specifies all functions and class available through wildcard import
__all__ = [
   "Percent",
   "pct10",
   "pct20",
   "pct25",
   "pct30",
   "pct40",
   "pct50",
   "pct60",
   "pct70",
   "pct75",
   "pct80",
   "pct90",

   "asine",
   "cosine",
   "sine",
]