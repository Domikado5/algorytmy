def part(a, l, r):
    i = l-1
    m = a[r]
    for j in range(l,r):
        if a[j] < m:
            i = i+1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

def sort(a, l, r):
    if l < r:
        i = part(a, l, r)
        sort(a, l, i-1)
        sort(a, i+1, r)
    return a