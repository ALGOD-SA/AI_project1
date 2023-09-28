import csv
from search import aStarSearch
from eightpuzzle2 import EightPuzzleSearchProblem, createRandomEightPuzzle, EightPuzzleState
from Heuristics import h1, h2, h3, h4



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
    h1_array = [0,0,0]
    h2_array = [0,0,0]
    h3_array = [0,0,0]
    h4_array = [0,0,0]
    h1_results =[]
    h2_results =[]
    h3_results =[]
    h4_results =[]

    # Read scenarios from the CSV file
    with open('scenarios.csv', 'r') as file:
        reader = csv.reader(file)
        numberOfRows=0
        for row in reader:
            # Convert the flattened puzzle from the CSV into a 2D list
            puzzle = [list(map(int, row[i:i+3])) for i in range(0, 9, 3)]
            flattened_puzzle = [tile for row in puzzle for tile in row]
            puzzleState = EightPuzzleState(flattened_puzzle)
            print(flattened_puzzle)
            problem = EightPuzzleSearchProblem(puzzleState)
            numberOfRows +=1
          
            for heuristic in [h1, h2, h3, h4]:
                actions, depth, expanded_nodes, max_fringe_size = aStarSearch(problem, heuristic)
                heuristic_name = heuristic.__name__
                results.append((heuristic_name, depth, expanded_nodes, max_fringe_size))
                if(heuristic==h1):
                    h1_array[0]+=depth
                    h1_array[1]+=expanded_nodes
                    h1_array[2]+=max_fringe_size

                elif(heuristic==h2):
                    h2_array[0]+=depth
                    h2_array[1]+=expanded_nodes
                    h2_array[2]+=max_fringe_size
                elif(heuristic==h3):
                    h3_array[0]+=depth
                    h3_array[1]+=expanded_nodes
                    h3_array[2]+=max_fringe_size
                elif(heuristic==h4):
                    h4_array[0]+=depth
                    h4_array[1]+=expanded_nodes
                    h4_array[2]+=max_fringe_size

    for i in range(3):
        h1_array[i]/=numberOfRows
        h2_array[i]/=numberOfRows
        h3_array[i]/=numberOfRows 
        h4_array[i]/=numberOfRows     
           
    h1_results.append(("h1: ",h1_array[0],h1_array[1],h1_array[2]))            
    h2_results.append(("h2: ",h2_array[0],h2_array[1],h2_array[2]))            
    h3_results.append(("h3: ",h3_array[0],h3_array[1],h3_array[2]))            
    h4_results.append(("h4: ",h4_array[0],h4_array[1],h4_array[2]))            

    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Heuristic", "Depth", "Expanded Nodes", "fringe size"])
        writer.writerows(results)
        writer.writerow(["Heuristice","Average Depth", "Average Expanded Nodes", "Average fringe size"])
        writer.writerows(h1_results)
        writer.writerows(h2_results)
        writer.writerows(h3_results)
        writer.writerows(h4_results)

        

if __name__ == "__main__":
    generate_puzzles_to_csv(40)
    main()