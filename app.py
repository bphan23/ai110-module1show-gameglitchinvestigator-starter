import random
import streamlit as st
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

# Hint messages shown in the UI for each outcome from check_guess
HINT_MESSAGES = {
    "Win": "🎉 Correct!",
    "Too High": "📉 Go LOWER!",
    "Too Low": "📈 Go HIGHER!",
}

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

# FIX: was initialized to 1, causing off-by-one — player lost one attempt on every game
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")

# FIX: was computed at the top of the page using the pre-increment attempts value, so it
# always showed the count from BEFORE the current submission. This caused "1 attempt left"
# to display on the same render where game-over fired, making it look like the game skipped
# from 1 to 0 automatically. Now using a placeholder that gets filled AFTER the submit
# block so the displayed count always matches the actual post-submission state.
attempts_placeholder = st.empty()

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

# FIX: was only resetting attempts and secret — status/score/history were left stale,
# causing the game-over check to fire immediately after pressing New Game
if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.status = "playing"
    st.session_state.score = 0
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    attempts_placeholder.info(
        f"Guess a number between {low} and {high}. "
        f"Attempts left: {max(0, attempt_limit - st.session_state.attempts)}"
    )
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error(
            f"Out of attempts! "
            f"The secret was {st.session_state.secret}. "
            f"Score: {st.session_state.score}"
        )
    st.stop()

if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        # FIX: reject guesses outside the valid range
        if guess_int < low or guess_int > high:
            st.error(f"Please enter a number between {low} and {high}.")
        else:
        # FIX: moved attempts increment here so invalid/out-of-range guesses don't consume
        # an attempt — previously, submitting 0 or a non-number would eat an attempt and
        # cause the game to end 2-3 guesses earlier than the displayed limit
            st.session_state.attempts += 1
            st.session_state.history.append(guess_int)

            secret = st.session_state.secret
            outcome = check_guess(guess_int, secret)
            message = HINT_MESSAGES[outcome]

            if show_hint:
                st.warning(message)

            st.session_state.score = update_score(
                current_score=st.session_state.score,
                outcome=outcome,
                attempt_number=st.session_state.attempts,
            )

            if outcome == "Win":
                st.balloons()
                st.session_state.status = "won"
                st.success(
                    f"You won! The secret was {st.session_state.secret}. "
                    f"Final score: {st.session_state.score}"
                )
            else:
                # FIX: rerun immediately on game over so the status check at the top fires
                # before the input/button are rendered — without this, the widgets stay on
                # screen and the player can submit a guess with 0 attempts left
                if st.session_state.attempts >= attempt_limit:
                    st.session_state.status = "lost"
                    st.rerun()

# Fill the placeholder here so every render — including the one where a guess was just
# submitted — shows the correct post-submission attempts count
attempts_placeholder.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {max(0, attempt_limit - st.session_state.attempts)}"
)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
