def ask_number(minimum=0, max_tries=3):
    """
    Vraagt gebruiker om een getal >= minimum.
    - Probeert max_tries keer (default 3).
    - Bij succes: retourneert het getal.
    - Bij falen: retourneert minimum (fallback).
    """
    for try_count in range(max_tries):
        try:
            user_input = input(": ")
            number = int(user_input.strip())
            
            if number >= minimum:
                return number
            else:
                print(f"That number is too small. (min: {minimum})")
                
        except ValueError:
            print(f"Ongeldige invoer. Gebruik een geheel getal >= {minimum}.")
    
    print(f"Max {max_tries} pogingen overschreden. Gebruik {minimum}.")
    return minimum


def generate_ip_addresses(start_octet, end_octet, base="192.168.178"):
    """
    Genereert IP-adressen van start_octet tot end_octet.
    - Sanitiseert: start <= end, beide 0-255.
    - Print elk adres in formaat base.octet.
    """
    # Sanitization: zorg dat start <= end
    if start_octet > end_octet:
        start_octet, end_octet = end_octet, start_octet
        print(f"Start > end gedetecteerd. Verwisseld: {start_octet}-{end_octet}")
    
    # Genereer en print IPs
    for octet in range(start_octet, end_octet + 1):
        ip = f"{base}.{octet}"
        print(ip)


def main():
    print("How many ip-adressen should be created?")
    ip_count = ask_number(minimum=1)  # Min 1 IP
    
    print("What is the start-octet?")
    start_octet = ask_number(minimum=0, max_tries=3)  # Octet 0-255
    
    # Bereken end op basis van count
    end_octet = start_octet + ip_count - 1
    
    print(f"Genereren {ip_count} IPs vanaf octet {start_octet} tot {end_octet}")
    generate_ip_addresses(start_octet, end_octet)


if __name__ == "__main__":
    main()
