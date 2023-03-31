import unittest
from temperature_converter import TemperatureConverter

class TestTemperatureConverter(unittest.TestCase):
    """
    This class contains unit tests for the TemperatureConverter class.
    """

    def test_celsius_to_fahrenheit(self):
        converter = TemperatureConverter()
        self.assertAlmostEqual(converter.celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(converter.celsius_to_fahrenheit(100), 212)

    def test_fahrenheit_to_celsius(self):
        converter = TemperatureConverter()
        self.assertAlmostEqual(converter.fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(converter.fahrenheit_to_celsius(212), 100)

if __name__ == '__main__':
    unittest.main()
