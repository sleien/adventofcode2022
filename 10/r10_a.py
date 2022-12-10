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

        sum = 0

        for line in lines:
            if line.startswith("noop"):
                cycle += 1
                if (cycle - 20) % 40 == 0:
                    sum += x * cycle
            elif line.startswith("addx"):
                v = int(line.split(" ")[1])
                for _ in range(2):
                    cycle += 1
                    if (cycle - 20) % 40 == 0:
                        sum += x * cycle
                x += v
        print(sum)
        
if __name__ == '__main__':
    main()
