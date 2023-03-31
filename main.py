from converter.temperature_converter import TemperatureConverter

def main():
    """Main function for the temperature converter application."""
    print("Welcome to the Temperature Converter!")

    converter = TemperatureConverter.get_instance()

    while True:
        print("Please select an option:")
        print("1. Convert from Celsius to Fahrenheit")
        print("2. Convert from Fahrenheit to Celsius")
        print("3. Quit")

        choice = input("> ")

        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = converter.to_fahrenheit(celsius)
            print(f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit.\n")

        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = converter.to_celsius(fahrenheit)
            print(f"{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius.\n")

        elif choice == "3":
            print("Thank you for using the Temperature Converter!")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
