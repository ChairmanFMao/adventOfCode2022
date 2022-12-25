f = open("25Input.txt","r")

lines = f.read().split()
f.close()

convertDec = {'2':2,'1':1,'0':0,'-':-1,'=':-2}
convertSnaf = {2:'2',1:'1',0:'0',-1:'-',-2:'='}

def toDec(s):
    current = 0; power = 1
    s = s[::-1]
    for i in range(len(s)):
        current += convertDec[s[i]] * power
        power *= 5
    return current

def toSnaf(num):
    current = []; power = 1
    while num:
        power *= 5
        current.append((num%power)//(power//5))
        num //= power
        num *= power

    current.append(0)

    for i in range(len(current)-1):
        if current[i] >= 3:
            current[i] -= 5
            current[i+1] += 1

    # Removes leading zeros from the output
    while not current[len(current)-1]:
        current.pop()

    current = current[::-1]
    s = ""
    for i in current:
        s += convertSnaf[i]
    return s

out = 0
for line in lines:
    out += toDec(line)

print(toSnaf(out))

