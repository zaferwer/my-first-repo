s = input(int)
times = int(s)
print("#" * times)
for i in range(times - 2):
    print("#" + " " * (times - 2) + "#")
if times > 1:
    print("#" * times)
