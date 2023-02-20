import datetime
cur = datetime.datetime.now()
print("First programm: ")
print(cur - datetime.timedelta(days=5))

print("Second programm: ")
print("today ",cur.strftime("%A"))
yst = cur - datetime.timedelta(days=1)
print("yesterday ",yst.strftime("%A"))
tmw = cur + datetime.timedelta(days=1)
print("tomorrow ",tmw.strftime("%A"))

print("Third programm: ")
#print("введите микросекунды")
m = 1000 #int(input())
print(cur)
print(cur - datetime.timedelta(microseconds=m))

print("Fourth programm: ")
#print("введите даты через пробел год месяц день")
#d1 = str(input()).split(" ")
#d2 = str(input()).split(" ")
#d1y = int(d1[0])
#d1m = int(d1[1])
#d1d = int(d1[2])
#d2y = int(d2[0])
#d2m = int(d2[1])
#d2d = int(d2[2])
#dt1 = datetime.datetime(d1y,d1m,d1d)
#dt2 = datetime.datetime(d2y,d2m,d2d)
#delt = dt1 - dt2
#print(delt)
sd1 = '2023/02/19'
sd2 = '2004/10/06'
d1 = datetime.datetime.strptime(sd1, "%Y/%m/%d")
d2 = datetime.datetime.strptime(sd2, "%Y/%m/%d")
delta = d1 - d2
print(delta.days)



