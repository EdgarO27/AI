'''
8 QUEENS

Using A* ( A star ) algorithm

    What is A* ?
        f(n) = g ( n ) + h ( n )

    g ( n ) : being the cost from START to N 

    h ( n ) : being the cost from N to GOAL STATE ( NO 2 QUEENS ATTACK EACH OTHER)

    How does a QUEEN Move ?

        It moves all 8 directions : UP , DOWN , LEFT , RIGHT , DIAGONAL ( 4 SIDES )

    What Hueristic to pick for this problem?

        I can use Euclidean          
'''
#Create a Priority Queue

#for visted nodes

#non visited nodes

# def placement(queens):

    # place queen in the first square at [0,0]

    #Assign queen to all_nodes[0] with a 1 to represent its occucpied

    #Keep looping till you exhaust all queen placements

    #check if placement satisfies conditions like no queen is attacking and f ( n ) = g ( n ) + h ( n )


#Creating the graph 
from math import sqrt

QUEENS_NUM = 8

#HELPS AVOID HAVING THE SAME OBJECT 
#They all have own ID 
queens = [1 for i in range(QUEENS_NUM)]

#THIS CREATES 8 LIST INSIDE ONE LIST 

GRID = []

for _ in range(len(queens)):
    GRID.append([0]* 8)

# WE START OUR PROGRAM FROM HERE TO ITERATE THROUGH THE QUEENS LIST WHO ARE ASSIGNED TO 1
def start(queens):
    k,j = 1,1
    for i in range(0,len(GRID),1):
        
        #If conditional only true once we start the function otherwise it always goes to else 
        if i == 0:
            GRID[0][0] = queens[0]
        #Else statement/ conditional places in the next COL like a counter plus 1 and row is also incremented by 1 
        else:
            GRID[k][j] = queens[i]

            if valid_Placement(k,j) is True:
                k+= 1
                j+= 1
                print("True excuted: Valid function")
            else:
                j+= 1
                valid_Placement(k,j)
                print("Only excuted: Valid Function is False ")
    
    
        

#As we excute start function we use valid placement to check for if queens attack each other designated by 1 in the CHESS GRID

#WE RETURN A BOOL IF current queen and placement is valid 
def valid_Placement(k,j):
    state = True

    #USE A WHILE LOOP 

        # check all 8 directions with while 
        # allows us to stay in true state until we find a false 
        # Minimze code with checking all directions 
    while k > QUEENS_NUM and j > QUEENS_NUM:
        #We still check first queen at [0][0] to ensure safety of the one not being moved
        if GRID[k][j] == 0:
            state = True
        else:
            state = False

    #NORTH YOU DECREMENT INDEX
        #COL , ROW -1
             #SOUTH YOU INCREMENT 
                #COL  , ROW + 1
                    #EAST YOU DECREMENT 
                        #ROW - 1, COL
                            #WEST YOU INCREMENT
                                #ROW + 1, COL
                                    #NORTH, WEST YOU DO A MIX OF BOTH
                                        #N : COL - 1 
                                            #W : ROW + 1
                                                #NORTH, EAST YOU DO MIX OF BOTH
                                                    #N: COL - 1
                                                    #W: ROW - 1
                                                        #SOUTH , WEST 
                                                            #S: COL + 1
                                                                #W: ROW + 1
                                                                    #SOUTH , EAST
                                                                        #S: COL + 1
                                                                            #E: ROW - 1    
    
    return state



'''

CHECK DIRECTIONS 

FOR EXAMPLE:
            QUEEN IN POSITION AT 2,2


            SO IF WE CHECK UP 
'''
#USING EUCLIDEAN DISTANCE TO CHECK ALL 8 SIDES

# COST FOR EACH MOVE IS 1
#ULTIMATE GOAL IS TO GET H(N) = 0
# def heuristic(node):
#         D = 1
#         dx = abs(node.x - goal.x)
#         dy = abs(node.y - goal.y)
#         return D * sqrt(dx * dx + dy * dy)

start(queens)





for i in range(len(GRID)):
    
    print(GRID[i])
    print()

