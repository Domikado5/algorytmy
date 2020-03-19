import random
def part(a, l, r):
    tmp = random.randint(l,r)
    a[l], a[tmp] = a[tmp], a[l]
    m = a[l]
    i = l+1
    for j in range(l+1,r+1):
        if a[j] <= m:
            a[i], a[j] = a[j], a[i]
            i = i+1
    a[i-1], a[l] = a[l], a[i-1]
    return i-1

def sort(a, l, r):
    if l < r:
        i = part(a, l, r)
        sort(a, l, i-1)
        sort(a, i+1, r)
    return a