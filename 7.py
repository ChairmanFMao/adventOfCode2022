f = open("7Input.txt","r")

lines = [i.split(" ") for i in f.read().split("\n")]
lines.pop()

# We are going to store the directories in a tree structure

# Stores the edges within the graph
adj = dict()
# Stores the weight of each of the nodes
w = dict()
# Acts as a stack to keep which directory we are in
st = ["init"]

ptr = 0
while ptr < len(lines):
    line = lines[ptr]
    # Takes care of changing directory
    if line[1] == "cd":
        if line[2] == "/":
            st = ["init"]
        elif line[2] == "..":
            st.pop()
        else:
            st.append(line[2])
        ptr += 1
    # Takes care of adding files to directories
    if line[1] == "ls":
        ptr += 1
        line2 = lines[ptr]
        # This goes through all the files within the directory
        while ptr < len(lines) and line2[0] != "$":
            # This adds a new directory
            if line2[0] == "dir":
                adj.setdefault("/".join(st), [])
                adj["/".join(st)].append(line2[1])
            # This adds a new file to the current directory
            else:
                w.setdefault("/".join(st), 0)
                w["/".join(st)] += int(line2[0])
            ptr += 1
            if ptr >= len(lines):
                break
            line2 = lines[ptr]

# Now I need to do a final dfs to get all the weights
def dfs(node):
    w.setdefault(node, 0)
    adj.setdefault(node,[])
    for i in adj[node]:
        dfs(node+"/"+i)
        w[node] += w[node+"/"+i]

dfs("init")

""" part 1
out = 0
print(w)
for i in w.values():
    if i <= 100000:
        out += i

print(out)
"""

current = 70000000 - w["init"]

out = int(1e10)
for i in w.values():
    if current + i >= 30000000:
        out = min(out,i)

print(out)

f.close()

