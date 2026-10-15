from numbers import Real
from . import Validators as vls


class Percent:
    """
    This class calculates a chosen percentage of a given value.
    """
    def __init__(self, percentage: Real) -> None:
        """
        Initializes the percentage value.
        :param percentage: percentage value to calculate
        :return: None
        """
        vls.real_validate()(percentage, name="percentage")
        self.percentage = percentage/100

    def __call__(self, value: Real) -> Real:
        """
        Calculates the percentage value.
        :param value: given value
        :return: calculated percentage value
        """
        vls.real_validate()(value, name="value")

        return value * self.percentage

def pct10(value: Real) -> Real:
    """
    Calculates 10% percent of the given value
    :param value: real number
    :return: 10% of the given value
    """
    vls.real_validate()(value, name="value")
    return Percent(10)(value)

def pct20(value: Real) -> Real:
    """
    Calculates 20% percent of the given value
    :param value: real number
    :return: 20% of the given value
    """
    vls.real_validate()(value, name="value")
    return Percent(20)(value)

def pct30(value: Real) -> Real:
    """
    Calculates 30% percent of the given value
    :param value: real number
    :return: 30% of the given value
    """
    vls.real_validate()(value, name="value")
    return Percent(30)(value)

def pct40(value: Real) -> Real:
    """
    Calculates 40% percent of the given value
    :param value: real number
    :return: 40% of the given value
    """
    vls.real_validate()(value, name="value")
    return Percent(40)(value)

def pct50(value: Real) -> Real:
    """
    Calculates 50% percent of the given value
    :param value: real number
    :return: 50% of the given value
    """
    vls.real_validate()(value, name="value")
    return Percent(50)(value)

def pct60(value: Real) -> Real:
    """
    Calculates 60% percent of the given value
    :param value: real number
    :return: 60% of the given value
    """
    vls.real_validate()(value, name="value")
    return Percent(60)(value)

def pct70(value: Real) -> Real:
    """
    Calculates 70% percent of the given value
    :param value: real number
    :return: 70% of the given value
    """
    vls.real_validate()(value, name="value")
    return Percent(70)(value)

def pct80(value: Real) -> Real:
    """
    Calculates 80% percent of the given value
    :param value: real number
    :return: 80% of the given value
    """
    vls.real_validate()(value, name="value")
    return Percent(80)(value)

def pct90(value: Real) -> Real:
    """
    Calculates 90% percent of the given value
    :param value: real number
    :return: 90% of the given value
    """
    vls.real_validate()(value, name="value")
    return Percent(90)(value)