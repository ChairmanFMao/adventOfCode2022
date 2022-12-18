from collections import deque

f = open("18Input.txt","r")

lines = f.read().split()
f.close()

# Values only go up to 25 so we will do a simulation
# I think we can just do a bfs for part 2 from an outside point

grid = [[[0 for i in range(27)] for j in range(27)] for k in range(27)]

points = []
for line in lines:
    x, y, z = map(int,line.split(","))
    grid[x][y][z] = 1
    points.append([x,y,z])

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

""" part 1
out = 0
for point in points:
    for i in range(6):
        if not grid[point[0]+dx[i]][point[1]+dy[i]][point[2]+dz[i]]:
            out += 1
"""

seen = [[[0 for i in range(27)] for j in range(27)] for k in range(27)]

q = deque()
q.append([0,0,0])
seen[0][0][0] = 1

# This returns if a value is within given bounds
def v(val,bounds):
    return bounds[0] <= val and val <= bounds[1]

# This explores all points accessible from the exterior
while len(q):
    point = q.popleft()
    for i in range(6):
        x = point[0]+dx[i]
        y = point[1]+dy[i]
        z = point[2]+dz[i]
        if not v(x,[0,26]) or not v(y,[0,26]) or not v(z,[0,26]):
            continue
        if grid[x][y][z]:
            continue
        if not seen[x][y][z]:
            seen[x][y][z] = 1
            q.append([x,y,z])

# This iterates through all the points and sees which touch the
# outside
out = 0
for point in points:
    for i in range(6):
        if not grid[point[0]+dx[i]][point[1]+dy[i]][point[2]+dz[i]] and seen[point[0]+dx[i]][point[1]+dy[i]][point[2]+dz[i]]:
            out += 1

print(out)

