print("=" * 50)
print("     PASSWORD SECURITY ANALYZER")
print("=" * 50)

score = 0
recommendations = []

password = input("Enter the password to analyze : ")

#comparing common passwords
common_passwords = ["password", "123456", "qwerty", "admin", "password123!"]
is_common = password.lower() in common_passwords

print("\nPassword Received.")
print("Password length", len(password))

print()

#in here checking for any uppercase letters
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_numbers = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

print("Contains uppercase: ", has_uppercase)
print("Contains lowercase: ", has_lowercase)
print("Contains Numbers: ", has_numbers)
print("Contains Special: ", has_special)

#getting decisions 
if len(password) >= 12:
    print("Your password is Good")
else:
    print("Your password is short")

print()

#scoring
if has_uppercase:
    score = score + 1

if has_lowercase:
    score = score + 1

if has_numbers:
    score = score +1

if has_special:
    score = score + 1

if len(password) >= 12:
    score = score + 1

print("Security Score : ", score,"/5")

print()

#Strength level
if is_common:
    print("Password strength : WEAK")

elif score == 5:
    print("Password strength : STRONG")

elif score == 3 or score == 4:
    print("Password strength : MEDIUM")

else:
    print("Password strength : WEAK")

print()

#Recommendations

if not has_uppercase:
    recommendations.append("Add at least one uppercase letter.")

if not has_lowercase:
    recommendations.append("Add at least one lowercase letter.")

if not has_numbers:
    recommendations.append("Add at least one number.")

if not has_special:
    recommendations.append("Add at least one special character.")

if len(password) < 12:
    recommendations.append("Add at least 12 characters.")

if is_common:
    recommendations.append("Avoid using common passwords.")

if len(recommendations) > 0:
    print("Recommendations :")

    for recommendation in recommendations:
        print("- ",recommendation)
