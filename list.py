from os import remove

number=[1,3,4,5,6,]
name=["sket","prathamesh","agrisha","kunal"]
mix_list=[1,"saket",2,3,"keshav",4,5]
print(mix_list)
print(mix_list[0])
print(mix_list[4])#for perticular number
print(mix_list[-2])#start from back
print(number[0:4])#between
print(number[1:5:2])#jumpby2
number.reverse()

print(min(number))
print(max(number))
number.append(55)#add one number at the end at once
print(number)
number.sort()
print(number)
number.pop()
print(number)
number.insert(2,66)#add number at some perticular position
print(number)
number.extend([56,58,48,5,7,6])#in the extend the list with multiple number at once to the end
print(number)
number[3]=33#for change the value at perticular position
print(number)
number[4:7]=11,22 #for change value in between of some position
print(number)
number.remove(1)#it will remove though value
print(number)
number.pop(0)#it will remove through index
print(number)
print(number.pop(0))
