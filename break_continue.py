count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        break
    print("hii")
print("end of loop")



list1=["hi","hello","welcome"]
name1=["krishna","ram","madhav"]
for item in list1:
    for name in name1:
        print(item,name)
        if item=="hello" and name=="ram":
            break
    print("end inner loop")
print("end of outer loop")

count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        continue
    print("hii")
print("end of loop")


for i in range(1,11):
    if i==7:
        continue
    else:
        print(i)



#for pass statement
count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        pass
    print("hii")
print("end of loop")

for i in range(1,11):
    pass