from random import choice

while True:
    print("*"*80)
    print("*"*20 +  "hangman"+ "*"*20)
    print("*"*80)
    
    kelime=choice(["ankara","istanbul","eskisehir","izmir","losangeles","toronto","prag"])
    kelime=kelime.upper()
    
    harf =len(kelime)
    print("\nKelimemiz---> {} harflidir".format(harf))
    
    print("*"*80)
    tahmin=[]
    hata=[]
    deneme=7

    while deneme>0:
        tabela=""
        for harf in kelime:
            if harf in tahmin:
                tabela= tabela+harf
                
            else:
                tabela=tabela+" _ "
        if tabela==kelime:
            print("kelimeyi bildin!!!!")
            break
        print("kelimeyi tahmin et",tabela)
        print(deneme,"canin kaldi")
        
        
        tahmn=input("bir harf soyle--->")
        tahmn=tahmn.upper()
        
        
        if tahmn==kelime:
            print("bravo")
            break
        if tahmn in tahmin or tahmn in hata:
            print("{} daha once solendi baska bir harf gir".format(tahmn)),
        elif tahmn in kelime:
            rpt=kelime.count(tahmn)
            print("Doğru {0} harfi iceride {1} kez geciyor".format(tahmn,rpt))
            tahmin.append(tahmn)
        else:
            print("kelimede bu harf yok")
            hata.append(tahmn)
            deneme=deneme-1
    if deneme==0:
        print("oldun!!!")
        print("kelimemiz {}".format(kelime))
    print("oyundan cikmak istiyorsan \n H tusuna bas")
    devam=input(">>>>>")
    if devam=="H":
        break
    else:
        continue
    
        
            
            
            
            
        
        
    