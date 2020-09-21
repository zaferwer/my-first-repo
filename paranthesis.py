x = ""
xlist=list(x)
for i in ["()","{}","[]"]:
    if i in x or len(x)==0:
        result=True
    else:
        for i in range(len(xlist)//2):
            if xlist[i]=="(" and xlist[-(i+1)]==")":
                result=True
            elif xlist[i]=="[" and xlist[-(i+1)]=="]":
                result=True
            elif xlist[i]=="{" and xlist[-(i+1)]=="}":
                result=True
            else:
                result=False
print(result)
