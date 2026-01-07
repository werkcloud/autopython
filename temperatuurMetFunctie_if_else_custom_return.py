def draag_trui(temp):
    """Draag een trui als temp < 16°."""
    if temp < 16:
        return "Draag ook een trui!"
    else:
        return "Geen trui nodig."


def jas_advies(temp):
    """jasadvies  op basis van temperatuur."""
    if temp < 12:
        return "Trek een jas aan!"
    else:
        return "Laat je jas thuis."


# Vraag de temperatuur
temp = int(input("Wat is de huidige temperatuur? "))

# Gebruik de return-waarden
print(jas_advies(temp))
print(draag_trui(temp))
