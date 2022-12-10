f = open("9Input.txt","r")

lines = f.read().split("\n")
lines.pop()

def dif(a,b):
    return max(abs(a[0]-b[0]),abs(a[1]-b[1]))

d = {"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)}

""" part 1
h = (0,0)
t = (0,0)
"""

pos = [(20,20) for i in range(10)]

seen = set()

# Getting 80 on the test case where I should get 36

for line in lines:
    tmp = line.split()

    for i in range(int(tmp[1])):
        """ part 1
        nextH = (h[0]+d[tmp[0]][0], h[1]+d[tmp[0]][1])
        if dif(nextH,t) >= 2:
            t = (h[0],h[1])
        h = (nextH[0],nextH[1])
        """

        # We always move diagonally
        # To do this I might need to alter the code
        # Just do coordinates of the next minus current and turn all 2 in 1
        # I think that this might work
        pos[0] = (pos[0][0]+d[tmp[0]][0],pos[0][1]+d[tmp[0]][1])

        for j in range(1,len(pos)):
            # This checks if the current part needs to move
            if dif(pos[j],pos[j-1]) >= 2:
                # This gets the vector that the part will move
                move = [pos[j-1][0] - pos[j][0], pos[j-1][1] - pos[j][1]]
                # This allows the parts to connect diagonally
                if abs(move[0]) == 2:
                    move[0] //= 2
                if abs(move[1]) == 2:
                    move[1] //= 2
                pos[j] = (pos[j][0] + move[0], pos[j][1] + move[1])

        seen.add(pos[-1])

print(len(seen))

f.close()

