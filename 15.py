f = open("15Input.txt","r")

lines = f.read().split("\n")
lines.pop()
f.close()

# maximum values are around 4e6, i might need to make the dimensions 6e6 on the list
# could probably do this mathematically or with a binary search for the start and end
# Did some mathematical stuff with the absolute value and it made it much faster
# part 2 seems quite interesting as we can't brute force simulate the grid kinda
# Unsure of what kinda way I should go about this
# I managed to get my code to give the correct output though, it
# was a little slow and takes about a minute to run

""" part 1
# Stores the posititions of all the beacons
beacons = []

# This is very large so that negative indexes don't interfere
impossible = [0 for i in range(int(1e7))]
for line in lines:
    line = line.replace("Sensor at ","").replace("x=","").replace("y=","").split(": closest beacon is at ")
    start = list(map(int,line[0].split(", ")))
    nearest = list(map(int,line[1].split(", ")))
    dist = abs(start[0]-nearest[0]) + abs(start[1]-nearest[1])
    beacons.append(nearest)

    dist -= abs(int(2e6)-start[1])
    
    if dist < 0:
        continue

    for i in range(start[0]-dist,start[0]+dist+1):
        impossible[i] = 1

# Removes the positions of existing beacons on the line
for beacon in beacons:
    if beacon[1] == int(2e6):
        impossible[beacon[0]] = 0

print(sum(impossible))
"""

# relates the beacon to their distance
sensors = dict()

# This finds all of the beacons and their dist values
for line in lines:
    line = line.replace("Sensor at ","").replace("x=","").replace("y=","").split(": closest beacon is at ")
    start = tuple(map(int,line[0].split(", ")))
    nearest = tuple(map(int,line[1].split(", ")))
    dist = abs(start[0]-nearest[0]) + abs(start[1]-nearest[1])

    sensors[start] = dist

MAXVAL = int(4e6)
def val(starting, dif):
    return [max(starting-dif,0),min(starting+dif,MAXVAL)]

print("starting first bit")

# This stores all of the ranges
grid = [[] for i in range(int(MAXVAL+1))]
for sensor in sensors.keys():
    start = sensor[0]
    initial = sensor[1]
    current = sensors[sensor]
    if 0 <= start and start <= MAXVAL:
        grid[start].append(val(initial,current))
    lptr = start-1; rptr = start+1
    current -= 1
    while current >= 0:
        if 0 <= lptr and lptr <= MAXVAL:
            grid[lptr].append(val(initial,current))
            lptr -= 1
        if 0 <= rptr and rptr <= MAXVAL:
            grid[rptr].append(val(initial,current))
            rptr += 1
        current -= 1

print("starting second bit")

# We first sort all of the columns to ensure we process them in
# the right order
for i in range(len(grid)):
    grid[i].sort()
    pos = -1; flag = 1
    for j in range(len(grid[i])):
        if grid[i][j][0] > pos+1:
            print(i*MAXVAL+pos+1)
            flag = 0
            break
        pos = max(pos,grid[i][j][1])

    if flag and pos < MAXVAL:
        print(i*MAXVAL+pos+1)

    if flag:
        break

