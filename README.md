## Common Password Dataset

This project uses a common-password wordlist from the SecLists project for common-password detection.

Dataset:
`xato-net-10-million-passwords-1000.txt`

Source:
SecLists – Passwords/Common-Credentials

The dataset is loaded from `common_passwords.txt`. During loading, the application removes surrounding whitespace, converts entries to lowercase, and ignores empty entries before performing password comparisons.