class __Location:
    i = -1
    j = -1

def __MatrixCreator(key):
    alphabets = []
    for k in key:
        if k == 'J':
            k = 'I'
        if k not in alphabets:
            alphabets.append(k)
    for char in range(ord('A'), ord('Z') + 1):
        k = chr(char)
        if (k not in alphabets) and (k != 'J'):
            alphabets.append(k)

    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(alphabets[(5 * i) + j])
        matrix.append(row)
    return matrix

def __CharsSplitter(planeText):
    planeText = planeText.replace('J', 'I')
    text = []
    i = 0
    while i < len(planeText):
        if i == (len(planeText) - 1):
            text.append(planeText[-1] + 'X')
        else:
            char1 = planeText[i]
            char2 = planeText[i + 1]
            if char1 == char2:
                text.append(char1 + 'X')
            else:
                text.append(char1 + char2)
                i += 1
        i += 1
    return text

def __FindInMatrix(char, matrix):
    if char == 'J':
        char = 'I'
    location = __Location()
    for i in range(5):
        for j in range(5):
            if char == matrix[i][j]:
                location.i = i
                location.j = j
    return location

def Encrypt(planetext, key):
    planetext = str(planetext).upper().replace(' ', '')
    key = str(key).upper().replace(' ', '')
    matrix = __MatrixCreator(key)
    planetext = __CharsSplitter(planetext)
    cipher = ''
    for chars in planetext:
        char1 = chars[0]
        char2 = chars[1]
        char1_loc = __FindInMatrix(char1, matrix)
        char2_loc = __FindInMatrix(char2, matrix)
        if char1_loc.i == char2_loc.i:
            char1 = matrix[char1_loc.i][(char1_loc.j + 1) % 5]
            char2 = matrix[char2_loc.i][(char2_loc.j + 1) % 5]
        elif char1_loc.j == char2_loc.j:
            char1 = matrix[(char1_loc.i + 1) % 5][char1_loc.j]
            char2 = matrix[(char2_loc.i + 1) % 5][char2_loc.j]
        else:
            char1 = matrix[char1_loc.i][char2_loc.j]
            char2 = matrix[char2_loc.i][char1_loc.j]
        cipher += char1
        cipher += char2
    return cipher

def Decrypt(cipher, key):
    cipher = str(cipher).upper().replace(' ', '')
    key = str(key).upper().replace(' ', '')
    matrix = __MatrixCreator(key)
    cipher = __CharsSplitter(cipher)
    planetext = ''
    for chars in cipher:
        char1 = chars[0]
        char2 = chars[1]
        char1_loc = __FindInMatrix(char1, matrix)
        char2_loc = __FindInMatrix(char2, matrix)
        if char1_loc.i == char2_loc.i:
            char1 = matrix[char1_loc.i][(char1_loc.j - 1) % 5]
            char2 = matrix[char2_loc.i][(char2_loc.j - 1) % 5]
        elif char1_loc.j == char2_loc.j:
            char1 = matrix[(char1_loc.i - 1) % 5][char1_loc.j]
            char2 = matrix[(char2_loc.i - 1) % 5][char2_loc.j]
        else:
            char1 = matrix[char1_loc.i][char2_loc.j]
            char2 = matrix[char2_loc.i][char1_loc.j]
        planetext += char1
        planetext += char2
    
    planetext = planetext.replace('I', '(I/J)').replace('X', '(X)')
    return planetext