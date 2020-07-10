number = int(input("Please enter the number you want to learn if it is a prime number:"))
#this part is for making the program faster. 
if number%2==0 or number<0:
    print(f"{number} is NOT a prime number")
else:    
    for i in range(2,number):
        if number%i==0:
            print(f"{number} is NOT a prime number")
            break 
        else:
            print(f"{number} is a prime number")
            break 
