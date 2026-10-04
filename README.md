# Password Security Analyzer

Password Security Analyzer is a Python-based command-line tool designed to evaluate password strength based on several security criteria. It checks password length and the presence of uppercase letters, lowercase letters, numbers, and special characters, while also checking whether the password appears in a common-password dataset.

The analyzer calculates a strength score and provides recommendations when security requirements are not met. The project also includes automated tests covering normal behavior, boundary conditions, and edge cases to help ensure that the analyzer behaves consistently.




## Features

- Checks whether a password contains uppercase and lowercase letters.
- Checks for numbers and special characters.
- Verifies whether the password meets the minimum length requirement of 12 characters.
- Calculates a password security score from 0 to 5 based on the criteria met.
- Classifies passwords as WEAK, MEDIUM, or STRONG based on the calculated score.
- Checks passwords against a common-password dataset and classifies matching passwords as WEAK.
- Provides recommendations for security criteria that are not satisfied.
- Uses hidden password input so the entered password is not displayed in the terminal.



## How It Works

1. The user enters a password through the command-line interface. The password input is hidden using Python's `getpass` module.

2. The password is passed to the `analyze_password()` function, which performs the main password analysis.

3. The analyzer checks whether the password:
   - Contains an uppercase letter.
   - Contains a lowercase letter.
   - Contains a number.
   - Contains a special character.
   - Meets the minimum length requirement of 12 characters.

4. The password is compared against the entries loaded from `common_passwords.txt` to determine whether it is a known common password.

5. A score from 0 to 5 is calculated based on the security criteria satisfied by the password.

6. The analyzer determines the password strength:
   - **STRONG** — score of 5.
   - **MEDIUM** — score of 3 or 4.
   - **WEAK** — score of 0 to 2.
   - A password found in the common-password dataset is classified as **WEAK**, regardless of its score.

7. Recommendations are generated for any security criteria that the password does not satisfy.

8. The analysis results are returned to the command-line interface, which displays the password characteristics, score, strength level, and recommendations.



## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/don-kalindu/password-security-analyzer.git
cd password-security-analyzer
```

### 2. Create a Virtual Environment

#### Windows

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Development Dependencies

```bash
python -m pip install -r requirements-dev.txt
```

The application itself uses Python standard-library modules. The development requirements include `pytest` for running the automated test suite.



## Usage

With the virtual environment activated, run:

```bash
python main.py
```

### Example Output

```text
==================================================
     PASSWORD SECURITY ANALYZER
==================================================

Enter the password to analyze:

Password Analysis
--------------------------------------------------
Length:            10
Uppercase:         No
Lowercase:         Yes
Numbers:           Yes
Special character: Yes

Score:             3/5
Strength:          MEDIUM

Recommendations:
- Add at least one uppercase letter.
- Add at least 12 characters.
```



## Testing

The project uses `pytest` for automated testing. The test suite covers password strength analysis, recommendations, common-password detection, dataset loading, boundary conditions, and edge cases.

To run the tests:

```bash
python -m pytest
```

The current test suite includes:

- Tests for WEAK, MEDIUM, and STRONG password analysis.
- Common-password detection using the external password dataset.
- Validation of the common-password dataset loader.
- Boundary-value tests around the 12-character minimum length requirement, including 11, 12, and 13-character passwords.
- An empty-password edge case.
- A whitespace-only password edge case to verify that whitespace is not treated as a special character.



## Project Structure

```text
password-security-analyzer/
|-- main.py
|-- analyzer.py
|-- common_passwords.txt
|-- tests/
|   `-- test_analyzer.py
|-- requirements-dev.txt
|-- README.md
`-- .gitignore
```

### File Responsibilities

- `main.py` — Handles command-line interaction, hidden password input, and presentation of the analysis results.
- `analyzer.py` — Contains the core password analysis logic, scoring, strength classification, common-password checking, and recommendation generation.
- `common_passwords.txt` — Contains the common-password dataset used by the analyzer.
- `tests/test_analyzer.py` — Contains the automated `pytest` test suite.
- `requirements-dev.txt` — Defines development and testing dependencies.
- `README.md` — Provides project documentation, setup instructions, usage information, and security considerations.
- `.gitignore` — Prevents generated or local development files such as `.venv` and `__pycache__` from being tracked by Git.



## Common Password Dataset

This project uses a common-password wordlist from the SecLists project for common-password detection.

Dataset:
`xato-net-10-million-passwords-1000.txt`

Source:
SecLists — `Passwords/Common-Credentials/xato-net-10-million-passwords-1000.txt`

The dataset is loaded from `common_passwords.txt`. During loading, the application removes surrounding whitespace, converts entries to lowercase, and ignores empty entries before performing password comparisons.



## Security and Privacy

The analyzer is designed to process passwords locally and does not intentionally store or transmit the entered password.

- Password input is hidden from the terminal using Python's `getpass` module, reducing the risk of exposing the password to someone viewing the screen.
- Entered passwords are not written to a file or database by the application.
- Passwords are not sent to an external API or network service.
- The common-password comparison is performed locally using `common_passwords.txt`.
- The entered password temporarily exists in the application's memory while it is being analyzed.

`getpass` hides the password during input but does not encrypt the password in memory. For this reason, the project should be treated as an educational password-analysis tool rather than a production password-management or authentication system.



## Limitations

This project provides a rule-based assessment of password strength and is intended primarily for educational purposes. A STRONG result does not guarantee that a password is secure against every type of attack.

Current limitations include:

- The scoring system is based on five predefined criteria and does not calculate password entropy.
- Common-password detection uses exact matching after converting the password to lowercase.
- Modified versions of common passwords may not be detected. For example, a variation of a common password with additional characters may not match the dataset.
- The source common-password file contains 1,000 lines, with 999 usable entries after empty entries are removed during loading.
- The analyzer does not check passwords against known breached-password databases or online services.
- Password patterns, repeated characters, keyboard patterns, names, dates, and other predictable structures are not currently analyzed.
- The tool does not replace the password security controls required by a production authentication system.


## Future Improvements

Possible improvements for future versions include:

- Password entropy estimation for more detailed strength analysis.
- Detection of repeated characters and predictable password patterns.
- Improved detection of variations of common passwords.
- Privacy-preserving breached-password checking.
- Support for structured output formats such as JSON.
- A web-based interface or API for integrating the analyzer with other applications.
- Expansion of the automated test suite as new features are introduced.
