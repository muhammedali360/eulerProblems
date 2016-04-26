from time import clock, time
from datetime import datetime
start = clock()

def problem62(n):
    num = 100
    h = {}
    result = 0

    while True:
        num+=1
        cubed = num ** 3
        cubed = int(''.join( sorted(str(cubed), reverse = True) ))

        if cubed not in h:
            h[cubed] = [num]
        else:
            h[cubed].append(num)
        if len(h[cubed]) == n:
            result = (min(h[cubed])**3)
            print (h[cubed])
            break
        
    
    #print (cubed)
    return result


#print (problem62(9'))
if __name__ == "__main__": 

    n =  [  2,  3,  4,  5]
    expected = [ 5**3, 345**3, 1002**3, 5027**3]                                                                                          
    errors = 0
    for i in range(len(n)):
        print ("Computing S({0})   time={1}".format(n[i], datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    if n[i] <= 1:                                                                                                                              
        DEBUG = True                                                                                                                            
    else:                                                                                                                                      
        DEBUG = False
                 
    res = problem62(n[i])                                                                                                                         
    if res == expected[i]: # round(expected[i],4):                                                                                             
        print ("GOOD  : S({0})={1}   (errors={2})  time={3}\n".format(n[i], res, errors, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))           
    else:                                                                                                                                      
        errors += 1                                                                                                                             
        print ("ERROR  : S({0})={1} (expected={2})   (errors={3})  time={4}\n".format(n[i], res, expected[i], errors, datetime.now().strftime("%\Y-%m-%d %H:%M:%S")))                                                                                                                             
                                                                                                                                            
    print ("Total number of errors={0}".format(errors))
    print ("Run Time = {0:.0f} sec".format(clock()-start)) 

