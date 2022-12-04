# get all input from input.txt

def main():
    # open file
    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [line.strip() for line in lines]
        #split lines by coma
        lines = [line.replace(',', '-').split('-') for line in lines]
        # init sum
        sum = 0
        # loop through lines
        for line in lines:
            line[0] = int(line[0])
            line[1] = int(line[1])
            line[2] = int(line[2])
            line[3] = int(line[3])
            if (line[0] >= line[2] and line[0] <= line[3]) or (line[2] >= line[0] and line[2] <= line[1]):
                sum += 1
        print("Sum: " + str(sum))


if __name__ == '__main__':
    main()
