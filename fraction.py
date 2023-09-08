# ===============================================================
# Name: Jude Vargas
# Date: 09/15/2023
# Algorithm: N/A
# References: <References used i.e., www.python.org, realpython.com, TA, Instructor, any collaborator>
# ===============================================================

class Fraction:
    def __init__(self, numerator, denominator):
        """
        Function __init__ is called when a new instance of Fraction is created.
        It handles incorrect argument values and defines attributes for later behavior.
        :param numerator: The int on the top of the fraction; what is being divided by the denominator
        :param denominator: The int on the bottom of the fraction; what is dividing the numerator
        Returns: None
        """
        # Make sure both the numerator and denominator are integers
        if not(isinstance(numerator, int) or isinstance(denominator, int)):
            raise TypeError("TypeError: Numerator and Denominator must both be of type <int>")
        if denominator == 0:
            raise ValueError("ValueError: denominator must not be zero")

        self.__numerator = numerator
        self.__denominator = denominator
        self.reduce()

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def getNumerator(self):
        return self.__numerator

    def getDenominator(self):
        return self.__denominator

    def setNumerator(self, value):
        if not isinstance(value, int):
            raise TypeError("TypeError: value must be of type <int>")

        self.__numerator = value

    def setDenominator(self, value):
        if not isinstance(value, int):
            raise TypeError("TypeError: value must be of type <int>")
        if value == 0:
            raise ValueError("ValueError: denominator must not be zero")

        self.__denominator = value

    def reduce(self):
        gcd = self.__calcGCD()
        self.__numerator //= gcd
        self.__denominator //= gcd

    def __calcGCD(self):
        a = max(self.__numerator, self.__denominator)
        b = min(self.__numerator, self.__denominator)
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a

    ###
    # Methods for Special Mathematical Operators
    ###

    def __neg__(self):
        return Fraction(-self.__numerator, self.__denominator)

    def __add__(self, other):
        numerator = self.__numerator * other.getDenominator() + other.getNumerator() * self.__denominator
        denominator = self.__denominator * other.getDenominator()
        return Fraction(numerator, denominator)


    def __sub__(self, other):
        return self.__add__(-other)

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    ###
    # Methods for Special Boolean Operators
    ###

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass


def main():
    pass


if __name__ == "__main__":
    main()