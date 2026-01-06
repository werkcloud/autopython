# Get temperature from user (in Celsius)
temp = int(input("What is the current temperature? "))

# Decide on jacket
if temp < 12:
    print("Put on a jacket!")
else:
    print("Leave jacket at home.")