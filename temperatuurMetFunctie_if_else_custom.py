def wear_sweater(temp, sweater_threshold=16):
    """Simple function: sweater if temp < sweater_threshold°C."""
    if temp < sweater_threshold:
        print(f"Wear a sweater too! (threshold: {sweater_threshold}°C)")
    else:
        print("No sweater needed.")


# Ask user for thresholds (optional)
custom = input("Use custom sweater threshold? (y/n) ")
if custom.lower().startswith("y"):
    sweater_threshold = int(input("Sweater threshold (°C)? "))
else:
    sweater_threshold = 16  # default


# Get temperature from user
temp = int(input("What is the current temperature? "))

# Decide on jacket
if temp < 12:
    print("Put on a jacket!")
else:
    print("Leave jacket at home.")

# Call the sweater function with chosen threshold
wear_sweater(temp, sweater_threshold)

