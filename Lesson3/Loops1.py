
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
