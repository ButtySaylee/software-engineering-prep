# Day 3 - Loops (for  & while)
# Butty Saylee - software-engineering-prep

# ====================================
# PART 1 - The for loop with range()
# ====================================

# range(5)
for i in range(5):
    print(i)

print("---")

# range(start, stop)
for i in range(1, 6):
    print(i)

print("---")

# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)

print("---")

# looping backwards
for i in range(10, 0, -1):
    print(i)

print("-----------------")

# =====================================
# PART 2 - The while loop
# =====================================

count = 1
while count <= 5:
    print(f"Count is {count}")
    count += 1

print("-------------------")

# =======================================
# PART 3 - break and continue
# =======================================

for i in range(1, 11):
    if i ==5:
        break
    print(i)

print("---")

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

print("---------------")

# ====================================
# PART 4 - Nested loops
# ====================================

for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

    print("---")
print("-------------------")

# ===========================================
# PART 5 - Looping through strings and lists
# ===========================================

word = "Python"

for letter in word:
    print(letter)

print("---")

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

print("--------------------")

# ====================================
# PART 6 - enumerate()
# ====================================

for index, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")




