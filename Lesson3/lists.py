#lists.py
#Short Program to show how lists are used in Python. 
#Program Written By: Alexander Parsan
#Under the GPL v3.0

#This is just a short intro to lists, we can do a lot more with them.
#Let's say you wanted to collect variables into one list. You could do that using a list.

mylist = ["Bowen", "Derek", "Palash", "Rizwan", "Aaron"]

print mylist #Prints all names 
print mylist[0] + " is god" #Prints Bowen
print mylist[1] #Prints Derek

#This works with numbers

numbers = [9,10,11,12,13,14,15,16]

print numbers #prints all numbers
print numbers[0] #prints 9 

#you can add values to lists after
fathers = ["Sir John A Macdonald", "Sir Charles Tupper", "George Etienne Cartier"]
print fathers 
name = raw_input("Enter a name:") 
fathers.append(name) #Adds the name entered by the user to the list fathers
print fathers

#Or add multiple values
id = [900041, 945748, 48950483, 31431]
print id 
id.extend([2,3,4,5])#Adds more values
print id

#Delete a value by simply deleting it like this

del id[2]; #Removes 48950483


