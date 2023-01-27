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


a= [[1,2],[3,4]]
b = [[5,6],[7,8]]
def matrix_multiplication(a,b): 
    a_rows = len(a) 
    a_column = len(a[1])
    b_rows = len(b) 
    b_column = len(b[1])  

    

    matrix = [] 

    b_temp_column = []
    for z in range(b_rows):
        for y in range(b_column): 
            b_temp_column.append(b[z][y])
            print(b_temp_column) 


matrix_multiplication(a,b)


    