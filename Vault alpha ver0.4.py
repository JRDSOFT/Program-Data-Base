#newest version fo Vault
#this version we can find a better interface, animations and (maybe) another option.
#this part  is import modules part 
from collections import deque# this module import a pile where is use for import file
from datetime import datetime#import date automaticaly on file.txt
import os, platform#import commands for all systems and check where in os programm's running
#this is the formules's part for import, export etc etc.
def inlist():#this function update list file
    try:
        date=open("list.txt", "a+")#open file list.txt in write mode 
        date.write("|+"+name_file+"\n")#write name file on list 
        date.close()#close list
    except FileExistsError:#check if the file exist
            clearshell()
            print("""
 _ 
| |
| |
|_|
(_)
""")
            print("|+error, file exist")
def imp_file(): #this function it's used for create new file and insert all input on new file
        quest = deque (["type:", "version:", "description:",])#this pile is use on input wait
        ans = deque (["|+type = ", "|+version = ", "|+description = "])#this pile is used with base.write
        try:
            if platform.system()=="Windows":#if the os is Windows run this|
                base=open("archives\\ "+name_file+".txt", "x+")#<---------
            elif platform.system()=="Linux":#else os is Linux run this|
                base=open("archives/ "+name_file+".txt", "x+")#<---------
        except FileExistsError:#check if the file exist
            clearshell()
            print("""
 _ 
| |
| |
|_|
(_)
""")
            print("|+error, file exist")
        else:
            base.write("|+name= "+name_file+"\n")#insert archive name on file list.txt
            for allforone in range(3):#repeat loop for print same message but with a differend words
                a2=input("|+insert "+quest.popleft()+"\n")#print same message but with a differend words
                base.write(ans.popleft()+a2+"\n")#write info on file.txt but with a differend words
            t=datetime.now()#take date of today
            date=t.strftime("%d-%m-%Y")#convert date to string
            base.write("|+start dev= "+date)#save the date of today
            base.close()#close file

def show_list():#print all text contenet on list.txt
    print_list=open("list.txt", "r+")#open list on read mode
    red=print_list.read()
    print(red)
    print_list.close()

def show():#print infos
    clearshell()
    try:
        if platform.system()=="Windows":#if the os is Windows run this|
                    print_info=open("archives\\ "+temp+".txt", "r+" )#<---------
                    for allforone in range(6):
                        red=print_info.readline()
                        print(red)
                    print_info.close
        elif platform.system()=="Linux":#else os is Linux run this|
                    print_info=open("archives/ "+temp+".txt", "r+" )#<--------- 
                    for allforone in range(6):
                        red=print_info.readline()
                        print(red)
                    print_info.close   
    except File:#check if the file exist
            clearshell()
            print("""
 _ 
| |
| |
|_|
(_)
""")
            print("|+error, wrong name or input")


def clearshell():#clear shell
    if platform.system()=="Windows":
        os.system("cls")
    elif platform.system()=="Linux":
        os.system("clear")

#menu for chose what we want do
print("""
__     __          _ _                     ___   _____ 
\ \   / /_ _ _   _| | |_  __   _____ _ __ / _ \ |___ / 
 \ \ / / _` | | | | | __| \ \ / / _ \ '__| | | |  |_ \ 
  \ V / (_| | |_| | | |_   \ V /  __/ |  | |_| | ___) |
   \_/ \__,_|\__,_|_|\__|   \_/ \___|_|   \___(_)____/ 
""")
ans1=input("""
|+Press I if you want import info
|+Press S if you want show archives
|+Press M if you want mod info or archives
|+Press D if you want del info or archives
|+Press E if you want exit 
""")
if ans1=="i":
        ans2="y"
        while ans2 =="y":
                clearshell()
                print("""
 ___                            _   
|_ _|_ __ ___  _ __   ___  _ __| |_ 
 | || '_ ` _ \| '_ \ / _ \| '__| __|
 | || | | | | | |_) | (_) | |  | |_ 
|___|_| |_| |_| .__/ \___/|_|   \__|
              |_|                   
""")
                
                name_file=input("|+Insert name archive:\n")#user insert name's file and will save on file .txt
                inlist()#recall repeat_ins function
                imp_file()
                ans2=input("|+Do you want insert another file? Y|N\n")#ask to user if he/she want insert another file
        temp=name_file
        del name_file
        ans3 =input("|+Do you want see file already created? Y|N\n")
        if ans3 == "y":
            clearshell()
            show()
            input("|+Done, bye")#print info already created and print bye, the programm stop working
        else:
            input("|+Bye")#print bye and the programm stop working

            
        
elif ans1=="s":
        ans2="y"
        while ans2 =="y":
            clearshell()
            print("""
 ____  _                   
/ ___|| |__   _____      __
\___ \| '_ \ / _ \ \ /\ / /
 ___) | | | | (_) \ V  V / 
|____/|_| |_|\___/ \_/\_/  
""")
            show_list()#repeat prewious work
            temp=input("|+Insert name archive print now on screen: \n")
            show()        
            ans2=input("|+Do you want to see another file? Y/N\n")#ask again to user if he/she want see another file
        input("|+Bye")#print bye and the programm stop working

elif ans1=="m":
        clearshell()
        print("""
 __  __           _ _  __       
|  \/  | ___   __| (_)/ _|_   _ 
| |\/| |/ _ \ / _` | | |_| | | |
| |  | | (_) | (_| | |  _| |_| |
|_|  |_|\___/ \__,_|_|_|  \__, |
                          |___/ 
""")
        print("|+work in proggress")

elif ans1=="d":
        clearshell()
        print("""
 ____       _      _       
|  _ \  ___| | ___| |_ ___ 
| | | |/ _ \ |/ _ \ __/ _ \ 
| |_| |  __/ |  __/ ||  __/
|____/ \___|_|\___|\__\___|
""")
        print("|+work in proggress")

elif ans1=="e":
        clearshell()
        print("""
""")
        print("|+work in proggress")

else:
        print("|+work in proggress")
