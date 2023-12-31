import itertools
import hashlib

def to_hash(pin):
    encryptie = hashlib.sha256()
    encryptie.update(str(pin).encode('utf-8'))
    securePasswoord = encryptie.hexdigest()
    return securePasswoord

def vergelijk(pin, pins):
    for woord in pins:
        hashwoord = to_hash(woord)
        if hashwoord == pin:
            return woord
    return "niets"

def generate_pin_codes():
    pin_lengths = [1, 2, 3, 4]
    secure_pins = []

    for length in pin_lengths:
        pin_combinations = itertools.product(range(10), repeat=length)
        for pin in pin_combinations:
            secure_pins.append(''.join(map(str, pin)))
    return secure_pins

if __name__ == "__main__":
    eigen_pin = input("Geef een pincode van 1 - 4 cijfers: ")
    secure_pin = to_hash(eigen_pin)
    pins = generate_pin_codes()
    juiste_pin = vergelijk(secure_pin, pins)
    if juiste_pin == "niets":
        print("We hebben je pincode niet gevonden met deze methode.")
    else:
        print(f"We hebben je pincode geraden, het is: {juiste_pin}")
