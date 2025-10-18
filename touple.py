#tuple1=(1) python does not recognise as a touple it is recignize as integer only have must put value after comma
#tuple are unchangeable
tuple1=(1,2,3,4,4,5,5)
print(tuple1[2:4])#range print
print(tuple1[::2])#SKIP 2
tuple2=(6,"raam",2,4,"aaam,2,4")
touple4=(tuple1,tuple2)
print(touple4)
rouple3=("eaaa","kddkdk","sowks")
print(rouple3[1])
print(type(rouple3))
print(rouple3[1:])
print(len(rouple3))
tuple5=tuple2+rouple3 #concetinate
print(tuple1.count(4)) #count 4
list1=[23,3,24,45,43,12]
print(tuple(list1))#converting list into tuple
tuple6=(1,2,3,4,4,5,5)*10 #it will help in print 10 times
print(tuple6)
