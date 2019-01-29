import os as sis #import sistem command like cmd
#this function import info into one file
#import list for this function.
def listar(): #this function add voice in list
    lis=open("list.txt", "w+")
    lis.write(name+"\n")
    lis.close()
   

#start program
print("welcome to program data base\n")#title screen
a=input("press I for import program's infos.\npress S to see program's infos already created.\npress D to delete program's infos already created \n")# instuction for use program
if a=="i":#import sistem, a= is a char and is use for insert an input for if, elif and else.
    name=input("write program's name here \n")#name is a variable where you find a program's name
    listar()
    prg=open(name+".txt", "w+")#create new file where import program's info
    prg.write("name="+name+"\n")#import name
    nar=["program type", "program description", "start dev data"]
    nar2=["type", "desc.prog", "startdev"]
    for i=="2":
        i="0"
        b=input("insert"+nar.pop(i)+"\n")#give a output then insert a type program, the info will save on b variable 
        i=+1
    if:
        prg.write(nar2+"="+b+"\n")#write on the file the info that contained on b
    prg.close()


elif a=="s": #display all file and infos of one file
    g=open("list.txt", "r")
    lil=g.read()
    print("this is infos existing")
    print(lil)
    g.close()
    name=input("write program name \n")
    prg=open(name+".txt", "r")
    red= prg.read()
    print(red )
    input("press any button to continue")
elif a=="d":# del one file than you have created
    g=open("list.txt", "r")
    lil=g.read()
    print("this is infos existing")
    print(lil)
    g.close()
    name=input("insert program name. \n")
    sis.remove(name+".txt")
    g=open("list.txt", "r+")
    oldname=g.read()
    g.close()
    newname=oldname.replace(name, "")
    newname.strip()
    g2=open("list.txt", "w+")
    g2.write(newname)
    g2.close()
else:
     print("error, you have insert wrong letter, program shutting down, bye")
     input("press any key to continue.")

#debug log:
#   find a for o while loop, array and lists/dictionary.
#   insert a 4th option, modify option.
#   insert "stop dev" and "status" voices.
#-------------------------------------------------
#Copyright (c) 2018 JRDSOFT All rights reserved.