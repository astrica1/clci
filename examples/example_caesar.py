import os
from clci import caesar

def ClearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def Encryption():
    planeText = input('Plane text: ').upper().replace(' ', '')
    key = int(input('Key number: '))
    print(caesar.Encrypt(planeText, key))

def Decryption():
    cipher = input('Cipher text: ').upper().replace(' ', '')
    key = int(input('Key number: '))
    print(caesar.Decrypt(cipher, key))
    
    
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