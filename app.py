import streamlit as st
from huggingface_hub import InferenceClient
from groq import Groq
import requests, base64, asyncio, io, json
import edge_tts
from PIL import Image
import time
import urllib.parse
import random
from duckduckgo_search import DDGS 
from supabase import create_client, Client # අලුතින් එක් කළා
import datetime

# -----------------------
# 1. Page Config & Identity
# -----------------------
st.set_page_config(page_title="Alpha AI | Created by Hasith", layout="wide", page_icon="⚡")

# --- GOOGLE VERIFICATION TAG ---
st.markdown('<meta name="google-site-verification" content="W6jIGzCkkez2SpjygP6z0dJfinBNALmw2Hv-MkJvFB0" />', unsafe_allow_html=True)

# -----------------------
# 2. Database & API Setup
# -----------------------
# Supabase Setup
SUPABASE_URL = st.secrets.get("SUPABASE_URL")
SUPABASE_KEY = st.secrets.get("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
HF_TOKEN = st.secrets.get("HF_TOKEN")
POLLINATIONS_KEY = st.secrets.get("POLLINATIONS_API_KEY", "sk_Z0oEnm05szbphnbZ9ClRCukKV2HyDMH5")
OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY")

groq_client = Groq(api_key=GROQ_API_KEY)
hf_client = InferenceClient(token=HF_TOKEN)

# -----------------------
# 3. Session State Init
# -----------------------
if "messages" not in st.session_state: st.session_state.messages=[]
if "logged_in" not in st.session_state: st.session_state.logged_in=False
if "user_full_name" not in st.session_state: st.session_state.user_full_name=None

# -----------------------
# 4. Custom UI Styling
# -----------------------
st.markdown("""
<style>  
    .premium-banner { width:100%; padding:15px; background: linear-gradient(90deg, #FFD700, #FF8C00); color:#000; border-radius:15px; text-align:center; font-weight:bold; margin-bottom:20px; font-size: 22px; box-shadow: 0px 4px 15px rgba(0,0,0,0.3); }  
    .stChatMessage { border-radius: 15px; }  
    div.stButton > button { background-color: #1e1e1e; color: #FFD700; border-radius: 12px; width: 100%; height: 45px; font-weight: bold; border: 1px solid #FFD700; transition: 0.3s; }  
    div.stButton > button:hover { background-color: #FFD700; color: #000; }  
    .lab-box { border: 1px solid #333; padding: 20px; border-radius: 15px; background: #0e1117; margin-bottom: 20px; }  
    .limit-box { padding:10px; border-radius:10px; background:#262730; border:1px solid #FFD700; text-align:center; margin-bottom:10px; }
</style>  """, unsafe_allow_html=True)

# -----------------------
# 5. Helper Functions (Database Logic)
# -----------------------
def check_user_limit(username):
    today = str(datetime.date.today())
    try:
        res = supabase.table("user_usage").select("*").eq("username", username).execute()
        if not res.data:
            supabase.table("user_usage").insert({"username": username, "last_date": today, "image_count": 0, "is_premium": False}).execute()
            return True, 0, False
        
        user = res.data[0]
        is_premium = user.get('is_premium', False)
        if is_premium: return True, 0, True
        
        if user['last_date'] != today:
            supabase.table("user_usage").update({"last_date": today, "image_count": 0}).eq("username", username).execute()
            return True, 0, False
        
        return (user['image_count'] < 5), user['image_count'], False
    except: return True, 0, False # Error එකක් ආවොත් allow කරනවා

def update_usage(username, current_count):
    try:
        supabase.table("user_usage").update({"image_count": current_count + 1}).eq("username", username).execute()
    except: pass

async def speak_alpha(text):
    try:
        comm = edge_tts.Communicate(text, "en-US-SteffanNeural")
        audio = b""
        async for chunk in comm.stream():
            if chunk["type"]=="audio": audio+=chunk["data"]
        if audio:
            b64 = base64.b64encode(audio).decode()
            st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{b64}">', unsafe_allow_html=True)
    except: pass

def web_search_tool(query):
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=3)]
            if results:
                context = "\n".join([f"Source: {r['title']} - {r['body']}" for r in results])
                return context
    except: return ""
    return ""

def generate_video_robust(prompt):
    models = ["guoyww/AnimateDiff", "cerspense/zeroscope_v2_576w"]
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    for model_id in models:
        try:
            API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
            response = requests.post(API_URL, headers=headers, json={"inputs": prompt}, timeout=60)
            if response.status_code == 200: return response.content
        except: continue
    return None

# -----------------------
# 6. Login System
# -----------------------
if not st.session_state.logged_in:
    st.markdown('<div class="premium-banner">ALPHA CORE SYSTEM ACCESS</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#FFD700; font-weight:bold;">Developed by Hasith</p>', unsafe_allow_html=True)
    name = st.text_input("Operator Name")
    password = st.text_input("Master Key", type="password")
    if st.button("Initialize Alpha"):
        if password == "Hasith12378":
            st.session_state.user_full_name = name or "Hasith"
            st.session_state.logged_in = True
            st.rerun()
        else: st.error("Access Denied: Invalid Master Key")
    st.stop()

