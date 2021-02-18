from functions import *
import random
win_combinations=[['1','4','7'],['2','5','8'],['3','6','9'],['1','2','3'],['4','5','6'],['7','8','9'],['1','5','9'],['3','5','7']]
        
def tic_tac_toe():
    a=['1','2','3']
    b=['4','5','6']
    c=['7','8','9']
    
    print a,"\n",b,"\n",c,'\n'
    r=0
    p=input("Player enter 'X' or 'O' of your choice")
    if p=="X" or p=="x":
        p1="X"
        p2="O"
    else:
        p1="O"
        p2="X"

    for i in range(9):
        while(1):
            if a[0]==a[1]==p2 and a[2]!=p2 and a[2]!=p1:
                a[2]=p2
                break
            elif a[1]==a[2]==p2 and a[0]!=p2 and a[0]!=p1:
                a[0]=p2
                break
            elif a[0]==a[2]==p2 and a[1]!=p2 and a[1]!=p1:
                a[1]=p2
                break
            elif b[0]==b[1]==p2 and b[2]!=p2 and b[2]!=p1:
                b[2]=p2
                break
            elif b[1]==b[2]==p2 and b[0]!=p2 and b[0]!=p1:
                b[0]=p2
                break
            elif b[0]==b[2]==p2 and b[1]!=p2 and b[1]!=p1:
                b[1]=p2
                break
            elif c[0]==c[1]==p2 and c[2]!=p2 and c[2]!=p1:
                c[2]=p2
                break
            elif c[1]==c[2]==p2 and c[0]!=p2 and c[0]!=p1:
                c[0]=p2
                break
            elif c[0]==c[2]==p2 and c[1]!=p2 and c[1]!=p1:
                c[1]=p2
                break
            elif a[0]==b[1]==p2 and c[2]!=p2 and c[2]!=p1:
                c[2]=p2
                break
            elif b[1]==c[2]==p2 and a[0]!=p2 and a[0]!=p1:
                a[0]=p2
                break
            elif a[0]==c[2]==p2 and b[1]!=p2 and b[1]!=p1:
                b[1]=p2
                break
            elif c[0]==b[1]==p2 and a[2]!=p2 and a[2]!=p1:
                a[2]=p2
                break
            elif b[1]==a[2]==p2 and c[0]!=p2 and c[0]!=p1:
                c[0]=p2
                break
            elif c[0]==a[2]==p2 and b[1]!=p2 and b[1]!=p1:
                b[1]=p2
                break
            elif a[0]==b[0]==p2 and c[0]!=p2 and c[0]!=p1:
                c[0]=p2
                break
            elif a[0]==c[0]==p2 and b[0]!=p2 and b[0]!=p1:
                b[0]=p2
                break
            elif c[0]==b[0]==p2 and a[0]!=p2 and a[0]!=p1:
                a[0]=p2
                break
            elif a[1]==b[1]==p2 and c[1]!=p2 and c[1]!=p1:
                c[1]=p2
                break
            elif a[1]==c[1]==p2 and b[1]!=p2 and b[1]!=p1:
                b[1]=p2
                break
            elif c[1]==b[1]==p2 and a[1]!=p2 and a[1]!=p1:
                a[1]=p2
                break
            elif a[2]==b[2]==p2 and c[2]!=p2 and c[2]!=p1:
                c[2]=p2
                break
            elif a[2]==c[2]==p2 and b[2]!=p2 and b[2]!=p1:
                b[2]=p2
                break
            elif c[2]==b[2]==p2 and a[2]!=p2 and a[2]!=p1:
                a[2]=p2
                break

            
            elif a[0]==a[1]==p1 and a[2]!=p2:
                a[2]=p2
                break
            elif a[1]==a[2]==p1 and a[0]!=p2:
                a[0]=p2
                break
            elif a[0]==a[2]==p1 and a[1]!=p2:
                a[1]=p2
                break
            elif b[0]==b[1]==p1 and b[2]!=p2:
                b[2]=p2
                break
            elif b[1]==b[2]==p1 and b[0]!=p2:
                b[0]=p2
                break
            elif b[0]==b[2]==p1 and b[1]!=p2:
                b[1]=p2
                break
            elif c[0]==c[1]==p1 and c[2]!=p2:
                c[2]=p2
                break
            elif c[1]==c[2]==p1 and c[0]!=p2:
                c[0]=p2
                break
            elif c[0]==c[2]==p1 and c[1]!=p2:
                c[1]=p2
                break
            elif a[0]==b[1]==p1 and c[2]!=p2:
                c[2]=p2
                break
            elif b[1]==c[2]==p1 and a[0]!=p2:
                a[0]=p2
                break
            elif a[0]==c[2]==p1 and b[1]!=p2:
                b[1]=p2
                break
            elif c[0]==b[1]==p1 and a[2]!=p2:
                a[2]=p2
                break
            elif b[1]==a[2]==p1 and c[0]!=p2:
                c[0]=p2
                break
            elif c[0]==a[2]==p1 and b[1]!=p2:
                b[1]=p2
                break
            elif a[0]==b[0]==p1 and c[0]!=p2:
                c[0]=p2
                break
            elif a[0]==c[0]==p1 and b[0]!=p2:
                b[0]=p2
                break
            elif c[0]==b[0]==p1 and a[0]!=p2:
                a[0]=p2
                break
            elif a[1]==b[1]==p1 and c[1]!=p2:
                c[1]=p2
                break
            elif a[1]==c[1]==p1 and b[1]!=p2:
                b[1]=p2
                break
            elif c[1]==b[1]==p1 and a[1]!=p2:
                a[1]=p2
                break
            elif a[2]==b[2]==p1 and c[2]!=p2:
                c[2]=p2
                break
            elif a[2]==c[2]==p1 and b[2]!=p2:
                b[2]=p2
                break
            elif c[2]==b[2]==p1 and a[2]!=p2:
                a[2]=p2
                break


            y=random.randint(1,10)
            if y<=3 and a[y-1]!=p1 and a[y-1]!=p2:
                a[y-1]=p2
                break
            elif y>3 and y<=6 and b[y-4]!=p1 and b[y-4]!=p2:
                b[y-4]=p2
                break
            elif y>6 and y<=9 and c[y-7]!=p1 and c[y-7]!=p2:
                c[y-7]=p2
                break
        print a,"\n",b,"\n",c,'\n'
        print "CPU had entered the location",'\n'
        if check_col(a,b,c)==p2:
            print "HARD LUCK!!!!Computer wins",'\n'
            r+=1
            break
        if check_row(a,b,c)==p2:
            print "HARD LUCK!!!!Computer wins",'\n'
            r+=1
            break
        if check_diag(a,b,c)==p2:
            print "HARD LUCK!!!!Computer wins",'\n'
            r+=1
            break
        
        if i==4:
            break
        
        print "Player enter the location "
        while(1):
            x=input("Enter the location ")
            if x<=3:
                if a[x-1]==p2:
                    print "Enter the valid location",'\n'
            elif x<=6:
                if b[x-4]==p2:
                    print "Enter the valid location",'\n'
            elif x<=9:
                if c[x-7]==p2:
                    print "Enter the valid location",'\n'
            if x<=3 and a[x-1]!=p2 and a[x-1]!=p1:
                a[x-1]=p1
                break
            elif x>3 and x<=6 and b[x-4]!=p2 and b[x-4]!=p1:
                b[x-4]=p1
                break
            elif x>6 and x<=9 and c[x-7]!=p2 and c[x-7]!=p1:
                c[x-7]=p1
                break
        print a,"\n",b,"\n",c,'\n'
        if check_col(a,b,c)==p1:
            print "CONGRATULATIONS!!!!Player wins",'\n'
            r+=1
            break
        if check_row(a,b,c)==p1:
            print "CONGRATULATIONS!!!!Player wins",'\n'
            r+=1
            break
        if check_diag(a,b,c)==p1:
            print "CONGRATULATIONS!!!!Player wins",'\n'
            r+=1
            break


    if r==0:
        print "The game is draw....",'\n'
    print "Press 'Y' if you want to play again else 'N'"
    q=input()
    if q=='Y' or 'y':
        tic_tac_toe()
    else:
        exit(-1)
tic_tac_toe()
