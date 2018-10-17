# Caesar Cipher

def encode(p,k):
    c = ''
    for char in p:
        x = ord(char)
        y = (x+k)%128
        c += chr(y)
    return  c

def decode(c,k):
    d = ''
    for char in c:
        y = ord(char)
        x = (y-k)%128
        d += chr(x)
    return d
        
plaintext = input('Enter plaintext to encode: ')
key = int(input('Enter key: '))

ciphertext = encode(plaintext, key)

print('Plaintext: ',plaintext)   
print('Ciphertext: ',ciphertext)

decipheredtext = decode(ciphertext, key)

print('Deciphered text: ',decipheredtext)





    
