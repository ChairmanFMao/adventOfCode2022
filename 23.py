f = open("23Input.txt","r")

lines = f.read().split()
f.close()

# I think I will try to implement this storing all of the point in
# a list rather than an actual grid

points = []
pointsLookup = dict()
nextPoint = dict()

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            points.append((i+10,j+10))
            pointsLookup[(i+10,j+10)] = 1

dx = (-1,0,1,1,1,0,-1,-1)
dy = (-1,-1,-1,0,1,1,1,0)
check = {0:(0,1,2),
         1:(4,5,6),
         2:(6,7,0),
         3:(2,3,4),
         }
relate = {0:1,
          1:5,
          2:7,
          3:3,
          }

moving = 1; rounds = 0
#while moving and rounds < 10: part 1
while moving:
    rounds += 1
    moving = 0
    nextPoint = dict()
    for i in range(len(points)):
        # Checks if there is anything around the point
        clean = 1
        for j in range(8):
            if pointsLookup.get((points[i][0]+dy[j],points[i][1]+dx[j])) == 1:
                clean = 0

        if clean:
            nextPoint.setdefault((points[i][0],points[i][1]),[])
            nextPoint[(points[i][0],points[i][1])].append((points[i][0],points[i][1]))
            continue
        
        moving = 1
        
        valid = 0

        # Checks for which direction the elf proposes
        for l in range((4+rounds-1)%4,(4+rounds-1)%4+4,1):
            j = l%4
            good = 1
            for k in range(3):
                if pointsLookup.get((points[i][0]+dy[check[j][k]],points[i][1]+dx[check[j][k]])) == 1:
                    good = 0

            if good:
                nextPoint.setdefault((points[i][0]+dy[relate[j]],points[i][1]+dx[relate[j]]),[])
                nextPoint[(points[i][0]+dy[relate[j]],points[i][1]+dx[relate[j]])].append((points[i][0],points[i][1]))
                valid = 1
                break

        # This caters for the case where the point can't move
        if not valid:
            nextPoint.setdefault((points[i][0],points[i][1]),[])
            nextPoint[(points[i][0],points[i][1])].append((points[i][0],points[i][1]))

    points = []
    pointsLookup = dict()
    for point in nextPoint.keys():
        # This prevents collisions
        if len(nextPoint[point]) != 1:
            for second in nextPoint[point]:
                points.append(second)
                pointsLookup[second] = 1
            continue


        # This just does normal transitions
        points.append(point)
        pointsLookup[point] = 1


""" part 1
minX = int(1e9); minY = int(1e9)
maxX = int(-1e9); maxY = int(-1e9)

for point in points:
    minX = min(minX,point[0])
    maxX = max(maxX,point[0])
    minY = min(minY,point[1])
    maxY = max(maxY,point[1])

print((maxY-minY+1)*(maxX-minX+1) - len(points))
"""
print(rounds)

