"""
Euclidean Algorithm:
    Start with the two initial numbers a and b.
    Do a division with remainder: a=q0⋅b+r0
    Use the remainder (r0) and the divisor (b) from the last calculation to set up the next calculation: b=q1⋅r0+r1
    Repeat steps 2 and 3 until the remainder is 0.
    The second last remainder calculated is the greatest common divisor.
"""


def find_gcd(num1: int, num2: int) -> int:
    quotient = num1 // num2
    remainder = num1 % num2

    if remainder == 0:
        return num2

    return find_gcd(num2, remainder)
