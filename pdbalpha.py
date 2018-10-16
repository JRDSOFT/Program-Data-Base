print("welcome to program data base")
a=input("press I for import program's info, or press S to see program's info already created. \n")
if a=="i":
    name=input("write program's name here \n")
    prg=open(name+".txt", "w+")
    prg.write(name+"\n")
    b=input("insert program's type \n")
    prg.write("type="+b)
    prg.close()

elif a=="s":
    name=input("write program's name \n")
    prg=open(name+".txt", "r")
    red= prg.read()
    print(red )
else:
     print("error, you have insert wrong letter, program shutting down, bye")