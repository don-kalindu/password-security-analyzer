from pathlib import Path


#loading common passwords to analyze
def load_common_passwords():
    base_dir = Path(__file__).parent
    password_file = base_dir / "common_passwords.txt"

    with open(password_file, "r") as file:
        content = file.read()
        common_passwords = content.splitlines()
    
    #cleaning common_password list and add that into clean_passwrdds list
    clean_passwords = []

    for common_password in common_passwords:
        common_passwords = common_password.strip().lower()
        if common_password != "":
            clean_passwords.append(common_password)

    return clean_passwords

#simple function experiment
def analyze_password(password):

    #comparing common passwords
    common_passwords = load_common_passwords()
    is_common = password.lower() in common_passwords

    #checking some parameters

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_numbers = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    score = 0
    recommendations = []

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

    #Strength level
    if is_common:
        strength = "WEAK"

    elif score == 5:
        strength = "STRONG"

    elif score == 3 or score == 4:
        strength = "MEDIUM"

    else:
        strength = "WEAK"

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


    result = {
    "score": score,
    "strength": strength,
    "recommendations": recommendations,
    "Contains uppercase" : has_uppercase,
    "Contains lowercase" : has_lowercase,
    "Contains Numbers" : has_numbers,
    "Contains Special" : has_special,
    "Password_length" : len(password)
    }

    return result