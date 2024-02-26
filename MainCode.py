#Find the sum of all the multiples of 3 or 5 below 1000.

list1 =[]
list2 =[]
for i in range(1,10):
    if i%3 == 0:
        j = i
        if j%5 == 0:
            list1.append(j)
