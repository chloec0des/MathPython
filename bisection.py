
import matplotlib.pyplot as plt
import math

from numpy import linspace
list=[]

def bisection(f, a, b, k):
    ak=a
    bk=b
    for n in range(1,k+1):
        xk=(ak+bk)/2
        fxk=f(xk)
        #print(xk)
        list.append(xk)
    

        if f(xk)*f(ak)<0:
            ak=ak
            bk=xk
        else:
            bk=bk
            ak=xk
    return list

fsqt = lambda x:2*math.sin(x)-x

list=bisection(fsqt, -(math.pi), -((math.pi)/2), 20)
list=bisection(fsqt, (math.pi), ((math.pi)/2), 20)
print(list)
xlist=linspace(-5,5, 100)
ylist=[]
for x in xlist:
    ylist.append(fsqt(x))

plt.plot(xlist, ylist)
plt.plot([-1.8954954183525143, 1.8954954183525143], [0, 0], 'b*', label='Bluestars')
plt.title('Graph')
plt.xlabel('X axis')
plt.ylabel('Y axis')
for x in list:
    plt.axvline(x=x)
plt.show()