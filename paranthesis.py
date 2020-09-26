<<<<<<< HEAD
x = "{[()[({})]]}"
for i in range(len(x)//2):
    x = x.replace("()", "")
    x = x.replace("[]", "")
    x = x.replace("{}", "")
=======
x = "{[]}"
for i in range(len(x)//2):
    x = x.replace("()","")
    x = x.replace("[]","")
    x = x.replace("{}","")
>>>>>>> a08daceccaba833f5aa10f5808b7c0c0adb23f7c
print(not bool(x))
