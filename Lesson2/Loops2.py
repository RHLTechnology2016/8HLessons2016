#Loops2.py
#Short Program to show how loops are used in Python. 
#Program Written By: Alexander Parsan
#Parts of Program By: Warren Sande, 2009 from "Hello world"
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php

    
#while loops will continue executing the code as long as the condition is true


print "Type 3 to continue, anything else to quit."
someInput = raw_input()
while someInput == '3':                                  # While the input is Three
    print "Thank you for the 3.  Very kind of you."          #Print this
    print "Type 3 to continue, anything else to quit."       #Restarts
    someInput = raw_input()                                  #
print "That's not 3, so I'm quitting now." #When the loops ends

#AS we take a look at CCC Questions, loops are used a lot to repeat bits of code.


