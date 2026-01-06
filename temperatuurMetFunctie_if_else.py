def wear_sweater(temp):
    """Simple function: sweater if temp < 16°C."""
    if temp < 16:
        print("Wear a sweater too!")
    else:
        print("No sweater needed.")

# Get temperature from user
temp = int(input("What is the current temperature? "))

# Decide on jacket
if temp < 12:
    print("Put on a jacket!")
else:
    print("Leave jacket at home.")

# Call the sweater function
wear_sweater(temp)
