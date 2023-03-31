class TemperatureConverter:
    """
    This class encapsulates the temperature conversion logic.
    """

    _instance = None

    def __init__(self):
        """
        Initializes the TemperatureConverter object.
        """
        if TemperatureConverter._instance is not None:
            raise Exception("TemperatureConverter is a singleton class. Use TemperatureConverter.get_instance() to get the instance.")
        TemperatureConverter._instance = self

    @staticmethod
    def get_instance():
        """
        Returns the shared instance of the TemperatureConverter class.
        """
        if TemperatureConverter._instance is None:
            TemperatureConverter()
        return TemperatureConverter._instance

    def to_fahrenheit(self, celsius):
        """
        Converts temperature from Celsius to Fahrenheit.
        """
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    def to_celsius(self, fahrenheit):
        """
        Converts temperature from Fahrenheit to Celsius.
        """
        celsius = (fahrenheit - 32) * 5/9
        return celsius
