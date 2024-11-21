#question1
class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color       
car1 = Car("mercedez_benz","grey")
car1.brand = "mercedez_benz"
car1.color = "grey"
print(f"I bought a {car1.color} {car1.brand}")
#question2
class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    
    
    def start_engiene(self):
        print("The engiene of the car has started")
    
    
car2 = Car("range_rover","white")  
car2.start_engiene() #when calling a method of a class we use a period and the instance


#question3
class Bankacount:
    def __init__(self,account_number,balance):
        self.account = account_number
        self.balance = balance
        
    def deposit(self,deposit_money):
        self.option = deposit_money
        
        user_input = int(input("Choose an option of your choice\n 1.Deposit money\n 2.Withdraw money\n 3.See your account balance"))
        while user_input == 1:
            print("Enter your deposit amount: ")
Bankacount.deposit()
        
        
        
        
        
 
    
