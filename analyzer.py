from pathlib import Path


#loading common passwords to analyze
def load_common_passwords():
    base_dir = Path(__file__).parent
    password_file = base_dir / "common_passwords.txt"

    with open(password_file, "r") as file:
        content = file.read()
        common_passwords = content.splitlines()

    return common_passwords

#simple function experiment
def analyze_password(password):
    print("Analyzing Password...")

    #comparing common passwords
    common_passwords = load_common_passwords()
    is_common = password.lower() in common_passwords

    print("\nPassword Received.")
    print("Password length", len(password))

    print()

    #checking some parameters

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_numbers = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    print("Contains uppercase: ", has_uppercase)
    print("Contains lowercase: ", has_lowercase)
    print("Contains Numbers: ", has_numbers)
    print("Contains Special: ", has_special)

    score = 0
    recommendations = []

    print()

    #getting decisions 
    if len(password) >= 12:
        print("Your password is Good")
    else:
        print("Your password is Short")

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
        strength = "WEAK"

    elif score == 5:
        strength = "STRONG"

    elif score == 3 or score == 4:
        strength = "MEDIUM"

    else:
        strength = "WEAK"

    print("Password strength :", strength)

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

    print()

    result = {
    "score": score,
    "strength": strength,
    "recommendations": recommendations
    }

    return result