
#Code by Hydrogen_HW
#还原侧身，以玄鸟之资缤纷此尘荏#

#Imports
from random import randint

#Varibles
guess=""
answer=""

#Functions
def checkInputValid(targetStr="0"):
    if len(targetStr) != 4:
        return False
    else:
        for i in targetStr:
            if ord(i)<ord("0") or ord(i)>ord("9"):
                return False
    return True

def getUserInput():
    global guess
    while True:
        guess=input("Please input 4 digits: ")
        if checkInputValid(guess):
            break

def generateAnswer():
    global answer
    for i in range(0,4):
        while True:
            present=randint(0,9)
            presentChr=chr(ord("0")+present)
            if answer.find(presentChr)==-1:
                break
        answer=answer+presentChr

def countA():
    global answer
    count=0
    for i in range(0,4):
        if answer[i]==guess[i]:
            count+=1
    return count

def countB():
    global answer
    count=0
    for i in range(0,4):
        j=answer.find(guess[i])
        if j!=-1 and j!=i:
            count+=1
    return count

#Main
generateAnswer()
attempts=0
print(answer)
while True:
    getUserInput()
    attempts+=1
    a=countA()
    b=countB()
    if a==4:
        print(f"You Win!!\nAttempts:{attempts}")
        break
    else:
        print(f"{a} A (Bulls) {b} B (Cows)")