import hashlib

def to_hash(passwoord):
    encryptie = hashlib.sha256()
    encryptie.update(passwoord.encode('utf-8'))
    securePasswoord = encryptie.hexdigest()
    return securePasswoord

if __name__ == "__main__":
    passwoord = input("geef een wachtwoord in om te testen: ")
    securePasswoord = to_hash(passwoord)
