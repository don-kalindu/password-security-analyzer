import getpass
from analyzer import analyze_password

print("=" * 50)
print("     PASSWORD SECURITY ANALYZER")
print("=" * 50)

password = getpass.getpass("Enter the password to analyze : ")
analyze_password(password)

