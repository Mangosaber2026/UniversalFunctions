"""
This module contains the HelperFunctions class which provides a collection of reusable helper functions
so that the user can easily use them without having to write the code for them again.

Some other functions:

sine -> calculates sine value

range_f -> acts like the conventional range function except for that this takes rational inputs
"""

from . import decorator_archive as dec_arc
import numbers as num
import collections.abc as cabc


@dec_arc.cls_deco_superposition(staticmethod)
class HelperFunctions:
    """
    This class provides a collection of reusable helper functions
    so that the user can easily use them without having to write the code for them again.
    """

    def intervals_f() -> num.Real:
        """
        Asks the user for rational intervals.

        :return: the number of intervals as a rational number
        """

    def length_float() -> num.Real:
        """
        Asks the user for rational lengths.

        :return: the length as a rational number
        """

    def radius_float() -> num.Real:
        """
        Asks the user for rational radius.

        :return: the radius as a rational number
        """

    def object_num() -> int:
        """
        Asks the user for the number of objects.

        :return: the number of objects as an integer
        """

    def sides_num() -> int:
        """
        Asks the user for the number of sides.

        :return: the number of sides as an integer
        """

    def row_num() -> int:
        """
        Asks the user for the number of rows.

        :return: the number of rows as an integer
        """

    def row_pair() -> int:
        """
        Asks the user for the number of pairs of rows.

        :return: the number of pairs of rows as an integer
        """

    def diameter_sq(length: num.Real) -> tuple[num.Real, num.Real]:
        """
        Calculates the diameter of a square with given length.

        :param length: the length of the square

        :return: a tuple containing the diameter and half of the diameter
        """

    def x_ft() -> num.Real:
        """
        Asks the user for the x value (on the coordinate system).

        :return: the x value as a rational number
        """

    def y_ft() -> num.Real:
        """
        Asks the user for the y value (on the coordinate system).

        :return: the y value as a rational number
        """

    def list_helperfunctions() -> dict:
        """
        Returns a dictionary of all the helper functions in this class.

        :return: a dictionary with function names as keys and function objects as values
        """

def range_f(
        start: num.Real,
        stop: num.Real,
        step: num.Real
) -> cabc.Generator[num.Real, None, None]:
    """
    Lets the user choose Real inputs for start, stop and step.

    :param start: start value; Real number

    :param stop: stop value; Real number

    :param step: step value; Real number
    
    :return: a generator that yields values from start to stop with the given step
    """