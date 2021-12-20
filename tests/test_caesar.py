from clci import caesar

def test_Encript():
    assert caesar.Encrypt('Hi') == 'KL'
    assert caesar.Encrypt('welcome', 1) == 'XFMDPNF'
    assert caesar.Encrypt('tErrA Fo Rm', 27) == 'UFSSBGPSN'
    assert caesar.Encrypt('TeSt', '1') == 'UFTU'
    
def test_Decript():
    assert caesar.Decrypt('Kl') == 'HI'
    assert caesar.Decrypt('Xfmdpnf', 1) == 'WELCOME'
    assert caesar.Decrypt('uFSSB Gp Sn', 27) == 'TERRAFORM'
    assert caesar.Decrypt('UFTU', '1') == 'TEST'