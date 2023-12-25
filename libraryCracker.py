import hashlib

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

if __name__ == "__main__":
    passwoord = input("geef een wachtwoord in om te testen: ")
    securePasswoord = to_hash(passwoord)
    passwoorden = uitlezen()
    antwoord = vergelijk(securePasswoord, passwoorden)
    if antwoord == "niets":
        print ("we hebben het wachtwoord niet gevonden aan de hand van deze methode")
    else:
        print (f"we hebben het wachtwoord geraden, het is: {antwoord}")