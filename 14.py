f = open("14Input.txt","r")

lines = f.read().split("\n")
lines.pop()
f.close()

# If we just reach the bottom of the grid on a grain of sand then
# we know that we can't place anymore sand

# 0 represents empty
# 1 represents filled with a block
# 2 represents filled with sand
grid = [[0 for i in range(1000)] for j in range(1000)]

# This stores the highest y value we get for part 2
highest = 0
for line in lines:
    current = [list(map(int,i.split(","))) for i in line.split(" -> ")]
    x = y = 0
    for i in range(len(current)-1):
        x, y = current[i][0], current[i][1]
        highest = max(highest,y)
        grid[y][x] = 1
        while x != current[i+1][0]:
            x += 1 if current[i+1][0] - x > 0 else -1
            grid[y][x] = 1
        while y != current[i+1][1]:
            y += 1 if current[i+1][1] - y > 0 else -1
            grid[y][x] = 1
        highest = max(highest,y)

# This is to fill in the row after the highest y value
for i in range(len(grid)):
    grid[highest+2][i] = 1

good = 1; grains = 0
# This creates grains until it is done
while good:
    x, y = 500,0
    # This is for part 2
    if grid[y][x]:
        break
    grid[y][x] = 2
    moving = 1
    while moving:
        if y >= len(grid)-1:
            good = 0
            break
        if not grid[y+1][x]:
            grid[y+1][x] = 2
            grid[y][x] = 0
            y += 1
        elif not grid[y+1][x-1]:
            grid[y+1][x-1] = 2
            grid[y][x] = 0
            y += 1
            x -= 1
        elif not grid[y+1][x+1]:
            grid[y+1][x+1] = 2
            grid[y][x] = 0
            y += 1
            x += 1
        else:
            moving = 0
    grains += good

print(grains)

