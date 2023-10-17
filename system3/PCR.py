import random
import numpy as np
from matplotlib import pyplot as plt
import math

N = 1000000
E = 0
m = 10
p = 0.001
# for i in range(N):
#     E += (N/10 + i*m)*math.comb(N/m, i)*(1-(1-p)**m)**i*((1-p)**m)**(N/m-i)

m_lst = np.arange(1, 200 + 1)
Elst = []
def Expect(m, p):
    E = N/m*(1+m-m*(1-p)**m)
    return E
for m in m_lst:
    Elst.append(Expect(m, p))

fig, ax = plt.subplots()
ax.plot(m_lst,Elst)
plt.show()


plst = np.arange(0,1,0.0001)



N = 10000


def group_inspect(m, p =0.001):
    ratio = m/N
    result_lst = []
    inspect_times = 0

    for i in range(int(1/ratio) + 1):
        ra = random.random()
        if ra < (1-p)**m :
            result_lst.append(False)
        else :
            result_lst.append(True)
        inspect_times += 1
        
    for result in result_lst:
        if result:
            inspect_times += m
    return inspect_times



m_lst = np.arange(1, 500 + 1)

# print(m_lst)
times_lst = []
for m in m_lst:
    times = group_inspect(m)
    times_lst.append(times)
    
min_id = np.argmin(times_lst)
m_min = m_lst[min_id]
print(m_min)
print(min(times_lst))
fig, ax = plt.subplots()
ax.plot(m_lst, times_lst)
plt.show()

p_lst = np.arange(0,1,0.001)
times_lst = []
for p in p_lst:
    times = group_inspect(m_min, p)
    times_lst.append(times)

for i in range(len(times_lst)):
    if times_lst[i] > N :
        bound = p_lst[i]
        break
print(bound)
fig, ax = plt.subplots()
ax.plot(p_lst, times_lst)
ax.axhline(N, c = "r")
ax.axvline(bound, c = "r")
plt.show()