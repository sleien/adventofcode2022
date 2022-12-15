import re
# get all input from input.txt


def main():

    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [line.strip() for line in lines]

        # build tuples from numbers after =
        for i in range(len(lines)):
            lines[i] = re.sub("[A-Za-z= ]", "", lines[i]).strip()
            lines[i] = lines[i].split(":")
            lines[i][0] = lines[i][0].split(",")
            lines[i][1] = lines[i][1].split(",")
            lines[i] = (int(lines[i][0][0]), int(lines[i][0][1]),
                        int(lines[i][1][0]), int(lines[i][1][1]))
        search_y = 2000000

        scanned = []

        for i in range(len(lines)):
            x_s, y_s, x_b, y_b = lines[i]
            diff = abs(y_b - y_s) + abs(x_b - x_s)
            if y_s <= search_y and y_s + diff >= search_y:
                for j in range(y_s + diff - search_y + 1):
                    scanned.append(x_s + j)
                    scanned.append(x_s - j)
            elif y_s >= search_y and y_s - diff <= search_y:
                for j in range(search_y - y_s + diff + 1):
                    scanned.append(x_s + j)
                    scanned.append(x_s - j)
        scanned = list(set(scanned))

        for line in lines:
            x_s, y_s, x_b, y_b = line
            if y_b == search_y and x_b in scanned:
                scanned.remove(x_b)
        print(len(scanned))


if __name__ == '__main__':
    main()
