# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game loaded fine and looked normal: a title, a difficulty picker in the sidebar, a guess box, and Submit, New Game, and Show hint controls. The problems showed up once I started playing on the 1 to 100 range. When I guessed 1, the hint said "Go LOWER" instead of "Go HIGHER", and when I guessed 100, it said "Go HIGHER" instead of "Go LOWER", so the hints were backwards. The game also accepted 1000 even though it was outside the range. No hint appeared at all, even with "Show hint" ticked.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|1      | Go higher         | Go lower        | No errors|
|100    | Go higher         | Go lower        | No errors |
|Start a new game|attempts left:8 | attempts left:7|no error |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

--- I used the AI chat in VS Code to find and fix the bugs adn Claude to review my changes and help me fix my pytest setup.

Correct suggestion: After I described the backwards hints, the VS Code AI found the problem in check_guess: the "Too High" result returned "Go HIGHER!" and the "Too Low" result returned "Go LOWER!". It swapped the two messages. I reviewed the diff before clicking Keep, then verified it by running pytest (test_hints_point_the_right_way passes) and by playing again, where guessing 1 now says "Go HIGHER".

Suggestion I did not accept as written: The VS Code AI added a GuessResult class and a _coerce_number helper to logic_utils.py. GuessResult was a tuple that also compared equal to a string, only so the starter tests (assert result == "Win") would pass even though check_guess returns two values. It worked, but when I reviewed it with Claude, we agreed it was over-engineered and harder to read for a small game. I removed it and changed the three starter tests to unpack the result instead (outcome, message = check_guess(50, 50)). I verified my simpler version by running python -m pytest, and all tests passed.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---I counted a bug as fixed only when it passed both a pytest test and a manual check in the game. For example, test_hints_point_the_right_way checks that a guess of 60 against a secret of 50 says "Go LOWER" and a guess of 40 says "Go HIGHER", and it passes. I also played the game again and guessed 1 and 100 to confirm the hints and the range error. At first pytest failed with ModuleNotFoundError: No module named 'logic_utils', which taught me that I had to run pytest from the project folder and add a conftest.py so the tests could find the module. AI helped me write tests for each fix and edge cases like range boundaries, negative numbers, decimals, and empty input.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- Every time you click a button or type in a Streamlit app, the whole Python script runs again from top to bottom. That means normal variables reset on every click, so a secret number stored in a normal variable would change each time. st.session_state is like a notebook that survives reruns, so the game stores the secret, attempts, score, and history there. Code like if "secret" not in st.session_state: makes sure the secret is only picked once, not on every click.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to keep is reviewing every diff before clicking Keep, instead of accepting all of the AI's changes at once. Next time, I would ask the AI to fix one bug at a time with a short, specific prompt, because when it made bigger changes it also added code I didn't need. This project showed me that AI-generated code can look finished and still have hidden logic bugs, so I need to test it and read it myself before trusting it.

Another important lesson I learned is that documentation is crucial. I didn't write anything down while I was playing the game because I convinced myself I would remember everything, but I didn't remember all of it. I also learned I should always check README.md, there are important details such as opening the Google Chrome Developer tools, which the assignment instruction omit for whatever reason, but if I checked first, it would have saved a lot of time.