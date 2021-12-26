from clci import playfair

def test_Encript():
    assert playfair.Encrypt('Hi', 'bye') == 'ID'
    assert playfair.Encrypt('welcome', 'tEst') == 'EDIFRISW'
    assert playfair.Encrypt('tErrA Fo Rm', 'ci pHer') == 'UHBVABRUDG'
    assert playfair.Encrypt('TeSt', 1) == 'PITP'
    
def test_Decript():
    assert playfair.Decrypt('ID', 'bye') == 'H(I/J)'
    assert playfair.Decrypt('EDIFRISW', 'tEst') == 'WELCOME(X)'
    assert playfair.Decrypt('UHb VAB RuDG', 'ci pHer') == 'TER(X)RAFORM'
    assert playfair.Decrypt('PItP', 1) == 'TEST'