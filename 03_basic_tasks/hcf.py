def HCF(n,m):
    factor_n=[]
    factor_m=[]
    while n!=1:
        for i in range (2,n+1):
            if n%i==0:
                n=n//i
                factor_n.append(i)
                break
    while m!=1:
        for i in range (2,m+1):
            if m%i==0:
                m=m//i
                factor_m.append(i)
                break
    hcf=1
    for k in factor_n:
        if k in factor_m:
            hcf=hcf*k
            factor_m.remove(k)
    print(hcf) 
       
HCF(12,18)          
               
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

                                                                                                                         

    


