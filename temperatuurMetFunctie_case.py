def wear_sweater(temp):
    """Sweater advice using match case."""
    match temp:
        case t if t < 10:
            print("Wear a thick sweater! It's very cold.")
        case t if t < 16:
            print("Wear a sweater too!")
        case _:
            print("No sweater needed.")

def wear_jacket(temp):
    """Jacket advice using match case."""
    match temp:
        case t if t < 8:
            print("Bundle up with a heavy jacket! Extreme cold.")
        case t if t < 12:
            print("Put on a jacket!")
        case _:
            print("Leave jacket at home.")

# Get temperature with validation
while True:
    try:
        temp_input = input("What is the current temperature in °C? ").strip()
        if not temp_input:
            print("Please enter a number.")
            continue
        temp = int(temp_input)
        break
    except ValueError:
        print("Invalid input. Enter an integer temperature (e.g., 10).")

# Provide advice
wear_jacket(temp)
wear_sweater(temp)
print(f"Current temp: {temp}°C")

