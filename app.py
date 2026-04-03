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
from supabase import create_client, Client
import datetime

# -----------------------
# 1. Page Config & Identity
# -----------------------
st.set_page_config(page_title="Alpha AI | Created by Hasith", layout="wide", page_icon="⚡")

# --- GOOGLE VERIFICATION TAG ---
st.markdown('<meta name="google-site-verification" content="W6jIGzCkkez2SpjygP6z0dJfinBNALmw2Hv-MkJvFB0" />', unsafe_allow_html=True)

# -----------------------
# 2. API & Database Setup
# -----------------------
# Streamlit Secrets වලින් දත්ත ලබා ගැනීම
SUPABASE_URL = st.secrets.get("SUPABASE_URL")
SUPABASE_KEY = st.secrets.get("SUPABASE_KEY")
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
HF_TOKEN = st.secrets.get("HF_TOKEN")
OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY")

# Clients Initialize කිරීම
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
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
    .limit-info { padding:10px; background:#262730; border-radius:10px; border:1px solid #FFD700; text-align:center; margin-bottom:15px; font-weight:bold; }
</style>  """, unsafe_allow_html=True)

# -----------------------
# 5. Helper Functions (Logic)
# -----------------------

def check_user_access(username):
    """දිනපතා සීමාව සහ Premium තත්ත්වය පරීක්ෂා කිරීම"""
    today = str(datetime.date.today())
    try:
        res = supabase.table("user_usage").select("*").eq("username", username).execute()
        if not res.data:
            # අලුත් යූසර් කෙනෙක් නම් ඇතුළත් කිරීම
            supabase.table("user_usage").insert({
                "username": username, "last_date": today, "image_count": 0, "is_premium": False
            }).execute()
            return True, 0, False
        
        user_data = res.data[0]
        is_vip = user_data.get('is_premium', False)
        
        if is_vip: return True, 0, True # Premium නම් සීමාවක් නැත
        
        if user_data['last_date'] != today:
            # අලුත් දවසක් නම් count එක reset කිරීම
            supabase.table("user_usage").update({"last_date": today, "image_count": 0}).eq("username", username).execute()
            return True, 0, False
        
        return (user_data['image_count'] < 5), user_data['image_count'], False
    except:
        return True, 0, False # Error එකක් ආවොත් allow කරනවා

def update_usage_count(username, current_count):
    """ෆොටෝ එකක් හැදූ පසු count එක වැඩි කිරීම"""
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
                return "\n".join([f"Source: {r['title']} - {r['body']}" for r in results])
    except: return ""
    return ""

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
# 7. Sidebar & Payment Control
# -----------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluent/100/000000/artificial-intelligence.png", width=70)
    st.title("Alpha Control")
    st.markdown(f"Operator: **{st.session_state.user_full_name}**")
    
    # දත්ත ගබඩාවෙන් තොරතුරු ලබා ගැනීම
    can_gen, img_count, is_premium = check_user_access(st.session_state.user_full_name)
    
    # සීමාව පෙන්වීම
    status_label = "💎 PREMIUM (Unlimited)" if is_premium else f"📊 Daily Photos: {img_count}/5"
    st.markdown(f'<div class="limit-info">{status_label}</div>', unsafe_allow_html=True)
    
    # Premium නොවේ නම් පේමන්ට් බටන් එක පෙන්වීම
    if not is_premium:
        st.subheader("Get Premium Upgrade")
        # PayHere Sandbox URL (පසුව Live URL එකට මාරු කරන්න)
        pay_html = f"""
        <form method="post" action="https://sandbox.payhere.lk/pay/checkout">   
            <input type="hidden" name="merchant_id" value="1211149"> 
            <input type="hidden" name="return_url" value="https://alpha-ai.streamlit.app">
            <input type="hidden" name="cancel_url" value="https://alpha-ai.streamlit.app">
            <input type="hidden" name="notify_url" value="https://your-api.com/notify">  
            <input type="hidden" name="order_id" value="PREMIUM_{st.session_state.user_full_name}">
            <input type="hidden" name="items" value="Alpha AI Premium">
            <input type="hidden" name="currency" value="LKR">
            <input type="hidden" name="amount" value="500.00">  
            <input type="hidden" name="first_name" value="{st.session_state.user_full_name}">
            <input type="hidden" name="last_name" value="User">
            <input type="hidden" name="email" value="user@example.com">
            <input type="hidden" name="phone" value="0771234567">
            <input type="hidden" name="address" value="Sri Lanka">
            <input type="hidden" name="city" value="Bandarawela">
            <input type="hidden" name="country" value="Sri Lanka">
            <input type="submit" value="UPGRADE TO PREMIUM - RS.500" 
                style="background:#FFD700; color:black; border:none; padding:10px; border-radius:10px; font-weight:bold; width:100%; cursor:pointer;">
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
    st.markdown('<div class="lab-box">', unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])
    img_p = col1.text_input("Describe image:", key="img_prompt")
    img_model = st.selectbox("Model:", ["flux", "turbo", "zimage"], key="img_model_select")  
    
    if col2.button("Generate Photo"):  
        if img_p:  
            # සීමාව පරීක්ෂා කිරීම
            can_gen, current_count, is_vip = check_user_access(st.session_state.user_full_name)
            
            if can_gen:
                with st.spinner("Alpha is painting... 🖌️"):  
                    try:  
                        seed = random.randint(1, 1000000)  
                        url = f"https://gen.pollinations.ai/image/{urllib.parse.quote(img_p)}?width=1024&height=1024&seed={seed}&model={img_model}&nologo=true"  
                        response = requests.get(url, timeout=60)  
                        if response.status_code == 200:  
                            st.image(response.content, caption=f"Created for {st.session_state.user_full_name}", use_container_width=True)  
                            st.download_button("Download 📥", response.content, f"alpha_{seed}.png")
                            # සාමාන්‍ය යූසර් කෙනෙක් නම් විතරක් count එක වැඩි කිරීම
                            if not is_vip:
                                update_usage_count(st.session_state.user_full_name, current_count)
                                st.rerun()
                    except Exception as e: st.error(f"Error: {e}")  
            else:
                st.error("🚫 Daily free limit (5/5) reached! Upgrade to Premium for unlimited photos.")
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# 9. Hybrid Intelligence Chat
# -----------------------
st.write("### 💬 Heartfelt Conversation")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])

