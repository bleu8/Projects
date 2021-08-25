import random
import time


def Intro():
    print("Once upon a time,it was a state who leads by a gorgeous king. The public has lived in a peace.However the dragon sat down enter of the city")
    time.sleep(5)
    
    print('''You  have two paths
          one of the dragons is friendly and want to give a gift for you
          Other one is such a cruel.And wanna eat everyone''','\n')
          
          
          
def find_pth():
    pth=""
    pth=str(input("which path do you prefer??? 1 or 2" ))
    
    return pth


def ch(pth):
    print("you ll go to the path")
    time.sleep(2)
    print("dark and foggy weather....")
    time.sleep(2)
    print("the huge dragon is in front of you ")
    time.sleep(2)
    calmp=random.randint(1,2)
    print(calmp)
    
    if pth==str(calmp):
        print("saved!!! all treasure is yours")
    else:
        print("RIP")
        
ply_a="yes"

while ply_a=="yes" or ply_a=="y":
    Intro()
    pthno=find_pth()
    ch(pthno)
    print("play again?? yes or no")
    ply_a==input("enter>>>>")
    
    
    
    
        
    
    
    
    
    
    