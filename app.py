import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Alpha Studio | The Ultimate Creative Hub",
    page_icon="⚡",
    layout="wide"
)

# --- Background + CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');

    .stApp {
        background: linear-gradient(rgba(10, 10, 15, 0.85), rgba(10, 10, 15, 0.95)), 
                    url('https://images.unsplash.com/photo-1603575448366-153f093fd0fd?q=80&w=2070&auto=format&fit=crop');
        background-size: cover;
        background-attachment: fixed;
    }

    .main-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 85px;
        font-weight: 900;
        color: #ffffff;
        text-transform: uppercase;
        margin-top: 60px;
        margin-bottom: 10px;
        text-align: center;
        letter-spacing: 10px;
        animation: glowPulse 3s infinite alternate;
    }

    @keyframes glowPulse {
        0% { text-shadow: 0 0 10px #00ffff; }
        100% { text-shadow: 0 0 60px #00ffff; }
    }

    .sub-header {
        text-align: center;
        color: #00ffff;
        font-family: 'Orbitron', sans-serif;
        font-size: 20px;
        letter-spacing: 6px;
        margin-bottom: 70px;
    }

    .studio-card {
        backdrop-filter: blur(10px);
        background: rgba(255,255,255,0.05);
        border-radius: 20px;
        overflow: hidden;
        height: 480px;
        transition: 0.4s;
    }

    .studio-card:hover {
        transform: translateY(-15px);
        box-shadow: 0 0 40px rgba(0,255,255,0.4);
    }

    .card-img {
        width: 100%;
        height: 240px;
        object-fit: cover;
    }

    .card-body {
        padding: 25px;
        text-align: center;
    }

    .card-title {
        font-size: 26px;
        color: white;
        font-family: 'Orbitron';
    }

    .card-text {
        color: #ccc;
        margin: 15px 0;
    }

    .action-link {
        padding: 12px 30px;
        border: 2px solid #00ffff;
        color: #00ffff;
        text-decoration: none;
        border-radius: 8px;
    }

    .action-link:hover {
        background: #00ffff;
        color: black;
    }

    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<h1 class="main-header">ALPHA STUDIO</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Professional Video Production & Creative Hub</p>', unsafe_allow_html=True)

# Row 1
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('''
    <div class="studio-card">
        <img src="https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600" class="card-img">
        <div class="card-body">
            <div class="card-title">Alpha AI</div>
            <div class="card-text">AI assistant for creative workflows.</div>
            <a href="#" class="action-link">Open →</a>
        </div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="studio-card">
        <img src="https://images.unsplash.com/photo-1492724441997-5dc865305da7?w=600" class="card-img">
        <div class="card-body">
            <div class="card-title">Video Creation</div>
            <div class="card-text">Professional filmmaking tools.</div>
            <a href="#" class="action-link">Coming Soon</a>
        </div>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown('''
    <div class="studio-card">
        <img src="https://images.unsplash.com/photo-1517602302552-471fe67acf66?w=600" class="card-img">
        <div class="card-body">
            <div class="card-title">Movie Editing</div>
            <div class="card-text">Edit like a pro studio.</div>
            <a href="#" class="action-link">Coming Soon</a>
        </div>
    </div>
    ''', unsafe_allow_html=True)

# Row 2
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown('''
    <div class="studio-card">
        <img src="https://images.unsplash.com/photo-1542038784456-1ea8e935640e?w=600" class="card-img">
        <div class="card-body">
            <div class="card-title">Photo Lab</div>
            <div class="card-text">High-end retouching tools.</div>
            <a href="#" class="action-link">Coming Soon</a>
        </div>
    </div>
    ''', unsafe_allow_html=True)

with col5:
    st.markdown('''
    <div class="studio-card">
        <img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=600" class="card-img">
        <div class="card-body">
            <div class="card-title">Game Dev</div>
            <div class="card-text">Build immersive worlds.</div>
            <a href="#" class="action-link">Coming Soon</a>
        </div>
    </div>
    ''', unsafe_allow_html=True)

with col6:
    st.markdown('''
    <div class="studio-card">
        <img src="https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=600" class="card-img">
        <div class="card-body">
            <div class="card-title">Color Grading</div>
            <div class="card-text">Hollywood color tones.</div>
            <a href="#" class="action-link">Coming Soon</a>
        </div>
    </div>
    ''', unsafe_allow_html=True)
