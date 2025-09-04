
##method1 :  all the methods are imported to the programspace
import math 
print(math.tan(1))
print(math.log(1))

#method2 :  importing with alias name
import math as m
print(m.log(1))
print(m.cos(1))

# method3: importing required methods only
from math import cos,sin,log
print(cos(3))
print(sin(1))