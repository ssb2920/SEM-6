import Crypto.Util.number

from Crypto import Random

import sys


bits=100

if (len(sys.argv)>1):
        bits=int(sys.argv[1])

print ("No of bits in prime is ",bits)

p=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print ("\nRandom n-bit Prime (p): ",p)

q=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print ("\nRandom n-bit Prime (q): ",q)

N=p*q

print ("\nN=p*q=",N)		

PHI=(p-1)*(q-1)

print ("\nPHI (p-1)(q-1)=",PHI)

e=65537
print ("\ne=",e)
d=Crypto.Util.number.inverse(e,PHI)
print ("d=",d)

print ("\nCount of decimal digits (p): ",len(str(p)))
print ("Count of decimal digits (N): ",len(str(N)))

M=5
print ("\n\n=== Let's try these keys ==")
print ("\nRSA Message: ",M)
enc=pow(M,e,N)
print ("RSA Cipher(c=M^e mod N): ",enc)
dec = pow(enc,d,N)
print ("RSA Decipher (c^d mod N): ",dec)
