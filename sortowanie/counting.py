def sort(a,n,maxNumber):
    count = [0 for i in range(maxNumber+1)]
    for i in a:
        count[i] += 1
    total = 0
    for i in range(maxNumber+1):
        count[i], total = total, count[i] + total
    b = [0 for i in range(len(a))]
    for i in a:
        b[count[i]] = i
        count[i] += 1
    return b