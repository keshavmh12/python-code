#duplicate item are not allow in set
#sets have not any defined order
#idexing also allowed in the set
#item of sets are unchangeable
#true and 1 both are also a duplicate value of eachother
set1={1,2,3,4,5,6}
print(set1)
set2={"keshav","jerry","harry"}
print(set2)
set3={1,2,3,4,"keshav","jarry",5,6}
print(set3)
set4={1,"true"}
print(set4)
#indexing not allowed print(set1[2])
set5={} #it type show dictonary
print(type(set5),type(set3))
#set1[2]=65 it give error because set item are unchangeable
set1.add("keshav") # for add item in sets
print(set1)
set1.remove(3)
print(set1)
set1.discard(2)#this is also for remove the item
print(set1)
set4.clear()
print(set4)
set3.pop()
print(set3)#this is use for remove any random item from the sets
print(set3.pop())#this is for print which item remove
set3.add((34,54,33,22))#this is for add a tuple
print(set3)
set3.add([34,55,32,11])#list are not add in the set because list are changeable