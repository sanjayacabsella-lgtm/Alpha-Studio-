import streamlit as st

# --- 1. Page Configuration (Keep it hidden for a cleaner look) ---
st.set_page_config(
    page_title="Alpha Studio | The Art of Creation",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. Advanced CSS for a Professional & Creative Look ---
st.markdown("""
    <style>
    /* Import Professional Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Orbitron:wght@700;900&display=swap');

    /* Global Styles */
    .stApp {
        background-color: #050a14; /* Dark futuristic background */
        color: #e0e0e0;
        font-family: 'Poppins', sans-serif;
    }

    /* --- Full Screen Video Background --- */
    .video-background {
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
        opacity: 0.2; /* Subtle visibility */
        object-fit: cover;
    }

    /* --- Main Title Styling (Orbitron + Glow) --- */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 70px;
        font-weight: 900;
        text-align: center;
        color: #ffffff;
        letter-spacing: 10px;
        text-transform: uppercase;
        margin-top: 60px;
        margin-bottom: 5px;
        text-shadow: 0 0 20px rgba(0, 255, 255, 0.7);
    }
    
    .subtitle {
        text-align: center;
        color: #00ffff;
        font-size: 20px;
        letter-spacing: 3px;
        margin-bottom: 70px;
        font-weight: 300;
    }

    /* --- Glassmorphism Card Styling --- */
    .card-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 40px;
        padding: 20px;
        max-width: 1300px;
        margin: auto;
    }

    .studio-card {
        background: rgba(255, 255, 255, 0.03); /* Translucent background */
        backdrop-filter: blur(10px); /* Frosted glass effect */
        border: 1px solid rgba(0, 255, 255, 0.2); /* Subtle cyan border */
        border-radius: 20px;
        padding: 0;
        text-align: center;
        transition: all 0.4s ease-in-out;
        overflow: hidden;
        height: 480px;
        display: flex;
        flex-direction: column;
    }

    .studio-card:hover {
        transform: translateY(-15px); /* Lift up on hover */
        border-color: rgba(0, 255, 255, 0.8);
        box-shadow: 0 0 40px rgba(0, 255, 255, 0.5); /* Neon glow on hover */
        background: rgba(255, 255, 255, 0.06);
    }

    /* Professional Images for Cards */
    .card-image {
        width: 100%;
        height: 250px;
        object-fit: cover;
        border-top-left-radius: 20px;
        border-top-right-radius: 20px;
        filter: brightness(0.8); /* Slightly darker for better text contrast */
    }

    .card-content {
        padding: 25px;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .card-title {
        font-size: 24px;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 10px;
        text-transform: uppercase;
    }

    .card-description {
        color: #b0b0b0;
        font-size: 15px;
        line-height: 1.6;
        margin-bottom: 25px;
    }

    /* --- Neon Enter Button --- */
    .enter-btn {
        display: inline-block;
        padding: 12px 30px;
        background-color: transparent;
        border: 2px solid #00ffff;
        color: #00ffff;
        text-transform: uppercase;
        font-weight: bold;
        text-decoration: none;
        border-radius: 8px;
        transition: all 0.3s;
        font-size: 14px;
    }

    .enter-btn:hover {
        background-color: #00ffff;
        color: #050a14;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.8);
    }

    /* Hide standard Streamlit header and footer for a pure website feel */
    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. Full Screen Video Background Implementation ---
# I am using a subtle abstract tech video from Pixabay. 
# You can change this URL to any direct video link.
st.markdown("""
    <video autoplay loop muted class="video-background">
        <source src="https://cdn.pixabay.com/video/2018/12/12/20124-307567018_tiny.mp4" type="video/mp4">
    </video>
    """, unsafe_allow_html=True)

# --- 4. Main Content (The Website) ---

st.markdown('<h1 class="main-title">ALPHA STUDIO</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Where Creativity Meets Technology • Sri Lanka</p>', unsafe_allow_html=True)

# Using Columns to create the Grid
col1, col2, col3 = st.columns(3)

# Service 1: ALPHA AI (Integrated with your existing link)
with col1:
    st.markdown(f'''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1620712943543-bcc4628c6757?q=80&w=600&auto=format&fit=crop" class="card-image">
            <div class="card-content">
                <div class="card-title">Alpha AI</div>
                <div class="card-description">Chat with our advanced AI assistant, built by Hasith. It can code, write, and think.</div>
                <a href="https://alpha-ai-dibjvtzmag2vhb8a4knhdh.streamlit.app/" target="_blank" class="enter-btn">Chat with Alpha →</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# Service 2: Video Creation
with col2:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1536240478700-b869070f9279?q=80&w=600&auto=format&fit=crop" class="card-image">
            <div class="card-content">
                <div class="card-title">Video Creation</div>
                <div class="card-description">Cinematic video production, short films, documentaries, and professional storytelling.</div>
                <a href="#" class="enter-btn">Explore →</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# Service 3: Movie Editing & Sound
with col3:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=600&auto=format&fit=crop" class="card-image">
            <div class="card-content">
                <div class="card-title">Movie Editing</div>
                <div class="card-description">High-end movie editing, post-production, sound engineering, and visual effects.</div>
                <a href="#" class="enter-btn">Explore →</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

st.write("---")

col4, col5, col6 = st.columns(3)

# Service 4: Photo Lab (Retouching & Grading)
with col4:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1542038784456-1ea8e935640e?q=80&w=600&auto=format&fit=crop" class="card-image">
            <div class="card-content">
                <div class="card-title">Photo Lab</div>
                <div class="card-description">Advanced digital retouching, artistic photo manipulation, and detailed color grading.</div>
                <a href="#" class="enter-btn">Explore →</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# Service 5: Game Development
with col5:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=600&auto=format&fit=crop" class="card-image">
            <div class="card-content">
                <div class="card-title">Game Dev</div>
                <div class="card-desc">Building immersive 3D worlds, interactive gaming experiences, and next-gen mechanics.</div>
                <a href="#" class="enter-btn">Explore →</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# Service 6: Cinematic Grading (Special Feature)
with col6:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.unsplash.com/photo-1535223289827-42f1e9919769?q=80&w=600&auto=format&fit=crop" class="card-image">
            <div class="card-content">
                <div class="card-title">Color Grading</div>
                <div class="card-description">Cinematic color correction and artistic photo grading for high-end photography.</div>
                <a href="#" class="enter-btn">Explore →</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)
