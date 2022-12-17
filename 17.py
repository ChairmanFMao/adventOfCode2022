f = open("17Input.txt","r")

# This is pretty similar to tetris
# Just need to make it sufficently tall, like 10000
# rocks spawn in 3 blocks above the highest bit
# I might make some methods to place and remove shapes

lines = f.read()
f.close()

""" these are all the possible shapes
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""

grid = [[0 for i in range(7)] for j in range(100000)]

# This takes care of spawning or removing blocks
def edit(pos,block,spawn):
    dx = []; dy = []
    if block == 0:
        dx = [0,1,2,3]
        dy = [0,0,0,0]
    if block == 1:
        dx = [0,1,1,1,2]
        dy = [1,0,1,2,1]
    if block == 2:
        dx = [0,1,2,2,2]
        dy = [0,0,0,1,2]
    if block == 3:
        dx = [0,0,0,0]
        dy = [0,1,2,3]
    if block == 4:
        dx = [0,0,1,1]
        dy = [0,1,0,1]

    # This is just a prior check
    for i in range(len(dx)):
        if pos[0]+dy[i] < 0 or pos[0]+dy[i] >= 100000 or pos[1]+dx[i] < 0 or pos[1]+dx[i] >= 7 or grid[pos[0]+dy[i]][pos[1]+dx[i]] == spawn:
            return 1

    for i in range(len(dx)):
        grid[pos[0]+dy[i]][pos[1]+dx[i]] = spawn
    return 0

# still overestimating
# found an issue on the 10th one, it doesn't go far enough left
# 3202 is not right

""" part 1
start = 3; gas = lines.strip(); ptr = 0
for i in range(2022):
    block = i%5
    # This stores the bottom left pos of the hitbox
    pos = [start,2]
    while 1:
        # This does the move sideways
        edit(pos,block,1)
        move = 1 if gas[ptr%len(gas)] == '>' else -1
        edit(pos,block,0)
        val = edit([pos[0],pos[1]+move],block,1)
        ptr += 1
        if val:
            edit(pos,block,1)
        else:
            pos[1] += move

        # This does the move down
        edit(pos,block,0)
        val = edit([pos[0]-1,pos[1]],block,1)
        if val:
            edit(pos,block,1)
            start = max(start,pos[0]+(1 if block == 0 else 3 if block == 1 else 3 if block == 2 else 4 if block == 3 else 2)+3)
            break
        else:
            pos[0] -= 1

print(start-3)
"""

# Unsure about part 2
# I think that it may be cyclic when we reach a full row again
# However, I'm not sure if this works properly
# We can use the fact that we just start fresh every time that we
# completely fill a row, all that is different is our pos in gas
# and our block number
# If we can get back to the same ones prior then we have can use
# this as a cycle and skip forward a lot
# I managed to get this to work with a dictionary and I got it
# first try without any wrong answers :)
# This code is very efficient

start = 3; gas = lines.strip(); ptr = 0; i = 1000000000000;
before = dict(); out = 0
while i:
    block = (5-i%5)%5
    # This stores the bottom left pos of the hitbox
    pos = [start,2]
    while 1:
        # This does the move sideways
        edit(pos,block,1)
        move = 1 if gas[ptr%len(gas)] == '>' else -1
        edit(pos,block,0)
        val = edit([pos[0],pos[1]+move],block,1)
        ptr += 1
        if val:
            edit(pos,block,1)
        else:
            pos[1] += move

        # This does the move down
        edit(pos,block,0)
        val = edit([pos[0]-1,pos[1]],block,1)
        if val:
            edit(pos,block,1)
            start = max(start,pos[0]+(1 if block == 0 else 3 if block == 1 else 3 if block == 2 else 4 if block == 3 else 2)+3)
            break
        else:
            pos[0] -= 1
    for j in range(pos[0], pos[0]+5):
        if sum(grid[j]) == 7:
            if before.get((block,ptr%len(gas))) == None:
                before[(block,ptr%len(gas))] = (i,start)
            else:
                last = before[(block,ptr%len(gas))]
                time = last[0] - i
                height = start- last[1]
                out += height * (i // time)
                i %= time
    i -= 1

print(start-3 + out)

