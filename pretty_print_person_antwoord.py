def pretty_print_person(first_name, last_name):
    '''Print naam in mooie box met borders.'''
    full_name = f"{first_name} {last_name}"
    width = len(full_name) + 4  # padding
    
    print("┌" + "─" * (width - 2) + "┐")
    print(f"│ {full_name:<{width-4}} │")  # :< links uitlijnen
    print("└" + "─" * (width - 2) + "┘")


def main():
    f_name = "Guido"
    l_name = "van Rossum"
    pretty_print_person(f_name, l_name)


if __name__ == "__main__":
    main()
