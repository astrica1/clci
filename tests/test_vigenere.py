from clci import vigenere

def test_Encript():
    assert vigenere.Encrypt('Hi', 'bye') == 'IG'
    assert vigenere.Encrypt('welcome', 'tEst') == 'PIDVHQW'
    assert vigenere.Encrypt('tErrA Fo Rm', 'ci pHer') == 'VMGYEWQZB'
    assert vigenere.Encrypt('TeSt', 1) == 'DOCD'
    
def test_Decript():
    assert vigenere.Decrypt('IG', 'bye') == 'HI'
    assert vigenere.Decrypt('PIdVHqW', 'tEst') == 'WELCOME'
    assert vigenere.Decrypt('VMG YEW QZB', 'ci pHer') == 'TERRAFORM'
    assert vigenere.Decrypt('DOCD', 1) == 'TEST'