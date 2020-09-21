try: 
    my_list = []
    x=0 
    while True: 
        my_list.append(int(input())) 
except: 
    print(my_list) 
result =my_list[0]
for i in my_list:
    if i>result:
        result=i
print(result)
