import os
def menu():
    print("***Menu**")
    print("1-Kaydet")
    print("2-Listele")
    print("3-Duzenle")
    print("4-Sil")
    print("5-Sirala")
    print("6-İstatistik")
    print("7-Cikis")
    
    secim=int(input("secim??"))
    return secim


def kaydet():
    dv=True
    while dv:
        with open("data.txt","a")as ds:
         print("kaydet")
         num=input("numara?")
         isim=input("isim?")
         ders=input("ders")
         vize=input("vize")
         final=input("final")
         satir="{:12}\t{:12}\t{:15}\t{:5}\t{:5}\n".format(num,isim,ders,vize,final)
         ds.write(satir)
         sec=(input("yeni kayit??? E/H"))
         if sec=="E":
             dv=True
         else:
             dv=False
            
def listele():
    print("***LİSTELE***")
    with open("data.txt","r")as ds:
        for satir in ds:
            print("{:12}\t{:12}\t{:15}\t{:5}\t{:5}\n".format(satir[0:12],satir[13:28],satir[29:45],satir[46:51],satir[51:57]))

            
def duzenle():
    print("**DUZENLE**")
    numara=input("Duzeltilcek numara--->")
    eski=open("data.txt","r") #degisiklik yok
    yeni=open("yeni.txt","w")
    for sat in eski:
        parca=sat.split("\t")
        if parca[0].strip()==numara.strip():
            yenin=input("yeni numara-->")
            yeni.write(yenin+"\t" +parca[1]+"\t"+parca[2]+"\t"+parca[3]+"\t"+parca[4])
            continue
        else:
            yeni.write(sat)
        eski.close()
        yeni.close()
        os.remove("./data.txt")
        os.rename("./yeni.txt","data.txt")
        
            
def sil():
    numara=input("Silincek ogrencı numarasi---->")
    eski=open("data.txt","r")
    yeni=open("yeni.txt","w")
    for sat in eski:
        parca=sat.split("\t")
        if parca[0].strip()==numara.strip():
            continue
        else:
            yeni.write(sat)
        eski.close()
        yeni.close()
        os.remove("./data.txt")
        os.rename("./yeni.txt","data.txt")
            

def sirala():
    print("**Sırala**")
    lis=list()
    with open("data.txt") as ds:
        for satir in ds:
            parca=sat.split("\t")
            s=parca[0]
            lis.append(s)
        lis.sort()
        for i in lis:
            print(i)
devam=True
while devam:
    secim=menu()
    if secim==1:
       kaydet()
       
    elif secim==2:
        listele()
       
    elif secim==3:
        duzenle()
        
    elif secim==4:
        sil()
        
    elif secim==5:
        sirala()
    
    elif secim==6:
        pass
    
    elif secim==7:
        devam= False
        

  