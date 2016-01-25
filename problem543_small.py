

def P(i,k):
    return i    


def S(n):
    summ=0
    for i in range (n):
        for k in range (n):
            summ += P(i,k)
    return summ

def F(k):
    F=[0,1]
    for x in range (2,k):
        F.append((F[x-2]+F[x-1]))
    return(F[3:k])

#print (F(5))

def problem_543(g):
    ar = F(g+(1))
    finalsum=0
    for x in range (len(ar)):
        print (ar[x])
        finalsum+=S(ar[x])
    return finalsum
        
print(problem_543(44))
