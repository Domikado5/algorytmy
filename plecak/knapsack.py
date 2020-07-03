# n - all items (length)
# c - knapsack capacity

import itertools
import json
import random
import time

def generate_items(data, n, c):
    items = []
    for i in range(n):
        item = data[i]
        item['weight'] = random.randint(1, c)
        item['value'] = random.randint(1, n*10)
        items.append(item)
    return items

def brute_force(items, n, c):
    posibilities = [ list(i) for i in itertools.product([0, 1], repeat=n) ]
    result = 0

    for combination in posibilities: # iterate all posibilities
        index = 0
        sum_of_value = 0
        capacity = 0

        for item in combination: # iterate through items
            if item:
                sum_of_value += items[index]["value"]
                capacity += items[index]["weight"]

            index += 1

        if capacity <= c and sum_of_value > result:
                result = sum_of_value

    return result

def dynamic(items, n, c):
    costs = [ [ None for j in range(c+1) ] for i in range(n+1) ]
    for i in range(n+1):
        for j in range(c+1):
            if i == 0 or j == 0:
                costs[i][j] = 0
            else:
                if items[i-1]["weight"] > j:
                    costs[i][j] = costs[i-1][j]
                elif items[i-1]["weight"] <= j:
                    w = items[i-1]["weight"]
                    v = items[i-1]["value"]
                    costs[i][j] = max([ costs[ i - 1 ][ j ], costs[ i - 1 ][ j - w ] + v ] )
    return costs[-1][-1]

json_file = open('./plecak/products.json') # directory depend from the location where we run python script so it may be different
products = json.load(json_file)

# f(N) test

test1 = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]


file1 = open('./fN.txt', 'w')

for n in test1:
    c = 1000
    print(n, end=' ')

    items = generate_items(products, n, c)

    before = time.time()*1000
    x1 = brute_force(items, len(items), c)
    after = time.time()*1000

    time1 = round(after-before, 0)
    print(time1, end=' ')

    before = time.time()*1000
    x2 = dynamic(items, len(items), c)
    after = time.time()*1000

    time2 = round(after-before, 0)
    print(time2)

    if x1 != x2:
        print('FAIL')
        print('Brute force: ', x1, 'Dynamic: ', x2)
        break

    file1.write(f"{n};{time1};{time2}\n")

file1.close()

test2 = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]


file2 = open('./fC.txt', 'w')

for c in test2:
    n = 15
    print(c, end=' ')

    items = generate_items(products, n, c)

    before = time.time()*1000
    x1 = brute_force(items, len(items), c)
    after = time.time()*1000

    time1 = round(after-before, 0)
    print(time1, end=' ')

    before = time.time()*1000
    x2 = dynamic(items, len(items), c)
    after = time.time()*1000

    time2 = round(after-before, 0)
    print(time2)

    if x1 != x2:
        print('Brute force: ', x1, 'Dynamic: ', x2)
        break

    file2.write(f"{c};{time1};{time2}\n")

file2.close()