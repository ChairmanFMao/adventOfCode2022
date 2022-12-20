from collections import deque

f = open("20Input.txt","r")

lines = f.read().split()
f.close()

vals = [[int(lines[i]),i] for i in range(len(lines))]

# Quite happy that I got this to work quickly
# Its really easy to do with the python deque

# This is for part 2
for i in range(len(vals)):
    vals[i][0] *= 811589153

q = deque(vals)

# This is also for part 2
for j in range(10):
    for i in range(len(lines)):
        # This gets the next element we want to process to the
        # front of the queue
        while q[0][1] != i:
            q.rotate(1)

        # This removes the current element
        # Then applies the rotation
        # inserts it back into the deque
        # then it rotates it back so that it is just like
        # making an insertion and a removal
        current = q.popleft()
        q.rotate(-current[0])
        q.appendleft(current)
        q.rotate(current[0])

# This aligns it so that the 0 element is at the start
out = 0
while q[0][0]:
    q.rotate(1)

# This is to get the final output
for i in range(3):
    q.rotate(-1000)
    out += q[0][0]

print(out)

