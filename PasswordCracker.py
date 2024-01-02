import hashlib
import itertools
import string
import time

def to_hash(passwoord):
    encryptie = hashlib.sha256()
    encryptie.update(passwoord.encode('utf-8'))
    securePasswoord = encryptie.hexdigest()
    return securePasswoord

def uitlezen():
    with open ("passwoorden.txt", "r") as f:
        goedpasswoordlijst = []
        passwoord = f.readlines()
        for woord in passwoord:
            goedpasswoordlijst.append(woord.strip())
        return goedpasswoordlijst

def vergelijk(passwoord, passwoordenlijst):
    for woord in passwoordenlijst:
        hashwoord = to_hash(woord)
        if hashwoord == passwoord:
            return woord
    return "niets"

def vergelijkWoorden(passwoord, password):
    if password == passwoord:
        return password
    return "niets"

def generate_pin_codes():
    pin_lengths = [1, 2, 3, 4]
    secure_pins = []

    for length in pin_lengths:
        pin_combinations = itertools.product(range(10), repeat=length)
        for pin in pin_combinations:
            secure_pins.append(''.join(map(str, pin)))
    return secure_pins

def generate_and_print_combinations(passwoord):
    alphabet = string.ascii_letters

    for length in range(1, 9):
        combo = itertools.product(alphabet, repeat=length)
        for item in combo:
            combination = ''.join(item)
            print(combination)
            secure_combo = to_hash(combination)
            antwoord = vergelijkWoorden(passwoord, secure_combo)
            if antwoord != "niets":
                return combination
                
    return "niets"

def generate_and_print_combinations_All(passwoord):
    toetsenbord_tekens = string.printable 

    for length in itertools.count(start=1): 
        combo = itertools.product(toetsenbord_tekens, repeat=length)
        for item in combo:
            combination = ''.join(item)
            print(combination)
            secure_combo = to_hash(combination)
            antwoord = vergelijkWoorden(passwoord, secure_combo)
            if antwoord != "niets":
                return combination

if __name__ == "__main__":
    passwoord = input("geef een wachtwoord in om te testen: ")
    securePasswoord = to_hash(passwoord)
    print("we gaan beginnen met de eerste methode: gebruik maken van de meest voorkomende passwoorden. Druk op enter om verder te gaan")
    input()
    start = time.time()
    passwoorden = uitlezen()
    antwoord = vergelijk(securePasswoord, passwoorden)
    eind = time.time()
    totaal = eind - start
    if antwoord == "niets":
        print(f"deze methode heeft er {totaal} seconden over gedaan")
        print ("we hebben het wachtwoord niet gevonden aan de hand van deze methode, we gaan nu pincodes raden. Druk op enter om verder te gaan.")
        input()
        begin = time.time()
        pins = generate_pin_codes()
        juiste_pin = vergelijk(securePasswoord, pins)
        stop = time.time()
        tot = stop - begin
        if juiste_pin == "niets":
            print(f"deze methode heeft er {tot} seconden over gedaan")
            print("We hebben je pincode niet gevonden met deze methode, we gaan nu alle combinaties van letters uittesten tot lengte 8. Druk op enter om verder te gaan.")
            input()
            star = time.time()
            an = generate_and_print_combinations(securePasswoord)
            ein = time.time()
            to = ein - star
            if an == "niets":
                print(f"deze methode heeft er {to} seconden over gedaan")
                print("We hebben het wachtwoord niet gevonden met deze methode, we gaan nu alle mogelijke combinaties uittesten. Druk op enter om verder te gaan.")
                input()
                beg = time.time()
                a = generate_and_print_combinations_All(securePasswoord)
                sto = time.time()
                alles = sto - beg
                if antwoord == "niets":
                    print(f"deze methode heeft er {alles} seconden over gedaan")
                    print("We hebben het wachtwoord niet gevonden.")
                else:
                    print(f"deze methode heeft er {alles} seconden over gedaan")
                    print(f"We hebben je wachtwoord gevonden: {a}")
            else:
                print(f"deze methode heeft er {to} seconden over gedaan")
                print(f"We hebben je wachtwoord gevonden: {an}")

        else:
            print(f"deze methode heeft er {tot} seconden over gedaan")
            print(f"We hebben je pincode geraden, het is: {juiste_pin}")
    else:
        print(f"deze methode heeft er {totaal} seconden over gedaan")
        print (f"we hebben het wachtwoord geraden, het is: {antwoord}")