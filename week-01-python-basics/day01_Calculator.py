# Day 1 - Variables and Data Types
# Butty Saylee - software-engineering-prep

name = "Butty"
age = 27
cgpa = 6.3
is_student = True

print(f"name: {name}")
print(f"Age: {age}")
print(f"CGPA: {cgpa}")
print(f"Is student: {is_student}")

# Check the type of each variable
print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

# ====================================
# Day 1 Project - CLI Calculator
#=====================================

def calculator():
    print("=" * 30)
    print("   Welcome to CLI Calculator")
    print("=" * 30)
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"\nResults for {num1} and {num2}:")

    print(f"Addition:     {num1} + {num2} = {num1 + num2}")
    print(f"Substraction: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} x {num2} = {num1 * num2}")

    if num2 != 0:
        print(f"Division: {num1} / {num2} = {num1 /num2:.2f}")
        print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
        print(f"Remainder: {num1} % {num2} = {num1 % num2}")
        print(f"Power: {num1} ** {num2} = {num1 ** num2}")
    else:
        print("Division: Cannot divide by zero!")

calculator()



