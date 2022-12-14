f = open("13Input.txt","r")

lines = f.read().split("\n\n")
f.close()

pairs = [i.split("\n") for i in lines]

# They just want us to do a sorting algorithm for part 2

# Can return 3 values
# 0 means undetermined
# 1 means right order
# 2 means wrong order
def evaluate(first, second):
    fptr = 0; sptr = 0
    while fptr < len(first) and sptr < len(second):
        if isinstance(first[fptr],list) and isinstance(second[sptr],list):
            val = evaluate(first[fptr],second[sptr])
        elif isinstance(first[fptr],list):
            val = evaluate(first[fptr],[second[sptr]])
        elif isinstance(second[sptr],list):
            val = evaluate([first[fptr]],second[sptr])
        else:
            val = 0 if first[fptr] == second[sptr] else 1 if first[fptr] < second[sptr] else 2

        if val:
            return val

        fptr += 1
        sptr += 1

    # Needed to cater for case when both had reached the end together
    return 0 if fptr == len(first) and sptr == len(second) else 1 if fptr == len(first) else 2

out = 0
items = []
for i in range(len(pairs)):
    first = eval(pairs[i][0])
    second = eval(pairs[i][1])

    """ part 1
    if evaluate(first,second) == 1:
        #print("good",first,second)
        print(i+1)
        out += i+1
    """

    items.append(first)
    items.append(second)

a = [[2]]; b = [[6]]
items.append(__import__("copy").deepcopy(a))
items.append(__import__("copy").deepcopy(b))

# This is just an implementation of bubble sort
for i in range(len(items)):
    for j in range(len(items)-1):
        if evaluate(items[j],items[j+1]) == 2:
            items[j], items[j+1] = items[j+1], items[j]

out = 1
# This just goes through all of the elements and finds where a and b are stored
for i in range(len(items)):
    if evaluate(items[i],a) == 0:
        out *= i+1
    if evaluate(items[i],b) == 0:
        out *= i+1

print(out)

