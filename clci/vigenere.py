def __LengthEqualizer(text, key):
    if len(key) == len(text):
        return key
    if len(key) > len(text):
        key = key[ : len(text)]
    else:
        key_length = len(key)
        length_pointer = 0
        while len(key) < len(text):
            key += key[length_pointer % key_length]
            length_pointer += 1
    return key

def __CharShifter(text_char, key_char, forward=True):
    char = ''
    char_order = 0
    if forward:
        char_order = ord(text_char) + (ord(key_char) - ord('A'))
    else:
        char_order = ord(text_char) - (ord(key_char) - ord('A'))
    if (char_order <= ord('Z')) and (char_order >= ord('A')):
        char = chr(char_order)
    elif char_order > ord('Z'):
        char = chr(ord('A') + (char_order % (ord('Z') + 1)))
    elif char_order < ord('A'):
        char = chr(ord('Z') - (ord('A') - char_order) + 1)
    return char

def Encrypt(planetext, key):
    planetext = str(planetext).upper().replace(' ', '')
    key = str(key).upper().replace(' ', '')
    key = __LengthEqualizer(planetext, key)
    cipher = ''
    for i in range(len(planetext)):
        cipher += __CharShifter(planetext[i], key[i], True)
    return cipher

def Decrypt(cipher, key):
    cipher = str(cipher).upper().replace(' ', '')
    key = str(key).upper().replace(' ', '')
    key = __LengthEqualizer(cipher, key)
    planetext = ''
    for i in range(len(cipher)):
        planetext += __CharShifter(cipher[i], key[i], False)
    return planetext