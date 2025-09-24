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


queens = [1] * 8

#THIS CREATES 8 LIST INSIDE ONE LIST 

GRID = []

for _ in range(8):
    GRID.append([0]* 8)

# WE START OUR PROGRAM FROM HERE TO ITERATE THROUGH THE QUEENS LIST WHO ARE ASSIGNED TO 1
def start(queens):
    k,j = 0,0
    for i in range(len(queens)):
        #If conditional only true once we start the function otherwise it always goes to else 
        if i == 0:
            GRID[0][0] = queens[0]
        #Else statement/ conditional places in the next COL like a counter plus 1 and row is also incremented by 1 
        else:
            GRID[k][j] = queens[i]

            if valid_Placement(k,j) is True:
                k+= 1
                j+= 1
            else:
                j+= 1
                valid_Placement(k,j)
        k += 1
        j += 1
        

#As we excute start function we use valid placement to check for if queens attack each other designated by 1 in the CHESS GRID

#WE RETURN A BOOL 
def valid_Placement(k,j):
    #We USE INDEX K and J to check if current placement is valid 
    ATTACK = True
    
    return True

#USING EUCLIDEAN DISTANCE TO CHECK ALL 8 SIDES

# COST FOR EACH MOVE IS 1
#ULTIMATE GOAL IS TO GET H(N) = 0
def heuristic(node):
        D = 1
        dx = abs(node.x - goal.x)
        dy = abs(node.y - goal.y)
        return D * sqrt(dx * dx + dy * dy)

start(queens)

print(GRID)