def validPars(s):
    # Okay, so we can have as many opening brackets as we want: (((({{{{ etc, it can still technically be valid. So whenever we see an opening par, we will add it to the stack.
    hashMap = {')':'(', '}':'{', ']':'[' }
    stack = []
    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        if char == ')' or char == '}' or char == ']':
            if len(stack) == 0:
                return False
            top = stack.pop()
            if hashMap[char] == top:
                continue
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

            



s = "(){}[]"
print(validPars(s))
