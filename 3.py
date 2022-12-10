f = open("3Input.txt","r")

lines = f.read().split()

out = 0
""" This is for part 1
for line in lines:
    n = len(line)
    s = set()
    for i in range(n//2):
        s.add(line[i])

    for i in range(n//2,n):
        if line[i] in s:
            out += ord(line[i]) - (64-26 if line[i].isupper() else 96)
            break
"""

for i in range(0,len(lines),3):
    seen = dict()
    for j in range(i,i+3,1):
        unique = list(set(list(lines[j])))
        for k in unique:
            if (seen.get(k) == None):
                seen[k] = 0
            seen[k] += 1

    for j in seen.keys():
        if seen[j] == 3:
            out += ord(j) - (64-26 if j.isupper() else 96)

print(out)

f.close()
