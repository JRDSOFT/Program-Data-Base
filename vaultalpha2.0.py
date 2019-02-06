from collections import deque# this import piles module
from datetime import date#import date 
#this part is reserved for the functions for the programm
def update_list(): #make/update list for see the archives then we made
    date=open("list.txt", "w+")#open file list
    date.write(name_file+"\n")#write archive's name on file 
    date.close()#close file

def imp_file(): #this function can be used only for insert function
        cos = deque (["type:", "version:", "description:",])#this  print out all words on the pile
        cos2 = deque (["type=", "version=", "description="])#it's used on base.write
        base=open("archives/ "+name_file+".txt", "x+")#create archive
        base.write("name="+name_file+"\n")#insert archive name on file list.txt
        for allforone in range(3):#repeat loop for print same message but with a differend words
            a2=input("insert "+cos.popleft()+"\n")#print same message but with a differend words
            base.write(cos2.popleft()+a2+"\n")#write info on file.txt but with a differend words
        today = date.today()
        base.write("start dev= "+ today)
        base.close()#close file

def rep_ins():
        name_file=input("insert name archive:\n")#user insert name's file and will save on file .txt
        update_list()#recall update list function 
        imp_file()#recall import file funcition
        
def rep_see():
    show_list()
    temp=input("insert name archive print now on screen \n")
    show()

def show_list():
    print_list=open("list.txt", "r+")
    red=print_list.read()
    print(red)
    print_list.close()

def show():
    print_info=open("archives/ "+temp+".txt", "r+" )
    for allforone in range(4):
        red=print_info.readline()
        print(red)
    print_info.close

#main menu
print("welcome to vault ver:1.1\n")#title screen
ans1=input("press I for import program's infos.\npress S to see program's infos already created.\npress D to delete program's infos already created \n")# ans is used for select one of 4 options avariable
if ans1=="i":#1°option, import all informations and will save in a file.txt
        name_file=input("insert name archive:\n")#user insert name's file and will save on file .txt
        update_list()#recall update list function 
        imp_file()#recall import file funcition
        print("done\n")#print done message
        ans2=input("do you want insert another file? Y/N\n")#ask to user if he/she want insert another file
        while ans2 =="y":
                rep_ins()#recall repeat_ins function
                ans2=input("do you want insert another file? Y/N\n")#ask to user if he/she want insert another file
        input("bye")#print bye and the programm stop working
elif ans1 =="s":#2°option, print list.txt and print all informations that had saved on a archive
        show_list()#print list
        temp=input("insert name archive print now on screen \n")#user insert archive name
        show()#print all info saved on file.txt
        ans2=input("do you want to see another file? Y/N\n")#ask to user if he/she want see another file
        while ans2 =="y":
                    rep_see()#repeat prewious work
                    ans2=input("do you want to see another file? Y/N\n")#ask again to user if he/she want see another file
        input("bye")#programm stop

else:
     input("command error, shutting down, bye")#print this message when the user insert wrong letter

#debug log:
#   inserire voci STOP DEV e STATUS in modifica.
#   inserire la seconda opzione, visualizzazione dati.
#   inserire terza opzione, modifica file.
#   inserire quarta opzione, cancellazione file.
#   
#-------------------------------------------------
#Copyright (c) 2018 JRDSOFT All rights reserved.
