import os, sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: intcode.py filename")

    filename = sys.argv[1]

    if not os.path.exists(filename):
        sys.exit("Error: file '%s' not found" % sys.argv[1])

    f = open(filename)
    program_str = f.read().split(",")
    f.close()

    program = map(int, program_str)
    program_cp = list(program)

    run_intcode(program_cp, 12, 2)

    print program_cp[0]

    for noun in xrange(0,100):
        for verb in xrange(0, 100):
            program_cp = list(program)

            run_intcode(program_cp, noun, verb)

            if program_cp[0] == 19690720:
                print 100 * noun + verb
                break

def run_intcode(program, noun, verb):
    program[1] = noun
    program[2] = verb

    position = 0

    while position < len(program):
        if program[position] == 99:
            break
        if program[position] == 1:
            program[program[position + 3]] = program[program[position+1]] + program[program[position+2]]
        elif program[position] == 2:
            program[program[position + 3]] = program[program[position+1]] * program[program[position+2]]
        position += 4



if __name__ == "__main__":
    main()