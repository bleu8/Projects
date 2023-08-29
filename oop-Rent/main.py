from rent import carRent,BikeRent,Customer

bike=BikeRent(100)
car=carRent(10)

customer=Customer() 

main_menu=True
while True:
    if main_menu:
        print("""
              ******* vehicle rent site******
              a.bike
              b.car
              q.exit""")
        main_menu=False
        choice=input("enter--->")
        if choice== "a":
            print("""*****
                  1.display bikes
                  2.request hourly 5 dollar
                  3.request daily 80 dollar
                  4.return bike
                  6.main
                  6.exit
                  
                  *****""")
            choice=int(input("enter a choice--->"))
            if choice==1:
                bike.displayStock()
                choice=="a"
            elif choice==2: #saatlik -- zamani return edicek bisey ariyoruz
                customer.rentalT_b=bike.rentH(customer.reqVeh("bike"))
                customer.rental_basis_b=1 #saatlik
                main_menu=True
                print("-----------------")

            elif choice==2: #saatlik -- zamani return edicek bisey ariyoruz
                customer.rentalT_b=bike.rentD(customer.reqVeh("bikes"))
                customer.rental_basis_b=2
                main_menu=True
                print("-----------------")
            elif choice==4:
                customer.bill=bike.returnV(customer.returnV("bikes"),"bike")
                customer.rental_basis_b,customer.rentalT_b, customer.bikes=0,0,0
                main_menu=True
                
            elif choice==5: #main menusune cikis
                main_menu=True
            
            elif choice==6:
                break
            else:
                print("enter 1 -6")
                
                
                #araba menusu
                
        if choice=="b":    
            print("""*****
                  1.display car
                  2.request hourly 5 dollar
                  3.request daily 80 dollar
                  4.return car
                  6.main
                  6.exit
                  
                  *****""")
            choice=int(input("enter a choice--->"))
            if choice==1:
                car.displaystock()
                choice=="b"
            elif choice==2: #saatlik -- zamani return edicek bisey ariyoruz
                customer.rentalT_c=car.rentH(customer.reqVeh("car"))
                customer.rental_basis_c=1 #saatlik
                main_menu=True
                print("-----------------")

            elif choice==2: #saatlik -- zamani return edicek bisey ariyoruz
                customer.bill=customer.rentalT_c=car.rentD(customer.reqVeh("car"))
                customer.rental_basis_c=2
                main_menu=True
                print("-----------------")
            elif choice==4:
                bike.returnV(customer.returnV("car"),"car")
                customer.rental_basis_b,customer.rentalT_b, customer.cars=0,0,0
                main_menu=True
                
            elif choice==5: #main menusune cikis
                main_menu=True
            
            elif choice==6:
                break
            else:
                print("enter  between 1 -6")
                main_menu=True
                
        elif choice=="q":
            break
        
        else:   
            print("invalid operation enter a b or q")
            main_menu=True
            
            
        print("thank you :) ")
            
                
                
                
