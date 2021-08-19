
kisiler= []

for i in range(3):
    isim=input("isim gir??")
    kilo=float(input("kilo???"))/100
    boy=int(input("boy??"))
    
    bki=round(kilo/(boy**2),2)
    
    kisi={isim:bki}
    kisiler.append(kisi)
    
    
  
    
print(list(kisiler[0].keys())[0],list(kisiler[0].values())[0])   
print(list(kisiler[1].keys())[0],list(kisiler[1].values())[0]) 
print(list(kisiler[2].keys())[0],list(kisiler[2].values())[0])   
