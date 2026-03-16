# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  The first time I ran it, I encountered many errors because my Python libraries didn’t match. Due to these errors, I wasn’t able to see or play the game at all.

- List at least two concrete bugs you noticed at the start
  (for example: "the hints were backwards").

  After playing the game, I immediately noticed that the hint message always says "Go Lower," even when I type 1 as my guess. Since the message says, "Guess a number between 1 and 100," I would assume we shouldn’t be able to enter 0, so that seems like a bug. I then tried entering 0 as my guess, and it still said "Go Lower," which is another bug. I also tested numbers greater than 100 and less than 1, and the same message appeared, indicating yet another bug. Another issue I found was that when I had 1 attempt left, the game indicated I was out of attempts, even though I still had one remaining clearly another bug.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Copilot, ChatGPT,and Claude on this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One example of a correct AI suggestion was to reject guesses outside the valid range. I verified this by reviewing the game logic to ensure it handled out-of-range inputs properly, and then I tested it myself to confirm it worked.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One example of an incorrect or misleading AI suggestion was when, after I reported all my bugs and fixed them, it indicated that everything was resolved. In reality, there was still one bug remaining, which I confirmed by testing the game again.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

To decide whether a bug was really fixed, I re-tested the exact input that originally triggered it. For the swapped hints, I entered a guess I knew was too low and checked that it now said "Go Higher" instead of "Go Lower." For the range bug, I typed 0 and 101 and confirmed the game rejected them with an error message. For the attempts bug, I played through a full game and verified the counter started at the correct number and that the "Out of attempts" message only appeared after I had genuinely used my last guess, not while the display still showed 1 remaining.

- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.

I ran a manual test by entering 1 as my guess when the secret was somewhere in the middle of the range. The game showed "Go Lower," which was the opposite of what it should say. This revealed that the hint messages in check_guess were swapped — the "Too High" branch was returning "Go HIGHER!" and the "Too Low" branch was returning "Go LOWER!" when they should have been reversed. I also tested entering 0 and numbers above 100, which showed the game accepted them without complaint, confirming there was no range validation at all.

- Did AI help you design or understand any tests? How?

Yes, I asked Claude to explain what tests already existed in the project and how to run them. It walked me through the three pytest tests in tests/test_game_logic.py and explained that they would all fail because logic_utils.py contains stub functions that raise NotImplementedError. That helped me understand the structure of the project: the tests are written to test logic_utils.py, not app.py directly, which means the intended next step is to refactor the working functions from app.py into logic_utils.py so the tests can actually run.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

- What is one thing you would do differently next time you work with AI on a coding task?

- In one or two sentences, describe how this project changed the way you think about AI generated code.
