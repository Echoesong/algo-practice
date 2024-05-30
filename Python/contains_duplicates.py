def containsDuplicates(array):
    mySet = set()
    for value in array:
        mySet.add(value)
    if len(mySet) == len(array):
        return False
    else: 
        return True
    

data = [1, 2, 3, 4, 5]
data2 = [1, 1, 2, 3, 4, 5]

print(containsDuplicates(data))
print(containsDuplicates(data2))