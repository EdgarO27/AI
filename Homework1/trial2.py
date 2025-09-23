

# f(n) = h(n ) + g (n)

'''
g(n) = cost of path from start node to n

h(n) = heuristic function that estimates the cost of the cheapest path from n to the goal 
    NOTE: ADMISSIBLE VS INADMISSBIEL

uses PRIORITY QUEUE
    KNOWN :     Open Set , Fringe , Frontier

    EACH step node with lowest f(x) VALUE IS REMOVED FROM QUEUE
    
    f and g values of its neighbors are updated and added to the queue

    CONTINES unitl a removed node is a goal node ( thus the node with the lowest f value out of all fringe nodes)

    h at the goal is zero
'''


'''
QUEEN moves all 8 directions due to also having DIAGONAL moves
Able to move unlimited squares
'''

#   A* Algorithm
'''
    we need OPEN LIST
            CLOSED LIST
            PRIORITY QUEUE
            G_Score 
            F_score

'''