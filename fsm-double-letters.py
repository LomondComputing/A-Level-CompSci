# FSM for machine that only accepts double letters a, b, c

def validate(s):
    global currentState
    for c in s:
 
        foundTransition = False
        t = 0
        while not foundTransition:
            if transitions[t][0] != currentState and transitions[t][1] != c:
                t += 1
            else:
                foundTransition= True
        if not foundTransition:
            return False
        else:
            nextState = transitions[t][2]
            currentState = nextState
    if currentState == accept:
        return True
    elif currentState == dead:
        return False
    
def printStateTable():
    print('STATE TRANSITION TABLE')
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
        
states = ['S0','S1','S2','S3','D','A']
transitions = [
               ('S0','a','S1'), ('S0','b','S2'), ('S0','c','S3'),
               ('S1','a','A'),  ('S1','b','D'), ('S1','c','D'),
               ('S2','a','D'),  ('S2','b','A'), ('S2','c','D'),
               ('S3','a','D'),  ('S3','b','D'), ('S3','c','A'),
               ('D','a','D'),  ('D','b','D'), ('D','c','D'),
               ('A','a','S1'),  ('A','b','S2'), ('A','c','S3'),
               ]
start = states[0]
accept = states[5]
dead = states[4]
currentState = start

# Main Program  
string = input('Enter a string: ')
result = validate(string)

if result:
    print('The sequence ' + string + ' was accepted by the FSM')
else:
    print('The sequence ' + string + ' was not accepted by the FSM')        
               
#printStateTable()


        
