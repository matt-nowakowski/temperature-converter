from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="temperature-converter",
    version="1.0.0",
    author="Mateusz Nowakowski",
    description="A Comand Line Porgramme for converting temperatures between Celsius and Fahrenheit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "temperature-converter=temperature_converter.temperature_converter:main"
        ]
    },
)
