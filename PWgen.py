from hashlib import pbkdf2_hmac

lowerCaseLetters = list('abcdefghijklmnopqrstuvwxyz')
upperCaseLetters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
specialCharacters = list('"!§$%&/()=?+#-.,;:_')
passwortCharacters = lowerCaseLetters + upperCaseLetters + numbers + specialCharacters
salt = "treehousegaming"

def convertBytesToPassword(hashedBytes, length):
    number = int.from_bytes(hashedBytes, byteorder='big')
    passwort = ''
    while number > 0 and len(passwort) < length:
        passwort = passwort + passwortCharacters[number % len(passwortCharacters)]
    number = number // len(passwortCharacters)
    return passwort

masterPasswort = input('Masterpasswort: ')
domain = input('Domain: ')
while len(domain) < 1:
    print('Bitte gib eine Domain an.')
    domain = input('Domain: ')
hashString = domain + masterPasswort
hashedBytes = pbkdf2_hmac(
    'sha512',
    hashString.encode('utf-8'),
    salt.encode('utf-8'),
    4096)
print('Passwort: ' + convertBytesToPassword(hashedBytes, 10))
input()
