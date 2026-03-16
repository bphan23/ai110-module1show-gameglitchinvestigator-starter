from logic_utils import check_guess, parse_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# AI Collaboration note: Claude helped identify that parse_guess and get_range_for_difficulty
# needed tests too — the original test file only tested check_guess, leaving the input
# parsing and difficulty range logic untested.

def test_parse_guess_valid_number():
    # A normal numeric string should parse successfully
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_empty_string():
    # An empty input should return an error, not crash
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_guess_non_number():
    # A word should return a "not a number" error
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None

def test_range_easy():
    # Easy mode should return a narrower range than Normal
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100
