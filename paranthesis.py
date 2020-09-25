x = "(){((([])))}"
for i in x:
    x = x.replace("()","")
    x = x.replace("[]","")
    x = x.replace("{}","")
print(not bool(x))
