f = open("5Input.txt","r")

lines = f.read().split("\n")
lines.pop()

st = []
for i in range(0,9):
    st.append(lines[i].split())

for i in range(9,len(lines)):
    move = lines[i].split()
    times = int(move[1])
    start = int(move[3]); start -= 1
    end = int(move[5]); end -= 1
    tmp = []
    for j in range(times):
        tmp.append(st[start][len(st[start])-1])
        st[start].pop()

    """ part 1
    for j in range(times):
        st[end].append(tmp[j])
    """
    for j in range(times-1,-1,-1):
        st[end].append(tmp[j])

for i in range(9):
    print(st[i][len(st[i])-1],end="")

f.close()
