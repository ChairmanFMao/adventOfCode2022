from collections import deque

f = open("24Input.txt","r")

lines = f.read().split()
f.close()

# I think we can just do this with a bfs as there won't be that
# many possiblities for the person to be
# The period of the blizzard would be the lcm of the length of
# rows and the length of the columns
# maybe a brute force approach won't work
# 120 wide and 25 tall; lcm of 120 and 25 is 600
# there are 600 different states for the wind to be in

blizzards = deque()
blizzardLookup = dict()

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "^":
            blizzards.append([i,j,0])
        if lines[i][j] == ">":
            blizzards.append([i,j,1])
        if lines[i][j] == "v":
            blizzards.append([i,j,2])
        if lines[i][j] == "<":
            blizzards.append([i,j,3])

length = len(blizzards)
for i in range(length):
    blizzard = blizzards.popleft()
    blizzards.append(blizzard)
    blizzardLookup[(blizzard[0],blizzard[1])] = 1

dx = (0,1,0,-1,0)
dy = (-1,0,1,0,0)

q = deque()
q.append((0,1,0));
time = 0; out = 0
grid = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
while len(q):
    current = q.popleft()
    # This is when we trigger an update for the blizzards
    if current[2] > time:
        blizzardLookup = dict()
        for i in range(length):
            blizzard = blizzards.popleft()
            # We need to do the wrapping here
            blizzard[0] += dy[blizzard[2]]
            blizzard[1] += dx[blizzard[2]]
            # does upwards
            if blizzard[0] == 0 and blizzard[2] == 0:
                blizzard[0] = len(lines)-2
            # does downwards
            if blizzard[0] == len(lines)-1 and blizzard[2] == 2:
                blizzard[0] = 1
            # does left
            if blizzard[1] == 0 and blizzard[2] == 3:
                blizzard[1] = len(lines[0])-2
            # does right
            if blizzard[1] == len(lines[0])-1 and blizzard[2] == 1:
                blizzard[1] = 1
            
            blizzards.append(blizzard)
            blizzardLookup[(blizzard[0],blizzard[1])] = 1
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                grid[i][j] = 0
        time += 1


    # Need to check that we aren't in a blizzard
    if blizzardLookup.get((current[0],current[1])) == 1:
        continue

    if current[0] == len(lines)-1 and current[1] == len(lines[0])-2:
        out += current[2]
        break
    
    # This tests all of the possible moves
    for i in range(5):
        if 0 <= current[0]+dy[i] and current[0]+dy[i] < len(lines) and 0 <= current[1]+dx[i] and current[1]+dx[i] < len(lines[0]) and lines[current[0]+dy[i]][current[1]+dx[i]] != "#" and not grid[current[0]+dy[i]][current[1]+dx[i]]:
            grid[current[0]+dy[i]][current[1]+dx[i]] = 1
            q.append((current[0]+dy[i],current[1]+dx[i],current[2]+1))

# These two later bits are for the second part
q = deque()
q.append((len(lines)-1,len(lines[0])-2,0))
time = 0
grid = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
while len(q):
    current = q.popleft()
    # This is when we trigger an update for the blizzards
    if current[2] > time:
        blizzardLookup = dict()
        for i in range(length):
            blizzard = blizzards.popleft()
            # We need to do the wrapping here
            blizzard[0] += dy[blizzard[2]]
            blizzard[1] += dx[blizzard[2]]
            # does upwards
            if blizzard[0] == 0 and blizzard[2] == 0:
                blizzard[0] = len(lines)-2
            # does downwards
            if blizzard[0] == len(lines)-1 and blizzard[2] == 2:
                blizzard[0] = 1
            # does left
            if blizzard[1] == 0 and blizzard[2] == 3:
                blizzard[1] = len(lines[0])-2
            # does right
            if blizzard[1] == len(lines[0])-1 and blizzard[2] == 1:
                blizzard[1] = 1
            
            blizzards.append(blizzard)
            blizzardLookup[(blizzard[0],blizzard[1])] = 1
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                grid[i][j] = 0
        time += 1


    # Need to check that we aren't in a blizzard
    if blizzardLookup.get((current[0],current[1])) == 1:
        continue

    if current[0] == 0 and current[1] == 1:
        out += current[2]
        break
    
    # This tests all of the possible moves
    for i in range(5):
        if 0 <= current[0]+dy[i] and current[0]+dy[i] < len(lines) and 0 <= current[1]+dx[i] and current[1]+dx[i] < len(lines[0]) and lines[current[0]+dy[i]][current[1]+dx[i]] != "#" and not grid[current[0]+dy[i]][current[1]+dx[i]]:
            grid[current[0]+dy[i]][current[1]+dx[i]] = 1
            q.append((current[0]+dy[i],current[1]+dx[i],current[2]+1))

q = deque()
q.append((0,1,0));
time = 0
grid = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
while len(q):
    current = q.popleft()
    # This is when we trigger an update for the blizzards
    if current[2] > time:
        blizzardLookup = dict()
        for i in range(length):
            blizzard = blizzards.popleft()
            # We need to do the wrapping here
            blizzard[0] += dy[blizzard[2]]
            blizzard[1] += dx[blizzard[2]]
            # does upwards
            if blizzard[0] == 0 and blizzard[2] == 0:
                blizzard[0] = len(lines)-2
            # does downwards
            if blizzard[0] == len(lines)-1 and blizzard[2] == 2:
                blizzard[0] = 1
            # does left
            if blizzard[1] == 0 and blizzard[2] == 3:
                blizzard[1] = len(lines[0])-2
            # does right
            if blizzard[1] == len(lines[0])-1 and blizzard[2] == 1:
                blizzard[1] = 1
            
            blizzards.append(blizzard)
            blizzardLookup[(blizzard[0],blizzard[1])] = 1
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                grid[i][j] = 0
        time += 1


    # Need to check that we aren't in a blizzard
    if blizzardLookup.get((current[0],current[1])) == 1:
        continue

    if current[0] == len(lines)-1 and current[1] == len(lines[0])-2:
        out += current[2]
        break
    
    # This tests all of the possible moves
    for i in range(5):
        if 0 <= current[0]+dy[i] and current[0]+dy[i] < len(lines) and 0 <= current[1]+dx[i] and current[1]+dx[i] < len(lines[0]) and lines[current[0]+dy[i]][current[1]+dx[i]] != "#" and not grid[current[0]+dy[i]][current[1]+dx[i]]:
            grid[current[0]+dy[i]][current[1]+dx[i]] = 1
            q.append((current[0]+dy[i],current[1]+dx[i],current[2]+1))

print(out)

