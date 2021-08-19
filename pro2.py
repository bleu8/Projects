#rehber uygulamasi


import random


#rehber uygulamasi


import random


rehber ={}

def kisiek(isim,num):
    global rehber 
    if not isim in rehber.keys():
        rehber[isim]=num
    else:
        print("var")
    
    
def kisisil(isim):
    global rehber
    try:
        del rehber[isim]
        print("kisi silindi")
    except KeyError:
            print("yok")
            
def ismgun(isim,yeni):
    global rehber
    if isim in  rehber.keys():
        if isim not in rehber.keys():
            rehber[yeni]=rehber[isim]
            del rehber[isim]
            print("isim guncelleme")
        else:
            print("yeni kullanici adi ")
    else:
        print("isim guncellendi")
        
def num_gun(isim,yenin):
    global rehber
    if isim in rehber.keys():
        rehber[isim]=yenin
        print("guncellendi")
    else:
        print("kisi bulunamadı")
        
def rastgele_kisi():
    isim=random.choice(list(rehber.keys()))
    return isim,rehber[isim]

def kisi_gr():
    global rehber
    if not len(rehber)==0:
        print("rehber\n")
        i=1
        for key,value in rehber.items():
            print(f"{i}\n\tİsim: {key}\n\tNumara: {value}")
            i+=1
        return 
    print("rehber bos")
    
def main():
    global rehber
    menu ='''
    ------------------------
    |1.kisi ekle            |
    |2.kisi sil             |
    |3.isim guncelle        | 
    |4.numara guncelle      |
    |5.rastgele kisi sec    |
    |6.kisileri goruntule   |
    |q:cıkıs yap            |
     ------------------------
   '''
   
   
    print(menu)
    
main()
   
   
while True:
    secim=input("lutfen secim yapınız")
    if secim=="1":
        isim=input("yeni isim gir")
        num=input("yeni numara-->")
        kisiek(isim,num)

    elif secim=="2":
        isim=input("silmek istedigin gir")
        kisisil(isim)
    elif secim=="3":
        isim=input("degistirmek istedigin gir")
        yeni=input("numarasini gir")
        kisiek(isim,yeni)
          
    elif secim=="4":
        isim=input("numarası degistirmek istedigin kisiyi gir")
        yenin=input("gir-->") 
        num_gun(isim,yenin)
          
    elif secim=="5":
        isim,num=rastgele_kisi()
        print(f"\n\t:{isim}\n\tNumara{num}")

    elif secim =="6":
        kisi_gr()
          
    elif secim=="q":
        break
    else:
        print("yanlıs islem")
        
        

        
      
        
               
   
        
    
    
            
    
  