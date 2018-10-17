# Program to implement a simple Hash Function

# Initalise Hash Table

maxSize = int(input('How big is the Hash Table? '))
hashTable = [ None for i in range(maxSize) ]
print('Hash Table: ',hashTable)

def hashF(string):
     #global hashTable
     total = 0
     collision = True
     for char in string:
          total += ord(char)
     pos = total % maxSize
     print(pos)
     while collision and pos < maxSize:
          if hashTable[pos] is None:
               hashTable[pos] = string
               collision = False
          else:
               print('Collision detected ..')
               pos += 1
     if pos == maxSize:
          print('Hash Table is full!')

stop = False
while not stop:
     data = input('Enter: data value to store (\'stop\'to end): ' )
     if data.lower() != 'stop':
          hashF(data)
          print('Hash Table: ',hashTable)
     else:
          stop = True
