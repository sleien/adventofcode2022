import json
# get all input from input.txt

def main():

    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [line.strip() for line in lines]
        lines = [line.split(" -> ") for line in lines]

        grid_array = []

        x_min = 1000
        x_max = 0
        y_min = 0
        y_max = 0

        for idx, line in enumerate(lines):
            grid_array.append([])
            for char in line:
                char = char.split(",")
                char[0] = int(char[0])
                char[1] = int(char[1])
                if char[0] < x_min:
                    x_min = char[0]
                if char[0] > x_max:
                    x_max = char[0]
                if char[1] < y_min:
                    y_min = char[1]
                if char[1] > y_max:
                    y_max = char[1]
                grid_array[idx].append((char[0], char[1]))

        grid = [(". " * (x_max - x_min + 1) + ".").split(" ") for i in range(y_max - y_min + 1)]


        for line in grid_array:
            for i in range(len(line)):
                if i != len(line) - 1:
                    x, y = line[i]
                    x_next, y_next = line[i+1]
                    for j in range((max(x, x_next) - min(x, x_next) + 1)):
                        grid[y - y_min][min(x, x_next) - x_min + j] = "#"
                    for k in range((max(y, y_next) - min(y, y_next) + 1)):
                        grid[min(y, y_next) - y_min + k][x - x_min] = "#"

        for line in grid:
            
            print("".join(line))

        
        start_x = 500 - x_min
        start_y = 0 - y_min
        void = False
        sand = -1

        while not void:
            x = start_x
            y = start_y
            sand += 1
            while True:
                if y == len(grid) - 1:
                    void = True
                    break
                if grid[y + 1][x] != "#":
                    y += 1
                    continue
                if x == 0:
                    void = True
                    break
                if grid[y + 1][x - 1] != "#":
                    x -= 1
                    y += 1
                    continue
                if x == len(grid[y]) - 1:
                    void = True
                    break
                if grid[y + 1][x + 1] != "#":
                    x += 1
                    y += 1
                    continue
                grid[y][x] = "#"
                break
        print(sand)

        for line in grid:
            
            print("".join(line))


if __name__ == '__main__':
    main()
