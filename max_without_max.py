try: 
    my_list = [] 
      
    while True: 
        my_list.append(int(input())) 
except: 
    print(my_list) 
result =my_list[0]
for i in my_list:
    if i>result:
        result=i
    else:
        pass
print(result)
