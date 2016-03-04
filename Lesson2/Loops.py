#Loops.py
#Short Program to show how loops are used in Python. 
#Program Written By: Alexander Parsan
#Parts of Program By: Warren Sande, 2009 from "Hello world"
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php

#Loops help us repeat code over and over again. 

#Instead of doing this
print "hello"
print "hello"
print "hello"
print "hello"
print "hello"

print "Now let's try using a For Loop"
#Below prints Hello 5 times
for looper in [1, 2, 3, 4, 5]:
    print "hello"
    
#If you have want to loop more than 10 times, a shortcut is to use range()

for looper in range (1, 100):
    print looper, "times 8 =", looper * 8 #Prints nth time we have looped * 8 
    
#You can also go through a list like this:
for cool_guy in ["Spongebob", "Spiderman", "Justin Timberlake", "My dad"]:
    print cool_guy, "is the coolest guy ever!"
    
#while loops will continue executing the code as long as the condition is true


print "Type 3 to continue, anything else to quit."
someInput = raw_input()
while someInput == '3':                                  # While the input is Three
    print "Thank you for the 3.  Very kind of you."          #Print this
    print "Type 3 to continue, anything else to quit."       #Restarts
    someInput = raw_input()                                  #
print "That's not 3, so I'm quitting now." #When the loops ends

#AS we take a look at CCC Questions, loops are used a lot to repeat bits of code.


