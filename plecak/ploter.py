import matplotlib.pyplot as plt

fC = open("fC.txt", 'r')
c = []
bf1 = []
dp1 = []

for line in fC:
    tmp = line.split(';')
    c.append(int(tmp[0]))
    bf1.append(float(tmp[1]))
    dp1.append(float(tmp[2]))

fC.close()

plt.plot(c, bf1, c, dp1)
plt.ylabel('Time (ms)')
plt.xlabel('n - how many items')
plt.title('f(C), n = 15')
plt.legend(['Brute Force', 'Dynamic'])
plt.show()

fN = open("fN.txt", 'r')

n = []
bf2 = []
dp2 = []

for line in fN:
    tmp = line.split(';')
    n.append(int(tmp[0]))
    bf2.append(float(tmp[1]))
    dp2.append(float(tmp[2]))

fN.close()

plt.plot(n, bf2, n, dp2)
plt.ylabel('Time (ms)')
plt.xlabel('c - capacity of knapsack')
plt.title('f(N), c = 1000')
plt.legend(['Brute Force', 'Dynamic'])
plt.show()