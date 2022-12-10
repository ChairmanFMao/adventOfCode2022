f = open("4Input.txt","r")

lines = f.read().split()
out = 0

for line in lines:
    ranges = line.split(",")
    left = list(map(int,ranges[0].split("-")))
    right = list(map(int,ranges[1].split("-")))
    
    """ part 1
    # Checks if right within left
    if left[0] <= right[0] and right[1] <= left[1]:
        out += 1
    # Checks if left within right
    elif right[0] <= left[0] and left[1] <= right[1]:
        out += 1
    """

    # Checks if right within left
    if left[0] <= right[0] and right[1] <= left[1]:
        out += 1
    # Checks if left within right
    elif right[0] <= left[0] and left[1] <= right[1]:
        out += 1
    # Checks if ends of the right range are within left range
    elif left[0] <= right[0] and right[0] <= left[1]:
        out += 1
    elif left[0] <= right[1] and right[1] <= left[1]:
        out += 1

print(out)

f.close()
