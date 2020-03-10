def sort(a):
    for i in range(len(a)):
        for j in range(i,0,-1):
            if a[j] >= a[j-1]:
                break
            else:
                a[j], a[j-1] = a[j-1], a[j]
    return a