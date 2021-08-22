import random



def bs_uret():
    n=random.randint(1,3)
    if n==1:
        return "tas"
    elif n==2:
        return "makas"
    elif n==3:
        return "kagıt"

skorb=0
skoru=0

while True:
        user=input("tas kagıt mı makas mı ??")
        bs=bs_uret()

        print("bilgisayar--->",bs)


        if bs==user:
            print("berabere")


        elif bs =="tas" and user=="kagıt":
            skoru+=1


        elif bs =="makas" and user=="tas":
            skoru+=1


        elif bs =="kagıt" and user=="makas":
            skoru+=1


        else:
        skorb+=1

        print(f"siz  {skoru} vs bilgisayar{skorb}")


if skoru==3 or skorb==3:
        break

if skoru>skorb :
        print("kaybettin")

else:
        print("kazandın!!!")
