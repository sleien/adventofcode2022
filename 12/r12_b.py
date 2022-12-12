from collections import deque
# get all input from input.txt

def main():

    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        grid = [list(line.strip()) for line in lines]

        goal_x = 0 
        goal_y = 0

        for y, row in enumerate(grid):
            for x, item in enumerate(row):
                if item == "S":
                    grid[y][x] = "a"
                if item == "E":
                    goal_y = y
                    goal_x = x
                    grid[y][x] = "z"
                    
        queue2 = deque()
        queue2.append((0, goal_y, goal_x))

        visited2 = {(goal_y, goal_x)}

        while queue2:
            distance, y, x = queue2.popleft()
            for step_y, step_x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if step_y < 0 or step_x < 0 or step_y >= len(grid) or step_x >= len(grid[0]):
                    continue
                if (step_y, step_x) in visited2:
                    continue
                if ord(grid[step_y][step_x]) - ord(grid[y][x]) < -1:
                    continue
                if grid[step_y][step_x] == "a":
                    print(distance + 1)
                    exit(0)
                visited2.add((step_y, step_x))
                queue2.append((distance + 1, step_y, step_x))
if __name__ == '__main__':
    main()
