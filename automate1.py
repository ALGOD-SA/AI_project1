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

    # Read scenarios from the CSV file
    with open('scenarios.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Convert the flattened puzzle from the CSV into a 2D list
            puzzle = [list(map(int, row[i:i+3])) for i in range(0, 9, 3)]
            flattened_puzzle = [tile for row in puzzle for tile in row]
            puzzleState = EightPuzzleState(flattened_puzzle)
            print(flattened_puzzle)
            problem = EightPuzzleSearchProblem(puzzleState)
            
          
            for heuristic in [h1, h2, h3, h4]:
                actions, depth, expanded_nodes, max_fringe_size = aStarSearch(problem, heuristic)
                heuristic_name = heuristic.__name__
                results.append((heuristic_name, depth, expanded_nodes, max_fringe_size))

    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Heuristic", "Depth", "Expanded Nodes", "fringe size"])
        writer.writerows(results)

if __name__ == "__main__":
    generate_puzzles_to_csv(5)
    main()