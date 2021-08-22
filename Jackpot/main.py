from random import random
sans=int(input("kac defa denemek istersin---->"))
ikili=0
ilk_sans=sans
oyunsayisi=0
while sans>0:
    for k in range(sans):
        a=int (random()*10) #0,1,2..10
        b=int (random()*10) #0,1,2..10
        c=int (random()*10) #0,1,2..10
        oyunsayisi+=1
        print(k+1,"de gelen sayılar",a,b,c)
        if a==b==c:
            print("Kazandiniz",ilk_sans*100)
            sans=0
            break
        elif a==b or a==c or b==c :
            ikili+=1
        
    if sans!=0:
        print("tutturulan ikililer",ikili)

        sans=ikili
        ikili=0
    if ikili==0:
        print("kaybettiniz!")
print("oyun sayisi--->",oyunsayisi)
        





