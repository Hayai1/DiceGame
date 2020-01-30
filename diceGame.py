import random
import time
start = input("press enter to start!\n")
if start == (""):
    print("Ok!!!!")


#putting the imports at the top no need fot them to be anywhere else out of the way like the variables
c_1 = 0#setting the variables so they are out of the way
c = 5
myfilename="H:\\year 10\\IT\\games\\dice game\\notepad\\dice.txt"#the file where all the names, scores and passwords are  
#<-------------------------------login process--------------------------------------->
def l(user, password):#using a function so that i don't have to repeat the process for both players
    if user in mynamelist:# if the p1/p2 is in the file name /\ then there will be no need to make antoher acc
        print("")
    else:
        print("you are not in the list creating a new user")
        time.sleep(1)
        mynamelist.append(user)
        mynamelist.append("0")#if player is in side the list then it appends a name a score of 0 and a password
        mynamelist.append(password)
        separator = " "#the seperator that seperates the attrubutes such as the scrore from the name
        newnamelist = separator.join(mynamelist)#joins the name score and password together
        f = open(myfilename,"w")
        f.write(newnamelist)#opens the list in the file name
        f.close

def password(password, p_index, c):
    while c != -1:
        if password == mynamelist[p_index+2]:
            print("welcome")#if they get the password right it says welcome
            time.sleep(1)
            c = -1
        else:
            if c != 0:
                print("wrong password")#they get 5 attempts to get the password right
                print(c, "attemps left")
                password =input("enter password\n")
                c = c - 1
            else:
                print("no attempts left")# if they use all the attempts the system ends
                exit()
#<------------------------------------input for p1---------------------------------------->
f = open(myfilename,"r")
mynamelist= f.read().split()
f.close()

p1=input("Player 1 enter your username:\n")
p1_password =input("enter password\n")#p1 inputs name and password and puts them into the function to check if they are in the list and if not make an account for them
l(p1, p1_password)
p1_index = mynamelist.index(p1)
#<------------------------pasword check for p1-------------------------------------->
password(p1_password, p1_index, c)
score_p1 = int(mynamelist[p1_index+1])
print(p1, "your score is", score_p1)
#,------------------------------------------input p2---------------------------------------->
p2 = input("input player 2\n")#inputs p2 name
p2_password =input("enter password\n")#p2 inputs password
l(p2, p2_password)#puts the name and password into the function
p2_index = mynamelist.index(p2)
c_1 = 0
c = 5
#<------------------------------------------password input p2----------------------->
password(p2_password, p2_index, c)# if they use all the attempts the system ends
score_p2 = int(mynamelist[p2_index+1])
print(p2, "your score is", score_p2)
total1 = 0
total2 = 0
#<---------------------p1 presses enter to role the dice------------------------>
c = 0
def roll(p_, total):
    roll = input("press enter to roll the dice "+ p_ )
    if roll == "":
        roll_1 = random.randint(1, 6)
        print("roll 1:\n", roll_1)
        roll_2 = random.randint(1, 6)
        print("roll 2:\n", roll_2)
        firstRolls = roll_1 + roll_2
        if roll_1 == roll_2:
            print("you got the same number \n you get another roll")
            roll_3 = random.randint(1, 6)
            print("roll 3:\n", roll_3)
            total = roll_3 + firstRolls
        else:
            if (firstRolls % 2) == 0:
                print("Even + 10")
                total = firstRolls+ 10
            else:
                print("Odd - 5")
                total =firstRolls - 5
        if total < 0:
            total = 0
        print(p_, "your score is", total)
       
       
while c != 5:
    roll(p1, total1)
    roll(p2, total2)
    c = c + 1

#<--------------------sees who wins----------------------------->
if total1 > total2:#checks if player1's score is higher then p2
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print(p1, "wins!")#prints that p1 wins
    print("your scrores:\n")
    print(p1, total1)
    print(p2, total2)# if it is then p1 wins
elif total1 < total2:#if not p2 wins
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print(p2, "wins!")#prints that p2 wins
    print("your scrores:\n")
    print(p2, total2)
    print(p1, total1)
#<-----------------------sudden death----------------------------------->
elif total1 == total2:#if they get the same score then they win
    print("SUDDEN DEATH!!!!!")
    final_roll_p1 = random.randint(1, 6)#they both get a final roll
    final_roll_p2 = random.randint(1, 6)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    total1 = total1 + final_roll_p1#adds up all the remaining scores
    total2 = total2 + final_roll_p2
    if total1 > total2:#if p1 is hiher p1 wins
        print(p1, "wins!!!!")
        print("your scrores:\n")
        print(p1, total1)
        print(p2, total2)
    else:
        print(p2, "wins!!!!")#if not p2 wins
        print("your scrores:")
        print(p2, total2)
        print(p1, total1)
#~<-----------------edetting file socres----------------------->
if total1>int(mynamelist[p1_index+1]):#eddits the score if it is higher then the original one in the note pad this applys to both players
    mynamelist[p1_index+1]=str(total1)
    print("edditing", p1, "scores\n")
    print("loading")
    time.sleep(1)
if total2>int(mynamelist[p2_index+1]):
    mynamelist[p2_index+1]=str(total2)
    print("edditing", p2, "scores\n")
    print("loading")
    time.sleep(1)
separator = " "
newnamelist = separator.join(mynamelist)
f = open(myfilename,"w")
f.write(newnamelist)
f.close()
#<-------------------leader board--------------------------->
lb = input("see the leaderboard\n")#asks if you want to see the leader baord
if lb == "yes":
    f = open(myfilename,"r")
    mynamelist= f.read().split()
    f.close()

    scores=[]
    leaders=""


    for i in mynamelist:
        if mynamelist.index(i)%3 == 1:
       
            scores.append(i)#puts all the people in the list for the leaderboard
       
    scores.sort

    for x in scores:
        i = mynamelist.index(str(x))
        leaders=leaders + str(mynamelist[i-1]) + " " + str(mynamelist[i]) + "\n"
        mynamelist.pop(i)
        mynamelist.pop(i-1)

    print(leaders)#prints the leader board

#<--------------------------------end-------------------------->