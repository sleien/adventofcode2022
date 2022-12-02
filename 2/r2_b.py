# get all input from input.txt
# add 1 for A, 2 for B and 3 for C
# if X add additionally 0
# if Y add additionally 3
# if Z add additionally 6

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
            if line ==   'A X':
                sum += 3
            elif line == 'B X':
                sum += 1
            elif line == 'C X':
                sum += 2
            elif line == 'A Y':
                sum += 4
            elif line == 'B Y':
                sum += 5
            elif line == 'C Y':
                sum += 6
            elif line == 'A Z':
                sum += 8
            elif line == 'B Z':
                sum += 9
            elif line == 'C Z':
                sum += 7
    print(sum)
if __name__ == '__main__':
    main()
