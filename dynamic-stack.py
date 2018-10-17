# Dynamic Stack Implementation

# To initialise the stack
def initialise():
     global top, size, s
     top = -1
     size = 0
     s = []

# To test for an empty stack
def isEmpty():
     global size
     return size == 0

# To push a new item on the stack
def push(newItem):
     global top, s, size
     print('Adding',newItem,'to top of stack ..')
     s.append(newItem)
     top += 1
     size += 1

# To pop an item from the top of stack
def pop():
     global top, size, s
     if isEmpty():
          print('Stack is empty')
          item = None
     else:
          item = s.pop()
          print('Popping',item,'from top of stack ..')
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
     for item in range(top,-1,-1):
          print(s[item])


# Main program to test stack
initialise()
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
pop()
display()




