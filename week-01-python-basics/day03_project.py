# Day 3 Project - Pattern Printer & Number Analyzer
# Butty Saylee - software-engineering-prep

# ================================
# PART 1 - Patten Printer
# ================================

print("=" * 35)
print("    Pattern Printer")
print("=" * 35)

size = int(input("\nEnter the size of the pattern (eg. 5): "))

# Pattern - 1: Right triangle of stars
print("\nPattern 1 - Triangle: ")
for i in range(1, size + 1):
    print("*" * i)

# Pattern - 2: Inverted triangle
print("\nPattern 2 - Inverted Triangle: ")
for i in range(size, 0, -1):
    print("*" * i)

# Pattern -3: Number pyramid
print("\nPattern 3 - Number Pyramid: ")
for i in range(1, size + 1):
    row = ""
    for j in range(1, i + 1):
        row = row + str(j)

    print(row)

# ==================================
# PART 2 - Number Analyzer
# ==================================

print("\n" + "=" * 35)
print("    Number Analyzer")
print("=" * 35)

count = int(input("\nHow many numbers do you want to analyze? "))

total = 0
even_count = 0
odd_count = 0
biggest = None

for i in range(count):
    num = int(input(f"Enter number {i + 1}: "))

    #add to running total
    total = total + num

    #check even or odd
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

#Track the biggest number seen so far
if biggest is None or num > biggest:
    biggest = num

#calculate average
average = total / count

# =========================
# Print final report
# =========================

print("\n" + "=" * 35)
print("    Analysis Report")
print("=" * 35)

print(f"Total numbers entered: {count}")
print(f"Sum:                   {total}")
print(f"Average:               {average:.2f}")
print(f"Even numbers:          {even_count}")
print(f"Odd numbers:           {odd_count}")
print(f"Biggest number:        {biggest}")