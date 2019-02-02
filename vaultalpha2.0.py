from collections import deque# this import piles module
#this part is reserved for the functions for the programm
def update_list(): #make/update list for see the archives then we made
    date=open("list.txt", "w+")#open file list
    date.write(name_file+"\n")#write archive's name on file 
    date.close()#close file

def imp_file(): #this function can be used only for insert function
        cos = deque (["type:", "version:", "start dev:", "description:"])#this  print out all words on the pile
        cos2 = deque (["type=", "version=", "start dev=", "description="])#it's used on base.write
        base=open("archives\ "+name_file+".txt", "w+")#create archive
        base.write("name= "+name_file+"\n")
        for allforone in range(4):
            a2=input("insert "+cos.popleft()+"\n")
            base.write(cos2.popleft()+a2+"\n")
        base.close()

def repeat():
        name_file=input("insert name archive:\n")#user insert name's file and will save on file .txt
        update_list()
        imp_file()

#main menu
print("welcome to vault ver:1.1\n")#title screen
ans1=input("press I for import program's infos.\npress S to see program's infos already created.\npress D to delete program's infos already created \n")# ans is used for select one of 4 options avariable
if ans1=="i":#1°option, import all informations and will save in a file.txt
        name_file=input("insert name archive:\n")#user insert name's file and will save on file .txt
        update_list()
        imp_file()
        print("done\n")
        ans2=input("do you want insert another file? Y/N\n")
        while ans2 =="y":
                repeat()
                ans2=input("do you want insert another file? Y/N\n")

        input("bye")
else:
     input("command error, shutting down, bye")

#debug log:
#   mantenere nomi su file list.txt.
#   conferma inserimento dati.
#   ripetizione inserimento dati nel caso l'utente voglia inserire altri dati
#   inserire voci STOP DEV e STATUS in modifica.
#   inserire la seconda opzione, visualizzazione dati.
#   inserire terza opzione, modifica file.
#   inserire quarta opzione, cancellazione file.
#   
#-------------------------------------------------
#Copyright (c) 2018 JRDSOFT All rights reserved.