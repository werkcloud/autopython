import datetime
import time

def get_current_inner_temperature():
    """
    - wat heeft de functie van buiten nodig om te functioneren?
    - wat is een MOGELIJK resultaat van de functie? return waarde
    - wat kan er mogelijk mis gaan dat de functie zijn taak niet kan uitvoeren
    """
    print("De binnentemperatuur wordt gemeten")
    temperature = 16.8  # fixture TODO: Get the the measurement from a sensor
    return temperature

def ask_the_user_for_prefered_temperature():
    prefered_temperature = 21.0  # fixture
 
    user_input = input(
        "Wat is je gewenste temperatuur in graden Celsius? (bijv. 20.5) "
    )

    try:
        prefered_temperature = float(user_input)
    except ValueError:
        print("Ongeldige invoer, de standaard waarde 21.0 wordt gebruikt.")
        prefered_temperature = 21.0

    return prefered_temperature

def get_prefered_temperature():
    """Returns the prefered temperature"""
    print("Getting the prefered temperature")
    prefered = ask_the_user_for_prefered_temperature()
    return prefered

def turn_heating_on():
    """Zet de verwarming aan (fake-implementatie)."""
    print("De verwarming gaat AAN.")

def turn_heating_off():
    """Zet de verwarming uit (fake-implementatie)."""
    print("De verwarming gaat UIT.")

def is_night(current_time: datetime.time) -> bool:
    """
    Bepaal of het nacht is.

    Simpele regel:
    - Nacht is tussen 22:00 en 06:00.
    """
    start_night = datetime.time(22, 0)  # 22:00
    end_night = datetime.time(6, 0)    # 06:00

    # Nacht is van 22:00 tot 23:59 en van 00:00 tot 05:59
    return current_time >= start_night or current_time < end_night

def adjust_heating(temperature, prefered_temperature):
    """Adjust the heating given the temperature and prefered temperature"""

    print(f"De verwarming wordt aangepast met de temperatuur {temperature}")
    print(f"en voorkeurstemperatuur {prefered_temperature}")
    # genereert een SIDE EFFECT, retourneert in principe niks
    """
    bereken het temperatuursverschil
    als het verschil negatief is, schakel dan de kachel aan
    en anders juist uit (ook al was die misschien al uit)

    implementeer zelf even de bijbehorende functies.
    turn_heating_on()
    turn_heating_off()
    """

    # meetmoment bepalen
    now = datetime.datetime.now()
    current_time = now.time()
    print(f"Meetmoment: {now.isoformat()}")

    # eerst checken of het nacht is
    if is_night(current_time):
        print("Het is nacht, de verwarming wordt niet aangezet.")
        turn_heating_off()
        return

    # temperatuursverschil berekenen
    difference = prefered_temperature - temperature
    print(f"Temperatuursverschil: {difference:.1f} °C")

    # als het verschil positief is, is het kouder dan gewenst -> verwarming aan
    if difference > 0:
        print("Het is kouder dan de voorkeurstemperatuur.")
        turn_heating_on()
    else:
        print("Het is warm genoeg (of warmer).")
        turn_heating_off()

def main():
    """
    Zou het niet mooi zijn als...
    Laat de verwarming maar aangaan als de binnentemperatuur onder
    de 20 graden is, maar niet als het nacht is. Het kan natuurlijk veel uitgebreider dan je 
    eerst bedenkt. (Sanatization 20% werkende versie/ proof of concept
    80% fijnslijpen, schoonpoetsen, foutafhandeling.)

    Fake it until you make it!
    Welke lokatie??
      we willen ook het meetmoment vastleggen.

      Prefered temperature kan ook natuurlijk van een tabel of iets dergelijks
      komen. :)
    """
    print("Heating control gestart. Druk op Ctrl+C om te stoppen.")
    
    # Keuze bij start: vaste waarde of elke keer input?
    use_fixed_temp = input("Gebruik vaste voorkeurstemperatuur? (j/n, anders elke 15 min input): ").lower().startswith('j')
    
    if use_fixed_temp:
        fixed_temp = get_prefered_temperature()  # Eenmalig vragen
        print(f"Vaste temperatuur ingesteld op {fixed_temp}°C")
    
    try:
        while True:
            if use_fixed_temp:
                prefered_temperature = fixed_temp  # Gebruik vaste waarde
            else:
                prefered_temperature = get_prefered_temperature()  # Elke cyclus input
            
            room_temperature = get_current_inner_temperature()
            adjust_heating(room_temperature, prefered_temperature)
            print("Wachten 15 minuten op volgende controle...")
            time.sleep(9)  # 15 minuten = 900 seconden
    except KeyboardInterrupt:
        print("\nHeating control gestopt door gebruiker.")
        turn_heating_off()  # Zorg dat verwarming uitgaat bij exit

if __name__ == "__main__":
    main()
