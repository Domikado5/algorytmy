def sort(a):
    gap = len(a) // 2
    while gap > 0:
        for i in range(gap):
            tmp = a[i]
            j=0
            while True:
                for g in range(i,len(a)-gap,gap):
                    if a[g] > a[g+gap]:
                        a[g], a[g+gap] = a[g+gap], a[g]
                    else:
                        j+=1  
                if j == len(a[i:len(a):gap])-1:
                    break
                else:
                    j = 0
        gap = gap // 2
    return a