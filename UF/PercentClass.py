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