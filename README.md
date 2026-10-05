# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Game Glitch Investigator is a Streamlit number guessing game. The player picks a difficulty (Easy 1–20, Normal 1–100, Hard 1–50), then tries to guess a secret number within a limited number of attempts. After each guess the game gives a hint ("Go HIGHER" or "Go LOWER") and updates the score. 
The starter code was written by an AI and contained bugs that I had to find, explain, and fix. 

[ ] The hints were backwards: guessing 1 said "Go LOWER" and guessing 1000 said "Go HIGHER".
Guesses outside the range were accepted (1000 was allowed when the range was 1–100).
The secret number was turned into text on every even attempt, which broke the high/low comparison.
Attempts started at 1 instead of 0, so the player lost an attempt before guessing.
The info box always said "between 1 and 100", no matter the difficulty.
New Game didn't reset the score, history, or win/lose status, and ignored the difficulty range.

[ ] Moved get_range_for_difficulty, parse_guess, check_guess, and update_score from app.py into logic_utils.py, and imported them in app.py.
Swapped the hint messages so "Too High" says "Go LOWER" and "Too Low" says "Go HIGHER".
Added a range check to parse_guess so out-of-range guesses show an error.
Removed the code that turned the secret into a string, and the string-comparison fallback in check_guess.
Started attempts at 0, showed the real range in the info box, and made New Game fully reset the game.
Made every wrong guess cost 5 points, and only count an attempt when the guess is valid.
Updated the starter tests to unpack (outcome, message) from check_guess, and added new tests for each fix.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The user opens the game on Normal difficulty. The sidebar shows "Range: 1 to 100" and "Attempts allowed: 8", and the info box says "Guess a number between 1 and 100. Attempts left: 8".
2.  The user opens the game on Normal difficulty. The sidebar shows "Range: 1 to 100" and "Attempts allowed: 8", and the info box says "Guess a number between 1 and 100. Attempts left: 8".
3.  The user enters 50. The secret is 37, so the game returns "Too High" and shows " Go LOWER!". The score drops to -5 and attempts left go to 7.
4.  RThe user enters 25. The game returns "Too Low" and shows " Go HIGHER!". The score drops to -10 and attempts left go to.
5. The user enters 37. The game shows "Correct!", balloons appear, and the message says "You won! The secret was 37. Final score: 50".
6. The user clicks New Game. A new secret is picked from 1–100, and the score, attempts, and history all reset.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
plugins: anyio-4.15.1
collected 15 items                                         

tests/test_game_logic.py::test_winning_guess PASSED  [  6%]
tests/test_game_logic.py::test_guess_too_high PASSED [ 13%]
tests/test_game_logic.py::test_guess_too_low PASSED  [ 20%]
tests/test_game_logic.py::test_hints_point_the_right_way PASSED [ 26%]
tests/test_game_logic.py::test_parse_guess_rejects_out_of_range_values PASSED [ 33%]
tests/test_game_logic.py::test_too_high_always_loses_pointsPASSED [ 40%]
tests/test_game_logic.py::test_parse_guess_accepts_range_boundaries PASSED [ 46%]
tests/test_game_logic.py::test_parse_guess_rejects_just_outside_range PASSED [ 53%]
tests/test_game_logic.py::test_parse_guess_rejects_negative_number PASSED [ 60%]
tests/test_game_logic.py::test_parse_guess_rejects_text PASSED [ 66%]
tests/test_game_logic.py::test_parse_guess_rejects_empty_input PASSED [ 73%]
tests/test_game_logic.py::test_parse_guess_decimal_is_rounded_down PASSED [ 80%]
tests/test_game_logic.py::test_parse_guess_allows_spaces_around_number PASSED [ 86%]
tests/test_game_logic.py::test_win_score_never_drops_below_10 PASSED [ 93%]
tests/test_game_logic.py::test_unknown_outcome_does_not_change_score PASSED [100%]

=================== 15 passed in 0.04s ====================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
