def sort(a, l, r):
    if l < r:
        m = (l+r)//2
        sort(a, l, m)
        sort(a, m+1, r)
        merge(a, l, r, m)
    return a
def merge(a, l, r, m):
    tmp = a.copy()
    i = l
    j = m+1
    k = l
    while i <= m and j <= r:
        if tmp[i] < tmp[j]:
            a[k] = tmp[i]
            i+=1
        else:
            a[k] = tmp[j]
            j+=1
        k +=1
    while i <= m:
        a[k] = tmp[i]
        i+=1
        k+=1
    while j <= m:
        a[k] = tmp[j]
        j+=1
        k+=1