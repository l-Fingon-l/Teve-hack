from pathlib import Path
import re


def decrypt(string):
    result = ''
    data = string
    while len(data) > 0:
        n = int(string[len(data) - 2: len(data)])
        data = data[:len(data) - 2]
        if n == 99:
            result += '\n'
        elif n != 0:
            result += "0)M3}$lF%*(/|WdjviC{5u2Lm4nTb+\n><XZ I]t~h=?-_8DUcAy9oQGErV," \
                      "ax1[YP:qJB\"p!fSNe6wksH'@#gK7.O&zR;\\ "[n - 1: n]
    return result

while True:
    encrypted = input('encrypted: ')
    print('decrypted: "' + decrypt(encrypted) + '"')


def decrypt_re(string):
    result = '"'
    data = string.group(1)
    while len(data) > 0:
        n = int(string.group(1)[len(data) - 2: len(data)])
        data = data[:len(data) - 2]
        if n == 99:
            result += '\n'
        elif n != 0:
            result += "0)M3}$lF%*(/|WdjviC{5u2Lm4nTb+\n><XZ I]t~h=?-_8DUcAy9oQGErV," \
                      "ax1[YP:qJB\"p!fSNe6wksH'@#gK7.O&zR;\\ "[n - 1: n]
    return result + '"'

original = Path('C:\\Users\\I\\Desktop\\war3map_refactored.j').read_text()
p = re.compile(r'Pws\("((?:\d{2})+)"\)')
res = p.sub(decrypt_re, original)
refactored = Path('C:\\Users\\I\\Desktop\\war3map_refactored_.j').write_text(res)
