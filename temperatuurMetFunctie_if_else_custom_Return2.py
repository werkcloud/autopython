def draag_trui(temp, trui_drempel=16):
    """draag trui als temp < trui_drempel°C."""
    if temp < trui_drempel:
        print(f"Draag ook een trui! (drempel: {trui_drempel}°C)")
    else:
        print("Geen trui nodig.")


def vraag_trui_drempel(standaard_drempel=16):
    """ trui-drempel en return drempel ."""
    antwoord = input("Aangepaste trui drempel gebruiken? (j/n) ")
    if antwoord.lower().startswith("j"):
        drempel = int(input("Trui drempel (°C)? "))
        return drempel
    return standaard_drempel


def vraag_temperatuur():
    """Vraag de huidige temperatuur en return int."""
    temp = int(input("Wat is de huidige temperatuur? "))
    return temp


def bepaal_jas_advies(temp):
    """Bepaal jas-advies op basis van temperatuur, return tekst ."""
    if temp < 12:
        return "Trek een jas aan!"
    return "Laat de jas thuis."


def main():
    trui_drempel = vraag_trui_drempel()
    temp = vraag_temperatuur()

    jas_advies = bepaal_jas_advies(temp)
    print(jas_advies)

    draag_trui(temp, trui_drempel)


if __name__ == "__main__":
    main()
