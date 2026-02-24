# test of the system
import time
import sys
import random
import os

def clear_screen():
    _ = os.system('cls')

clear_screen()

# BIOS Startup
def award_bios():
    if os.name == 'nt': os.system('')

    clear_screen()
    print("Award Modular BIOS v4.50PG, An Energy Star Ally")
    print("Copyright (C) 1984-94, Award Software, Inc.\n")
    print("80486DX2 CPU at 32MHz")
    
    for i in range(0, 32769, 1024):
        sys.stdout.write(f"\rMemory Test : {i:5}K OK")
        sys.stdout.flush()
        time.sleep(0.09)
    
    print("\n")
    print("Press DEL to enter SETUP")
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
    
# login system prep
login_active = True
login_success = False
console_active = False
creation = False
users_db = {
    "ADMIN": "HWrnDLEMWmVpdMzpQqWLn9u6qvjk5n2E",
    "mason": "0327"
}
clear_screen()
time.sleep(1.5)

while login_active == True:
    # login system actuality
    a = input('Enter username: ')
    b = input('Enter password: ')
    
    if a in users_db:
        if b == users_db[a]:
            print(f'Login successful. Welcome {a}!')
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
                users_db[new_u] = new_p
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
            print("This is PYDOS, a simple DOS system for python!")
            print("To use this, you will use a console with commands!")
            print(f'Use the "help" command to see all of the commands!')
            login_success = False
            console_active = True
        elif choice == "N":
            print("Starting console...")
            login_success = False
            console_active = True
        else:
            print("You did not select a correct option!")
            print("Please select another option.")
while console_active:
    console = input('C:\> ')
    if console == str("help"):
        print("* ACALC\n* There are no other commands!")
    elif console == str("ACALC"):
        print("calculations coded later")