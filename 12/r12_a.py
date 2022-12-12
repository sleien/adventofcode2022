from collections import deque
# get all input from input.txt

def main():

    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        grid = [list(line.strip()) for line in lines]

        start_x = 0
        start_y = 0

        goal_x = 0 
        goal_y = 0

        for y, row in enumerate(grid):
            for x, item in enumerate(row):
                if item == "S":
                    start_y = y
                    start_x = x
                    grid[y][x] = "a"
                if item == "E":
                    goal_y = y
                    goal_x = x
                    grid[y][x] = "z"

        queue1 = deque()
        queue1.append((0, start_y, start_x))

        visited1 = {(start_y, start_x)}
        while queue1:
            distance, y, x = queue1.popleft()

            for step_y, step_x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if step_y < 0 or step_x < 0 or step_y >= len(grid) or step_x >= len(grid[0]):
                    continue
                if (step_y, step_x) in visited1:
                    continue
                if ord(grid[step_y][step_x]) - ord(grid[y][x]) > 1:
                    continue
                if step_y == goal_y and step_x == goal_x:
                    print(distance + 1)
                    queue1 = []
                    break
                visited1.add((step_y, step_x))
                queue1.append((distance + 1, step_y, step_x))

if __name__ == '__main__':
    main()
