from logic_utils import check_guess, parse_guess, update_score

# Starter tests. check_guess returns (outcome, message), so the tests
# unpack the tuple and check the outcome.

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# New tests for the bugs that were fixed.

def test_hints_point_the_right_way():
    # Bug: "Too High" told the player to go HIGHER
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_parse_guess_rejects_out_of_range_values():
    ok, guess, error = parse_guess("101", 1, 100)
    assert ok is False
    assert guess is None
    assert "between 1 and 100" in error.lower()

def test_too_high_always_loses_points():
    # Bug: "Too High" gave +5 points on even attempts
    assert update_score(50, "Too High", 1) == 45
    assert update_score(50, "Too High", 2) == 45

    # Challenge 1: Advanced edge-case tests.
 
def test_parse_guess_accepts_range_boundaries():
    # The lowest and highest numbers in the range should be allowed
    assert parse_guess("1", 1, 100) == (True, 1, None)
    assert parse_guess("100", 1, 100) == (True, 100, None)
 
def test_parse_guess_rejects_just_outside_range():
    ok, guess, error = parse_guess("0", 1, 100)
    assert ok is False
    ok, guess, error = parse_guess("101", 1, 100)
    assert ok is False
 
def test_parse_guess_rejects_negative_number():
    ok, guess, error = parse_guess("-5", 1, 100)
    assert ok is False
    assert "between 1 and 100" in error.lower()
 
def test_parse_guess_rejects_text():
    ok, guess, error = parse_guess("abc")
    assert ok is False
    assert guess is None
    assert error == "That is not a number."
 
def test_parse_guess_rejects_empty_input():
    ok, guess, error = parse_guess("")
    assert ok is False
    assert error == "Enter a guess."
 
def test_parse_guess_decimal_is_rounded_down():
    # "50.7" becomes 50
    assert parse_guess("50.7", 1, 100) == (True, 50, None)
 
def test_parse_guess_allows_spaces_around_number():
    assert parse_guess(" 42 ", 1, 100) == (True, 42, None)
 
def test_win_score_never_drops_below_10():
    # Winning after many attempts still gives at least 10 points
    assert update_score(0, "Win", 20) == 10
 
def test_unknown_outcome_does_not_change_score():
    assert update_score(30, "Something Else", 1) == 30
 