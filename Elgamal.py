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

p= 11
d= 3
e1 = 2
r = 4
pt = 7

e2 = np.mod(pow(e1,d),p)
print("VALUE OF E2 ",e2)

ct1 = np.mod(pow(e1,r),p)
print("VALUE OF CT1 ",ct1)

ct2 = np.mod(pt*pow(e2,r),p)
print("VALUE OF CT2 ",ct2)

print("ENCRYPTED TEXT [ct1,ct2] = [",ct1,",",ct2,"]")

# DECRYPTION

dpt = np.mod((ct2 * (find_mod_inv(pow(ct1,d), p))),p)
print(dpt)

# n=p*q
# eularTotient = (p-1)*(q-1)
# for i in range(4,eularTotient):
#     if(math.gcd(i,eularTotient)==1):
#         e = i
#         break

# d = find_mod_inv(e,eularTotient)
# print("PUBLIC KEY : "+str(e)+" , "+str(n))
# print("PRIVATE KEY : "+str(d)+" , "+str(n))

# plainText=31
# ciperext = pow((plainText),e)%n
# print('ENCRYPTION : ')
# print("CIPER TEXT : "+str(ciperext))

# # DECRYPTION
# p = pow(ciperext,d)%n
# print('AFTER DECRYPTION : ')
# print("PLAIN TEXT : "+str(p))
# print("19DCS088 GRACY PATEL")
