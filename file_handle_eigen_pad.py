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
            print(f"Directory gemaakt: {directory}")
        except OSError as e:
            print("❌ Could not create directory...")
            print(e)
            return

    try:
        with open(filename, mode="w", encoding="utf-8") as f:
            while True:
                raw_name = input("Enter servername (Enter to stop): ")
                name = raw_name.strip()

                # Enter zonder tekst → stoppen
                if name == "":
                    print("✅ Stopping input loop.")
                    break

                f.write(name + "\n")
                print(f"✨ Saved: {name}")
                
    except OSError as e:
        print("❌ Error while writing to file...")
        print(e)


def print_names_from_file(filename):
    """
    Leest filename en print alle niet-lege regels.
    """
    print(f"\n📖 Reading server names from: {filename}")

    if not os.path.exists(filename):
        print("📄 File does not exist, nothing to print.")
        return

    try:
        with open(filename, mode="r", encoding="utf-8") as f:
            count = 0
            for line in f:
                name = line.strip()
                if not name:  # Skip lege regels
                    continue
                print(f"  Server: {name}")
                count += 1
            print(f"📊 Totaal {count} servernamen gelezen.")
            
    except OSError as e:
        print("❌ Error while reading from file...")
        print(e)


def main():
    try:
        # EXACT JOUW PAD
        #filename = r"C:\Users\mal15\Videos\data\servernames.txt"
        filename = "C:/Users/mal15/Videos/data/servernames.txt"
        
        ask_servernames(filename)
        print_names_from_file(filename)

    except Exception as e:
        print("❌ Something went wrong...")
        print(e)


if __name__ == "__main__":
    main()
