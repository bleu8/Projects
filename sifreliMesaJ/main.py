import math
import random

def sifrele():
    try:
        n=int(input("Anahtar gir--->"))
        
    except:
            print("yanlıs giris!!")
            sifrele()
            
    if n ==0 and n==1:
            print("0 yada 1 olamaz!!!!")
            sifrele()
            
    else:
            key=[(n//(10**i)) for i in range (math.ceil(math.log(n,10))-1,-1,-1)]
            
        
    toplam=0
    for i in key:
        toplam=toplam+i
    print(toplam)
            
    
    text=str(input("Lutfen sifrelemek istedigini gir\n>>>"))
    
    text=text.lower()
    letters=[c for c in text]
    
    sifre=[]

    for i in letters:
        if i =="a":
            i=16
            sifre.append(i)
            
        elif i =="b":
            i=12
            sifre.append(i)
        elif i =="c":
            i=19
            sifre.append(i)
        elif i =="d":
            i=7
            sifre.append(i)
        elif i =="e":
            i=71
            sifre.append(i)
            
        elif i =="f":
            i=17
            sifre.append(i)
            
        elif i =="g":
            i=22
            sifre.append(i)
        elif i =="h":
            i=56
            sifre.append(i)
       
        elif i =="i":
            i=72
            sifre.append(i)
       
        elif i =="j":
            i=21
            sifre.append(i)
       
        elif i =="k":
            i=13
            sifre.append(i)
       
        elif i =="l":
            i=99
            sifre.append(i)
       
        elif i =="m": #2 geri git
            i=25
            sifre.append(i)
       
        elif i =="o":
            i=4
            sifre.append(i)
            
        elif i =="p":
            i=48
            sifre.append(i)
        elif i =="r":
            i=79
            sifre.append(i)
        elif i =="s":
            i=35
            sifre.append(i)
        elif i =="t":
            i=41
            sifre.append(i)
        elif i =="u":
            i=99
            sifre.append(i)
       
        elif i =="v":
            i=94
            sifre.append(i)
       
        elif i =="y":
            i=21
            sifre.append(i)
       
        elif i =="z":
            i=65
            sifre.append(i)
        elif i =="1":  #1 geri
            i=9
            sifre.append(i)
       
        elif i =="2":
            i=7
            sifre.append(i)
       
        elif i =="3":
            i=8
            sifre.append(i)
       
        elif i =="4":
            i=6
            sifre.append(i)
        elif i=="5":
            i=4
            sifre.append(i)
        elif i =="6":
            i=5
            sifre.append(i)
        elif i =="7":
            i=3
            sifre.append(i)
        elif i =="8":
            i=2
            sifre.append(i)
       
        elif i =="9":
            i=1
            sifre.append(i)

   
    tamKilit=[]
    for i in sifre:
        i=i*toplam
        tamKilit.append(i)
       
        
    x=str(random.randrange(1,10000))
    print("\nDosyanızın adı"+x+".txt")
    
    with open("%s.txt"%x,"w")as f:
        for item in tamKilit:
            f.write("%s\n"% item)
            
    print("Dosya Basariyla kaydedildi")
    
    for i in range(3):print("x"*70)
    print(tamKilit)
    for i in range(3):print("x"*70)
    
sifrele()



   
    
   
        
    
    
    
    
    
    
    
   
    