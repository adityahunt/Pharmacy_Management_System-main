# def greetings():
#     print("Welcome to python")
# greetings()
# def add(n1,n2):
#     return n1+n2
# result=add(10,20)
# print("sum is",result)
# def si(p,r,t):
#     return p*r*t/100
# simpleinterest=si(10000,6,1)
# print(f"Simple Interest is {simpleinterest}")

class product():
    code:int
    name:str
    supplier:str
    price:int
    def info(self):
        print("Product Code : ", self.code)
        print("Name         : ", self.name)
        print("Supplier      : ", self.supplier)
        print("Price         : ", self.price)

prod1=product()
prod1.code=1
prod1.name="Balm"
prod1.supplier="Vicks"
prod1.price=144000
print("\n\nDetails of Product 1:\n")
prod1.info()

class customer():
    def __init__(self,code,name,email,mobile):
        self.code=code
        self.name=name
        self.email=email
        self.mobile=mobile
def __str__(self):
    return "testing str"
cust1=customer(1,"aditya,aditya@gamil.com",9998887770)
print("\nCustomer Details:\n")
