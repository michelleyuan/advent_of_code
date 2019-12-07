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
    length_1, length_2 = {}, {}

    current_location = [0, 0]
    dist_traveled = 0
    for direction in wire_1:
        add_coords(wire_1_coords, direction, current_location, dist_traveled, length_1)
        # ints are immutable so updating total dist traveled before moving to next direction 
        dist_traveled += abs(int(direction[1:]))

    current_location = [0, 0]
    dist_traveled = 0
    for direction in wire_2:
        add_coords(wire_2_coords, direction, current_location, dist_traveled, length_2)
        dist_traveled += abs(int(direction[1:]))

    intersections = set(wire_1_coords).intersection(set(wire_2_coords))

    min_manhattan_distance = min([sum(coord) for coord in [(abs(intersection[0]), abs(intersection[1])) for intersection in intersections]])
    print min_manhattan_distance

    min_wire_length = min([length_1[coord] + length_2[coord] for coord in intersections])
    print min_wire_length

def add_coords(coords, direction, current_location, dist_traveled, length):
    if direction[0] == 'L':
        for dist in xrange(0, int(direction[1:])):
            current_location[0] = current_location[0] - 1
            coords.append(tuple(current_location))
            dist_traveled += 1
            length[tuple(current_location)] = dist_traveled
    elif direction[0] == 'R':
        for dist in xrange(0, int(direction[1:])):
            current_location[0] = current_location[0] + 1
            coords.append(tuple(current_location))
            dist_traveled += 1
            length[tuple(current_location)] = dist_traveled
    elif direction[0] == 'D':
        for dist in xrange(0, int(direction[1:])):
            current_location[1] = current_location[1] - 1
            coords.append(tuple(current_location))
            dist_traveled += 1
            length[tuple(current_location)] = dist_traveled
    elif direction[0] == 'U':
        for dist in xrange(0, int(direction[1:])):
            current_location[1] = current_location[1] + 1
            coords.append(tuple(current_location))
            dist_traveled += 1
            length[tuple(current_location)] = dist_traveled

if __name__ == "__main__":
    main()