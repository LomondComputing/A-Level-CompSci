numBits = int(input('How many bits to right of binary point? '))

for i in range(2^numBits):
     code = bin(i)[2:]
     zeros = 4-len(code)
     code = '0'*zeros + code
     total = 0
     for b in range(1,len(code)+1):
          value = 1/(b+1)
          
          

