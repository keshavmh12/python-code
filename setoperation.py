#these are for union method
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
set3={"kfkf","eokdoek","okdep","kwkkk"}
set1.union(set2)
set2.union(set1)
print(set1.union(set2))
print(set1|set2|set3)
print(set1.union(set2|set3))
print(set1.union("mohan","jenny"))#this is for union with tuple
#print(set1 | ("jdj","edde"))this is not support
set1.update(set2)#in this set1 and set2 are geting join without duplication
print(set1)
set1 |= set2 #this is also use for add two set

#intersection method
set4={"keshav","saket","mohan","myur"}
set5={"saket","aam","mnoj"}
set6={"kunal","prathamesh"}
print(set4.intersection(set5))
print(set4.intersection(set5,set6))
print(set4 & set5)
print(set5.intersection["loss","profit"])
set5.intersection_update(set6)#it will givwe olny commen item in set5 and set 6,in this set5 only update
print(set5)


print(set4.difference(set5))#it is like subtraction
print(set4 - set5)#same
print(set1.difference(("fjf","keshav","efoe")))#this is for tuple
print(set4.difference(set5,set6))
set4.difference_update(set5)#in this set 4 updated
print(set4)


print(set4.symmetric_difference(set5))#in this return all item from both set without common item
#print(set4.symmetric_difference(set5,set6)) for multiple set symmetric differece not allowed
print(set4^set5^set6)#symmetric difference for multiple set
set4.symmetric_difference_update(set5)