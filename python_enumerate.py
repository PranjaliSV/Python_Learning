# Python program to illustrate 
# enumerate function 
l1 = ["eat","sleep","repeat"] 
s1 = "pranjali"
  
# creating enumerate objects 
obj_l1 = enumerate(l1) 
obj_s1 = enumerate(s1) 

print ("l1", l1,"\n")  
print ("obj_l1", obj_l1)
print ("Return type:", type(obj_l1)) 
print ("list_enumerate_l1", list(enumerate(l1))) 
# changing start index to 2 from 0 
print (list(enumerate(l1,-10)), "\n\n\n")

print ("s1", s1, "\n") 
print ("obj_s1", obj_s1)
print ("Return type:", type(obj_s1)) 
print ("list_enumerate_s1", list(enumerate(s1))) 
# changing start index to 2 from 0 
print (list(enumerate(s1,2)))


  
 
