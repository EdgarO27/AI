


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

            function heuristic(node) =
        dx = abs(node.x - goal.x)
        dy = abs(node.y - goal.y)
        return D * sqrt(dx * dx + dy * dy)
'''


#Creating the graph 
queens = [1] * 8

# Make 8 queens with representation ( char, number )
# for i in range(8)

#Create a Priority Queue

#for visted nodes

#non visited nodes

# def placement(queens):

    # place queen in the first square at [0,0]

    #Assign queen to all_nodes[0] with a 1 to represent its occucpied

    #Keep looping till you exhaust all queen placements

    #check if placement satisfies conditions like no queen is attacking and f ( n ) = g ( n ) + h ( n )





#THIS CREATES 8 LIST INSIDE ONE LIST 

GRID = []

# RUN FOR LOOP FIRST TO TEST IF I CAN JUST ADD 


for _ in range(8):
    GRID.append([0]* 8)



# HOW IS THE ITERATION GOING TO WORK ?

    # Start by placing first QUEEN IN COL 0/ OR OUR SO CALLED FIRST COLUMN AND FIRST ROW [0]
    # Go to next col and ROW + 1
    #check placement if queen is being attacked so if it check all diagonal rows and sees a 1 it will then stay in that column and do row + 1



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
            valid_Placement(k,j)
        k += 1
        j += 1
        

#As we excute start function we use valid placement to check for if queens attack each other designated by 1 in the CHESS GRID
def valid_Placement(place):
    #IF QUEEN IS 0 THEN WE JUST PLACE IT IN THE FIRST CORNER SPOT GRID[0][0]
    if GRID[0][0] is 0:
        GRID[0][0] = queens[0]

    return True

start(queens)

print(GRID)