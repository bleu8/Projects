# Rent A vehcle!!!
import datetime
#parent class
class RentAVeh():
    def __init__(self,stock):
        self.stock=stock
        self.now=0 #saatlik mi
        
    def displayStock(self):
        return self.stock
        print(" {} vehicle avaliable".format(self.stock))
    def rentH(self,n):
        if n<0:
            print("number should be positive!!")
            return None
        elif n>self.stock:
            print("sorry {} is avaliable ".format(self.stock))
            return None
        else:
            self.now=datetime.datetime.now() #arac kiralanma saati
        #inputla
            print("rented {} vehicle at {} hour".format(n,self.now.hour))
            self.stock-=n
            return self.now
    
    
    def rentD(self,n): #gun 
        if n<0:
            print("number should be positive!!")
            return None
        elif n>self.stock:
            print("sorry {} is avaliable ".format(self.stock))
            return None
        else:
            self.now=datetime.datetime.now() #arac kiralanma saati
            print("rented {} hvehicle at {} hour".format(n,self.now.hour))
            self.stock-=n
            return self.now
        pass
    def returnV(self,req,brand):
        """return a bill"""
        car_h_price=10
        car_d_price=car_h_price*0.8*24
        bike_h_price=5
        bike_d_price=bike_h_price*0.7*24
        
        
        rentT,rental_basis,numofVeh=req
        bill=0
        
        if brand=="car":
            if rentT and rental_basis and numofVeh: #bos degilse
                self.stock+=numofVeh
                now=datetime.datetime.now() #ne zaman return edildi.
                rentalPe=now-rentT #ne kadar musteride
                #aradaki sure farki
                
                if rental_basis==1: #saatlik
                    bill=rentalPe.seconds/3600*car_h_price*numofVeh
                elif rental_basis==2:
                    bill=rentalPe.seconds/(3600*24)*car_d_price*numofVeh
                if 2<=numofVeh:
                    print("20 discount")
                    bill=bill*0.8
                    print("price: {}".format(bill))
                    return bill
                
        if brand=="bike":
            if rentT and rental_basis and numofVeh: #bos degilse
                self.stock+=numofVeh
                now=datetime.datetime.now() #ne zaman return edildi.
                rentalPe=now-rentT #ne kadar musteride
                #aradaki sure farki
                
                if rental_basis==1: #saatlik
                    bill=rentalPe.seconds/3600*bike_h_price*numofVeh
                elif rental_basis==2:
                    bill=rentalPe.seconds/(3600*24)*bike_d_price*numofVeh
                if 4<=numofVeh:
                    print("20 discount")
                    bill=bill*0.8
                    print("price: {}".format(bill))
                    return bill               
        else:
            print("you didn't rent")
                
                
        
        
        
class carRent(RentAVeh): #child 1i
    global discount_rate
    discount_rate=15 #sabit 
    def __init__(self,stock):
        super().__init__(stock)
       
    def discount(self,b):
        bill=b-(b*discount_rate)/100
        return bill
    
class BikeRent(RentAVeh):
    def __init__(self,stock): #stock kac bikerent
        super().__init__(stock) #vehicle rent inherit-stock objesine eristi
    
        
    
class Customer(): #musteri
    def __init__(self):
        self.bikes=0
        self.rental_basis_b=0 #saatlik mi gunluk mu
        self.rentalT_b=0
        
        self.cars=0
        self.rental_basis_c=0
        self.rentalT_c=0
    def reqVeh(self,brand):
        """take request veh(bike,car)""" 
        if brand=="bike":
            bikes=input("how many bikes to rent")
            
            
            try:
                bikes=int(bikes)
            except ValueError:
                print("should be number")
                return -1
            
            if bikes<0:
                print("positive number!!!")
                return -1
            
            else:
                self.bikes=bikes
                return self.bikes

        
            
        elif brand=="car":
            cars=input("how many cars to rent")
            
            
            try:
                cars=int(cars)
            except ValueError:
                print("should be number")
                return -1
            
            if cars<0:
                print("positive number!!!")
                return -1
            
            else:
                self.cars=cars
                return self.cars

            
            
        else:
            print("false")
        
        
        
    def returnV(self,brand):
        "return bikes or car"
        if brand =="bike":
            if self.rentalT_b and self.rental_basis_b:
                return self.rentalT_b , self.rental_basis_b, self.bikes  
            else:
                return 0,0,0
        elif brand=="car":
            if self.rentalT_c and self.rental_basis_c:
                return self.rentalT_c , self.rental_basis_c, self.cars 
            else:
                return 0,0,0
        else:
            print("avaliable!")
            
            
            
            
            
            
        
        

