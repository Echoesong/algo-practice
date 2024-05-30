def isAnagram(s, t):
    if len(s) != len(t):
        return False
    myDict = {}
    for character in s:
        if character in myDict:
            myDict[character] += 1
        else:
            myDict[character] = 1
    for letter in t:
        if not letter in myDict:
            return False
        if letter in myDict:
            myDict[letter] -= 1
    dictValues = myDict.values()
    for count in dictValues:
        if count != 0:
            return False
    return True
    




print(isAnagram('racecar', 'racerac'))
print(isAnagram('racecar', 'raceca'))
print(isAnagram('racecar', 'racecaz'))
