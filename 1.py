# I decided to just make it in one line for fun
# To solve part 1 just change the [0:3] bit to [0:1]

with open("1Input.txt","r") as f: print(sum(sorted([sum([int("0"+j) for j in i.split("\n")]) for i in f.read().split("\n\n")],reverse=True)[0:3]))
