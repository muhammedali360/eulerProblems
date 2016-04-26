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


print (problem62(5))
