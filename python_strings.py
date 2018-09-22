#-------------------------------String Creation------------------------------------
  
myname = 'Pranjali'
mysurname = 'Vakil'                    # string with single quotes
hello_world = "Hello World"            # string with double quotes
triple_quote_string = '''Hey....    
How are you ? '''                      # string with triple quotes
  
#-------------------------Display a String---------------------------------- 
print(myname) 

#-------------------------Causes error-Strings are immutable----------------   
#myname[2] = 'E'
#print(myname)


#------------------------String can be appended to a string----------------- 

myname = myname + mysurname  
myname = "Name : " + myname
print(myname)

#----String ID-id() function is used to return the identity of an object.---
  
print("myname => ", id(myname)) 
myname = myname + ": Name"
print("myname _Changed String =>", id(myname)) 
print("mysurname => ", id(mysurname)) 

#-----------------Concatenation of strings created ------------------------ 

print("Concatenation of Different Strings =>" ,mysurname + hello_world + triple_quote_string)  
 
#-------------------- use of escape sequence------------------------------- 
print("He said, \"Welcome \"")   
print('Hey so happy to be here') 
 
#---------------------use of mix quotes------------------------------------ 
print ('Getting Geeky, "Loving it"')   

