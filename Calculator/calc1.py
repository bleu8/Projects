from tkinter import *
#0 VE NOKTA YAZ ICINDE OLUCAK
def yaz(x):
    #entryde basamak ayari--->s
    s=len(ine.get())
    ine.insert(s,str(x))
    print(x)

hesap=5
s1=0    
def islemf(x):
    global hesap 
    hesap=x
    global s1
    s1=float(ine.get()) #sayiyi al platformdan noktalilar icinde
    """print(hesap)
    print(s1)""" #iskemi console^da goruntu
    #Text field sifirlanmali
    ine.delete(0,'end')
    #0 = nokta butonu eksik!
    
def hesapla():
    global s2
    s2=float(ine.get())
    global hesap
    sonuc=0
    if hesap==0:
        sonuc=s1+s2
    elif hesap==1:
        sonuc=s1-s2
    elif hesap==2:
        sonuc=s1*s2
    elif hesap==3:
        sonuc=s1/s2
    ine.delete(0,'end')
    ine.insert(0,str(sonuc))
        
    
    
wn=Tk()
wn.geometry("250x300")


ine=Entry(font="Verdana 14 bold",width=15,justify=RIGHT)
#   justify --> sag a kay

ine.place(x=20,y=20)

b = []

for i in range(1,10):
    b.append(Button(text=str(i),font="Verdana 14 bold",command=lambda x=i:yaz(x)))
sayac=0    
for i in range(0,3):
    for j in range(0,3):
        b[sayac].place(x=20+j*50,y=i*50+50)
        sayac+=1
        
islem=[]

for i in range(0,4):
    islem.append(Button(font="Verdana 14 bold",command=lambda x=i:islemf(x)))
    
islem[0]['text']="+"
islem[1]['text']="-"
islem[2]['text']="*"
islem[3]['text']="/"


for i in range(0,4):
    islem[i].place(x=180,y=50*i+50)
    
sif=Button(text=0,font="Verdana 14 bold",command=lambda x=0:yaz(x))
sif.place(x=20,y=200)
nb=Button(text=".",font="Verdana 14 bold",command=lambda x=".":yaz(x))
nb.place(x=70,y=200)

es=Button(text="=",fg="GREEN",font="Verdana 14 bold",command=hesapla)
es.place(x=120,y=200)
wn.mainloop()



