import unittest
from Lesson32.entity.orange import Orange


class OrangeTest(unittest.TestCase):
    def test_orange_default_constructor(self):
        orange = Orange()

        expected_diameter = 100
        expected_vitamin = 1000
        expected_cost = 0

        self.assertEqual(expected_diameter, orange.diameter)
        self.assertEqual(expected_vitamin, orange.vitamin)
        self.assertEqual(expected_cost, orange.price)

    def test_orange_constructor_with_args(self):
        expected_diameter = 200
        expected_vitamin = 2000
        expected_cost = 15

        orange = Orange(expected_diameter, expected_vitamin, expected_cost)

        self.assertEqual(expected_diameter, orange.diameter)
        self.assertEqual(expected_vitamin, orange.vitamin)
        self.assertEqual(expected_cost, orange.price)

    def test_negative_orange_diameter(self):
        diameter = -200
        expected = 100

        orange = Orange(diameter=diameter)

        self.assertEqual(expected, orange.diameter)

    def test_negative_orange_vitamin(self):
        vitamin = -200
        expected = 1000

        orange = Orange(vitamin=vitamin)

        self.assertEqual(expected, orange.vitamin)

    def test_negative_orange_cost(self):
        cost = -200
        expected = 0

        orange = Orange(cost=price)

        self.assertEqual(expected, orange.price)

