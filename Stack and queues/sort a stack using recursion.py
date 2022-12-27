
def addsorted(stack, t):
    if len(stack) == 0:
        stack.append(t)
        return
    if stack[-1] > t:
        temp = stack.pop()
        addsorted(stack, t)
        stack.append(temp)
    else:
        stack.append(t)
    

def sortStack(stack):
    # given data structure is a python list 
    # as list have all the similar operations available so use them
    # Write your code here
    if len(stack) == 0:
        return
    temp = stack.pop()
    sortStack(stack)
    addsorted(stack, temp)