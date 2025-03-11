import pickle as p
a = open("D2.txt", "a+")
ind = 0
while True:
    if ind > 0:
        b=input("Want to exit, click on X")
        if(b=="X" or b=="x"):
            break
    a11=input("Enter Name of person :: ")        
    a.write(f"Name :: {a11}  ")
    a12=input("Enter degree of the person :: ")  
    a.write(f"Degree :: {a12}  ")
    ind+=1  
print("Thank you")    
a.close()     