import itertools
s = input()
ss = set()
m = -1
for i in s:
    if i.isdigit():
        ss.add(i)

        ll = list(itertools.permutations(ss, len(ss)))
        for x in ll:
            k = "".join(x)
            if int(k) % 2 == 0 and int(k) > m:
                m = int(k)

print(m)

# inputs
# infosys@337
# Hello#81@21349
