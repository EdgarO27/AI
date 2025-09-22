
import random
import math
from typing import Tuple 

#init Queens 
'''
We will randomize the placement of 8 queens

list 
'''
Queens = []
for i in range(8):
    #allows distinct objects created so it doesnt mess with access
    Queens.append([random.randint(0,7) for i in range(2)])


#Make our game board grid

board = []
for _ in range(8):
    row = [0 for i in range(8)] # Initialize each square as None (empty)
    board.append(row)

for i in board:
    print(i)
    print()
    
    
'''
Placement of our Queens is to go by ROW 
    1.  Go by row and check if Queen is attacking any other queen
    2. If no attack Add another queen from our Queens list of list and place where it has the location of it
    3. 
'''
    
#USING EUCLID due to diagonal moves from QUEENS
#MODIFY TO Handle MATRIX GRID 

def calculate_heuristic(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
    """
    Calculate the estimated distance between two points using Euclidean distance.
    """
    x1, y1 = pos1
    x2, y2 = pos2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)



#CHECKS FOR OTHER QUEENS ON BOARD
'''
modify to handle matrix 
'''

def get_valid_neighbors(grid: list, position: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Get all valid neighboring positions in the grid.
    
    Args:
        grid: 2D numpy array where 0 represents walkable cells and 1 represents obstacles
        position: Current position (x, y)
    
    Returns:
        List of valid neighboring positions
    """
    x, y = position
    rows, cols = grid.shape
    
    # All possible moves (including diagonals)
    possible_moves = [
        (x+1, y), (x-1, y),    # Right, Left
        (x, y+1), (x, y-1),    # Up, Down
        (x+1, y+1), (x-1, y-1),  # Diagonal moves
        (x+1, y-1), (x-1, y+1)
    ]
    
    return [
        (nx, ny) for nx, ny in possible_moves
        if 0 <= nx < rows and 0 <= ny < cols  # Within grid bounds
        and grid[nx, ny] == 0                # Not an obstacle
    ]
    

http://eightqueen.becher-sundstroem.de/

#A STAR ALGORITHM

'''

MODIFY TO HANDLE LIST MATRIX aand search in according to COLUMNS


'''
    
def find_path(grid: np.ndarray, start: Tuple[int, int], 
              goal: Tuple[int, int]) -> List[Tuple[int, int]]:
    # """
    # Find the optimal path using A* algorithm.
    
    # Args:
    #     grid: 2D numpy array (0 = free space, 1 = obstacle)
    #     start: Starting position (x, y)
    #     goal: Goal position (x, y)
    
    # Returns:
    #     List of positions representing the optimal path
    # """
    # Initialize start node
    start_node = create_node(
        position=start,
        g=0,
        h=calculate_heuristic(start, goal)
    )
    
    # Initialize open and closed sets
    open_list = [(start_node['f'], start)]  # Priority queue
    open_dict = {start: start_node}         # For quick node lookup
    closed_set = set()                      # Explored nodes
    
    while open_list:
        # Get node with lowest f value
        _, current_pos = heapq.heappop(open_list)
        current_node = open_dict[current_pos]
        
        # Check if we've reached the goal
        if current_pos == goal:
            return reconstruct_path(current_node)
            
        closed_set.add(current_pos)
        
        # Explore neighbors
        for neighbor_pos in get_valid_neighbors(grid, current_pos):
            # Skip if already explored
            if neighbor_pos in closed_set:
                continue
                
            # Calculate new path cost
            tentative_g = current_node['g'] + calculate_heuristic(current_pos, neighbor_pos)
            
            # Create or update neighbor
            if neighbor_pos not in open_dict:
                neighbor = create_node(
                    position=neighbor_pos,
                    g=tentative_g,
                    h=calculate_heuristic(neighbor_pos, goal),
                    parent=current_node
                )
                heapq.heappush(open_list, (neighbor['f'], neighbor_pos))
                open_dict[neighbor_pos] = neighbor
            elif tentative_g < open_dict[neighbor_pos]['g']:
                # Found a better path to the neighbor
                neighbor = open_dict[neighbor_pos]
                neighbor['g'] = tentative_g
                neighbor['f'] = tentative_g + neighbor['h']
                neighbor['parent'] = current_node
    
    return []  # No path found