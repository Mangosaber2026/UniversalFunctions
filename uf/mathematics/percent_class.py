# This is the anchor of this module: [[percent_class_anchor|percent_class.py]]

import numbers as num

from .. import validators as vls


# Percent class anchor: [[Percent-anchor|Percent]]
#* Calculates a given percentage of a given value
class Percent:

    #* Initializes the class instance with the desired percentage
    def __init__(self, percentage):
        
        vls.real_validate()(percentage, name="percentage")
        self.percentage = percentage/100

    #* Calculates the percentage of the given value with already provided percentage
    def __call__(self, value):

        vls.real_validate()(value, name="value")

        return value * self.percentage

# Pct10 function anchor: [[pct10-anchor|pct10]]
#* Calculates 10% of a given value
def pct10(value):
    
    vls.real_validate()(value, name="value")
    return Percent(10)(value)

# Pct20 function anchor: [[pct20-anchor|pct20]]
#* Calculates 20% of a given value
def pct20(value):
    
    vls.real_validate()(value, name="value")
    return Percent(20)(value)

# Pct25 function anchor: [[pct25-anchor|pct25]]
#* Calculates 25% of a given value
def pct25(value):
    
    vls.real_validate()(value, name="value")
    return Percent(25)(value)

# Pct30 function anchor: [[pct30-anchor|pct30]]
#* Calculates 30% of a given value
def pct30(value):
    
    vls.real_validate()(value, name="value")
    return Percent(30)(value)

# Pct40 function anchor: [[pct40-anchor|pct40]]
#* Calculates 40% of a given value
def pct40(value):
    
    vls.real_validate()(value, name="value")
    return Percent(40)(value)

# Pct50 function anchor: [[pct50-anchor|pct50]]
#* Calculates 50% of a given value
def pct50(value):
    
    vls.real_validate()(value, name="value")
    return Percent(50)(value)

# Pct60 function anchor: [[pct60-anchor|pct60]]
#* Calculates 60% of a given value
def pct60(value):

    vls.real_validate()(value, name="value")
    return Percent(60)(value)

# Pct70 function anchor: [[pct70-anchor|pct70]]
#* Calculates 70% of a given value
def pct70(value):
    
    vls.real_validate()(value, name="value")
    return Percent(70)(value)

# Pct75 function anchor: [[pct75-anchor|pct75]]
#* Calculates 75% of a given value
def pct75(value):
    
    vls.real_validate()(value, name="value")
    return Percent(75)(value)

# Pct80 function anchor: [[pct80-anchor|pct80]]
#* Calculates 80% of a given value
def pct80(value):
    
    vls.real_validate()(value, name="value")
    return Percent(80)(value)

# Pct90 function anchor: [[pct90-anchor|pct90]]
#* Calculates 90% of a given value
def pct90(value):
    
    vls.real_validate()(value, name="value")
    return Percent(90)(value)