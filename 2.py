f = open("2Input.txt","r")

# I spammed wa a lot here because I didn't read the question fully
# I need to take more time at the start to understand what is being asked

out = 0
s = f.read().split("\n")
for i in s:
    shapes = i.split(" ")
    if len(shapes) != 2:
        break
    p1 = ord(shapes[0])-65
    p2 = ord(shapes[1])-88

    """ This is for part 1
    out += p2+1
    if p1 == p2:
        out += 3
    elif (p1+1)%3 == p2:
        out += 6
    else:
        out += 0
    """

    # This is for part 2
    if p2 == 1:
        out += 3 + p1+1
    elif p2 == 2:
        out += 6 + (p1+1)%3 + 1
    else:
        out += 0 + (p1-1)%3 + 1

print(out)

f.close()
