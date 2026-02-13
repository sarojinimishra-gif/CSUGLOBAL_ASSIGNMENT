#input() method always return a string, so we need to convert it to an integer using int() method
num1 = int(input("Enter first number: ")) # Take first number from user and convert to int
num2 = int(input("Enter second number: ")) # Take second number from user and convert to int
sum = num1 + num2 # Addition of num1 and num2
sub = num1 - num2 # Subtraction of num1 and num2
print("The addition of",num1,"and",num2,"is: ",sum)
print("The subtraction of",num1,"and",num2,"is :",sub)