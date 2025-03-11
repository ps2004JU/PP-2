import pickle as p
a = open("D1.txt", "a+")
a11=input("Enter something inside the file :: ")
a.write(f"{a11}\n")
print("Success")
a.close()
