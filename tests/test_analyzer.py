from analyzer import analyze_password, load_common_passwords

def test_medium_password():
    result = analyze_password("Hello123!")
    assert result["score"] == 4
    assert result["strength"] == "MEDIUM"


def test_weak_password():
    result = analyze_password("hello123")
    assert result["score"] == 2
    assert result["strength"] == "WEAK"
    assert "Add at least one uppercase letter." in result["recommendations"]
    assert "Add at least one special character." in result["recommendations"]
    assert "Add at least 12 characters." in result["recommendations"]

def test_strong_password():
    result = analyze_password("Cyberworld@2003")
    assert result["score"] == 5
    assert result["strength"] == "STRONG"
    assert result["recommendations"] == []

    assert result["Password_length"] == 15
    assert result["Contains uppercase"]
    assert result["Contains lowercase"]
    assert result["Contains Numbers"]
    assert result["Contains Special"]

def test_external_dataset_password():
    result = analyze_password("dragon")
    assert result["strength"] == "WEAK"
    assert "Avoid using common passwords." in result["recommendations"]

def test_load_common_passwords():
    passwords = load_common_passwords()
    assert len(passwords) == 999
    assert "dragon" in passwords
    assert "" not in passwords

def test_password_length_boundary():
    result = analyze_password("CyberDra@003")
    assert result["Password_length"] == 12
    assert result["score"] == 5
    assert "Add at least 12 characters." not in result["recommendations"]

def test_password_below_length_boundary():
    result = analyze_password("CyberDra@03")
    assert result["Password_length"] == 11
    assert "Add at least 12 characters." in result["recommendations"]

def test_password_above_length_boundary():
    result = analyze_password("CyberDra@0034")
    assert result["Password_length"] == 13
    assert "Add at least 12 characters." not in result["recommendations"]

def test_empty_password():
    result = analyze_password("")
    assert result["Password_length"] == 0
    assert result["score"] == 0
    assert result["strength"] == "WEAK"
    assert "Add at least 12 characters." in result["recommendations"]

def test_whitespace_only_password():
    result = analyze_password("            ")
    assert result["Password_length"] == 12
    assert not result["Contains Special"]
    assert result["score"] == 1
    assert result["strength"] == "WEAK"