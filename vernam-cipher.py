# One-time pad

import random

plaintext = input('Enter message to encode: ')

print('Generating random numbers ...')
keyList = [ random.randint(32,127) for i in range(len(plaintext)+1) ]
key = ''
ciphertext = ''

print('Creating one-time-pad...')
for n in keyList:
    key += chr(n)

print('One-time-pad: ',key)

print('Creating ciphertext...')
for i in range(len(plaintext)):
    x = ord(plaintext[i])
    y = ord(key[i])
    ciphertext += chr(x ^ y)

print('Plaintext: ',plaintext)
print('Ciphertext: ',ciphertext)

decodedplaintext = ''
for i in range(len(ciphertext)):
      x = ord(ciphertext[i])
      y = ord(key[i])
      decodedplaintext += chr(x ^ y)

print('Decoded plaintext: ',decodedplaintext)
      




    
