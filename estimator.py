import sys
import math
import statistics

f = open(sys.argv[1], 'r')
values = f.read().split("\n")
values = [float(x) for x in values if x != ""]
f.close()



print (len(values))

mink = math.log(len(values), 2)
maxk = math.sqrt(len(values))

mean_values = statistics.mean(values)

costs = {}

for k in range(int(mink), int(maxk) + 1):
    delta = len(values) / k
    
    hist = []
    for v in values:
        index = int(v / delta)
        hist.append(index * delta + delta / 2)

    mean_hist = statistics.mean(hist)
    
    cost = abs(mean_hist - mean_values)
    costs[k] = cost
    
top_three = []
for i in range(3):
    top_three.append(min(costs.keys(), key=lambda x: costs[x]))
    del costs[top_three[-1]]
    
print (top_three)