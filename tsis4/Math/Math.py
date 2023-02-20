import math
d = 15
r = math.radians(d)
print("Input degree:" + str(d))
print("Output radian:" + str(round(r,6)))
print('\n')
h = 5
a = 5
b = 6
res = h*(a+b)/2
print("Height:" +str(h))
print("Base, first value:" +str(a))
print("Base, second value:" +str(b))
print("Expected Output:" +str(res))
print('\n')
n = 4
s = 25
t = math.tan(math.radians(180/n))
area = (s*s*n*0.25)/t
print("Input number of sides:" +str(n))
print("Input the length of a side:" + str(s))
print("The area of the polygon is:" +str(round(area)))
print('\n')
lb = 5
hp = 6
areap = lb * hp
print("Length of base:"+str(lb))
print("Height of parallelogram:"+str(hp))
print("Expected Output:"+str(areap))
