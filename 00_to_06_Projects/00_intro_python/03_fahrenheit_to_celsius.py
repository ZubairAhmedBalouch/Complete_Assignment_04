def main():
    print("Welcome to Fahrenheit to Celsius Converter")
    Farhenheit = float(input("Enter temperature in Fahrenheit: "))
    Celsius = (Farhenheit -32) * 5.0/9.0
    print(f"Temperature: {Farhenheit}°F is equal to {Celsius:.2f}°C")

if __name__ == "__main__":
    main()

    # This program converts temperature from Fahrenheit to Celsius.
    