# fichier: test_calculator.py

from utils import add

class TestAddPositiveNumbers:
    def test_small_numbers(self):
        assert add(1, 2) == 3

    def test_large_numbers(self):
        assert add(1000, 2000) == 3000

class TestAddNegativeNumbers:
    def test_small_numbers(self):
        assert add(-1, -2) == -3

    def test_large_numbers(self):
        assert add(-1000, -2000) == -3000

class TestAddMixedNumbers:
    def test_positive_and_negative(self):
        assert add(-1, 2) == 1

    def test_negative_and_positive(self):
        assert add(3, -2) == 1

class TestAddZero:
    def test_zero_and_positive(self):
        assert add(0, 5) == 5

    def test_positive_and_zero(self):
        assert add(5, 0) == 5

    def test_zero_and_zero(self):
        assert add(0, 0) == 0
