# get all input from input.txt

def follow(head, tail):
    if head[0] - tail[0] > 1:
        tail[0] += 1
        if head[1] - tail[1] != 0:
            tail[1] = head[1]
    elif head[0] - tail[0] < -1:
        tail[0] -= 1
        if head[1] - tail[1] != 0:
            tail[1] = head[1]
    elif head[1] - tail[1] > 1:
        tail[1] += 1
        if head[0] - tail[0] != 0:
            tail[0] = head[0]
    elif head[1] - tail[1] < -1:
        tail[1] -= 1
        if head[0] - tail[0] != 0:
            tail[0] = head[0]
    
    if head[0] - tail[0] not in [-1,0,1] or head[1] - tail[1] not in [-1,0,1]:
        print("ERROR")


def main():
    # open file
    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [list(line.split(" ")) for line in lines]

        head = [0,0]
        tail = [[0,0]]
        rope_len = 10
        for _ in range(rope_len - 1):
            tail.append([0,0])
        headVisited = []
        headVisited.append(str(head[0]) + "," + str(head[1]))
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
                headVisited.append(str(head[0]) + "," + str(head[1]))
                tailVisited.append(str(tail[0][0]) + "," + str(tail[0][1]))
                for i in range(rope_len - 1):
                    follow(tail[i], tail[i + 1])
                tailRopeVisited.append(str(tail[rope_len - 1][0]) + "," + str(tail[rope_len - 1][1]))

        tailVisited = list(dict.fromkeys(tailVisited))
        tailRopeVisited = list(dict.fromkeys(tailRopeVisited))

        # get min value of headVisited and tailVisited split by ","
        #minHead0 = min([int(i.split(",")[0]) for i in headVisited])
        #minTail0 = min([int(i.split(",")[0]) for i in tailVisited])
        #minHead1 = min([int(i.split(",")[1]) for i in headVisited])
        #minTail1 = min([int(i.split(",")[1]) for i in tailVisited])
        # get max value of headVisited and tailVisited split by ","
        #maxHead0 = max([int(i.split(",")[0]) for i in headVisited])
        #maxTail0 = max([int(i.split(",")[0]) for i in tailVisited])
        #maxHead1 = max([int(i.split(",")[1]) for i in headVisited])
        #maxTail1 = max([int(i.split(",")[1]) for i in tailVisited])

        #max0 = max(maxHead0, maxTail0)
        #min0 = min(minHead0, minTail0)
        #max1 = max(maxHead1, maxTail1)
        #min1 = min(minHead1, minTail1)

        #test = [["." for i in range(max1-min1+1)] for j in range(max0-min0+1)]

        #for h in headVisited:
        #    h = h.split(",")
        #    test[int(h[0]) - min0][int(h[1]) - min1] = "H"
        #for t in tailVisited:
        #    t = t.split(",")
        #    test[int(t[0]) - min0][int(t[1]) - min1] = "#"
        #for i in range(len(test)):
        #    print("".join(test[::-1][i])) 

        print(len(tailVisited))
        print(len(tailRopeVisited))

if __name__ == '__main__':
    main()
