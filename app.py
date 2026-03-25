import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AlphaStudio | Ultimate Cloud Gaming Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stApp {
        background: linear-gradient(160deg, #0e1117 0%, #1a1c24 100%);
    }
    h1 {
        color: #00f2fe;
        text-shadow: 2px 2px 10px #00f2fe66;
    }
    .game-card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #30363d;
        text-align: center;
        transition: 0.3s;
    }
    .game-card:hover {
        border-color: #58a6ff;
        transform: translateY(-5px);
    }
    </style>
    """, unsafe_allow_html=True)

# --- GAME DATA DICTIONARY ---
# You can easily add up to 100+ games here by following the same format
game_library = {
    "🔥 Action & Arcade": {
        "Super Mario Bros": "https://supermario-game.com/emulate",
        "Pac-Man Classic": "https://www.google.com/logos/2010/pacman10-i.html",
        "Sonic the Hedgehog": "https://www.retrogames.cc/embed/41727-sonic-the-hedgehog-usa-europe.html",
        "Street Fighter II": "https://www.retrogames.cc/embed/10042-street-fighter-ii-the-world-warrior-world-910522.html",
        "Tetris": "https://tetris.com/play-tetris",
        "Space Invaders": "https://freeinvaders.org/",
    },
    "🧩 Puzzle & Strategy": {
        "2048": "https://play2048.co/",
        "Chess.com": "https://www.chess.com/play/online",
        "Sudoku": "https://www.sudogrand.com/",
        "Minesweeper": "https://minesweeper-pro.com/",
    },
    "🏎️ Racing & Sports": {
        "Drift Hunters": "https://v6p9d9t4.ssl.hwcdn.net/html/1458210/index.html",
        "8 Ball Pool": "https://www.miniclip.com/games/8-ball-pool-multiplayer/en/web-embed/",
        "Moto X3M": "https://games.softgames.com/moto-x3m/",
    },
    "⭐ Community Favorites": {
        "Flappy Bird": "https://flappybird.io/",
        "Slither.io": "https://slither.io/",
        "Among Us (Clone)": "https://amogus.io/",
    }
}

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://img.icons8.com/neon/96/controller.png", width=80)
st.sidebar.title("ALPHA STUDIO")
st.sidebar.markdown("---")

category = st.sidebar.selectbox("📂 Select Category", list(game_library.keys()))
selected_game = st.sidebar.selectbox("🎮 Choose Your Game", list(game_library[category].keys()))

st.sidebar.markdown("---")
st.sidebar.write("👤 **Developer:** Hasith")
st.sidebar.write("🚀 **Powered by:** Alpha AI Cloud")
st.sidebar.success("v2.0 Pro Version Loaded")

# --- MAIN INTERFACE ---
col1, col2 = st.columns([3, 1])

with col1:
    st.title("🚀 AlphaStudio Gaming Hub")
    st.markdown(f"### Now Playing: **{selected_game}**")

with col2:
    st.info(f"**Category:** {category}")

# --- GAME PLAYER ENGINE ---
game_url = game_library[category][selected_game]

if game_url:
    # Creating a responsive container for the game
    st.markdown(
        f"""
        <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000; border-radius: 20px; border: 4px solid #1f2937;">
            <iframe 
                src="{game_url}" 
                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
                allowfullscreen>
            </iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.write("---")
    st.caption("Tip: Use Fullscreen mode for the best experience. Some games might take a few seconds to load from the cloud.")

# --- FOOTER ---
st.markdown("<br><center>AlphaStudio © 2026 | Unleash the Gamer in You</center>", unsafe_allow_html=True)
