#question1
student = {'name':'Peace','age':22,'grade':"A"}
# student.keys()
for key,value in student.items():
    print(f"{key}:{value}")


#question2
def info():
    people_older = []
    personal_info = {"Alice" : 24, "Bob" : 19, "Charlie" : 30}
    for name, age in personal_info.items():
        if age > 21:
            people_older.append(name)
    return people_older
print(info())


#question3
dict_store = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
list1 = ['apple', 'orange', 'banana', 'banana']
def total_cost():
    cost = 0
    for x in list1:
        cost += dict_store[x]
    return cost
print(total_cost())


#question4
def count_occurences(sentence):
    word_count = sentence.lower().split()
    count_dict = {}
    for word in word_count:
        if word in count_dict:
            count_dict[word] += 1
        else: 
            count_dict[word] = 1
    return count_dict
sentence =("hello world hello")
result = count_occurences(sentence)
print(result)
    