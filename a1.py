import pickle as p
a = open("D2.txt", "a+")
b = open("D2.pkl","ab")
ind=0
while True:
    if ind > 0:
        b=input("Want to exit, click on X")
        if(b=="X" or b=="x"):
            break
    ax=input("Enter Name of person :: ")        
    a.write(f"Name :: {ax}  ")
    p.dump(f"Name :: {ax} ",b)
    a12=input("Enter degree of the person :: ")  
    a.write(f"Degree :: {a12}  ")
    p.dump(f"Degree:: {a12} ",b)
    a13=input("Enter Alma Mater of the person :: ")  
    a.write(f"Alma Mater :: {a13}\n")
    p.dump(f"Alma Mater :: {a13}\n",b)
    ind+=1        
print("Thank you")    
a.close()     