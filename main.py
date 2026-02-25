# test of the system
import time
import sys
import random
import os
import json
import bcrypt

def clear_screen():
    _ = os.system('cls')

clear_screen()

# BIOS Startup
def award_bios():
    if os.name == 'nt': os.system('')

    clear_screen()
    print("Award Modular BIOS v4.50PG, An Energy Star Ally")
    print("Copyright (R) 1984-94, Award Software, Inc.\n")
    print("80486DX2 CPU at 32MHz")
    
    for i in range(0, 32769, 1024):
        sys.stdout.write(f"\rMemory Test : {i:5}K OK")
        sys.stdout.flush()
        time.sleep(0.09)
    
    print("\n")
    time.sleep(2.5)

    clear_screen()
    print("                         Award Software, Inc.                       ")
    print("                        System Configurations                       ")
    print(" ╔═════════════════════════════════════════════════════════════════╗")
    print(" ║ CPU Type         : 80486DX2        │ Base Memory      : 640K    ║")
    print(" ║ Co-Processor     : Installed       │ Extended Memory  : 31744K  ║")
    print(" ║ CPU Clock        : 32MHz           │ Cache Memory     : None    ║")
    print(" ╟────────────────────────────────────┼────────────────────────────╢")
    print(" ║ Diskette Drive A : 1.44M, 3.5 in.  │ Display Type     : EGA/VGA ║")
    print(" ║ Diskette Drive B : None            │ Serial Port(s)   : 3F8/2F8 ║")
    print(" ║ Pri. Master Disk : LRG, Mode 0, 420MB Parallel Port(s) : 378    ║")
    print(" ║ Pri. Slave Disk  : None            │                            ║")
    print(" ║ Sec. Master Disk : None            │                            ║")
    print(" ║ Sec. Slave Disk  : None            │                            ║")
    print(" ╚════════════════════════════════════╧════════════════════════════╝")
    
    time.sleep(1.0)

    print("\n\nUpdating ESCD ...")
    time.sleep(3)
award_bios()
"""
bver = "2311"
barch = "x64"
btype = "UEFI BIOS Utility"
borg = "ACER"
print(f'{btype} {bver} {barch} {borg}(R)')
"""

# PYDOS Startup Screen
clear_screen()
message = "PYDOS"
for char in message:
    print(char, end="", flush=True)
    time.sleep(0.1) #
print()

# PYDOS Loading (that really does nothing but it looks cool at least)
def fast_loading():
    for char in "Loading":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    for _ in range(10):
        time.sleep(random.uniform(0.01, 1))
        sys.stdout.write(".")
        sys.stdout.flush()
    print()

if __name__ == "__main__":
    fast_loading()

DB_FILE = "users_db.json"

def load_users():
    admin_hash = "$2a$12$.kkOEmoWzIJxtTF1LyLZHeqZ9cZTMt3k0qDuV3qxVF0CkTHHwHRrm"
    mason_hash = "$2a$12$CF0v5zAYLt/4oNwfQJL1JeXVsf1o7ilNiYiGqHvO5lIpoUOsJoQJy"
    if not os.path.exists(DB_FILE):
        # Ensure default values are ACTUAL bcrypt hashes
        return {"ADMIN": admin_hash, "mason": mason_hash}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_users(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

users_db = load_users()

# login system prep
login_active = True
login_success = False
console_active = False
creation = False

"""
users_db = {
    "ADMIN": "HWrnDLEMWmVpdMzpQqWLn9u6qvjk5n2E",
    "mason": "0327"
}
"""

clear_screen()
time.sleep(1.5)

while login_active == True:
    # login system actuality
    a = input('Enter username: ')
    b = input('Enter password: ')
    
    if a in users_db:
        stored_hash = users_db[a].encode('utf-8')
        if bcrypt.checkpw(b.encode('utf-8'), stored_hash):
            try:
                print(f'Login successful. Welcome {a}!')
            except:
                print(f'ERROR: Hash error.')
            login_active = False
            login_success = True
        else:
            print('ERROR: Password is incorrect.')
    else:
        print(f'ERROR: Username does not exist on this system.')
        time.sleep(0.6)
        print(f'Would you like to create a new user?')
        creation = True
        while creation == True:
            usernew = input(f'Choose an option (Y, N):')
            if usernew == "Y":
                new_u = input('Choose a username: ')
                new_p = input('Choose a password: ')
                hashed = bcrypt.hashpw(new_p.encode('utf-8'), bcrypt.gensalt())
                users_db[new_u] = hashed.decode('utf-8')
                save_users(users_db)
                print(f"User {new_u} created successfully!")
                creation = False
                clear_screen()
            elif usernew == "N":
                creation = False
                clear_screen()
            else:
                print("You did not select a correct option!")
                creation = True
                clear_screen()
            
if login_success == True:
    # prepare the variables!
    
    while login_success == True:
        clear_screen()
        print(f'Welcome, {a}!\nWould you like a tutorial for this DOS?')
        choice = input('Choose an option (Y,N): ')
        if choice == "Y":
            clear_screen()
            print("This is PYDOS, a simple DOS system for python!")
            time.sleep(1)
            print("To use this, you will use a console with commands! Commands ARE case-sensitive!")
            time.sleep(1)
            print(f'Use the "help" command to see all of the commands!')
            time.sleep(1)
            print(f'Use the "ahelp" command to see a detailed report of a command!')
            time.sleep(1.5)
            clear_screen()
            login_success = False
            console_active = True
        elif choice == "N":
            clear_screen()
            print("Starting console...")
            time.sleep(2.5)
            clear_screen()
            login_success = False
            console_active = True
        else:
            print("You did not select a correct option!")
            print("Please select another option.")
while console_active:
    console = input('C:\> ')
    if console == str("help"):
        print("* CALC\n* clear\n* ahelp\n* help\n* There are no other commands!")
    elif console == str("ahelp"):
        a = input("Enter command:")
        if a == "CALC":
            print("Does simple math equations with 2 numbers. (ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION.)")
        elif a == "Clear":
            print("Clears the console screen.")
        else:
            print("Not a valid command!")
    elif console == str("clear"):
        clear_screen()
    elif console == str("CALC"):
        def sum(a, b):
            return (a + b)
        def difference(a, b):
            return (a - b)
        def product(a, b):
            return (a * b)
        def quotient(a, b):
            return (a / b)
        
        a = int(input('Enter 1st number: '))
        b = int(input('Enter 2nd number: '))
        c = input('Enter operation (ADD, SUBTRACT, MULTIPLY, DIVIDE): ')
        if c == "ADD":
            print(f'The sum of {a} and {b} is {sum(a, b)}')
        elif c == "SUBTRACT":
            print(f'The difference of {a} and {b} is {difference(a, b)}')
        elif c == "MULTIPLY":
            print(f'The product of {a} and {b} is {product(a, b)}')
        elif c == "DIVIDE":
            print(f'The quotient of {a} and {b} is {quotient(a, b)}')
        else:
            print(f'You did not enter a valid operation! (ADD, SUBTRACT, MULTIPLY, DIVIDE).')
