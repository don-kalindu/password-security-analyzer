print("=" * 50)
print("     PASSWORD SECURITY ANALYZER")
print("=" * 50)

score = 0

password = input("Enter the password to analyze : ")

print("\nPassword Received.")
print("Password length", len(password))

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

#strength level
if score == 5:
    print("Password strength : STRONG")

elif score == 3 or score == 4:
    print("Password strength : MEDIUM")

else:
    print("Password strength : WEAK")
