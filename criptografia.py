nome = input('Digte um texto ').upper()
for char in nome:
    code = ord(char) + 1
    cipher = chr(code)
    print(cipher, end='')




