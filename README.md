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

**Game Purpose:**
A number guessing game where the player tries to guess a secret number within a limited number of attempts. The game gives hints after each guess to guide the player toward the answer, and tracks a score based on how quickly they win.

**Bugs Found:**
- The hint messages were swapped — "Too High" said "Go Higher" and "Too Low" said "Go Lower," so every hint pointed the player in the wrong direction.
- Out-of-range inputs (like 0 or 101) were accepted without any error message.
- The attempt counter was initialized to 1 instead of 0, so players silently lost one attempt every game.
- Invalid guesses (empty input, non-numbers, out-of-range) incremented the attempt counter, causing the game to end earlier than the displayed limit suggested.
- Pressing "New Game" only reset the attempt count and secret — `status`, `score`, and `history` were left over from the previous game, causing the game-over screen to appear immediately.
- When the last attempt was used, the display still showed "1 attempt left" while the game-over message appeared, making it look like the game ended one guess too early.
- With 0 attempts left, the input and submit button remained visible, allowing extra guesses after the game should have ended.

**Fixes Applied:**
- Swapped the hint messages in `check_guess` so "Too High" correctly says "Go Lower" and "Too Low" says "Go Higher."
- Added range validation in the submit block to reject guesses outside `[low, high]`.
- Initialized `st.session_state.attempts` to `0` instead of `1`.
- Moved the `attempts += 1` increment to only fire for valid, in-range guesses.
- Updated the New Game handler to also reset `status`, `score`, and `history`.
- Replaced the static "Attempts left" display with an `st.empty()` placeholder filled after the submit block, so the count always reflects the post-submission state.
- Added `st.rerun()` after setting `status = "lost"` so the status check fires before the input widgets render, preventing guesses after game over.
- Moved all four core functions (`get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`) from `app.py` into `logic_utils.py` and added 5 new pytest tests covering input parsing and difficulty ranges.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
