import os, sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: fuel_counter_upper.py filename")

    filename = sys.argv[1]

    if not os.path.exists(filename):
        sys.exit("Error: file '%s' not found" % sys.argv[1])

    f = open(filename)

    total_fuel = 0
    total_additional_fuel = 0

    for line in f: 
        module_fuel = int(line) / 3 - 2
        total_fuel += module_fuel
        total_additional_fuel += module_fuel

        while module_fuel > 0:
            module_fuel = module_fuel / 3 - 2
            module_fuel = (module_fuel if module_fuel > 0 else 0)
            total_additional_fuel += module_fuel

    f.close()

    print "Total fuel: %d \nTotal additional fuel: %d" % (total_fuel, total_additional_fuel)

if __name__ == "__main__":
    main()
