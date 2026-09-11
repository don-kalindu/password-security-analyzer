from analyzer import analyze_password

def test_medium_password():
    result = analyze_password("Hello123!")
    assert result["score"] == 4
    assert result["strength"] == "MEDIUM"


def test_weak_password():
    result = analyze_password("hello123")
    assert result["score"] == 2
    assert result["strength"] == "WEAK"

def test_strong_password():
    result = analyze_password("Cyberworld@2003")
    assert result["score"] == 5
    assert result["strength"] == "STRONG"

def test_common_password():
    result = analyze_password("Password123!")
    assert result["score"] == 5
    assert result["strength"] == "WEAK"