import os
import os.path


def ask_servernames(filename):
    """
    Vraagt in een loop om servernamen en schrijft ze naar filename.
    - Lege invoer (alleen Enter) stopt de lus.
    - Namen worden gesanitized (strip + skip lege regels).
    """
    print(f"Writing server names to: {filename}")

    # Zorg dat de directory bestaat
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory, exist_ok=True)
        except OSError as e:
            print("Could not create directory for file...")
            print(e)
            return

    try:
        with open(filename, mode="w", encoding="utf-8") as f:
            while True:
                raw_name = input("Enter servername (Enter to stop): ")
                name = raw_name.strip()

                # Enter zonder tekst → stoppen
                if name == "":
                    print("Stopping input loop.")
                    break

                # Eventueel extra sanitization, bv. spaties in naam voorkomen
                # name = name.replace(" ", "_")

                f.write(name + "\n")
    except OSError as e:
        print("Error while writing to file...")
        print(e)


def print_names_from_file(filename):
    """
    Leest filename en print alle niet-lege regels.
    """
    print(f"\nReading server names from: {filename}")

    if not os.path.exists(filename):
        print("File does not exist, nothing to print.")
        return

    try:
        with open(filename, mode="r", encoding="utf-8") as f:
            for line in f:
                name = line.strip()
                if not name:
                    # Sla lege regels over
                    continue
                print(f"Server: {name}")
    except OSError as e:
        print("Error while reading from file...")
        print(e)


def main():
    try:
        # Basisdirectory van het project
        # Stel: je script staat in bijv. C:\Users\mal15\Videos\projects\basic_programs\server_names.py
        # En je wilt data/servernames.txt in dezelfde projectstructuur.
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "..", "..", "data")
        filename = os.path.join(data_dir, "servernames.txt")

        # Alternatief, als je expliciet jouw pad wilt gebruiken:
        # filename = r"C:\Users\mal15\Videos\data\servernames.txt"

        ask_servernames(filename)
        print_names_from_file(filename)

    except Exception as e:
        print("Something went wrong...")
        print(e)


if __name__ == "__main__":
    main()
