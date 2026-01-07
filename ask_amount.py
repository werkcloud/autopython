# projects/basic_programs/ask_amount.py

def ask_amount():
    """Asks the user for an amount.

    Prints an error if the amount is smaller than 0 and returns 0.
    Else returns the amount the user entered.
    """
    # Ask the user for input as text
    raw_value = input("How many? ")

    # Convert the text to an integer
    amount = int(raw_value)

    # Check if the number is negative
    if amount < 0:
        print("That is not a positive number!")
        # In this case we want to return 0
        return 0
    else:
        # Otherwise the input is valid, return the original value
        return amount


def main():
    amount = ask_amount()
    message = f"The user wants {amount}."
    print(message)


if __name__ == "__main__":
    main()
