def problem21 (N):
    
    divisorsSum=[1]*N
    divisorsSum[0]=0



    for i in range (2,N+1):
        for j in range (2*i,N+1,i):
            divisorsSum[j-1]+=i
    #print (divisorsSum)
            
            
    print (divisorsSum[3])
            
            
        
    #print (divisors[283])
    total=0
    for x in range (1,N):
        for y in range (1,x):
            if x==divisorsSum[y-1] and y==divisorsSum[x-1] and x!=y:
                total+=(x+y)
    
    return total


print (problem21(10000))

