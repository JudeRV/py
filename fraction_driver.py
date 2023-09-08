# ===============================================================
# Name: Jude Vargas
# Date: 09/15/2023
# Algorithm: N/A
# References: <References used i.e., www.python.org, realpython.com, TA, Instructor, any collaborator>
# ===============================================================
from fraction import Fraction


def main():
    print("Creating fractions (1,2), (-1, 4), (0, 2), (4, 1), (2, 4)")
    frac1 = Fraction(1, 2)
    frac2 = Fraction(-1, 4)
    frac3 = Fraction(0, 2)
    frac4 = Fraction(4, 1)
    frac5 = Fraction(2, 4)
    frac6 = Fraction(1, 4)

    print("\n__str__ method")
    print(f"Frac1 should be 1/2 --- Value: {frac1}")
    print(f"Frac5 should be 1/2 --- Value: {frac5}")
    print(f"Frac1 + Frac2 == {frac1 + frac2}")
    print(f"{frac1} - {frac6} == {frac1 - frac6}")


if __name__ == "__main__":
    main()
