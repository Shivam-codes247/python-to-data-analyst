import streamlit as st
import numpy as np

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Tic Tac Toe",
    page_icon="⭕",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------

st.markdown("""
<style>
```css
.block-container {
    padding-top: 1rem;
    padding-bottom: 0.5rem;
    max-width: 500px;
}

.title {
    text-align: center;
    font-size: 2rem;
    font-weight: bold;
    margin: 0;
}

.subtitle {
    text-align: center;
    color: #888;
    font-size: 0.85rem;
    margin-bottom: 8px;
}

.player {
    text-align: center;
    font-size: 1.2rem;
    font-weight: bold;
    margin: 8px 0;
}

div.stButton > button {
    height: 85px;
    font-size: 32px !important;
    font-weight: bold;
    border-radius: 12px;
}

.footer {
    text-align: center;
    color: #777;
    font-size: 0.75rem;
    margin-top: 8px;
}



</style>
""", unsafe_allow_html=True)


# -----------------------------
# Game Initialization
# -----------------------------

if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)

if "current" not in st.session_state:
    st.session_state.current = 1

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "winner" not in st.session_state:
    st.session_state.winner = None


# -----------------------------
# Winner Checking
# -----------------------------

def check_winner(b):

    # Rows
    row_sum = np.sum(b, axis=1)

    # Columns
    col_sum = np.sum(b, axis=0)

    # X wins
    if 3 in row_sum or 3 in col_sum:
        return "X"

    # O wins
    if -3 in row_sum or -3 in col_sum:
        return "O"

    # Main diagonal
    if np.trace(b) == 3:
        return "X"

    if np.trace(b) == -3:
        return "O"

    # Opposite diagonal
    if np.trace(np.fliplr(b)) == 3:
        return "X"

    if np.trace(np.fliplr(b)) == -3:
        return "O"

    # Draw
    if not np.any(b == 0):
        return "DRAW"

    return None


# -----------------------------
# Make Move
# -----------------------------

def make_move(row, col):

    board = st.session_state.board

    # Don't allow moves after game ends
    if st.session_state.game_over:
        return

    # Don't allow occupied cells
    if board[row, col] != 0:
        st.warning("That cell is already taken!")
        return

    # Place player's move
    board[row, col] = st.session_state.current

    # Check result
    result = check_winner(board)

    if result is not None:

        st.session_state.game_over = True
        st.session_state.winner = result

    else:

        # Switch player
        st.session_state.current *= -1


# -----------------------------
# Reset Game
# -----------------------------

def reset_game():

    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.game_over = False
    st.session_state.winner = None


# -----------------------------
# UI
# -----------------------------

st.markdown(
    '<div class="title">⭕ TIC TAC TOE ❌</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Tic-Tac-Toe</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Game Status
# -----------------------------

if st.session_state.game_over:

    if st.session_state.winner == "DRAW":

        st.warning("🤝 It's a Draw!")

    else:

        st.success(
            f"🎉 Player {st.session_state.winner} Wins!"
        )

else:

    if st.session_state.current == 1:
        current_player = "X"
    else:
        current_player = "O"

    st.markdown(
        f'<div class="player">Player {current_player}\'s Turn</div>',
        unsafe_allow_html=True
    )


# -----------------------------
# Board and controls
# -----------------------------

board = st.session_state.board

symbols = {
    0: " ",
    1: "❌",
    -1: "⭕"
}

left_col, right_col = st.columns([1.2, 3.5])

with left_col:
    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

    if st.button(
        "🔄 Restart Game",
        use_container_width=True
    ):
        reset_game()
        st.rerun()

with right_col:
    for row in range(3):
        cols = st.columns(3)

        for col in range(3):
            value = board[row, col]

            if value == 0:
                button_text = " "
            else:
                button_text = symbols[value]

            with cols[col]:
                if st.button(
                    button_text,
                    key=f"{row}-{col}",
                    use_container_width=True
                ):
                    make_move(row, col)
                    st.rerun()


# -----------------------------
# Footer
# -----------------------------

st.markdown(
    """
    <div style="text-align:center; color:#777; margin-top:20px;">
        Built with Python • NumPy • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)

