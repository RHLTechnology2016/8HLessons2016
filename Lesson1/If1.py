#This program should expalin how If Statments work. As you can see we use == to represent equal to, != to represent not equal to, the <> than signs to represent greater/less than, etc. 


user = raw_input("Enter some text:")

#If the user enters Hello then we will print a special message.
if user == "Hello":
  print "You entered the secret password!"

#If the User does not enter Hello, we then check to see if the user entered something else and print another message.

elif user == "I was wondering after all these years":
  print "You entered a bad password!"

#If none of the user never entered Hello or I was wondering after all these years let's give them a final message. 
else:
  print "Helloo, from the other sidee....."
  

#you can have if Statments inside If Statements as well

pass = raw_input("Enter the password:")
bad  = raw_input("Enter the bad password:")
name = raw_input("Enter Your name:")

#you can test for two things as we can see in the below statement. 
if pass == "8IA" and pass != "8GA" : #Tests to see if the password is 8IA and if its is not 8GA. If either one of these conditions are false, the code below it will not be run. 
  print "Welcome agent!"
  if name == "AgentSpyname":
    print "Hi Alex"
  elif name == "Agent Cloud":
    print "Hi Derek :D"


else:
  print "Wrong Password"
  
#Now let's see what we can do with Numbers
num1 = input("Enter a number:")

if num1 == 21:
  print "That is the best number!" 
elif num1 == 19:
  print "That is a good number!"
elif num1 > 15 and num1 < 19:
  print "Close to the best number!"

elif num1 > 15 and num1 < 19:
  print "Close to the best number!"

elif num1 > 19 and num1 < 21:
  print "Close to a good number!"
  
else:
  print "Far away!" 
  
#This was quite a bit, even more than we did in class. There is even a few more things we can do we IF Statments, but we will look at those later!
  
