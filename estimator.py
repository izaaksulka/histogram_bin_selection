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


for k in range(mink, maxk):
    delta = len(values) / k
    