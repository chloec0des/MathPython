def Heron(x, k):
   xk=x
   for n in range(1,k+1):
       xk=((x/2)+1)/(2*xk)
       xk=xk
       return xk
fsqt = lambda x:x**2 -2
Heron(fsqt,20)