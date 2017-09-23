"""
Create a Program that does the following:
1.	Prompt the user to select a shape
2.	Depending on the shape the user selects, calculate the area of that shape
3.	Print the area of that shape to the user.
4.	Verify all errors including users inputting uppercase letters or single letters of the shapes .

"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "The calculator is starting up..."

print '%s/%s/%s %s:%s' % (now.month, now.day, now.year, now.hour, now.minute)
sleep(1)

hint = "Don't forget to include the correct units! \nExiting... "

option = raw_input("Enter C for Circle or T for Triangle: ")

option = option.upper()

if option == 'C':
    radius = float(raw_input("Enter the radius: "))
    area = pi * radius ** 2
    print "The pie is baking..."
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))
    if option == 'T':
        base = float(raw_input("Enter the base: "))
        height = float(raw_input("Enter the height: "))
        area = (0.5) * base * height
        print "Uni Bi Tri..."
        sleep(1)
        print ("Area: %.2f. \n%s" % (area, hint))
