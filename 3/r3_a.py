# get all input from input.txt

def main():
    # open file
    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [line.strip() for line in lines]
        
        # init sum
        sum = 0
        # loop through lines
        for line in lines:
            # split line in half
            line1 = line[:(len(line)//2)]
            line2 = list(line[(len(line)//2):])
            sim = next(char for char in line2 if char in line1)
            if(ord(sim)>96):
                sum += ord(sim)-96
            else:
                sum += ord(sim)-64+26
        print("Sum: " + str(sum))


if __name__ == '__main__':
    main()
