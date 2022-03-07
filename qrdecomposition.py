#QR decomposition

#1.3
import numpy as np
import math
A = np.random.randint(2, size=(7, 5))
#A=np.array([[1,1],[1,0]])
#test = np.array([[3.0, 1.0], [2.0, 2.0]])
#test2 = np.array([[1.0, 1.0, 0.0], [1.0, 3.0, 1.0], [2.0, -1.0, 1.0]])
B=A.transpose()
n=len(B)
w=[]
w.append(B[0])
def fun1(x,v):
    de=0
    nu=0
    for i in range(len(v)):
        de+=v[i]*v[i]
    for i in range(len(v)):
        nu+=x[i]*v[i]
    res=[]
    for i in range(len(v)):
        res.append(v[i]*(nu/de))
    return res
def sub(x,v,flag):
    temp=[]
    if flag==0:
        return v
    for i in range(len(v)):
        temp.append(x[i]-v[i])
    return temp
        
def func2(x,n):
    i=1
    j=0
    flag=1
    while len(w)<n:
        j=0
        v=[0,0]
        while j<=i-1:
            temp=fun1(x[i],w[j])
            #print("yes")
            if j==0:
                flag=0
            else:
                flag=1
            v=sub(v,temp,flag)
            j=j+1
        w.append(sub(x[i],v,1))
        #print("f2",v)
        i=i+1

            



    #w.append(sub(x[i],fun1(x[i],w[i-1])))qw
        
def modlength(v):
    sums=0
    for i in v:
        sums=sums+(i**2)
    m=math.sqrt(sums)
    #print(sums,m)
    #print("vector",v)
    soln=[]
    for k in range(len(v)):
        #print(v[k]/m)
        soln.append(v[k]/m)
        #print(v[k])
    
    return soln
#print(B)
func2(B,n)
#print("After",w)
Z=[]
for k in w:
    Z.append(modlength(k))
Z=np.array(Z)


R=[]
R=np.dot(Z,A)
Soln=np.subtract(A,(np.dot(Z.transpose(),R)))

def normf(mat):
    sumsq=0
    m=len(mat)
    n=len(mat[0])
    import math
    for i in range(m):
        for j in range(n):
            sumsq+=(mat[i][j]**2)
    return sumsq
print("Norm",normf(Soln))



def gram_schmidt_columns(X):
    Q, R = np.linalg.qr(X)
    print(R)
    return Q
val=gram_schmidt_columns(A)

