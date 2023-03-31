# [Temperature Converter](https://github.com/matt-nowakowski/temperature-converter)

This is a command-line based temperature converter that converts temperature from Celsius to Fahrenheit or vice versa. The project has been developed using Python programming language and follows the Object-Oriented Programming (OOP) paradigm. The Singleton design pattern has been implemented in this project to ensure that only one instance of the temperature converter object exists.

## Requirements
- Python 3.x

## Instructions to Use
1. Clone the repository using the following command:
```
git clone https://github.com/matt-nowakowski/temperature-converter.git
```

2. Navigate to the project directory:
```
cd temperature-converter
```

3. Run the following command to install the required packages (currently none required):
```
pip install -r requirements.txt
```

4. Run the program:
```
python main.py
```

5. Follow the on-screen instructions to convert the temperature.

## Processes and Steps Used to Deliver Features
- Requirements gathering, ticket creation, pull requests and branch merges
- OOP Design
- Implementation of features
- Testing
- Documentation
- User test

## Testable Logic
The temperature converter has the following logic:
- The user enters the temperature in Celsius or Fahrenheit.
- The user specifies the unit of the temperature to be converted.
- The program converts the temperature to the other unit and displays the result to the user.

## Unit Tests:
The project includes unit tests to test the functionality of the temperature converter. The tests are included in the tests directory and can be run using the following command:
```
python -m unittest discover tests
```

## Good Coding Practices:

The project follows the following coding practices:

- Descriptive variable and class names.
- Code is modular and follows the single responsibility principle.
- Code is commented appropriately.
- Code is formatted according to PEP8 guidelines.
- Version control is used to keep track of changes.

## OOP Features:

The project uses the following OOP features:

- Classes: TemperatureConverter class is used to encapsulate the temperature conversion logic.
- Objects: An object of the TemperatureConverter class is created to convert the temperature.

## User Testing:

The project has been currently tested by at least one user. User testing feedback can be found in the feedback.txt file.

## Evaluation:

The project meets all the requirements stated in the excersie. It is modular, follows OOP design patterns, has both user and technical documentation, has testable logic with unit tests, uses good coding practices, and is evaluated in the README file. Overall, the project is well-organized and easy to use. It has been created gradually, with a ticketing system tracking feature requirements.
