import getpass
from analyzer import analyze_password

print("=" * 50)
print("     PASSWORD SECURITY ANALYZER")
print("=" * 50)

password = getpass.getpass("Enter the password to analyze : ")
result = analyze_password(password)

print("Password length is ", result["Password_length"])
print()
print("Uppercase letter detected: ", result["Contains uppercase"])
print("Lowercase letter detected: ", result["Contains lowercase"])
print("Numbers detected: ", result["Contains Numbers"])
print("Special character detected: ", result["Contains Special"])
print()
print("Score: ", result["score"])
print("Password Strength: ", result["strength"])
print()

if len(result["recommendations"]) > 0:
    print("Recommendations :")

    for recommendation in result["recommendations"]:
        print("- ",recommendation)

print()