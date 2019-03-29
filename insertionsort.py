def insertion_sort(n):
    for i in range (1,len(n)):
        value = n[i]
        pos = i
        while pos>0 and n[pos-1]>value:
            temp = n[pos-1]
            n[pos-1] = n[pos]
            n[pos] = temp
            pos = pos-1    
    print(n)

sorte = [9,8,7,6,5,4,3,2,1]    
insertion_sort(sorte)
