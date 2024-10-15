import pytest
from Other_Algos.euclidean_algorithm import find_gcd

find_gcd_testdata = [(40, 15, 5), (39, 24, 3), (40, 10, 10), (39, 2, 1)]


@pytest.mark.parametrize("num1, num2, actual_gcd", find_gcd_testdata)
def test_find_gcd(num1: int, num2: int, actual_gcd: int) -> None:
    calc_gcd = find_gcd(num1=num1, num2=num2)
    assert actual_gcd == calc_gcd
