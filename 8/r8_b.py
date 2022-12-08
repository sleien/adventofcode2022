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
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                view = [0,0,0,0]
                for a in range(i):
                    if lines[i - 1 - a][j] < lines[i][j]:
                        view[0] += 1
                    elif lines[i - 1 - a][j] >= lines[i][j]:
                        view[0] += 1
                        break
                    else:
                        break
                for a in range(i + 1, len(lines)):
                    if lines[a][j] < lines[i][j]:
                        view[1] += 1
                    elif lines[a][j] >= lines[i][j]:
                        view[1] += 1
                        break
                    else:
                        break
                for a in range(j):
                    if lines[i][j - 1 - a] < lines[i][j]:
                        view[2] += 1
                    elif lines[i][j - 1 - a] >= lines[i][j]:
                        view[2] += 1
                        break
                    else:
                        break
                for a in range(j + 1, len(lines[i])):
                    if lines[i][a] < lines[i][j]:
                        view[3] += 1
                    elif lines[i][a] >= lines[i][j]:
                        view[3] += 1
                        break
                    else:
                        break
                linez.append(view[0] * view[1] * view[2] * view[3])

        print(max(linez))

      

if __name__ == '__main__':
    main()
int()