import numbers as num

from .. import validators as vls


class Percent:
    
    def __init__(self, percentage):
        
        vls.real_validate()(percentage, name="percentage")
        self.percentage = percentage/100

    def __call__(self, value):

        vls.real_validate()(value, name="value")

        return value * self.percentage

def pct10(value):
    
    vls.real_validate()(value, name="value")
    return Percent(10)(value)

def pct20(value):
    
    vls.real_validate()(value, name="value")
    return Percent(20)(value)

def pct25(value):
    
    vls.real_validate()(value, name="value")
    return Percent(25)(value)

def pct30(value):
    
    vls.real_validate()(value, name="value")
    return Percent(30)(value)

def pct40(value):
    
    vls.real_validate()(value, name="value")
    return Percent(40)(value)

def pct50(value):
    
    vls.real_validate()(value, name="value")
    return Percent(50)(value)

def pct60(value):

    vls.real_validate()(value, name="value")
    return Percent(60)(value)

def pct70(value):
    
    vls.real_validate()(value, name="value")
    return Percent(70)(value)

def pct75(value):
    
    vls.real_validate()(value, name="value")
    return Percent(75)(value)

def pct80(value):
    
    vls.real_validate()(value, name="value")
    return Percent(80)(value)

def pct90(value):
    
    vls.real_validate()(value, name="value")
    return Percent(90)(value)