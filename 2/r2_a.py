# get all input from input.txt
# add 1 for X, 2 for Y and 3 for Z
# A and Y or B and Z or C and X add additionally 6
# A and Z or B and X or C and Y add additionally 0
# A and X or B and Y or C and Z add additionally 3

def main():
    # open file
    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [line.strip() for line in lines]
        # sum lines between empty lines and get highest sum
        
        # init sum
        sum = 0

        for line in lines:
            # if line is empty
            if line == 'A X':
                sum += 4
            elif line == 'B Y':
                sum += 5
            elif line == 'C Z':
                sum += 6
            elif line == 'A Y':
                sum += 8
            elif line == 'B Z':
                sum += 9
            elif line == 'C X':
                sum += 7
            elif line == 'A Z':
                sum += 3
            elif line == 'B X':
                sum += 1
            elif line == 'C Y':
                sum += 2
    print(sum)
if __name__ == '__main__':
    main()
