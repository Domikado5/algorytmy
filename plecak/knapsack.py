# n - all items (length)
# c - knapsack capacity

import itertools
import json
import random


def generate_items(data, n, c):
    items = []
    for i in range(n):
        item = data[i]
        item['weight'] = random.randint(1, c)
        item['value'] = random.randint(1, n*100)
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
    costs = [ [ None for j in range(c) ] for i in range(n) ]
    for i in range(n):
        for j in range(c):
            if i == 0 or j == 0:
                costs[i][j] = 0
            else:
                if items[i]["weight"] > j:
                    costs[i][j] = costs[i-1][j]
                elif items[i]["weight"] <= j:
                    costs[i][j] = max([ costs[ i - 1 ][ j ], costs[ i - 1 ][ j - items[ i ]['weight'] ] + items[ i ]['value']] )
    return costs[-1][-1]

json_file = open('./plecak/products.json') # directory depend from the location where we run python script so it may be different
products = json.load(json_file)

test1 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]



for n in test1:
    c = 30

    items = generate_items(products, n, c)

    print(brute_force(items, len(items), c))

    print(dynamic(items, len(items), c))

