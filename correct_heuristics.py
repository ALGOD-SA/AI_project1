'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
current_state = [[2, 7, 8], [0, 1, 4], [6, 5, 3]] 


def manhattanDistance( xy1, xy2 ):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )

def h1(state, problem= None):
        goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        misplaced = 0
        for i in range(3):
            for j in range(3):
                tile=state[i][j]
                if tile != 0:
                    goal_row, goal_col = divmod(tile, 3)
                    if(i!=goal_row or j!=goal_col):
                        misplaced += 1
        return misplaced
print(h1(current_state))

def h2(state, problem=None):
        goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] 
        distance = 0
        for i in range(3):
            for j in range(3):
                tile = state[i][j]
                if tile != 0:
                    goal_row, goal_col = divmod(tile, 3)
                    distance += ((i - goal_row) ** 2 + (j - goal_col) **2)**0.5
        return distance

#print(h2(current_state))

def h3(state, problem=None):
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] 
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0: 
                goal_row, goal_col = divmod(tile, 3) 
                t1 = (i,j)
                t2=(goal_row,goal_col)
                distance +=  manhattanDistance(t1,t2)
                print(distance)
    return distance
#h3(current_state)

def h4(state, problem=None) :
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] 
    h4 = 0
    for i in range(3):  
        for j in range(3): 
            tile = state[i][j]
            if (tile !=0):
                goal_row,goal_column=divmod(tile,3)
                if(i != goal_column):
                    h4 += 1
                if(j != goal_row):
                    h4 += 1 
    return h4

