def sieve(n):
    a=[True]*(n+1)
    for i in range(2,n):
        if a[i]:
            print(i)
            for j in range(i*i,n,i):
                a[i]=False
sieve(100)
                
    
