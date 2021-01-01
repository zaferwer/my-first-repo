Q = int(input())
result = []
for i in range(Q):
    req = list(map(int, input().split(" ")))
    if req[0] == 1:
        result.append(req[1])
    elif req[0] == 2:
        result.remove(req[1])
    elif req[0] == 3:
        print(min(result))
