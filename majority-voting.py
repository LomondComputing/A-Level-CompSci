# Program to demonstrate the majority voting type of error correction
# First 3 bits in data indicate number of repetitions of bits

data = input('Enter the input stream of bits: ')

correctData = ''

reps = int(data[:3],base=2)
print('Number of bit repetitions is: ',reps)

if reps % 2 == 0:
     print('Number of bit repetitions must be ODD ... ')
elif len(data[3:]) % reps == 0:
     print('Data stream is valid ...')
     for bit in range(3,len(data),reps):
          votes = data[bit:bit+reps]
          print('bits = ',votes)
          num0 = votes.count('0')
          num1 = votes.count('1')
          if num0 > num1:
               vote = '0'
          else:
               vote = '1'
          print('Winning bit is: ',vote)
          correctData += vote
     print('Correct data: ',correctData)
          
else:
     print('Data stream is NOT valid!')

