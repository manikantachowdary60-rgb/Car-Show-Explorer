class carshowroom:
    def __init__(self,cgst,sgst,insurance):
        self.cgst=cgst
        self.sgst=sgst
        self.insurance=insurance
    def company(self):
        while True:
            b=input("select your company:")
            self.b=b
            if b=="mahindra":
                print("welcome to mahindra family")
                break
            elif b=="toyota":
                print("welcome to toyota family")
                break
            elif b=="suzuki":
                print("welcome to  Suzuki family")
                break
            else:
                print("choose correct one")   
    def model(self):
        while True: 
            if self.b=="mahindra":
                m=["thar","scorpio"]
                print(m)
                m=input("select your model:")
                self.m=m 
                break
            elif self.b=="toyota":
                m=["innova","fortuner"]
                print(m)
                m=input("select your model:")
                self.m=m 
                break
            elif self.b=="suzuki":
                m=["baleno","swift"]
                print(m)
                m=input("select your model:")
                self.m=m 
                break
            else:
                print("invalid")   
             
    def price(self):
        while True:
            if self.b=="mahindra" and self.m=="thar" :
                p=1700000
                break
            elif self.b=="mahindra" and self.m=="scorpio" :
                p=2000000
                break
            elif self.b=="toyota" and self.m=="innova" :
                p=2600000
                break
            elif self.b=="toyota" and self.m=="fortuner" :
                p=5000000
                break
            elif self.b=="suzuki" and self.m=="baleno" :
                p=900000
                break
            elif self.b=="suzuki" and self.m=="swift":
                p=1000000
                break
            else:
                print("invaild")   
        final_price =p+ p*(self.cgst+self.sgst)/100+self.insurance
        print(final_price)            
c =["mahindra","suzuki","toyota"]
print(c)        
obj=carshowroom(18,18,200000)
obj.company()
obj.model()
obj.price()
