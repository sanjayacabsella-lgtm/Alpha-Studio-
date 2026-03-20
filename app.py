import streamlit as st

st.set_page_config(page_title="Alpha Studio", layout="wide")

# --- CSS ---
st.markdown("""
<style>

.stApp {
    background-color: #0b0f19;
}

/* NAVBAR */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 40px;
    background: #0f172a;
    border-radius: 10px;
    color: white;
}

.nav-links span {
    margin: 0 15px;
    color: #ccc;
    cursor: pointer;
}

/* HERO */
.hero {
    margin-top: 20px;
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.8)),
                url('https://images.unsplash.com/photo-1603575448366-153f093fd0fd?q=80&w=2070');
    background-size: cover;
    border-radius: 20px;
    padding: 80px;
    color: white;
}

.hero h1 {
    font-size: 50px;
    font-weight: bold;
}

.hero p {
    font-size: 18px;
    margin: 20px 0;
}

/* BUTTONS */
.btn {
    padding: 12px 25px;
    border-radius: 8px;
    text-decoration: none;
    margin-right: 10px;
    font-weight: bold;
}

.btn-orange {
    background: orange;
    color: white;
}

.btn-outline {
    border: 2px solid orange;
    color: orange;
}

/* SECTION */
.section {
    margin-top: 50px;
    color: white;
}

/* CARD */
.card {
    background: #111827;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-10px);
}

.card img {
    width: 100%;
    border-radius: 10px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown("""
<div class="navbar">
    <h2>ALPHA</h2>
    <div class="nav-links">
        <span>Home</span>
        <span>Films</span>
        <span>Services</span>
        <span>Shop</span>
        <span>About</span>
        <span>Contact</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
<div class="hero">
    <h1>Welcome to Alpha Studio & Shop</h1>
    <p>Your hub for professional video production and gear!</p>
    <a class="btn btn-orange">Explore Films</a>
    <a class="btn btn-outline">Visit Our Shop</a>
</div>
""", unsafe_allow_html=True)

# --- FEATURED ---
st.markdown('<div class="section"><h2>Featured Films & Videos</h2></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <img src="https://images.unsplash.com/photo-1492724441997-5dc865305da7">
        <p>Action Short</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <img src="https://images.unsplash.com/photo-1517602302552-471fe67acf66">
        <p>Music Video</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <img src="https://images.unsplash.com/photo-1485846234645-a62644f84728">
        <p>Drama Film</p>
    </div>
    """, unsafe_allow_html=True)

# --- SERVICES + SHOP ---
st.markdown('<div class="section"><h2>Professional Services & Shop</h2></div>', unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="card">
        <img src="https://images.unsplash.com/photo-1519183071298-a2962be96a9c">
        <p>Video Production</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card">
        <img src="https://images.unsplash.com/photo-1581091215367-59ab6b3d3f1c">
        <p>Editing & Post Production</p>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card">
        <img src="https://images.unsplash.com/photo-1516035069371-29a1b244cc32">
        <p>Camera Gear Shop</p>
    </div>
    """, unsafe_allow_html=True)
