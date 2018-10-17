# FSM for Parking Ticket Machine

def getCoin():
    validCoin = False
    while not validCoin:
        coin = input('Enter 5p, 10p or 20p coin: ')
        if int(coin) in transitions:
            return int(coin)
        else:
            print('That is not a valid coin!')

def printStateTable():
    print('State\t',end='')
    for t in transitions:
        print(t,'\t',end='')
    print()
    for s in states:
        print(s,'\t',end='')
        for t in transitions:
            if s+t >= dead:
                print(dead,'\t',end='')
            else:
                print(s+t,'\t',end='')
        print()
        
states = [0,5,10,15,20,25,30]
transitions = [5,10,20]
start = 0
accept = 25
dead = 30
currentState = start

# Main Program  
coin = getCoin()
while currentState != accept and currentState < dead:
    nextState = currentState + coin
    print(nextState)
    if nextState == accept:
        print('Thank you, that is 25p. Parking ticket is being printed ...')
    elif nextState >= dead:
        print('You have entered too much money!')        
    else:
        print('Please enter another coin ...')
        coin = getCoin()
    currentState = nextState
printStateTable()


        
