import os, sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: manhattan.py filename")

    filename = sys.argv[1]

    if not os.path.exists(filename):
        sys.exit("Error: file '%s' not found" % sys.argv[1])

    f = open(filename)

    wire_1 = f.readline().split(",")
    wire_2 = f.readline().split(",")

    f.close()

    wire_1_coords, wire_2_coords = [], []

    current_location = [0, 0]
    for direction in wire_1:
        add_coords(wire_1_coords, direction, current_location)

    current_location = [0, 0]
    for direction in wire_2:
        add_coords(wire_2_coords, direction, current_location)

    intersections = set(wire_1_coords).intersection(set(wire_2_coords))

    min_manhattan_distance = min([sum(coord) for coord in [(abs(intersection[0]), abs(intersection[1])) for intersection in intersections]])
    print min_manhattan_distance

def add_coords(coords, direction, current_location):
    if direction[0] == 'L':
        for dist in xrange(0, int(direction[1:])):
            current_location[0] = current_location[0] - 1
            coords.append(tuple(current_location))
    elif direction[0] == 'R':
        for dist in xrange(0, int(direction[1:])):
            current_location[0] = current_location[0] + 1
            coords.append(tuple(current_location))
    elif direction[0] == 'D':
        for dist in xrange(0, int(direction[1:])):
            current_location[1] = current_location[1] - 1
            coords.append(tuple(current_location))
    elif direction[0] == 'U':
        for dist in xrange(0, int(direction[1:])):
            current_location[1] = current_location[1] + 1
            coords.append(tuple(current_location))

if __name__ == "__main__":
    main()