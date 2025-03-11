import pickle as p
a = open("D2.txt", "a+")
b = open("D2.pkl","ab")
ind=0
while True:
    if ind > 0:
        en=input("Want to exit, click on X :: ")
        if(en=="X" or en=="x"):
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
a.close()
b.close()
xxxx = open("D2.pkl", "rb")
try:
    # Use a loop to read all serialized objects
    while True:
        r = p.load(xxxx)
        print(r)
except EOFError:
    # End of file is reached
    print("End of file reached!")
finally:
    # Close the file
    xxxx.close()
print("Thank you")