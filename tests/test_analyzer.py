from analyzer import analyze_password

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

def test_common_password():
    result = analyze_password("Password123!")
    assert result["score"] == 5
    assert result["strength"] == "WEAK"
    assert "Avoid using common passwords." in result["recommendations"]