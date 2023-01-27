#part 1
def dot_product(a,b): 
    ans = 0
    for i in range(len(a)):
        q = a[i] * b[i]
        ans = ans + q 
    
    return(ans)


a = [1,1,1,1]
b = [1,1,1,1]

print(dot_product(a,b))
