import os, sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: intcode.py filename")

    filename = sys.argv[1]

    if not os.path.exists(filename):
        sys.exit("Error: file '%s' not found" % sys.argv[1])

    f = open(filename)

    program_str = f.read().split(",")
    program = map(int, program_str)

    f.close()

    program[1] = 12
    program[2] = 2

    position = 0
    while position < len(program):
        if program[position] == 99:
            break
        if program[position] == 1:
            program[program[position + 3]] = program[program[position+1]] + program[program[position+2]]
        elif program[position] == 2:
            program[program[position + 3]] = program[program[position+1]] * program[program[position+2]]
        position += 4

    print program[0]

if __name__ == "__main__":
    main()