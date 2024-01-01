import itertools
import string
import hashlib

gevonden = False

def to_hash(passwoord):
    encryptie = hashlib.sha256()
    encryptie.update(passwoord.encode('utf-8'))
    securePasswoord = encryptie.hexdigest()
    return securePasswoord

def vergelijk(passwoord, password):
    if password == passwoord:
        return password
    return "niets"

def generate_and_print_combinations(passwoord):
    alphabet = string.ascii_letters  # Alle letters van het alfabet

    for length in range(1, 9):  # Lengte varieert van 1 tot 8
        combo = itertools.product(alphabet, repeat=length)
        for item in combo:
            combination = ''.join(item)
            print(combination)
            secure_combo = to_hash(combination)
            antwoord = vergelijk(passwoord, secure_combo)
            if antwoord != "niets":
                return combination
                
    return "niets"
    
if __name__ == "__main__":
    passwoord = input("Geef een wachtwoord van 1 tot 8 letters: ")
    secure_passwoord = to_hash(passwoord)
    antwoord = generate_and_print_combinations(secure_passwoord)
    if antwoord == "niets":
        print("We hebben het wachtwoord niet gevonden met deze methode.")
    else:
        print(f"We hebben je wachtwoord gevonden: {antwoord}")
