def __CharShifter(text_char, key, forward=True):
    char = ''
    char_order = 0
    if forward:
        char_order = ord(text_char) + key
    else:
        char_order = ord(text_char) - key
    if (char_order <= ord('Z')) and (char_order >= ord('A')):
        char = chr(char_order)
    elif char_order > ord('Z'):
        char = chr(ord('A') + (char_order % (ord('Z') + 1)))
    elif char_order < ord('A'):
        char = chr(ord('Z') - (ord('A') - char_order) + 1)
    return char

def Encrypt(planetext, key=3):
    planetext = str(planetext).upper().replace(' ', '')
    key = int(key)
    cipher = ''
    for i in range(len(planetext)):
        cipher += __CharShifter(planetext[i], key, True)
    return cipher

def Decrypt(cipher, key=3):
    cipher = str(cipher).upper().replace(' ', '')
    key = int(key)
    plantext = ''
    for i in range(len(cipher)):
        plantext += __CharShifter(cipher[i], key, False)
    return plantext