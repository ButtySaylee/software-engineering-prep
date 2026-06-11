# Day 2 - Conditionals & User Inpur
# Butty Saylee - software-engineering-prep

# ====================================
# PART 1 - Comparison Operators
# ====================================

x = 10
y = 20

print(x == y)
print(x != y)
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)

# =====================================
# PART 2 - if/elif/else
# =====================================

age = int(input("\nEnter your age: "))

if age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")

# =====================================
# PART 3 - Logical Operators
# =====================================

score = int(input("\nEnter your score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D:)")
else:
    print("Grade: F") 
 
# not operator example
is_raining = False
if not is_raining:
    print("\nGo outside, it's not raining!")

# or operator example
day = input("\nEnter day of week: ")
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday, keep grinding!")

# =========================================
# PART 4 - Nested if statements
# =========================================

num = int(input("\nEnter a number: "))

if num >= 0:
    if num == 0:
        print("The number is zero")
    else:
        print("The number is positive")
else:
    print("The number is negative")

