#question1
def numbers():
    for even in range(2,21,2):
        print(even)
numbers()


#question2  
number = 0
while number <= 10:
    print("Processing user input ")
    number = int(input("Enter a number of your choice: "))
    number += 0
if number > 10:
    print("User input should be less than or equal to 10")    


#question3
number = int(input("Enter any number: "))
for count in range(1,11):
    product = number * count
    print(number, "x", count, "=", product )
    for count in range(1,6):
        product = number * count        
        print(number, "x", count, "=", product )
        
        
#question4
list1 = [4,7,2,9,12,15]
for odd in list1:
    sum = 0
if odd % 2 != 0:
    Total = sum + odd
    print(Total)
    
    
