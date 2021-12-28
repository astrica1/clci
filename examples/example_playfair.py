import os
from clci import playfair

def ClearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def Encryption():
    planeText = input('Plane text: ').upper().replace(' ', '')
    key = input('Key: ').upper().replace(' ', '')
    print(playfair.Encrypt(planeText, key))

def Decryption():
    cipher = input('Cipher text: ').upper().replace(' ', '')
    key = input('Key: ').upper().replace(' ', '')
    print(playfair.Decrypt(cipher, key))
    
    
def main():
    while True:
        print('Enter \'e\' for Encryption')
        print('Enter \'d\' for Decryption')
        char = input('Application mode: ').lower()
        ClearConsole()
        if char == 'd':
            print('Decryption')
            print('==========\n')
            Decryption()
            exit(0)
        elif char == 'e':
            print('Encryption')
            print('==========\n')
            Encryption()
            exit(0)

if __name__ == "__main__":
    main()