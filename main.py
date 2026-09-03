print("=" * 50)
print("     PASSWORD SECURITY ANALYZER")
print("=" * 50)

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