#Python Program to Convert Centimeters to Feet and Inches

height = int(input("Enter your height in CM : "))

inches = 0.394*height
feets = 0.0328*height
print("The length in inches",round(inches,2))
print("The length in feet",round(feets,2))