class FootMeasure:
    def __init__(self, feet = 0, inches = 0):
        if not (isinstance(feet, int) or isinstance(inches, int)):
            raise TypeError("MSG GOES HERE")
        if feet < 0 or inches < 0:
            raise ValueError("MSG GOES HERE")
        self.__feet = feet
        self.__inches = inches
        self.__adjust()

    def __str__(self):
        if self.__inches == 0 and self.__feet != 0:
            return f"{self.__feet}ft."
        return f"{self.__feet}ft. {self.__inches}ins."

    def get_feet(self):
        """
        Function get_feet acts as a public method to retrieve an instance's feet
        Parameters: None
        Returns: The instance's feet (as an int)
        """
        return self.__feet

    def get_inches(self):
        """
        Function get_inches acts as a public method to retrieve an instance's inches
        Parameters: None
        Returns: The instance's inches (as an int)
        """
        return self.__inches

    def set_feet(self, value):
        """
        Function set_feet acts as a public method to change the value of this instance's feet
        Parameters:
            value: the value that the instance's feet will be set to
        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("MSG GOES HERE")
        if value < 0:
            raise ValueError("MSG GOES HERE")
        self.__feet = value

    def set_inches(self, value):
        """
        Function set_inches acts as a public method to change the value of this instance's inches
        Parameters:
            value: the value that the instance's inches will be set to
        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("MSG GOES HERE")
        if value < 0:
            raise ValueError("MSG GOES HERE")
        self.__inches = value
        if value >= 12:
            self.__adjust()

    def __adjust(self):
        """
        Function __adjust reduces the value of an instance's inches to be below 12 and adds the appropriate amount to its feet
        Parameters: None
        Returns: None
        """
        self.__feet += self.__inches // 12
        self.__inches %= 12

    def __add__(self, other):
        """
        Function __add__ is called when two instances are added together
        Parameters:
            other: The other instance involved in the calculation
        Returns: A new instance as the result of adding this and the other instance together
        """
        feet = self.__feet + other.get_feet()
        inches = self.__inches + other.get_inches()
        return FootMeasure(feet, inches)

    def __eq__(self, other):
        """
        Function __eq__ is called when evaluating if this instance is equivalent with another one
        Parameters:
            other: The other instance involved in the calculation
        Returns: True if this and the other isntance are mathematically equivalent, else False
        """
        my_inches = self.__feet * 12 + self.__inches
        other_inches = other.get_feet() * 12 + other.get_inches()
        return my_inches == other_inches

    def __ne__(self, other):
        """
        Function __ne__ is called when evaluating if this instance is NOT equivalent with another one
        Parameters:
            other: The other instance involved in the calculation
        Returns: True if this and the other instance are NOT mathematically equivalent, else False
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Function __lt__ is called when evaluating if this instance is less than another one
        Parameters:
            other: The other instance involved in the calculation
        Returns: True if this instance is mathematically strictly less than the other instance, else False
        """
        my_inches = self.__feet * 12 + self.__inches
        other_inches = other.get_feet() * 12 + other.get_inches()
        return my_inches < other_inches

    def __le__(self, other):
        """
        Function __le__ is called when evaluating if this instance is less than or equal to another one
        Parameters:
            other: The other instance involved in the calculation
        Returns: True if this instance is mathematically less than or equivalent to the other instance, else False
        """
        return not self.__gt__(other)

    def __gt__(self, other):
        """
        Function __gt__ is called when evaluating if this instance is greater than another one
        Parameters:
            other: The other instance involved in the calculation
        Returns: True if this instance is mathematically strictly greater than the other instance, else False
        """
        my_inches = self.__feet * 12 + self.__inches
        other_inches = other.get_feet() * 12 + other.get_inches()
        return my_inches > other_inches

    def __ge__(self, other):
        """
        Function __ge__ is called when evaluating if this instance is greater than or equal to another one
        Parameters:
            other: The other instance involved in the calculation
        Returns: True if this instance is mathematically greater than or equivalent to the other instance, else False
        """
        return not self.__lt__(other)