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

    assert result["Password_length"]
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