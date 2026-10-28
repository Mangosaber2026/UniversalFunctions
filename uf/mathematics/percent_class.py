# ⚓ Anchor for this module: [[percent_class_anchor|percent_class.py]] 
# 🔗 Parent package: [[#mathematics-anchor|mathematics]] 


from .. import validators as vls


# ⚓ Percent class anchor: [[Percent-anchor|class Percent]] 
 #* 📝 Calculates a given percentage of a given value
class Percent:

     #* 📝 Initializes [[#Percent-anchor|the class]] instance with the desired percentage
    def __init__(self, percentage):
        
        vls.real_validate()(value=percentage, name="percentage")
        self.percentage = percentage/100

     #* 📝 Calls [[#Percent-anchor|this class]] and calculates 
     #* the percentage of the given value with already provided percentage
    def __call__(self, value):

        vls.real_validate()(value=value, name="value")

        return value * self.percentage

# ⚓ Pct10 function anchor: [[pct10-anchor|pct10()]] 
 #* 📝 Calculates 10% of a given value
def pct10(value):
    
    vls.real_validate()(value=value, name="value")
    return Percent(percentage=10)(value=value)


# ⚓ Pct20 function anchor: [[pct20-anchor|pct20()]] 
 #* 📝 Calculates 20% of a given value
def pct20(value):
    
    vls.real_validate()(value=value, name="value")
    return Percent(percentage=20)(value=value)


# ⚓ Pct25 function anchor: [[pct25-anchor|pct25()]] 
 #* 📝 Calculates 25% of a given value
def pct25(value):
    
    vls.real_validate()(value=value, name="value")
    return Percent(percentage=25)(value=value)


# ⚓ Pct30 function anchor: [[pct30-anchor|pct30()]] 
 #* 📝 Calculates 30% of a given value
def pct30(value):
    
    vls.real_validate()(value=value, name="value")
    return Percent(percentage=30)(value=value)


# ⚓ Pct40 function anchor: [[pct40-anchor|pct40()]] 
 #* 📝 Calculates 40% of a given value
def pct40(value):
    
    vls.real_validate()(value=value, name="value")
    return Percent(percentage=40)(value=value)


# ⚓ Pct50 function anchor: [[pct50-anchor|pct50()]] 
 #* 📝 Calculates 50% of a given value
def pct50(value):
    
    vls.real_validate()(value=value, name="value")
    return Percent(percentage=50)(value=value)


# ⚓ Pct60 function anchor: [[pct60-anchor|pct60()]] 
 #* 📝 Calculates 60% of a given value
def pct60(value):

    vls.real_validate()(value=value, name="value")
    return Percent(percentage=60)(value=value)


# ⚓ Pct70 function anchor: [[pct70-anchor|pct70()]] 
 #* 📝 Calculates 70% of a given value
def pct70(value):
    
    vls.real_validate()(value=value, name="value")
    return Percent(percentage=70)(value=value)


# ⚓ Pct75 function anchor: [[pct75-anchor|pct75()]] 
 #* 📝 Calculates 75% of a given value
def pct75(value):
    
    vls.real_validate()(value=value, name="value")
    return Percent(percentage=75)(value=value)


# ⚓ Pct80 function anchor: [[pct80-anchor|pct80()]] 
 #* 📝 Calculates 80% of a given value
def pct80(value):
    
    vls.real_validate()(value=value, name="value")
    return Percent(percentage=80)(value=value)


# ⚓ Pct90 function anchor: [[pct90-anchor|pct90()]] 
 #* 📝 Calculates 90% of a given value
def pct90(value):
    
    vls.real_validate()(value=value, name="value")
    return Percent(percentage=90)(value=value)