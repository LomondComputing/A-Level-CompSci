# Static Stack Implementation

# To initialise the static stack
def initialise(n):
     global top, size, maxSize, s
     top = -1
     size = 0
     maxSize = n
     s = []
     for item in range(maxSize):
          s.append(None)


# To test for an empty stack
def isEmpty():
     global size
     return size == 0

# To test for a full stack
def isFull():
     global size
     return size == maxSize

# To push a new item on the stack
def push(newItem):
     global top, maxSize, s, size
     if isFull():
          print('Stack overflow!')
     else:
          print('Adding',newItem,'to top of stack ..')
          top += 1
          s[top] = newItem
          size += 1

# To pop an item from the top of stack
def pop():
     global top, size, s, maxSize
     if isEmpty():
          print('Stack is empty')
          item = None
     else:
          item = s[top]
          print('Popping',item,'from top of stack ..')
          s[top] = None
          top -= 1
          size -= 1
     return item

# To see what item is at the top of stack
def peek():
     global s, top
     if isEmpty():
          print('Stack is empty')
          item = None
     else:
          item = s[top]
     print('The item at the top of stack is:',item)

# To display the stack visually
def display():
     global top, s
     print('STACK:')
     for item in range(maxSize-1,-1,-1):
          print(s[item])


# Main program to test stack
initialise(6)
push('Ben')
display()
push('Sam')
push('Tim')
push('Sue')
push('Lim')
push('Wes')
display()
push('Ana')
peek()
pop()
display()




