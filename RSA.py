import random
# Use recursion similar to the euclidian algorithm to find the gcd, s and t
def EEA(r0, r1):
    r = [r0, r1]
    s = [1, 0]
    t = [0, 1]
    q = []
    while r[-1] != 0:
        q.append(r[-2] // r[-1])
        r.append(r[-2] % r[-1])
        s.append(s[-2] - q[-1] * s[-1])
        t.append(t[-2] - q[-1] * t[-1])
    if (r[-2] == 1):
        return (t[-2]%r[0])
    else:
        return ('there is no modular inverse')
# Use recursion to get the remainder then returns a once it equals to 0
def EA(a, b):
    if (b == 0):
        return a
    return EA(b, a % b)
    
def powmod_sm(bs, exp, n):
# Turns the exponent into binary value
    exp = bin(exp)
    x = bs
 # Starts on the 3rd item in the binary and stop once it exceeds it length
    for i in range(3,len(exp)):
        x = (x * x) % n
 # Turns the string in an array and check to see if It's either 1 or 0
        if exp[i] == '1':
            x = (x * bs) % n
    return x
#Checks to see if a number is prime or composite
def MRT(n):
    s = 512
    r = n-1
    u = 0
    while r % 2 == 0:
        u += 1
        r = r // 2
    for _ in range(s):
        a = random.randrange(2, n - 2)
        z = powmod_sm(a,r,n)
        if z == 1 or z == n-1:
            for j in range(1,u-1):
                z= z*z%n
        else:
            return False
        return True
                
def RSA(p, q, msg):
#Calculation of n,phi of n and choosing a random e
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = random.randrange(1, phi_n - 1)
 
#If the gcd of e and phi of n equal to 1 continue else choose a new e
 
    if EA(e, phi_n) == 1:
 
#Modular inverse of e and phi is our d
 
        d = EEA(phi_n,e)
 
        print("Public Key:", n, ",", e)
 
        print("Private Key:", d)
 
#Encryption
 
        y = powmod_sm(msg, e, n)
 
        print("Encrypted message:", y)
 
#Decryption
 
        x = powmod_sm(y, d, n)
 
        print("Decrypted message:", x)
 
    else:
        RSA(p,q,msg)

def prime(bit):
 #Chooses a random number with the amount of bits
    n=int(random.randint(2**(bit-1)+1,2**bit))
 #If MRT returns True then return n or else choose a new n
    while MRT(n)!=True:
        return prime(bit)
    return n
    
def main():
#The number of bit your number should have
    bit = 30
#Generate a random prime number
    p = prime(bit)
    q = prime(bit)
#If p and q are equal change q
    while p == q:
        q = prime(bit)
    msg = 99
    print("Message=",msg)
    print("First Prime", p)
    print("Second Prime", q)
    #Calls RSA function
    RSA(p, q, msg)

main()
