dot = int(input()) # depth
line = int(input())

table = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def s(pos):
    k = 0
    while k < dot:
        if table[pos][k] == 1:
            print(k + 1, end = "")
            table[pos][k] = 0
            s(k)
            k += 1
        else:
            k += 1

i = 1
while i <= line:
    n = int(input())
    m = int(input())
    table[n - 1][m - 1] = 1
    i += 1

print(0, end = "")
s(0)