#input() method always return a string, so we need to convert it to an integer using int() method
num1 = int(input("Enter first number: ")) # Take first number from user and convert to int
num2 = int(input("Enter second number: ")) # Take second number from user and convert to int
mul = num1 * num2 #multiplying num1 and num2
print("The Multiplication of",num1,"and",num2,"is: ",mul)
# Check for division by zero before performing division
if num2 == 0:
    # Division by zero is not mathematically supported
    print("Division by zero is not allowed.")
else:
    div = num1 / num2 # division of num1 and num2
    print("The division of",num1,"and",num2,"is: ",div)