import sys
from parser import parse_json

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python turing_machine.py <path_to_json_file> <path_to_input_file>")
        sys.exit(1)

    json_path = sys.argv[1]
    input_path = sys.argv[2]

    turing_json = parse_json(json_path)


tape = [] # Turing machine tape
state = turing_json["initial"] # Variable that represents current state
final = turing_json["final"] # Variable that represents the final state
blank_space = turing_json["white"] # Blank space character for empty spaces on tape
index = 0 # Current index, used for tape navigation
transitions = dict() # Dictionary that stores all turing machine transitions

accepted = False

# Store all transitions in a dictionary
for transition in turing_json["transitions"]:
    transitions[(transition["from"], transition["read"])] = (transition["to"], transition["write"], transition["dir"])

# Read input file and store its contents in the tape
try:
    with open(input_path, "r") as file:
        for line in file:
            tape = list(line.strip())
            break
except FileNotFoundError:
    print(f"Error: The file {input_path} was not found.")
    sys.exit(1)
except IOError:
    print(f"Error: An error occurred while reading the file {input_path}.")
    sys.exit(1)

while(True):
    if(transitions.get((state, tape[index])) == None): # Check if there is a transition for the current state and symbol
        accepted = (state in final) # Check if the current state is the final state list, if so, the input was accepted
        break
    else:
        to, write, direction = transitions[(state, tape[index])]
        tape[index] = write
        state = to
        if direction == "R":
            index += 1
        elif direction == "L":
            index -= 1
        if index < 0:
            tape.insert(0, blank_space)
            index = 0
        elif index >= len(tape):
            tape.append(blank_space)

with open(input_path.split('.')[0]+'.out', "w") as file:
    file.write("".join(tape))

if(accepted):
    print("Accepted")