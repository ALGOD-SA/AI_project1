import csv
from search import aStarSearch,depthFirstSearch, breadthFirstSearch, uniformCostSearch
from eightpuzzle2 import EightPuzzleSearchProblem, createRandomEightPuzzle, EightPuzzleState
from Heuristics import h3


def generate_puzzles_to_csv(num_puzzles, filename='scenarios.csv'):

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        for _ in range(num_puzzles):
            puzzle_state = createRandomEightPuzzle(25)
            # Flatten the 2D puzzle state into a single row
            flattened_puzzle = [tile for row in puzzle_state.cells for tile in row]
            writer.writerow(flattened_puzzle)


def main():
    results = []
    AStar_array = [0,0,0]
    Bfs_array = [0,0,0]
    Dfs_array = [0,0,0]
    Ucs_array = [0,0,0]
    AStar_results =[]
    Bfs_results =[]
    Dfs_results =[]
    Ucs_results =[]
    # Read scenarios from the CSV file
    numberOfRows =0
    with open('scenarios.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Convert the flattened puzzle from the CSV into a 2D list
            puzzle = [list(map(int, row[i:i+3])) for i in range(0, 9, 3)]
            flattened_puzzle = [tile for row in puzzle for tile in row]
            puzzleState = EightPuzzleState(flattened_puzzle)
            print(flattened_puzzle)
            problem = EightPuzzleSearchProblem(puzzleState)
            numberOfRows+=1
            actions, depth, expanded_nodes, max_fringe_size = aStarSearch(problem, h3)
            results.append(("A* with h3", depth, expanded_nodes, max_fringe_size))
            AStar_array[0]+=depth
            AStar_array[1]+=expanded_nodes
            AStar_array[2]+=max_fringe_size

                

            actions, depth, expanded_nodes, max_fringe_size = depthFirstSearch(problem)
            results.append(("depthFirstSearch", depth, expanded_nodes, max_fringe_size))
            Dfs_array[0]+=depth
            Dfs_array[1]+=expanded_nodes
            Dfs_array[2]+=max_fringe_size

            actions, depth, expanded_nodes, max_fringe_size = breadthFirstSearch(problem)
            results.append(("breadthFirstSearch", depth, expanded_nodes, max_fringe_size))
            Bfs_array[0]+=depth
            Bfs_array[1]+=expanded_nodes
            Bfs_array[2]+=max_fringe_size

            actions, depth, expanded_nodes, max_fringe_size = uniformCostSearch(problem)
            results.append(("uniformCostSearch", depth, expanded_nodes, max_fringe_size))
            Ucs_array[0]+=depth
            Ucs_array[1]+=expanded_nodes
            Ucs_array[2]+=max_fringe_size
    for i in range(3):
        AStar_array[i]/=numberOfRows
        Bfs_array[i]/=numberOfRows
        Dfs_array[i]/=numberOfRows 
        Ucs_array[i]/=numberOfRows     
           
    AStar_results.append(("A* with h3: ",AStar_array[0],AStar_array[1],AStar_array[2]))            
    Bfs_results.append(("Bfs: ",Bfs_array[0],Bfs_array[1],Bfs_array[2]))            
    Dfs_results.append(("Dfs: ",Dfs_array[0],Dfs_array[1],Dfs_array[2]))            
    Ucs_results.append(("Ucs: ",Ucs_array[0],Ucs_array[1],Ucs_array[2]))     
    with open('results_comparison.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Algorithm", "Depth", "Expanded Nodes", "fringe size"])
        writer.writerows(results)
        writer.writerow(["Search methods","Average Depth", "Average Expanded Nodes", "Average fringe size"])
        writer.writerows(AStar_results)
        writer.writerows(Bfs_results)
        writer.writerows(Dfs_results)
        writer.writerows(Ucs_results)

if __name__ == "__main__":
    generate_puzzles_to_csv(5)
    main()

