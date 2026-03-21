import streamlit as st

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Alpha Studio & Shop | Your Creative Hub",
    page_icon="🎬",
    layout="wide"
)

# --- 2. Styling (CSS) - Based on your NEW Design ---
# මෙහිදී මම ඔයා එවපු ඩිසයින් එකේ තියෙන ෆොන්ට්, වර්ණ (නැවී බ්ලූ සහ වයිට්)
# සහ Layout එකට සමානව CSS නිර්මාණය කළා.
st.markdown("""
    <style>
    /* Importing a Clean, Professional Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    body, .stApp {
        font-family: 'Poppins', sans-serif;
        background-color: #f4f6f9; /* Light grey/white background from */
        color: #1a202c;
    }

    /* Navy Blue Top Navigation Bar - Based on */
    .top-navbar {
        background-color: #0f172a; /* Navy Blue like */
        color: white;
        padding: 10px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1000;
        height: 70px;
    }
    .nav-links {
        display: flex;
        gap: 30px;
        list-style: none;
        margin: 0;
        padding: 0;
    }
    .nav-links li a {
        color: white;
        text-decoration: none;
        font-weight: 600;
        font-size: 15px;
    }

    /* Main Content Styling to accommodate navbar */
    .main-content {
        margin-top: 100px;
        padding: 20px;
    }

    /* Section Styling */
    .section-container {
        max-width: 1300px;
        margin: auto;
        padding-bottom: 50px;
    }
    .section-title {
        font-size: 36px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 10px;
    }
    .section-subtitle {
        color: #4a5568;
        font-size: 16px;
        margin-bottom: 40px;
    }

    /* Card Styling for Grid Layout */
    .studio-card {
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        overflow: hidden;
        transition: transform 0.3s;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .studio-card:hover {
        transform: translateY(-5px);
    }
    .card-img {
        width: 100%;
        height: 250px;
        object-fit: cover;
    }
    .card-body {
        padding: 20px;
        flex-grow: 1;
        text-align: center;
    }
    .card-title {
        font-size: 20px;
        font-weight: 600;
        color: #1a202c;
        margin-bottom: 10px;
    }
    .card-desc {
        color: #4a5568;
        font-size: 14px;
        margin-bottom: 20px;
    }

    /* Navy Blue Buttons from */
    .btn {
        background-color: #0f172a;
        color: white;
        padding: 10px 25px;
        border: none;
        border-radius: 6px;
        text-transform: uppercase;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s;
        display: inline-block;
        text-decoration: none;
    }
    .btn:hover {
        background-color: #1e293b;
    }
    
    /* Spacer utility */
    .spacer { height: 50px; }

    /* Fix to hide standard streamlit elements and keep it looking like a website */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. Navbar Section (Top Bar) ---
st.markdown(f'''
    <div class="top-navbar">
        <div style="font-size: 24px; font-weight: bold; text-transform: uppercase; color: #ffcc00;">ALPHA</div>
        <ul class="nav-links">
            <li><a href="#">Home</a></li>
            <li><a href="#">Studio</a></li>
            <li><a href="#">Shop</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
        <a href="https://alpha-ai-dibjvtzmag2vhb8a4knhdh.streamlit.app/" target="_blank" class="btn" style="padding: 8px 20px;">Open AI</a>
    </div>
''', unsafe_allow_html=True)

# --- Main Content Area ---
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.write('<div class="spacer"></div>', unsafe_allow_html=True)

# --- 4. Hero Section (Welcome) - From ---
st.markdown(f'''
    <div class="section-container" style="text-align: center;">
        <h1 class="section-title">Welcome to Alpha Studio & Shop</h1>
        <p class="section-subtitle">Your Premier Hub for High-Quality Video Production, Professional Editing Services, and Cinematic Gear.</p>
        <div style="gap: 15px; display: flex; justify-content: center;">
            <a href="#" class="btn">Explore Our Services</a>
            <a href="#" class="btn" style="background-color: transparent; color: #0f172a; border: 2px solid #0f172a;">Visit the Shop</a>
        </div>
    </div>
''', unsafe_allow_html=True)

st.write('<div class="spacer"></div>', unsafe_allow_html=True)
st.write("---")

# --- 5. Studio Services Grid Section ---
st.markdown(f'''
    <div class="section-container">
        <h2 class="section-title">Alpha Studio Services</h2>
        <p class="section-subtitle">From conception to final cut, we provide end-to-end solutions for all your production needs.</p>
        <br>
    </div>
''', unsafe_allow_html=True)

# Grid Layout with 3 Columns
col1, col2, col3 = st.columns(3)

# Service 1: Video Creation
with col1:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.pexels.com/photos/2510428/pexels-photo-2510428.jpeg?auto=format&fit=crop&w=600" class="card-img">
            <div class="card-body">
                <div class="card-title">Video Creation</div>
                <div class="card-desc">Professional cinematic production from short films to advertisements.</div>
                <a href="#" class="btn">Learn More →</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# Service 2: Movie Editing
with col2:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.pexels.com/photos/1117132/pexels-photo-1117132.jpeg?auto=format&fit=crop&w=600" class="card-img">
            <div class="card-body">
                <div class="card-title">Movie Editing</div>
                <div class="card-desc">High-end movie editing, post-production, and sound design.</div>
                <a href="#" class="active-btn">Learn More →</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# Service 3: Photo Editing & Grading
with col3:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.pexels.com/photos/15420387/pexels-photo-15420387.jpeg?auto=format&fit=crop&w=600" class="card-img">
            <div class="card-body">
                <div class="card-title">Photo Lab</div>
                <div class="card-desc">Advanced photo editing, creative manipulation, and color grading.</div>
                <a href="#" class="btn">Learn More →</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

st.write('<div class="spacer"></div>', unsafe_allow_html=True)
st.write("---")

# --- 6. Shop Categories Grid Section ---
st.markdown(f'''
    <div class="section-container">
        <h2 class="section-title">Explore Alpha Shop</h2>
        <p class="section-subtitle">Find premium camera gear, audio equipment, and accessories for professional creators.</p>
        <br>
    </div>
''', unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

# Category 1: Photo Grading Gear (Filters/Flares)
with col4:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.pexels.com/photos/279906/pexels-photo-279906.jpeg?auto=format&fit=crop&w=600" class="card-img">
            <div class="card-body">
                <div class="card-title">Optics & Filters</div>
                <div class="card-desc">Advanced camera filters, lens flares, and artistic tools for grading.</div>
                <a href="#" class="btn">Shop Now →</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# Category 2: General Shop Area
with col5:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.pexels.com/photos/306763/pexels-photo-306763.jpeg?auto=format&fit=crop&w=600" class="card-img">
            <div class="card-body">
                <div class="card-title">Camera Gear</div>
                <div class="card-desc">Top-tier cameras, lenses, and bodies for video production.</div>
                <a href="#" class="btn">Shop Now →</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# Category 3: Audio & Accessories
with col6:
    st.markdown('''
        <div class="studio-card">
            <img src="https://images.pexels.com/photos/218018/pexels-photo-218018.jpeg?auto=format&fit=crop&w=600" class="card-img">
            <div class="card-body">
                <div class="card-title">Accessories</div>
                <div class="card-desc">Audio recorders, microphones, tripods, and other essential gear.</div>
                <a href="#" class="btn">Shop Now →</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# Close main content area
st.markdown('</div>', unsafe_allow_html=True)
