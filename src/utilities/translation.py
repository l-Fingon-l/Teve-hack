from pathlib import Path
import re

def encrypt(string):
    result = ''
    data = string
    key = "0)M3}$lF%*(/|WdjviC{5u2Lm4nTb+\n><XZ I]t~h=?-_8DUcAy9oQGErV,ax1[YP:qJB\"p!fSNe6wksH'@#gK7.O&zR;\\ "
    while len(data) > 0:
        symbol = data[0]
        position = 1 + key.find(symbol)
        if position < 10:
            encoded_symbol = '0' + str(position)
        else: 
            encoded_symbol = str(position)
        result =  encoded_symbol + result
        data = data[1:]

    return result

def decrypt(string, key: str):
    result = ''
    data = string
    while len(data) > 0:
        n = int(string[len(data) - 2: len(data)])
        data = data[:len(data) - 2]
        if n == 99:
            result += '\n'
        elif n != 0:
            result += key[n - 1: n]
            #"{#@.}B\nKNwcE*Jvp2/,[:VzOsDaR3%mC_ktI)8oy<-FHeYx6SMbl(P\\=>AQ9X&$Lh4 ?]rgq7G~'!|f+jd5u1UinT0\";ZW"
            #result += "0)M3}$lF%*(/|WdjviC{5u2Lm4nTb+\n><XZ I]t~h=?-_8DUcAy9oQGErV,ax1[YP:qJB\"p!fSNe6wksH'@#gK7.O&zR;\\ "[n - 1: n]
    return result

# while True:
#     encrypted = input('encrypted: ')
#     print('decrypted: "' + decrypt(encrypted, "{#@.}B\nKNwcE*Jvp2/,[:VzOsDaR3%mC_ktI)8oy<-FHeYx6SMbl(P\\=>AQ9X&$Lh4 ?]rgq7G~'!|f+jd5u1UinT0\";ZW") + '"')


def decrypt_re(string):
    result = 'Iji("'
    data = string.group(1)
    while len(data) > 0:
        n = int(string.group(1)[len(data) - 2: len(data)])
        data = data[:len(data) - 2]
        if n == 99:
            result += '\n'
        elif n != 0:
            result += "{#@.}B\nKNwcE*Jvp2/,[:VzOsDaR3%mC_ktI)8oy<-FHeYx6SMbl(P\\=>AQ9X&$Lh4 ?]rgq7G~'!|f+jd5u1UinT0\";ZW"[n - 1: n]
    decoded.write(result[5:] + '\n')
    return result + '"'

decoded = open('decoded.txt', 'w')

original = Path('original.j').read_text()
#p = re.compile(r'Pws\("((?:\d{2})+)"\)')
p = re.compile(r'Iji\("((?:\d{2})+)"')
res = p.sub(decrypt_re, original)
refactored = Path('war3map_refactored.j').write_text(res)

decoded.close()
