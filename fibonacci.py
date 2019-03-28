def fib(n1,n2,count,n_len,a):
    if n_len <= 0:
        print("Please enter a positive integer")
    elif n_len == 1:
        print("Fibonacci sequence upto",n_len,":")
        print(n1)
    else:
        pass    
    if count < n_len:
        a.append(n1)   
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
        fib(n1,n2,count,n_len,a)
    return a


n_len = int(input())

a = []
a1 = fib(0,1,0,n_len,a)
print("Fibonacci sequence upto",n_len,":")
print(a1)


# ,end=' , '