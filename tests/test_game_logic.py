from logic_utils import check_guess, parse_guess


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


def test_parse_guess_valid_int():
    ok, value, err = parse_guess("42", 1, 100)
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_guess_float_string():
    ok, value, err = parse_guess("3.0", 1, 100)
    assert ok is True
    assert value == 3
    assert err is None


def test_parse_guess_empty_and_none():
    ok, value, err = parse_guess("", 1, 100)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

    ok2, value2, err2 = parse_guess(None, 1, 100)
    assert ok2 is False
    assert value2 is None
    assert err2 == "Enter a guess."


def test_parse_guess_invalid():
    ok, value, err = parse_guess("notanumber", 1, 100)
    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_parse_guess_out_of_range():
    # Test guess below range
    ok, value, err = parse_guess("0", 1, 100)
    assert ok is False
    assert value is None
    assert err == "Please enter a number between 1 and 100."

    # Test guess above range
    ok2, value2, err2 = parse_guess("101", 1, 100)
    assert ok2 is False
    assert value2 is None
    assert err2 == "Please enter a number between 1 and 100."

    # Test with different range (Easy difficulty: 1-20)
    ok3, value3, err3 = parse_guess("25", 1, 20)
    assert ok3 is False
    assert value3 is None
    assert err3 == "Please enter a number between 1 and 20."
