# Linear Queue Implementation

# To initialise the queue
def initialise():
     global front, rear, size, maxSize, q
     front = 0
     rear = -1
     size = 0
     maxSize = 6
     q = []
     for item in range(maxSize):
          q.append(None)


# To test for an empty queue
def isEmpty():
     global size
     return size == 0

# To test for a full queue
def isFull():
     global size
     return size == maxSize

# To add an element to the queue
def enqueue(newItem):
     global rear, maxSize, q, size
     if isFull():
          print('Queue is full!')
     else:
          print('Adding',newItem,'to rear of queue ..')
          rear = rear+1
          q[rear] = newItem
          size += 1

# To remove an item from the queue
def dequeue():
     global front, size, q, maxSize, rear
     if isEmpty():
          print('Queue is empty')
          item = None
     else:
          item = q[front]
          print('Removing',item,'from front of queue ..')
          for item in range(front,rear+1):
               if item != rear:
                    q[item] = q[item+1]
               else:
                    q[item] = None
          rear -= 1
          size -= 1
     return item

# To see what item is at the front of the queue
def peek():
     global q, front
     if isEmpty():
          print('Queue is empty')
          item = None
     else:
          item = q[front]
     print('The item at the front of queue is:',item)

# To display the queue visually
def display():
     global front, rear, q         
     for item in range(front,maxSize):
          print(q[item],'\t',end='')       
     print('')


# Main program to test queue
initialise()
display()
enqueue('Ben')
display()
enqueue('Sue')
enqueue('Tom')
enqueue('Pam')
enqueue('Wes')
enqueue('Sal')
display()
dequeue()
display()
peek()
enqueue('Huw')
display()
enqueue('Zoe')
peek()