# -----------------------
# 7. Sidebar Control
# -----------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluent/100/000000/artificial-intelligence.png", width=70)
    st.title("Alpha Control")
    st.markdown(f"Operator: **{st.session_state.user_full_name}**")
    
    # Check Limit for Sidebar Info
    can_gen, count, is_vip = check_user_limit(st.session_state.user_full_name)
    status_text = "💎 PREMIUM (Unlimited)" if is_vip else f"📊 Daily Photos: {count}/5"
    st.markdown(f'<div class="limit-box">{status_text}</div>', unsafe_allow_html=True)
    
    if not is_vip:
        st.subheader("Upgrade to Premium")
        pay_html = f"""
        <form method="post" action="https://sandbox.payhere.lk/pay/checkout">   
            <input type="hidden" name="merchant_id" value="1211149">
            <input type="hidden" name="return_url" value="https://alpha-ai.streamlit.app">
            <input type="hidden" name="cancel_url" value="https://alpha-ai.streamlit.app">
            <input type="hidden" name="notify_url" value="https://your-api.com/notify">  
            <input type="hidden" name="order_id" value="UPGRADE_{st.session_state.user_full_name}">
            <input type="hidden" name="items" value="Alpha Premium">
            <input type="hidden" name="currency" value="LKR">
            <input type="hidden" name="amount" value="500.00">  
            <input type="hidden" name="first_name" value="{st.session_state.user_full_name}">
            <input type="hidden" name="last_name" value="Operator">
            <input type="hidden" name="email" value="user@example.com">
            <input type="hidden" name="phone" value="0771234567">
            <input type="hidden" name="address" value="Sri Lanka">
            <input type="hidden" name="city" value="Bandarawela">
            <input type="hidden" name="country" value="Sri Lanka">
            <input type="submit" value="BUY PREMIUM - RS.500" style="background:#FFD700; color:black; border:none; padding:10px; border-radius:10px; font-weight:bold; width:100%; cursor:pointer;">
        </form>
        """
        st.components.v1.html(pay_html, height=50)

    st.divider()
    mode = st.radio("Intelligence Level", ["Normal", "Pro", "Ultra"])
    web_search_on = st.checkbox("Web Search", value=False)
    voice_on = st.checkbox("Voice Output", value=True)
    if st.button("Log Out"):
        st.session_state.logged_in = False
        st.rerun()

st.markdown(f'<div class="premium-banner">⚡ ALPHA AI ULTIMATE | Created by Hasith</div>', unsafe_allow_html=True)

# -----------------------
# 8. AI Multimodal Labs
# -----------------------
tab_img, tab_vid = st.tabs(["🖼 Image Generation Lab", "🎬 Cinema Lab"])

with tab_img:
    with st.container():
        st.markdown('<div class="lab-box">', unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])
        img_p = col1.text_input("Describe image:", key="img_prompt")
        img_model = st.selectbox("Model:", ["flux", "turbo", "zimage"], key="img_model_select")  
        
        if col2.button("Generate Photo"):  
            if img_p:  
                can_gen, count, is_vip = check_user_limit(st.session_state.user_full_name)
                if can_gen:
                    with st.spinner("Alpha is painting... 🖌️"):  
                        try:  
                            seed = random.randint(1, 1000000)  
                            url = f"https://gen.pollinations.ai/image/{urllib.parse.quote(img_p)}?width=1024&height=1024&seed={seed}&model={img_model}&nologo=true"  
                            response = requests.get(url, timeout=60)  
                            if response.status_code == 200:  
                                st.image(response.content, use_container_width=True)  
                                st.download_button("Download 📥", response.content, f"alpha_{seed}.png")
                                if not is_vip: update_usage(st.session_state.user_full_name, count)
                                st.rerun()
                        except Exception as e: st.error(f"Error: {e}")  
                else:
                    st.error("🚫 Daily limit reached (5/5). Upgrade to Premium for Unlimited Access!")
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# 9. Hybrid Intelligence Chat (Logic remains same)
# -----------------------
st.write("### 💬 Heartfelt Conversation")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])

user_input = st.chat_input("State your command, Master...")

if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    with st.chat_message("user"): st.markdown(user_input)
    with st.chat_message("assistant"):
        # ... (ඔයාගේ chat logic එක මෙතනට දාන්න) ...
        st.write("Alpha is thinking...") 
        # (කෝඩ් එක දිග වැඩි නිසා කෙටි කළා, ඔයාගේ පරණ chat කෝඩ් එක මෙතනට දාන්න)

st.markdown("---")
st.caption("Alpha AI Project | Bandarawela Central College | Created by Hasith")
