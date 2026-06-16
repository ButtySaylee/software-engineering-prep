# Day 4 Project - Student Grade Manager
# Butty Saylee - software-engineering-prep

# =============================================
# A program to manage a list of studet scores
# Using lists, loops, and comprehensions
# =============================================

print("=" * 35)
print("     Student Grade Manager")
print("=" * 35)

scores = []

num_students = int(input("\n How many students? "))
for i in range(num_students):
    score = int(input(f"Enter score for student {i + 1}: "))
    scores.append(score)

print("\nAll scores entered: {scores}")

# ==================================
# Analyze the scores
# ==================================

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

print("\n" + "=" * 35)
print("      Class Statistics")
print("=" * 35)
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
print(f"Average score: {average:.2f}")

# =================================================
# Using list comprehension to find passing students
# =================================================

# if passing score is 50 or above
passing_scores = [s for s in scores if s >= 50]
failing_scores = [s for s in scores if s < 50]

print(f"\nPassing scores ({len(passing_scores)}): {passing_scores}")
print(f"Failing scores ({len(failing_scores)}): {failing_scores}")

# ====================================================================
# Assigning letter grades using list comprehension + a helper function
# ====================================================================

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
    
grades = [get_grade(s) for s in scores]

print(f"\nLetter grades: {grades}")

# =================================================================
# showing each student's score + grade side-by-side using enumerate
# =================================================================

print("\n" + "=" * 35)
print("     Final Report")
print("=" * 35)

for index, score in enumerate(scores):
    grade = grades[index]
    print(f"Student {index + 1}: Score = {score}, Grade = {grade}")

# ==========================================
# Sorting scores to showing ranking
# ==========================================

ranked = sorted(scores, reverse=True)

print(f"\nRanked scores (highest to lowest): {ranked}")

