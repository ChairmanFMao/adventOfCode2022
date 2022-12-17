from collections import deque

f = open("16Input.txt","r")

lines = f.read().split("\n")
lines.pop()
f.close()

# tunnels form a graph and we need to navigate it to find which
# node that we want to visit first
# we want to release as much pressure as possible
# Just like a dfs of depth 30 maybe?
# Actually I think a brute force approach would timeout
# very few nodes have an actual flow rate
# Just make a graph of the flow rate nodes and how to get there from each
# do a bfs from every node and then do a brute force on the simplified graph
# I successfully coded this up and it got part 1
# the second person adds more complications to the code

adj = dict()
flow = dict()
for line in lines:
    unique = line.split(" has flow")[0].replace("Valve ","")
    adj[unique] = []
    currentFlow = int(line.split("=")[1].split(";")[0])
    if currentFlow:
        flow[unique] = currentFlow
    for edge in line.split("valve")[1].replace("s","").strip().split(", "):
        adj[unique].append(edge)

flowArr = [i for i in flow.keys()]

INF = int(1e9)
# we will brute force all the paths and then do brute force
dist = dict()
for start in adj.keys():
    dist[start] = dict()
    for val in adj.keys():
        dist[start][val] = INF

    dist[start][0] = 0
    q = deque()
    q.append((start,0))
    while len(q):
        current = q.popleft()
        dist[start].setdefault(current,INF)
        if current[1] >= dist[start][current]:
            continue

        dist[start][current] = current[1]
        for u in adj[current[0]]:
            dist[start].setdefault(u,INF)
            if current[1]+1 < dist[start][u]:
                dist[start][u] = current[1]+1
                q.append((u,current[1]+1))

""" part 1
output = 0; end = 30
def dfs(node, seen, current, out, time):
    global output, itr
    itr += 1
    #print(node,seen,current,out,time,out + current*(end-time))
    output = max(output,out+current*(end-time))

    for i in range(len(flowArr)):
        # This means that it hasn't been seen
        if not (seen&(1<<i)):
            if dist[node][flowArr[i]] > end-time:
                output = max(output,out + current*(end-time));
                continue
            dfs(flowArr[i],seen|(1<<i), current+flow[flowArr[i]], out + (dist[node][flowArr[i]]+1) * current, time+dist[node][flowArr[i]]+1)

dfs("AA",0,0,0,0)
"""

# for part 2 I am thinking of modifying the dfs search I currently
# use and just have the elephant and person working in parallel
# getting 1675 for the sample when it should be 1707
# This code works for the sample but is really slow when run
# on the actual test case, time complexity might be very bad
# potentially just set who gets which and brute force like that
# takes like 1e5 operations for each go
# there are 15 nodes, leads to 2**15
# This leads to like 1e10 complexity
# This might actually be possible
# This takes like 5-10 mins to run but it gets the right answer
# This is because the middle nodes take less operations like 1e3

output = 0; end = 26
def dfs(node, seen, current, out, time, possible):
    global output
    #print(node,seen,current,out,time,out + current*(end-time))
    output = max(output,out+current*(end-time))

    for i in possible:
        # This means that it hasn't been seen
        if not (seen&(1<<i)):
            if dist[node][flowArr[i]] > end-time:
                output = max(output,out + current*(end-time));
                continue
            dfs(flowArr[i],seen|(1<<i), current+flow[flowArr[i]], out + (dist[node][flowArr[i]]+1) * current, time+dist[node][flowArr[i]]+1,possible)

finalOut = 0
for i in range(1<<(len(flowArr)-1)):
    print(i)
    tmp = 0
    arr = []; arr2 = []
    for j in range(len(flowArr)):
        if i&(1<<j):
            arr.append(j)
        else:
            arr2.append(j)
    dfs("AA",0,0,0,0,arr)
    tmp += output
    output = 0
    dfs("AA",0,0,0,0,arr2)
    tmp += output
    output = 0
    finalOut = max(finalOut,tmp)

print(finalOut)

