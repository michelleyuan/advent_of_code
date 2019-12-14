import os, sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Usage: guess_password.py lower_bound upper_bound")

    lower_bound = int(sys.argv[1])
    upper_bound = int(sys.argv[2])

    num_passwords = 0
    num_passwords_too = 0

    for number in xrange(lower_bound, upper_bound+1):
        number_str = str(number)
        if has_same_adjacent(number_str) and is_strictly_increasing(number_str):
            num_passwords += 1

            if has_a_double(number_str):
                num_passwords_too += 1

    print num_passwords
    print num_passwords_too


def has_same_adjacent(number_str):
    for digit in xrange(0, len(number_str)-1):
        if number_str[digit] == number_str[digit + 1]:
            return True
    return False

def has_a_double(number_str):
    for digit in xrange(1, len(number_str)-2):
        if number_str[digit] == number_str[digit + 1] and number_str[digit] != number_str[digit + 2] and number_str[digit] != number_str[digit - 1]:
            return True
    if number_str[0] == number_str[1] and number_str[0] != number_str[2]:
        return True
    if number_str[-1] == number_str[-2] and number_str[-1] != number_str[-3]:
        return True
    return False

def is_strictly_increasing(number_str):
    for digit in xrange(0, len(number_str)-1):
        if number_str[digit] > number_str[digit + 1]:
            return False
    return True


if __name__ == "__main__":
    main()