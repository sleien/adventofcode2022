# get all input from input.txt

def main():
    # open file
    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [list(line.strip()) for line in lines]
        for q in range(len(lines)):
            for w in range(len(lines[q])):
                lines[q][w] = int(lines[q][w])
        linez = []
        for line in lines:
            linez.append([-1 for i in line])
        sum = 0
        view = 0
        highest = -1
        for i in range(len(lines)):
            highest = -1
            for j in range(len(lines[i])):
                if lines[i][j] > highest:
                    highest = lines[i][j]
                    linez[i][j] = lines[i][j]
            highest = -1
            for j in range(len(lines[i])):
                if lines[i][len(lines[i]) - 1 - j] > highest:
                    highest = lines[i][len(lines[i]) - 1 - j]
                    linez[i][len(lines[i]) - 1 - j] = lines[i][len(lines[i]) - 1 - j]
        for i in range(len(lines[0])):
            highest = -1
            for j in range(len(lines)):
                if lines[j][i] > highest:
                    highest = lines[j][i]
                    linez[j][i] = lines[j][i]
            highest = -1
            for j in range(len(lines)):
                if lines[len(lines) - 1 - j][i] > highest:
                    highest = lines[len(lines) - 1 - j][i]
                    linez[len(lines) - 1 - j][i] = lines[len(lines) - 1 - j][i]
        for line in linez:
            for i in line:
                if i != -1:
                    sum += 1
                    print(i, end='')
                else:
                    print(' ', end='')
            print()
        print(sum)

      

if __name__ == '__main__':
    main()
