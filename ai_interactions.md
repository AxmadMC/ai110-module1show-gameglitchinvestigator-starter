# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

--- After playing the game and noticing that the hints were backwards and that out-of-range guesses like 1000 were accepted, I asked the VS Code AI chat to find where the issue was and fix it. The task also included moving the game logic from app.py into logic_utils.py.

**What did the agent do?**

--- The agent edited several files at once. It implemented the functions in logic_utils.py, swapped the hint messages in check_guess, added range checks to parse_guess and check_guess, and added new tests to tests/test_game_logic.py. It also added a GuessResult class and a _coerce_number helper. VS Code showed each change as a diff with Keep and Undo buttons.

**What did you have to verify or fix manually?**

--- I reviewed each diff before clicking Keep.
--- pytest failed with ModuleNotFoundError: No module named 'logic_utils'. I learned I had to run it from the game folder with python -m pytest.
--- The refactor was not finished: app.py still had its own copies of all four functions and never imported logic_utils.py, so the tests were checking different code than the game was running. I removed the copies and added the import.
--- The two check_guess versions returned different things (three values in app.py, two in logic_utils.py), so I made app.py use the logic_utils.py version.
--- I removed GuessResult and _coerce_number because they were over-engineered for this game, and changed the starter tests to unpack (outcome, message) instead.
--- I played the game again to confirm the fixes.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
|Guesses exactly at the range limits (1 and 100) | "Lets now do the next steps, earning even the bonus"| test_parse_guess_accepts_range_boundaries| yes| Off-by-one mistakes are common, so the lowest and highest valid numbers must be accepted.|
|Guesses just outside the range (0 and 101) | same prompt|test_parse_guess_rejects_just_outside_range |yes |Confirms the range check uses the right comparison (< and >), so 0 and 101 are rejected. |
|Negative number (-5) |the same prompt | test_parse_guess_rejects_negative_number| yes| 	A player could type a minus sign; it should get the range error, not crash.|

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