user_input = st.chat_input("State your command, Master...")

if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    with st.chat_message("user"): st.markdown(user_input)
    
    with st.chat_message("assistant"):
        with st.spinner("Alpha is thinking..."):
            res_placeholder = st.empty()
            search_context = web_search_tool(user_input) if web_search_on else ""
            
            sys_msg = f"Your name is Alpha AI. Developed by Hasith from Bandarawela Central College. Search context: {search_context}"
            
            try:
                # Chat logic (Llama/DeepSeek) - කෙටියෙන්
                if mode == "Ultra":
                    # OpenRouter API call මෙතනට
                    full_res = "Alpha Ultra is ready to assist you!" 
                else:
                    # Groq API call
                    stream = groq_client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "system", "content": sys_msg}] + st.session_state.messages[-10:],
                        stream=True
                    )
                    full_res = ""
                    for chunk in stream:
                        if chunk.choices[0].delta.content:
                            full_res += chunk.choices[0].delta.content
                            res_placeholder.markdown(full_res + "▌")
                
                res_placeholder.markdown(full_res)
                if voice_on: asyncio.run(speak_alpha(full_res))
                st.session_state.messages.append({"role":"assistant","content":full_res})
            except Exception as e: st.error(f"Brain Error: {e}")

st.markdown("---")
st.caption("Alpha AI Project | Created by Hasith")
