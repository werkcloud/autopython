def ask_number(minimum=0, maximum=255, max_tries=3):
    """
    Vraagt gebruiker om een getal >= minimum EN <= maximum.
    - Probeert max_tries keer (default 3).
    - Bij succes: retourneert het getal.
    - Bij falen: retourneert minimum (fallback).
    """
    for try_count in range(max_tries):
        try:
            user_input = input(": ")
            number = int(user_input.strip())
            
            if minimum <= number <= maximum:
                return number
            else:
                print(f"That number is invalid. Moet tussen {minimum}-{maximum} zijn.")
                
        except ValueError:
            print(f"Ongeldige invoer. Gebruik een geheel getal tussen {minimum}-{maximum}.")
    
    print(f"Max {max_tries} pogingen overschreden. Gebruik {minimum}.")
    return minimum


def generate_ip_addresses(start_octet, end_octet, base="192.168.178"):
    """
    Genereert IP-adressen van start_octet tot end_octet.
    - Sanitiseert: 0 <= octets <= 255, start <= end.
    - Print elk adres in formaat base.octet.
    """
    # Sanitization: clamp naar 0-255
    start_octet = max(0, min(255, start_octet))
    end_octet = max(0, min(255, end_octet))
    
    # Zorg dat start <= end
    if start_octet > end_octet:
        start_octet, end_octet = end_octet, start_octet
        print(f"Start > end gedetecteerd. Verwisseld: {start_octet}-{end_octet}")
    
    print(f"Genereren IPs vanaf octet {start_octet} tot {end_octet}")
    
    # Genereer en print IPs
    for octet in range(start_octet, end_octet + 1):
        ip = f"{base}.{octet}"
        print(ip)


def main():
    print("How many ip-adressen should be created?")
    ip_count = ask_number(minimum=1, maximum=255)  # 1-255 IPs
    
    print("What is the start-octet?")
    start_octet = ask_number(minimum=0, maximum=255)  # 0-255
    
    # Bereken end (beperk tot 255)
    end_octet = min(255, start_octet + ip_count - 1)
    
    generate_ip_addresses(start_octet, end_octet)

 
if __name__ == "__main__":
    main()
