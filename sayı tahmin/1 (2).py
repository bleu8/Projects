import random 

sayi=random.randint(1,90)

hak=10 

while hak>0:
    tahm=int(input("pozitif tam sayi gir"))

    if tahm<0:
        print("pozitif degil")
        continue
    hak-=1
    
    if sayi==tahm:
        print("dogru")
        break
    elif sayi>tahm:
        print("yukari kalan hak {}".format(hak))
    else:
        print("asagi kalan hak {}".format(hak))
    if hak==0:
        print("oldun!!!")

