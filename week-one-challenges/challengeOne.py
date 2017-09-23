"""
CHALLENGE ONE (PYTHON SYNTAX)
1.	First, let's declare the variable meal and assign it the value 44.50.
2.
Create the variable tax and set it equal to the decimal value of 6.75%.
3.
Set the variable tip to decimal value of 15%
4.	reassign meal to the value of itself + itself * tax. (And yes, you're allowed to reassign a variable in terms of itself!)
5.	Assign the variable total to the sum of meal + meal * tip .

"""


meal = 44.50
tax = 6.75 / 100
tip = 15.0 / 100

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)
