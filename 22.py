f = open("22Input.txt","r")

lines = f.read().split("\n")
lines.pop()
f.close()

# This gets the width and height of the grid
w = max([len(lines[i]) for i in range(len(lines)-2)])
h = len(lines)-2

# This pads all of the input with extra spaces to fill
# out the grid
for i in range(len(lines)):
    if not len(lines[i]):
        break
    lines[i] += " "*(w-len(lines[i]))

# This removes the moves from the end of lines
moves = lines[-1]
lines.pop()
lines.pop()

# This does further input parseing to make it easier later in the
# program
parsedMoves = []; val = 0
for i in moves:
    if i == "R" or i == "L":
        parsedMoves.append(val)
        val = 0
        parsedMoves.append(i)
    else:
        val *= 10
        val += int(i)
if val:
    parsedMoves.append(val)

# This will store the adjacent cells for each square in the grid
adj = [[dict() for j in range(w)] for i in range(h)]

# These are just movement vectors
# 0 means up
# 1 means right
# 2 means down
# 3 means to the left
dx = (0,1,0,-1)
dy = (-1,0,1,0)

flag = 1
start = []

# This iterates over all of the heights
for i in range(h):
    # This iterates over all of the widths for each height
    for j in range(w):
        if lines[i][j] == " ":
            continue
        if flag:
            start = [i,j]
            flag = 0
        # I need to make edits here for part 2
        for k in range(4):
            y = (i+dy[k])%h; x = (j+dx[k])%w

            # This is for when it goes off one side of the shape
            # otherwise we don't need to consider this
            if lines[y][x] == " ":
                # We iterate clockwise from the top left most
                # edge upwards
                # There are 7 pairs which are labelled
                # I think all of the directions are right
                # I just need to check over the coordinates
                # p1
                if i == 0 and 50 <= j < 100 and k == 0:
                    y = 150 + j%50; x = 0
                # p2
                if i == 0 and 100 <= j < 150 and k == 0:
                    y = 199; x = j%50
                # p3
                if j == 149 and 0 <= i < 50 and k == 1:
                    y = 100 + 49 - i%50; x = 99
                # p4
                if i == 49 and 100 <= j < 150 and k == 2:
                    y = 50 + j%50; x = 99
                # p4
                if j == 99 and 50 <= i < 100 and k == 1:
                    y = 49; x = 100 + i%50
                # p3
                if j == 99 and 100 <= i < 150 and k == 1:
                    y = 49 - i%50; x = 149
                # p5
                if i == 149 and 50 <= j < 100 and k == 2:
                    y = 150 + j%50; x = 49
                # p5
                if j == 49 and 150 <= i < 200 and k == 1:
                    y = 149; x = 50 + i%50
                # p2
                if i == 199 and 0 <= j < 50 and k == 2:
                    y = 0; x = 100 + j%50
                # p1
                if j == 0 and 150 <= i < 200 and k == 3:
                    y = 0; x = 50 + i%50
                # p6
                if j == 0 and 100 <= i < 150 and k == 3:
                    y = 50 - i%50; x = 50
                # p7
                if i == 100 and 0 <= j < 50 and k == 0:
                    y = 50 + j%50; x = 50
                # p7
                if j == 50 and 50 <= i < 100 and k == 3:
                    y = 100; x = i%50
                # p6
                if j == 50 and 0 <= i < 50 and k == 3:
                    y = 100 + 50 - i%50; x = 0

                # This checks if any of the coordinates have
                # managed to get through without properly setting
                # y and x
                if (y == (i+dy[k])%h and x == (j+dx[k])%w) or lines[y][x] == " ":
                    print(i,j,lines[i][j])


            """ part 1
            # Carries on moving until it finds a cell
            while lines[y][x] == " ":
                y = (y+dy[k])%h
                x = (x+dx[k])%w
            """
            # Sets the adjacent cell for the current one
            adj[i][j][k] = (y,x)

# This stores information about the grid
grid = [[0 for j in range(w)] for i in range(h)]

y = start[0]; x = start[1]; d = 1

# This performs all of the moves
for i in parsedMoves:
    # This means we move forward i steps
    if isinstance(i,int):
        for j in range(i):
            grid[y][x] = d
            if lines[adj[y][x][d][0]][adj[y][x][d][1]] == ".":
                y, x = adj[y][x][d]
            grid[y][x] = d
    elif i == "R":
        d = (d+1)%4
    elif i == "L":
        d = (d-1+4)%4

print((y+1)*1000+(x+1)*4+(d-1+4)%4)

# for part 2 I just need to reconfigure the adj matrix
# Somehow I need to get it such that the faces will wrap
# line a cube would
# directional vectors may change
# actually, I would just need to flip rows and columns or smth
# depending on where the blank spaces are
# I think I could just do this manually but it would be a little
# jank
# There is no point using the example as it has a different net
# corners are also going to be quite annoying
# There are many different edges which I might have to just do by
# hand with if statements
# 172132 is too high
# 148076 is also too high
# 50600 is too low
# I managed to get the right answer after tweaking all of the
# if statements a lot

