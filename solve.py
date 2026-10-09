def count_event(l):
    count=0
    for i in range(1,l+1):
        if i % 2 == 0:
            count = count + 1
    return count
print(count_event(7))            
