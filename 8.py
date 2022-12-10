f = open("8Input.txt","r")

# I think the second part will ask for how many tree house spots
# Turns out that is basically part 1

lines = f.read().split()

grid = [[int(i) for i in j] for j in lines]
seen = [[0 for i in j] for j in lines]

""" part 1
for j in range(len(grid)):
    lmax = -1; rmax = -1; vmax = -1; dmax = -1
    lptr = 0; rptr = len(grid[j])-1

    for i in range(len(grid[j])):
        if grid[j][lptr] > lmax:
            seen[j][lptr] = 1
            lmax = grid[j][lptr]
        if grid[j][rptr] > rmax:
            seen[j][rptr] = 1
            rmax = grid[j][rptr]
        if grid[lptr][j] > vmax:
            seen[lptr][j] = 1
            vmax = grid[lptr][j]
        if grid[rptr][j] > dmax:
            seen[rptr][j] = 1
            dmax = grid[rptr][j]

        lptr += 1
        rptr -= 1

print(sum([sum(i) for i in seen]))
"""

# This is structured so badly
# I'm not sure of how to do it more elegantly tho
out = 0; MAX = len(grid); INF = int(1e9)

def outside(a):
    return 0 > a or a >= MAX

def c(op,val,i,j):
    return grid[i][val] if op <= 1 else grid[val][j]

def com(op,val,i,j):
    return c(op,val,i,j) >= grid[i][j]

d = [-1,1,-1,1]

# This iterates over the column
for i in range(MAX):
    # This iterates over the row
    for j in range(MAX):
        ptr = [j-1,j+1,i-1,i+1]
        count = [1,1,1,1]
        unused = [1,1,1,1]
        val = 1
        for k in range(MAX):
            for l in range(4):
                if (outside(ptr[l]) or com(l,ptr[l],i,j)) and unused[l]:
                    val *= count[l]-outside(ptr[l]); ptr[l] = INF; unused[l] = 0
                count[l] += 1; ptr[l] += d[l]

        out = max(out, val)

print(out)

f.close()

