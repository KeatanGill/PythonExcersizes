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