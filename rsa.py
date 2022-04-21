import math
def find_mod_inv(a,m):
    flag = 1
    for x in range(1,m):
        if((a%m)*(x%m) % m==1):
            flag =0
            return x
    if(flag==1):
        print("Inverse not found")

p=1223
q=1229

n=p*q
eularTotient = (p-1)*(q-1)
for i in range(4,eularTotient):
    if(math.gcd(i,eularTotient)==1):
        e = i
        break

d = find_mod_inv(e,eularTotient)
print("PUBLIC KEY : "+str(e)+" , "+str(n))
print("PRIVATE KEY : "+str(d)+" , "+str(n))

plainText=31
ciperext = pow((plainText),e)%n
print('ENCRYPTION : ')
print("CIPER TEXT : "+str(ciperext))

# DECRYPTION
p = pow(ciperext,d)%n
print('AFTER DECRYPTION : ')
print("PLAIN TEXT : "+str(p))
print("19DCS088 GRACY PATEL")
