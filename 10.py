f = open("10Input.txt","r")

lines = f.read().split("\n")
lines.pop()

# This was quite a fun problem

val = 1; out = 0; extra = 0; ptr = 0; i = 0
crt = []
while ptr < len(lines):
    """ part 1
    if i%40 == 19:
        out += val * (i+1)
    """

    if i % 40 == 0:
        crt.append("")
    if abs(val-i%40) <= 1:
        crt[-1] += "#"
    else:
        crt[-1] += "."

    if extra:
        val += extra
        extra = 0
    elif ptr < len(lines):
        if lines[ptr] != "noop":
            extra = int(lines[ptr].split()[1])
        ptr += 1

    i += 1

# print(out)

for i in crt:
    print(i)

f.close()
