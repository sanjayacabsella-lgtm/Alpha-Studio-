import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Alpha Studio | The Ultimate Creative Hub",
    page_icon="⚡",
    layout="wide"
)

# --- Advanced Neon & Futuristic CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');

    .stApp {
        background: linear-gradient(rgba(5, 10, 20, 0.85), rgba(5, 10, 20, 0.95)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop');
        background-size: cover;
        background-attachment: fixed;
    }

    /* Animated Glow Title */
    .main-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 85px;
        font-weight: 900;
        text-align: center;
        color: #ffffff;
        letter-spacing: 18px;
        text-transform: uppercase;
        margin-top: 60px;
        animation: glowPulse 3s infinite alternate;
    }

    @keyframes glowPulse {
        0% {
            text-shadow: 0 0 10px #00ffff, 0 0 30px #00ffff;
        }
        100% {
            text-shadow: 0 0 20px #00ffff, 0 0 60px #00ffff, 0 0 120px #00ffff;
        }
    }

    .sub-header {
        text-align: center;
        color: #00ffff;
        font-family: 'Orbitron', sans-serif;
        font-size: 20px;
        letter-spacing: 6px;
        margin-bottom: 70px;
        text-transform: uppercase;
    }

    /* Glassmorphism Card */
    .studio-card {
        backdrop-filter: blur(12px);
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(0, 255, 255, 0.25);
        border-radius: 20px;
        transition: 0.5s;
        overflow: hidden;
        height: 480px;
        display: flex;
        flex-direction: column;
        margin-bottom: 30px;
        position: relative;
    }

    /* Neon Border Animation */
    .studio-card::before {
        content: "";
        position: absolute;
        inset: 0;
        border-radius: 20px;
        padding: 1px;
        background: linear-gradient(120deg, transparent, #00ffff, transparent);
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        opacity: 0;
        transition: 0.5s;
    }

    .studio-card:hover::before {
        opacity: 1;
    }

    .studio-card:hover {
        transform: translateY(-20px) scale(1.03);
        box-shadow: 0 0 60px rgba(0,255,255,0.5);
    }

    .card-img {
        width: 100%;
        height: 240px;
        object-fit: cover;
        filter: brightness(0.7);
        transition: 0.5s;
    }

    .studio-card:hover .card-img {
        transform: scale(1.08);
        filter: brightness(1);
    }

    .card-body {
        padding: 25px;
        text-align: center;
    }

    .card-title {
        font-size: 26px;
        font-weight: bold;
        color: #ffffff;
        text-transform: uppercase;
        margin-bottom: 12px;
        letter-spacing: 2px;
        font-family: 'Orbitron', sans-serif;
    }

    .card-text {
        font-size: 15px;
        color: #cccccc;
        line-height: 1.5;
        margin-bottom: 25px;
    }

    /* Neon Button */
    .action-link {
        display: inline-block;
        padding: 12px 35px;
        border: 2px solid #00ffff;
        color: #00ffff;
        text-decoration: none;
        font-weight: bold;
        border-radius: 8px;
        transition: 0.3s;
        text-transform: uppercase;
        font-family: 'Orbitron', sans-serif;
        font-size: 12px;
        position: relative;
        overflow: hidden;
    }

    .action-link::before {
        content: "";
        position: absolute;
        width: 0%;
        height: 100%;
        background: #00ffff;
        top: 0;
        left: 0;
        transition: 0.3s;
        z-index: -1;
    }

    .action-link:hover::before {
        width: 100%;
    }

    .action-link:hover {
        color: #050a14;
        box-shadow: 0 0 25px #00ffff;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #777;
        font-size: 14px;
        margin-top: 50px;
        padding-bottom: 30px;
        letter-spacing: 2px;
    }

    </style>
    """, unsafe_allow_html=True)

# --- Content ---
st.markdown('<h1 class="main-header">ALPHA STUDIO</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">The Collaborative Hub of Digital Excellence</p>', unsafe_allow_html=True)

# Row 1
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop" class="card-img">
            <div class="card-body">
                <div class="card-title">Alpha AI</div>
                <div class="card-text">Our flagship artificial intelligence for chat, logic, and creative generation.</div>
                <a href="https://alpha-ai-dibjvtzmag2vhb8a4knhdh.streamlit.app/" target="_blank" class="action-link">Open Alpha AI →</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1536240478700-b869070f9279?w=600&auto=format&fit=crop" class="card-img">
            <div class="card-body">
                <div class="card-title">Video Creation</div>
                <div class="card-text">Advanced tools for cinematic video production and professional storytelling.</div>
                <a href="#" class="action-link">Coming Soon</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1485846234645-a62644f84728?w=600&auto=format&fit=crop" class="card-img">
            <div class="card-body">
                <div class="card-title">Movie Editing</div>
                <div class="card-text">High-end movie post-production, sound engineering, and color correction.</div>
                <a href="#" class="action-link">Coming Soon</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# Row 2
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1542038784456-1ea8e935640e?w=600&auto=format&fit=crop" class="card-img">
            <div class="card-body">
                <div class="card-title">Photo Lab</div>
                <div class="card-text">Professional digital retouching and master photo manipulation services.</div>
                <a href="#" class="action-link">Coming Soon</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

with col5:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=600&auto=format&fit=crop" class="card-img">
            <div class="card-body">
                <div class="card-title">Game Dev</div>
                <div class="card-text">Designing immersive interactive worlds and next-gen gaming experiences.</div>
                <a href="#" class="action-link">Coming Soon</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

with col6:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1535223289827-42f1e9919769?w=600&auto=format&fit=crop" class="card-img">
            <div class="card-body">
                <div class="card-title">Color Grading</div>
                <div class="card-text">Cinematic color correction and artistic grading for master creators.</div>
                <a href="#" class="action-link">Coming Soon</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">ALPHA STUDIO • POWERED BY THE ALPHA TEAM</div>', unsafe_allow_html=True)
