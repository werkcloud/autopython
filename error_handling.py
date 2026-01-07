def ask_amount():
    """
    Vraagt positieve hoeveelheid (>=0).
    RAISES SPECIFIEKE ValueError:
    - NegativeAmountError bij negatief getal
    - InvalidInputError bij letters/niet-int
    """
    try:
        user_input = input("How many? ").strip()
        
        # Stap 1: Check conversie
        amount = int(user_input)
        
        # Stap 2: Check negatief
        if amount < 0:
            raise ValueError(f"Amount {amount} is negatief! Moet >= 0 zijn.")
        
        return amount
        
    except ValueError:
        # NIET int convertible → letters/niet-getal
        raise ValueError(f"Ongeldige invoer '{user_input}'. Gebruik een geheel getal >= 0.")


def main():
    """
    Volledige handling met aparte foutmeldingen.
    """
    amount = 0
    
    try:
        amount = ask_amount()
        print(f"✅ Succes! Gebruiker wil {amount} stuks.")
        
    except ValueError as error:
        if "negatief" in str(error):
            print(f"❌ NEGATIEF GETAL: {error}")
        elif "Ongeldige invoer" in str(error):
            print(f"❌ LETTERS/NIET-GETAL: {error}")
        else:
            print(f"❌ ANDERE FOUT: {error}")
        
        print("Gebruik standaard waarde 0.")
        amount = 0
    
    except KeyboardInterrupt:
        print("\n👋 Gestopt door gebruiker (Ctrl+C).")
        amount = 0
    
    finally:
        message = f"The user wants {amount}"
        print(message)
        print("🎉 Klaar.")


if __name__ == "__main__":
    main()
