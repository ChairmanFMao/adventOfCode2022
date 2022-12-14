import heapq

f = open("12Input.txt","r")

lines = f.read().split()
f.close()

# Takes like 10 seconds to run but it does give the correct answer
# I think its O(n^2 m^2) which is not the best
# maybe adding a priority queue would help
# I made the code much faster with a heapq

grid = [[i for i in j] for j in lines]
dist = [[int(1e11) for i in j] for j in lines]
seen = [[0 for i in j] for j in lines]
s = []; e = []; q = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if grid[i][j] == 'S':
            s = [i,j]
        if grid[i][j] == 'E':
            e = [i,j]
        # This is all that is required for part 2
        #if grid[i][j] == 'a':
            #dist[i][j] = 0
        """ This is for part 2 with the heapq """
        if grid[i][j] == 'a':
            dist[i][j] = 0
            heapq.heappush(q,(dist[i][j],i,j))


grid[s[0]][s[1]] = "a"
grid[e[0]][e[1]] = "z"
dist[s[0]][s[1]] = 0

runs = len(lines)*len(lines[0])
dy = [0,0,1,-1]
dx = [1,-1,0,0]

heapq.heappush(q,(dist[s[0]][s[1]],s[0],s[1]))

"""
for r in range(runs):
    current = [-1,-1]; val = int(1e11)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if dist[i][j] < val and not seen[i][j]:
                val = dist[i][j]
                current = [i,j]
    """
while len(q):

    tmp = heapq.heappop(q)
    current = [tmp[1],tmp[2]]
    if seen[current[0]][current[1]]:
        continue
    val = tmp[0]

    seen[current[0]][current[1]] = 1
    for i in range(4):
        if current[0] + dx[i] < 0 or current[0] + dx[i] >= len(grid) or current[1] + dy[i] < 0 or current[1] + dy[i] >= len(grid[0]):
            continue
        if dist[current[0]+dx[i]][current[1]+dy[i]] > val+1 and ord(grid[current[0]+dx[i]][current[1]+dy[i]])-ord(grid[current[0]][current[1]]) <= 1:
            dist[current[0]+dx[i]][current[1]+dy[i]] = val+1
            heapq.heappush(q,(val+1,current[0]+dx[i],current[1]+dy[i]))

print(dist[e[0]][e[1]])

