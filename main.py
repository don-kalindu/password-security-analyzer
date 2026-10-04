import getpass
from analyzer import analyze_password

print("=" * 50)
print("     PASSWORD SECURITY ANALYZER")
print("=" * 50)
print()
password = getpass.getpass("Enter the password to analyze: ")
result = analyze_password(password)
print()
print("Password Analysis")
print("-" * 50)

print(f'{"Length:":<19}{result["Password_length"]}')
print(f'{"Uppercase:":<19}{"Yes" if result["Contains uppercase"] else "No"}')
print(f'{"Lowercase:":<19}{"Yes" if result["Contains lowercase"] else "No"}')
print(f'{"Numbers:":<19}{"Yes" if result["Contains Numbers"] else "No"}')
print(f'{"Special character:":<19}{"Yes" if result["Contains Special"] else "No"}')
print()
print(f'{"Score:":<19}{result["score"]}/5')
print(f'{"Strength:":<19}{result["strength"]}')
print()

print("Recommendations:")

if len(result["recommendations"]) > 0:
    for recommendation in result["recommendations"]:
        print("-", recommendation)
else:
    print("No improvements required.")

print()
