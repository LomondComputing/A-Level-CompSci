# Program to implement a simple check digit error correction

def sendMessage(text):
     message = []
     total = 0
     for char in text:
          code = ord(char)
          message.append(code)
          total += code
     checkDigit = total%128
     message.append(checkDigit)
     print('Total: ',total)
     print('Check digit: ',checkDigit)
     print('Transmitted message: ',message)
     return message

def receiveMessage(text):
     checkDigit = text[-1]
     total = 0
     for code in range(len(text)-1):
          total += text[code]
     print('Total: ',total)
     print('Check digit: ',checkDigit)
     if total%128 == checkDigit:
          return True
     else:
          return False

message = input('Enter message to send: ')
messageWithCheckDigit = sendMessage(message)
if receiveMessage(messageWithCheckDigit):
     print('Message was correctly received')
else:
     print('Error with message transmission ...')
