def sequence(T):
    p_min = [0 for _ in range(len(T)//3)]
    p_max = [0 for _ in range(len(T)//3)]
    temp_first = 0
    leng = 1
    n = 0
    
    for i in range(len(T)-1):
        leng += 1
        
        if T[i] < T[i+1] and leng == 3:
            p_min[n] = temp_first
        elif T[i] < T[i+1] and leng == 2:
            temp_first = T[i]
        elif T[i] >= T[i+1] and leng > 3:
            p_max[n] = T[i]
            leng = 1
            n += 1
        elif T[i] >= T[i+1]:
            leng = 1

    if T[-1] > T[-2] and leng > 2:
        p_max[n] = T[-1]

    if p_min[1] != 0 and p_max[1] != 0:
        j = 0
        while j+1 < len(p_min) and p_min[j+1] != 0:
            k = j+1
            while k < len(p_min) and p_min[k] != 0:
                if p_min[k] > p_max[j] or p_min[j] > p_max[k]:
                    return True
                    #, p_min, p_max, p_min[k], p_max[j], p_min[j], p_max[k]
                k += 1
            
            j += 1

    return False

T = [2,15,17,13,17,19,23,2,6,4,8,3,5,7,1,3,2]
#T = [2,15,17,13,17,19,23,2,6,4,8,3,5,7,14,3,2]

print(sequence(T))
