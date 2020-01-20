"""Calculate DnD rolls from a string, example: \"10d6 + 4d8 + 10\" """

import random
import argparse

def parse_string(input):
    # This was a one-liner until I remembered subtraction existed
    terms = [term.replace(" ", "") for term in input.split('+')]
    ret = []
    for term in terms:
        if "-" in term:
            terms.remove(term)
            (term1, term2) = term.split("-")
            term2 = "-" + term2
            if not term1 == "":
                ret.append(term1)
            ret.append(term2)
        else:
            ret.append(term)
    return ret

def parse_term(die_str):
    try:
        if die_str.startswith('d'):
            return roll_dice(1,int(die_str[1:]))
        elif die_str.isdigit(): 
            value = int(die_str)
            return (value, [value], f"{value}", value)
        elif "-" in die_str and die_str[1:].isdigit():
            value = int(die_str[1:])
            return (-value, [-value], f"-{value}", -value)
        else:
            (count, sides) = die_str.upper().split('D')
            return roll_dice(int(count), int(sides))
    except:
        raise Exception('Invalid die string ' + die_str);

def roll_dice(count, sides):
    dice = [random.randint(1, sides) for i in range(count)]
    return (sum(dice), dice, f"{count}d{sides}", roll_average(count, sides))

def roll_average(count, sides):
    return count * (sides + 1) / 2 

def roll_string(input):
    terms = parse_string(input)
    data = []
    for term in terms:
        data.append(parse_term(term))
    data = list(zip(*data))
    return (sum(data[0]),
            data[1],
            " + ".join(data[2]),
            sum(data[3])
            )

def main():
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument("roll", nargs='*', help="string for dice roll", default=None)
    roll = parser.parse_args().roll
    if not roll == []:
        print(roll_string("".join(roll)))
    while True:
        print("> ", end="")
        roll = input()
        if roll.upper() == "EXIT" or roll.upper() == "QUIT":
            break
        result = roll_string(roll)
        die_rolls= result[1][0] if len(result[1])==1 else result[1]
        print(f"{result[0]}\t\t\t\t\t\t\t\t\t{die_rolls} {result[2]} {result[3]}")

if __name__ == "__main__":
    main()