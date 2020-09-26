#modules are in use
import os
import random
import getpass


#player1's function
def playerf(pn1,p1,pl1,list):
    while(p1!=getpass.getpass("%s enter your pin - "%pn1)):
        print("Wrong pin! enter again")
    os.system('cls')
    for i in range(0,25,6):
        print("\n\t|\t",pl1[i],"\t",pl1[i+1],"\t",pl1[i+2],"\t",pl1[i+3],"\t",pl1[i+4],"\t|")
    s=input("\n\nEnter your cell number - ")
    while True if s not in pl1 else False:
        s=input("Wrong input!!\nEnter again - ")
    i=0
    while s!=pl1[i]:
        i+=1
    pl1[i]="__"
    i=0
    while s!=list[i]:
        i+=1 
    list[i]="__"



#Generating random numbers from 1 to 25
def generate():
    list=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
    random.shuffle(list)
    for i in range(5,30,6):
        list.insert(i,"  ")
    for i in range(5):
        list.append("  ")
    return list


#Begining of the game
def game():
    os.system('cls')
    pn1,p1=input("\n\tEnter name of player1 - "),getpass.getpass("\n\tEnter pin for player1 - ")
    pn2,p2=input("\n\tEnter name of player2 - "),getpass.getpass("\n\tEnter pin for player2 - ")
    b1=b2=0
    pl1=generate()
    pl2=generate()
    while(b1 or b2)!=5:
        os.system('cls')
        b1=playerf(pn1,p1,pl1,pl2)
        os.system('cls')
        b2=playerf(pn2,p2,pl2,pl1)
        




#Main function
key=""
while key!="2":
    os.system('cls')
    print('\n\t\t_B_I_N_G_O_')
    print("\n\n\t1.Play Game\n\t2.Exit\n")
    key=input("Enter key - ")
    if key=="1":
        game()
    elif key=="2":
        os.system('cls')
        input("thanks for playing BINGO\n press enter")
    else:
        print("wrong input")
        