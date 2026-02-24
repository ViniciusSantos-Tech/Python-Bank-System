from argon2 import PasswordHasher
ph = PasswordHasher()

def hashpsswd(password):
    passtostr = str(password)
    return ph.hash(passtostr)

def verifyc(plain_password, hashed_password):
    try:
        return ph.verify(hashed_password, plain_password)
    except:
        return False



    


