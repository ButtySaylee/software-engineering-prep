# Day 2 Project - Smart Login System
# Butty Saylee - software-engieering-prep

# =======================================
# A simple login system with 3 attempts
# =======================================

correct_username = "butty"
correct_password = "python123"

max_attempts = 3

print("=" * 35)
print("     Welcome to SecureLogin")
print("=" *35)

attempts = 0

while attempts < max_attempts:

    attempts +=1

    print(f"\nAttempt {attempts} of {max_attempts}")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("\nAccess granted! Welcome,", username)
        print("Redirecting to dashboard...")
        break
    else:
        remaining_attempts = max_attempts - attempts

        if remaining_attempts > 0:
            print(f"X Wrong credentials. {remaining_attempts} attempts left.")
        else:
            print("\nX Too many failed attempts. Account locked.")
            print("Please contact support.")

# =============================
# Username validator
# =============================

print("\n" + "=" * 35)
print("    Username Validator")
print("=" * 35)

new_username = input("\nChoose a username: ")

if len(new_username) < 3:
    print("X Too short. Must be at least 3 characters.")
elif len(new_username) > 15:
    print("X Too long. Must be under 15 characters. ")
elif " " in new_username:
    print("X No spaces allowed in username.")
else:
    print(f" '{new_username}' is a valid username!")
