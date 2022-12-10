# get all input from input.txt

def main():
    # open file
    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [line.strip() for line in lines]

        x = 1
        cycle = 0

        screen = [["."] * 40,["."] * 40,["."] * 40,["."] * 40,["."] * 40,["."] * 40] 

        for line in lines:
            if line.startswith("noop"):
                cycle += 1
                if (cycle % 40 - x-1) in [-1, 0, 1]:
                    screen[int((cycle - 1)/40)][(cycle - 1)%40] = "#"
            elif line.startswith("addx"):
                v = int(line.split(" ")[1])
                for _ in range(2):
                    cycle += 1
                    if (cycle % 40 - x -1) in [-1, 0, 1]:
                        screen[int((cycle - 1)/40)][(cycle - 1)%40] = "#"
                x += v
        for row in screen:
            print("".join(row))
        
if __name__ == '__main__':
    main()
