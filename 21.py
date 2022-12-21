f = open("21Input.txt","r")

lines = f.read().split("\n")
lines.pop()
f.close()

# I think that we can just resolve this recursively
# for part 2 I am thinking of getting all the numbers possible
# processed and then working backwards from root
# I have stored all of the values that need to be calculated
# using the key -1e9 as their first value

# This stores the values of the monkeys
vals = dict()

# This recursively solve the problem
def recur(monkey):
    # This is the base case where the value has been calculated
    if len(vals[monkey]) <= 2:
        return

    # This recursively evaluates the two varaibles in the current
    # expression
    recur(vals[monkey][0])
    recur(vals[monkey][2])
    # This is for the root case
    if monkey == "root":
        vals[monkey] = [max(vals[vals[monkey][0]][0],vals[vals[monkey][2]][0]),vals[monkey]]
        return

    # This is to merge cases where we don't know the result
    if vals[vals[monkey][0]][0] == int(-1e9) or vals[vals[monkey][2]][0] == int(-1e9):
        vals[monkey] = [int(-1e9),vals[monkey]]
        return


    # This sets the value of the current monkey in the dictionary
    # using an eval statement
    vals[monkey] = [int(eval(str(vals[vals[monkey][0]][0])+vals[monkey][1]+str(vals[vals[monkey][2]][0])))]

# This is for part 2
# We will know the desired result and one of the inputs but we
# need to solve the equation for the last unknown
def recurDown(monkey):
    # We know desired, the operation and one of first and second
    if len(vals[monkey]) < 2:
        return
    # This gets all of the parts of the expression
    desired = vals[monkey][0]
    first = vals[vals[monkey][1][0]][0]
    operation = vals[monkey][1][1]
    second = vals[vals[monkey][1][2]][0]

    # This is the edge case where we process the root
    if monkey == "root":
        if first == int(-1e9):
            vals[vals[monkey][1][0]][0] = desired
            recurDown(vals[monkey][1][0])
        if second == int(-1e9):
            vals[vals[monkey][1][2]][0] = desired
            recurDown(vals[monkey][1][2])
        return

    # This solves the equation and evaluates expressions further
    # down the structure
    if first == int(-1e9):
        if operation == "+":
            first = desired-second
        if operation == "-":
            first = desired+second
        if operation == "*":
            first = desired//second
        if operation == "/":
            first = desired*second
        vals[vals[monkey][1][0]][0] = first
        recurDown(vals[monkey][1][0])
    if second == int(-1e9):
        if operation == "+":
            second = desired-first
        if operation == "-":
            second = first-desired
        if operation == "*":
            second = desired//first
        if operation == "/":
            second = first//desired
        vals[vals[monkey][1][2]][0] = second
        recurDown(vals[monkey][1][2])


# This reads in all of the lines and processes them
for line in lines:
    seperated = line.split()
    if len(seperated) == 2:
        vals[seperated[0].replace(":","")] = [int(seperated[1])]
    else:
        vals[seperated[0].replace(":","")] = seperated[1:]

vals["humn"] = [int(-1e9)]

recur("root")
recurDown("root")
print(vals["humn"])

