#Here is a program from the Book "Hello World!" with my comments, which should further explain If statments. This is a nice simple overview!

# Listing_7-1.py
# Copyright Warren Sande, 2009
# Modifications By Alexander Parsan, 2016 
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 62  ----------------------------


#Gets two numbers from user

num1 = input("Enter the first number: ") 
num2 = input("Enter the second number: ")

#If num1 is greater than num2 
if num1 < num2:
    print num1, "is less than", num2
    
#If Num1 less than Num2
if num1 > num2:
    print num1, "is greater than", num2

#If num1 is equal to Num2
if num1 == num2:                         
    print num1, "is equal to", num2

#If Num1 does not equal Num2

if num1 != num2:
    print num1, "is not equal to", num2
