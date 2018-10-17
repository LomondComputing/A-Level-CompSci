# Program to implement a Parity Check

def addParity(p,bits):
    num1s = bits.count('1')
    print('Number of 1s in message: ',num1s)
    if not p:
        rem = 0
    else:
        rem = 1
    if num1s % 2 == rem:
        parityBit = '0'
    else:
        parityBit = '1'
    print('Adding parity bit: ',parityBit)
    return parityBit + bits

message = input('Enter a message to send: ')
parity = int(input('Enter parity type (0=Even, 1=Odd: '))
binary = ''

for char in message:
    code = ord(char)
    binary += format(code,'b')

print('Binary of message: ',binary)
newMessage = addParity(parity, binary)
print('Binary with parity bit: ',newMessage)

