# get all input from input.txt

def follow(head, tail):
        y_diff = head[0] - tail[0]
        x_diff = head[1] - tail[1]
        if abs(y_diff) <= 1 and  abs(x_diff) <= 1:
            return
        if y_diff > 0:
            tail[0] += 1
        elif y_diff < 0:
            tail[0] -= 1
        if x_diff > 0:
            tail[1] += 1
        elif x_diff < 0:
            tail[1] -= 1
        


def main():
    # open file
    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [list(line.split(" ")) for line in lines]

        head = [0,0]
        tail = [[0,0]]
        rope_len = 9
        for _ in range(rope_len - 1):
            tail.append([0,0])
        tailVisited = []
        tailVisited.append(str(tail[0][0]) + "," + str(tail[0][1]))
        tailRopeVisited = []
        tailRopeVisited.append(str(tail[1][0]) + "," + str(tail[1][1]))

        for line in lines:
            line[1] = int(line[1].strip())
            for i in range(line[1]):
                if line[0] == "U":
                    head[0] += 1
                elif line[0] == "D":
                    head[0] -= 1
                elif line[0] == "R":
                    head[1] += 1
                elif line[0] == "L":
                    head[1] -= 1
                follow(head, tail[0])
                tailVisited.append(str(tail[0][0]) + "," + str(tail[0][1]))
                if len(tailVisited) == 201:
                    print("")
                for i in range(rope_len - 1):
                    follow(tail[i], tail[i + 1])
                tailRopeVisited.append(str(tail[rope_len - 1][0]) + "," + str(tail[rope_len - 1][1]))

        tailVisited = list(dict.fromkeys(tailVisited))
        tailRopeVisited = list(dict.fromkeys(tailRopeVisited))

        print(len(tailVisited))
        print(len(tailRopeVisited))

if __name__ == '__main__':
    main()
