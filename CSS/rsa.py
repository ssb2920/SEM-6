from math import gcd
p,q = [int(x) for x in input('Enter the value of p and q = ').split()]
print("n="+str(p*q))
m = int(input('Enter the value of text less than n = '))
Φn = (p-1)*(q-1)
for e in range(2,Φn):
    if gcd(e,Φn)== 1: break
for i in range(1,10):
    x = 1 + i*Φn
    if x % e == 0:
        d = int(x/e)
        break
ct = pow(m,e,p*q)
dt = pow(ct,d,p*q) 
print('n = '+str(p*q)+'\ne = '+str(e)+'\nΦ(n) = '+str(Φn)+'\nd = '+str(d)+'\ncipher text = '+str(ct)+'\ndecrypted text = '+str(dt))