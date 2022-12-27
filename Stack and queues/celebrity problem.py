
def findCelebrity(n, knows):

    # Write your code here.    
    st = [i for i in range(n)]
    while len(st) > 1:
        t1 = st.pop()
        t2 = st.pop()
        if (knows(t1, t2) and knows(t2, t1)):
            pass
        elif knows(t1, t2):
            st.append(t2)
        elif knows(t2, t1):
            st.append(t1)
    if len(st) > 0:
        for i in range(n):
            if i != st[0] and not knows(i, st[0]):
                return -1
        return st[0]
    return -1