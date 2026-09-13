for i in range(2,101):#yha se i ki value lega for eg.for first loop i=2
    for j in range(2,i):#ab i=2 k liye ye wala pura loop chalega 
        if i%j==0:#agar kisi bhi no.se divide to loop break ho jayega or agla no. check karega
            break
    else:print(i)#agar nhi divide hua to printa ho jayega no.
            