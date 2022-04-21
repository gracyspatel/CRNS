import math
import numpy as np

def find_mod_inv(a,m):
    flag = 1
    for x in range(1,m):
        if((a%m)*(x%m) % m==1):
            flag =0
            return x
    if(flag==1):
        print("Inverse not found")


# Step 1
h=int(input("Value of h"))
p=int(input("Value of p"))
q= int(input("Value of q"))
g = np.mod(pow(h,((p-1)/q)),p)
print("Value of g = ")
print(g)

x = int(input("Enter x"))
y = np.mod(pow(g,x),p)
print("Value of y = ")
print(y)

k = int(input("Enter k "))
r = np.mod( np.mod( pow(g,k) ,p), q )
print("Value of r = ")
print(r)

kinv = find_mod_inv(k, q)
print("Value of kinv = ")
print(kinv)

hm = int(input("Enter value of h(m)"))
s = np.mod(((kinv)*(hm+x*r)),q)
print(s)


# Verification
sinv = find_mod_inv(s, q)
print("Value of sinv = ")
print(sinv)

t = np.mod((hm*sinv),q)
print("Value of t = ")
print(t)

u = np.mod(r*sinv,q)
print("Value of u = ")
print(u)


v = np.mod(np.mod(pow(g,t) * pow(y,u),p ),q)
print("Value of v = ")
print(v)

if(v == r):
    print("Verified")