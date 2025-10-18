#range(start,stop,stepsize)  have three argument for range
a=range(2,8)
print(a[4])

#using loop
a=range(2,8)
for i in a:
    print(i)

#in this we use stepsize
a=range(2,12,2)  #for stepsize 0 not allowed
for i in a:
    print(i)


# sum no. from 1 to 101
total=0
for i in range(1,101):
    total+=i
print(total)