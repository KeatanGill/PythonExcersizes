from math import pi
# part 1
pi_100 = 0 

for i in range(0,100):
    q = 8/(((4*i)+1)*((4*i)+3)) 
    pi_100 = pi_100 + q

print (pi_100) 

pi_1000 = 0 

for i in range(0,1000):
    q = 8/(((4*i)+1)*((4*i)+3)) 
    pi_1000 = pi_1000 + q

print (pi_1000)  


pi_10000 = 0 

for i in range(0,10000):
    q = 8/(((4*i)+1)*((4*i)+3)) 
    pi_10000 = pi_10000 + q

print (pi_10000)  


#part 2
error_100 = abs(pi-pi_100)
print(error_100) 

error_1000 = abs(pi-pi_1000)
print(error_1000) 

error_10000 = abs(pi-pi_10000)
print(error_10000)   


#part 3
error = 1
n = 1 
while error > 10^(-7):
    eprox_pi = 8/(((4*n)+1)*((4*n)+3))
    error = abs(eprox_pi - pi)   
    n = n+1

print(n)


