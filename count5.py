
def power(m) : 

	if (m == 0) : 
		return 0
	else : 
		return 1 + power(m // 10) 


def MaximumProduct(N): 
    if (N == 2):  
        return 1;  
    if (N == 3):  
        return 2;  
    
    maxProduct=0;  
    if(N % 3==0):  
        maxProduct = power(int(N/3));  
        return maxProduct;  
    elif(N%3==1): 
        maxProduct =2* power(int(N/3) - 1);  
        return maxProduct; 
    elif(N%3==2): 
        maxProduct =2*power(int(N/3)); 
        return maxProduct;  
maxProduct = MaximumProduct(10);  
print(maxProduct);  