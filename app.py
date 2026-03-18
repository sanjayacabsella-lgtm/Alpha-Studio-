import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Alpha Studio | Creative Hub",
    page_icon="⚡",
    layout="wide"
)

# --- Custom Futuristic CSS ---
st.markdown("""
    <style>
    /* Main Background with Nebula Overlay */
    .stApp {
        background: linear-gradient(rgba(5, 10, 20, 0.8), rgba(5, 10, 20, 0.9)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop');
        background-size: cover;
        background-attachment: fixed;
    }

    /* Header Styling */
    .main-header {
        font-size: 60px;
        font-weight: 800;
        text-align: center;
        color: #ffffff;
        letter-spacing: 10px;
        text-transform: uppercase;
        margin-top: 30px;
        text-shadow: 0 0 20px rgba(0, 255, 255, 0.7);
    }
    
    .sub-header {
        text-align: center;
        color: #00ffff;
        font-size: 18px;
        letter-spacing: 3px;
        margin-bottom: 50px;
        opacity: 0.9;
    }

    /* Studio Card UI */
    .studio-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 255, 255, 0.3);
        border-radius: 20px;
        transition: 0.4s ease-in-out;
        overflow: hidden;
        height: 450px;
        display: flex;
        flex-direction: column;
        margin-bottom: 20px;
    }
    
    .studio-card:hover {
        transform: translateY(-15px);
        border-color: #00ffff;
        box-shadow: 0 0 40px rgba(0, 255, 255, 0.4);
        background: rgba(255, 255, 255, 0.08);
    }

    .card-img {
        width: 100%;
        height: 220px;
        object-fit: cover;
    }

    .card-body {
        padding: 25px;
        text-align: center;
    }

    .card-title {
        font-size: 24px;
        font-weight: bold;
        color: #ffffff;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .card-text {
        font-size: 14px;
        color: #bbbbbb;
        line-height: 1.5;
        margin-bottom: 20px;
    }

    /* Action Button */
    .action-link {
        display: inline-block;
        padding: 10px 25px;
        border: 2px solid #00ffff;
        color: #00ffff;
        text-decoration: none;
        font-weight: bold;
        border-radius: 5px;
        transition: 0.3s;
        text-transform: uppercase;
    }

    .action-link:hover {
        background: #00ffff;
        color: #050a14;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Branding Section ---
st.markdown('<h1 class="main-header">ALPHA STUDIO</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">ULTIMATE CREATIVE TOOLS • DESIGNED BY HASITH</p>', unsafe_allow_html=True)

# --- Studio Grid ---
row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    st.markdown(f'''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&auto=format&fit=crop" class="card-img">
            <div class="card-body">
                <div class="card-title">Alpha AI</div>
                <div class="card-text">Our flagship intelligent assistant for chat and instant image generation.</div>
                <a href="https://alpha-ai-dibjvtzmag2vhb8a4knhdh.streamlit.app/" target="_blank" class="action-link">Launch AI →</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

with row1_col2:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1536240478700-b869070f9279?w=600&auto=format&fit=crop" class="card-img">
            <div class="card-body">
                <div class="card-title">Video Creation</div>
                <div class="card-text">Professional cinematic production and creative video storytelling tools.</div>
                <a href="#" class="action-link">Coming Soon</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

with row1_col3:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1485846234645-a62644f84728?w=600&auto=format&fit=crop" class="card-img">
            <div class="card-body">
                <div class="card-title">Movie Editing</div>
                <div class="card-text">Advanced post-production, sound engineering, and color correction suite.</div>
                <a href="#" class="action-link">Coming Soon</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1542038784456-1ea8e935640e?w=600&auto=format&fit=crop" class="card-img">
            <div class="card-body">
                <div class="card-title">Photo Lab</div>
                <div class="card-text">Professional retouching and high-end photo manipulation tools.</div>
                <a href="#" class="action-link">Coming Soon</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

with row2_col2:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=600&auto=format&fit=crop" class="card-img">
            <div class="card-body">
                <div class="card-title">Game Dev</div>
                <div class="card-text">Designing immersive 3D worlds and interactive gaming experiences.</div>
                <a href="#" class="action-link">Coming Soon</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

with row2_col3:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1535223289827-42f1e9919769?w=600&auto=format&fit=crop" class="card-img">
            <div class="card-body">
                <div class="card-title">Photo Grading</div>
                <div class="card-text">Cinematic color grading and artistic filters for high-end photography.</div>
                <a href="#" class="action-link">Coming Soon</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)
