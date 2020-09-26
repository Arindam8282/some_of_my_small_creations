import os
key=0

def printl(list):
    os.system('color E')
    print("\n\n\t\t",list[0],"\t",list[1],"\t",list[2],"\n\n\t\t",list[3],"\t",list[4],"\t",list[5],"\n\n\t\t",list[6],"\t",list[7],"\t",list[8],"\n")

def full(list):
    if (((list[0]=='o') and (list[1]=='o') and (list[2]=='o')) or ((list[0]=='x') and (list[1]=='x') and (list[2]=='x'))):
        return 1
    elif (((list[3]=='o') and (list[4]=='o') and (list[5]=='o')) or ((list[3]=='x') and (list[4]=='x') and (list[5]=='x'))):
        return 1
    elif (((list[6]=='o') and (list[7]=='o') and (list[8]=='o')) or ((list[6]=='x') and (list[7]=='x') and (list[8]=='x'))):
        return 1
    elif (((list[0]=='o') and (list[3]=='o') and (list[6]=='o')) or ((list[0]=='x') and (list[3]=='x') and (list[6]=='x'))):
        return 1
    elif (((list[1]=='o') and (list[4]=='o') and (list[7]=='o')) or ((list[1]=='x') and (list[4]=='x') and (list[7]=='x'))):
        return 1
    elif (((list[2]=='o') and (list[5]=='o') and (list[8]=='o')) or ((list[2]=='x') and (list[5]=='x') and (list[8]=='x'))):
        return 1
    elif (((list[2]=='o') and (list[4]=='o') and (list[6]=='o')) or ((list[2]=='x') and (list[4]=='x') and (list[6]=='x'))):
        return 1
    elif (((list[0]=='o') and (list[4]=='o') and (list[8]=='o')) or ((list[0]=='x') and (list[4]=='x') and (list[8]=='x'))):
        return 1
    elif ((list[0]=='o' or list[0]=='x') and (list[1]=='o' or list[1]=='x') and (list[2]=='o' or list[2]=='x') and (list[3]=='o' or list[3]=='x') and (list[4]=='o' or list[4]=='x') and (list[5]=='o' or list[5]=='x') and (list[6]=='o' or list[6]=='x') and (list[7]=='o' or list[7]=='x') and (list[8]=='o' or list[8]=='x')):
        return 2
    else:
        return 0

def playero(po,list):
    os.system('cls')
    printl(list)
    os.system('color 09')
    cell=1
    print(po,'\'s turn ')
    cell=int(input('enter cell number taken(o) - '))
    while cell!='\0':
        if ((list[cell-1]=='o' or list[cell-1]=='x') or (not(cell<10 and cell>0))):
            print("Wrong input!!\nEnter again\n")
            cell=int(input('enter cell number taken(o) - '))
        else:
            break
    list[cell-1]='o'
    full(list)


    
def playerx(px,list):
    os.system('cls')
    printl(list)
    os.system('color 06')
    print(px,'\'s turn ')
    cell=int(input('enter cell number taken(x) - '))
    while cell!='\0':
        if ((list[cell-1]=='o' or list[cell-1]=='x') or (not(cell<10 and cell>0))):
            print("Wrong input!!\nEnter again\n")
            cell=int(input('enter cell number taken(o) - '))
        else:
            break
      
    list[cell-1]='x'
    full(list)
    
def decide(po,px,list):
     ox=input("\n\t\tChoose the player who will play first enter(o/x) - ")
     fulc=full(list)
     while fulc!=1:    
         if ox=='o':
            playero(po,list)
            ox='x'
            fulc=full(list)
            if fulc==2:
                os.system('cls')
                printl(list)
                print("Game Over Match Drawn\npress enter")
                input()
                return 0
            elif fulc==1:
                os.system('cls')
                printl(list)
                print(po," won the match\npress enter")
                input()
                return 0
             
         elif ox=='x':
            playerx(px,list)
            ox='o'
            fulc=full(list)
            if fulc==2:
                os.system('cls')
                printl(list)
                print("Game Over Match Drawn\npress enter")
                input()
                return 0
            elif fulc==1:
                os.system('cls')
                printl(list)
                print(px," won the match\npress enter")
                input()
                return 0
         else:
            print("Wrong input!!\nEnter again")
            decide(po,px,list)
def game(list):
    os.system('cls')
    po=input("\n\t\tEnter player's name who is taking (o) - ")
    px=input("\n\t\tEnter player's name who is taking (x) - ")
    decide(po,px,list)



    


while key!=2:
    list=[1,2,3,4,5,6,7,8,9]
    os.system('color E')
    print("\tTICTACTOE\n\n\t\t1.play game\n\n\t\t2.Exit\n")        
    key=int(input("Enter key - "))
    if key==1:
        game(list)
    elif key==2:
        os.system('cls')    
        print("\n\n\t\tThanks for playing TICTACTOE\n\t\tpress enter")
        input()
        break
    else:
        print("Wrong input!!\nEnter again")
    os.system('cls')
        

   
        

    