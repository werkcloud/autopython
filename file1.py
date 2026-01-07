def draag_trui(temp):
   """  draag een trui als temp < 16°."""
   if temp < 16:
        print("Draag ook een trui!")
   else:
        print("Geen trui nodig.")


# Vraag de temperatuur
temp = int(input("Wat is de huidige temperatuur? "))



if temp < 12:
    print("Trek een jas aan!")
else:
    print("Laat je jas thuis.")


draag_trui(temp)

