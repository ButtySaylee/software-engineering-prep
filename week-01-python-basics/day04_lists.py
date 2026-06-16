# Day 4 - List & List Operations
# Butty Saylee - software-engineering-prep

# ======================================
# PART 1 - Creating and accessing lists
# ======================================

nums = [10, 20, 30, 40, 50]

#Indexing
print(nums[0])
print(nums[2])
print(nums[-1])
print(nums[-2])

#Slicing
print(nums[1:4])
print(nums[:3])
print(nums[2:])
print(nums[:])

# ======================================
# PART 2 - Modifying lists
# ======================================

fruits = ["apple", "banana", "cherry"]

#append()
fruits.append("mango")
print(fruits)

#insert()
fruits.insert(1, "orange")
print(fruits)

#remove()
fruits.remove("banana")
print(fruits)

#pop()
last_item = fruits.pop()
print(last_item)
print(fruits)

# reverse()
fruits.reverse()
print(fruits)

# len()
print(len(fruits))

# ===============================
# PART 3 - Looping through lists
# ===============================

scores = [85, 92, 78, 60, 95]

#Method 1
for score in scores:
    print(score)

print("---")

#Method 2
for index, score in enumerate(scores):
    print(f"Student {index + 1}: {score}")

# ==================================
# PART 4 - List comprehensions
# ==================================

#without comprehension:
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)

#with comprehension:
squares2 = [x **2 for x in range(10)]
print(squares2)

#with a condition - only even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# Transform AND filter existing list
doubled_scores = [s * 2 for s in scores if s>= 80]
print(doubled_scores)

# ===================================
# PART 5 - 2D Lists (lists of lists)
# ===================================
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access an item:
print(grid[0][0])
print(grid[1][2])
print(grid[2][1])

print("---")

# Looping through a 2D list - nested loops
for row in grid:
    for item in row:
        print(item, end=" ")
        print()

print("---")

# ==================================
# PART 6 - Useful lis functions
# ==================================

values = [4, 2, 9, 1, 7]

print(max(values))
print(min(values))
print(sum(values))
print(sorted(values))
print(values)  

print("---")

# "in"
print(7 in values)
print(100 in values)