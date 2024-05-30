def isAnagram(str1, str2):
    myDict1 = {}
    myDict2 = {}
    for character in str1:
        if character in myDict1:
            myDict1[character] += 1
        else:
            myDict1[character] = 1
    for letter in str2:
        if letter in myDict2:
            myDict2[letter] += 1
        else:
            myDict2[letter] = 1
    print('Dict1: ', myDict1.keys(), myDict1.values())
    print('Dict2: ', myDict2.keys(), myDict2.values())
    if myDict1.keys() == myDict2.keys() and myDict1.values() == myDict2.values():
        return True
    else:
        return False
    




print(isAnagram('racecar', 'racerac'))
