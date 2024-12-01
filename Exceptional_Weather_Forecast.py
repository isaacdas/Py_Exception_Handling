#Temperature converter


def temp_convert(temperature):
    new_temp = (temperature - 32) * 5/9
    print(f"\n{temperature}°F converted to celsius is: {new_temp}°C")

while True:
    try:
        temperature_f = int(input("\nEnter the temperature in Fahrenheit (whole number please): "))

    except ValueError:
        print("\nYou did not enter a valid input")
    
    else: 
        temp_convert(temperature_f)
    
    finally:
        print("Thank you for using this program. Goodbye for now.\n")
        break
