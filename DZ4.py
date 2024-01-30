from functools import reduce
import math

def correlation (data1, data2):
    n = len(data1)
    mean1 = sum(data1) / n
    mean2 = sum(data2) / n

    deviation1 = list(map(lambda x: x - mean1, data1))
    deviation2 = list(map(lambda x: x - mean2, data2))

    numerator = reduce(lambda x, y:x+y[0]*y[1]\
                       , zip(deviation1, deviation2), 0)
    denominatior = math.sqrt(reduce(lambda  x, y:x+y**2, deviation2, 0))

    if denominatior == 0:
        return 0
    return numerator / denominatior

data1=[1,2,3,4,5]
data2=[2,3,8,10,15]
corr =correlation(data1,data2)

print(corr)