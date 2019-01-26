r1=input("enter no.of rows of first matrix")
c1=input("enter no.of columns of first matrix")
r2=input("enter no.of rows of second matrix")
c2=input("enter no.of columns of second matrix")
x=[]
y=[]
z=[]
if (c1==r2):
 for i in range(r1):
      a=[]
      for j in range(c1):
        p=input("enter element")
        a.append(p)
      x.append(a)
 print x
 for i in range(r2):
      b=[]
      for j in range(c2):
         q=input("enter elements")
         b.append(q)
      y.append(b)
 print y
 for i in range(r1):
       e=[]
       for j in range(c2):
         sum=0
         for k in range (c1):
            sum=sum+x[i][k]*y[k][j]
         e.append(sum)
       print e
else:
  print("matrix multiplication is not possible")
        
