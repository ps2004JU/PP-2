import pickle as p
a = open("D1.txt", "a+")
a11=input("Enter something inside the file :: ")
a.writelines(a11,end="\n")
print("Success")
print(a.read())
a.close()
