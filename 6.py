# This isn't really optimal time complexity
# However it was just easiest to code

f = open("6Input.txt","r")

s = f.read()

for i in range(len(s)):
    u = set()
    for j in range(i,i+14):
        u.add(s[j])

    if len(u) == 14:
        print(i+14)
        break

f.close()
