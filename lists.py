#a list is a sequence used to store items
#question1
fruits = ["apples","pears","water-mellon","oranges","pineapples"]
for fruit in fruits:
    print(fruit)
    
    
#question2
def squared_list():
    list2 = [1,2,3]
    for element in  list2:
     result = (element**2)
     print(result)

squared_list() 
     
#question3 (zip or list comprehension)
list1 =[1,2,3]
list2 = [4,5,6]
result = (list1 + list2)
print(result)


#question4
numbers = [3,1,4,1,5,9,2]
numbers.sort()
print(numbers)
print(numbers[6])
print(numbers[5])
print(f"The two largest numbers in the list are {numbers[5]} and {numbers[6]}")



   