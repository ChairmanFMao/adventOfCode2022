file = open("11Input.txt","r")

lines = file.read().split("\n")
lines.pop()

# To solve part 2 we just store all of the numbers under a modulo
# that is the product of all the divisibility checks we may need
# to do

# This stores all the information about each monkey
class Monkey:
    def __init__(self,operation,div,t,f):
        self.operation = operation
        self.div = div
        self.t = t
        self.f = f

    # Performs the monkey's operation on the value
    def op(self,val):
        return eval(self.operation.replace("old",str(val)))

    # Returns the index for the next bit
    def location(self,val):
        return self.f if (val%self.div) else self.t

monkeys = []
vals = []

i = 0; mod = 1
while i < len(lines):
    vals.append([])
    # Adds all of the starting values
    for j in lines[i+1].split(": ")[1].split(", "):
        vals[-1].append(int(j))

    operation = lines[i+2].split("new = ")[1]
    div = int(lines[i+3].split(" by ")[1])
    t = int(lines[i+4].split("monkey ")[1])
    f = int(lines[i+5].split("monkey ")[1])
    monkeys.append(Monkey(operation,div,t,f))
    mod *= div

    i += 7

ROUNDS = 10000

inspects = [0 for i in range(len(monkeys))]
for i in range(ROUNDS):
    print(i)
    for j in range(len(monkeys)):
        for k in range(len(vals[j])):
            inspects[j] += 1
            current = vals[j][k]
            current = monkeys[j].op(current)
            #current //= 3
            current %= mod
            location = monkeys[j].location(current)
            vals[location].append(current)
        vals[j].clear()

inspects.sort(reverse=True)
print(inspects[0]*inspects[1])

file.close()

