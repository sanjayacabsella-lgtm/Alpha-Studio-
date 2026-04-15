from huggingface_hub import InferenceClient
from groq import Groq
import requests, base64, asyncio, io, json
import edge_tts
from gtts import gTTS
from PIL import Image
import time
import urllib.parse
import random
from duckduckgo_search import DDGS 
from supabase import create_client, Client
import datetime
import streamlit as st
import cv2
import mediapipe as mp
from streamlit_agraph import agraph, Node, Edge, Config

# -----------------------
# 1. Page Config & Identity
# -----------------------
st.set_page_config(page_title="Alpha AI | Created by Hasith", layout="wide", page_icon="⚡")

# Google Verification
st.markdown('<meta name="google-site-verification" content="W6jIGzCkkez2SpjygP6z0dJfinBNALmw2Hv-MkJvFB0" />', unsafe_allow_html=True)

# -----------------------
# 2. API & Database Setup
# -----------------------
SUPABASE_URL = st.secrets.get("SUPABASE_URL")
SUPABASE_KEY = st.secrets.get("SUPABASE_KEY")
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
HF_TOKEN = st.secrets.get("HF_TOKEN")
CLOUDFLARE_ACCOUNT_ID = st.secrets.get("CLOUDFLARE_ACCOUNT_ID")
CLOUDFLARE_API_TOKEN = st.secrets.get("CLOUDFLARE_API_TOKEN")

if SUPABASE_URL and SUPABASE_KEY:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
else:
    st.error("Supabase credentials are missing.")
    st.stop()

if GROQ_API_KEY:
    groq_client = Groq(api_key=GROQ_API_KEY)
else:
    st.error("Groq API key is missing.")
    st.stop()

hf_client = InferenceClient(token=HF_TOKEN)

# -----------------------
# 3. Session State Init
# -----------------------
if "messages" not in st.session_state: st.session_state.messages=[]
if "logged_in" not in st.session_state: st.session_state.logged_in=False
if "user_full_name" not in st.session_state: st.session_state.user_full_name=None
if "generated_image" not in st.session_state: st.session_state.generated_image = None
if "generated_audio" not in st.session_state: st.session_state.generated_audio = None

# -----------------------
# 4. Custom UI Styling (Original Gold Styling)
# -----------------------
st.markdown("""
<style>  
    .premium-banner { width:100%; padding:15px; background: linear-gradient(90deg, #FFD700, #FF8C00); color:#000; border-radius:15px; text-align:center; font-weight:bold; margin-bottom:20px; font-size: 22px; box-shadow: 0px 4px 15px rgba(0,0,0,0.3); }  
    .stChatMessage { border-radius: 15px; }  
    div.stButton > button { background-color: #1e1e1e; color: #FFD700; border-radius: 12px; width: 100%; height: 45px; font-weight: bold; border: 1px solid #FFD700; transition: 0.3s; }  
    div.stButton > button:hover { background-color: #FFD700; color: #000; }  
    .lab-box { border: 1px solid #333; padding: 20px; border-radius: 15px; background: #0e1117; margin-bottom: 20px; }  
    .limit-box { padding:10px; border-radius:10px; background:#262730; border:1px solid #FFD700; text-align:center; margin-bottom:10px; font-weight:bold; }
</style>  """, unsafe_allow_html=True)

# -----------------------
# 5. Helper Functions
# -----------------------
def check_user_access(username, req_type="image"):
    today = str(datetime.date.today())
    limit = 5 if req_type == "image" else 6
    try:
        res = supabase.table("user_usage").select("*").eq("username", username).execute()
        if not res.data:
            supabase.table("user_usage").insert({"username": username, "last_date": today, "image_count": 0, "voice_count": 0, "is_premium": False}).execute()
            return True, 0, False
        user = res.data[0]
        is_vip = user.get('is_premium', False)
        if is_vip: return True, 0, True
        if user['last_date'] != today:
            supabase.table("user_usage").update({"last_date": today, "image_count": 0, "voice_count": 0}).eq("username", username).execute()
            return True, 0, False
        current_count = user.get('image_count', 0) if req_type == "image" else user.get('voice_count', 0)
        return (current_count < limit), current_count, False
    except: return True, 0, False

def update_usage(username, current_count, req_type="image"):
    try:
        field = "image_count" if req_type == "image" else "voice_count"
        supabase.table("user_usage").update({field: current_count + 1}).eq("username", username).execute()
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
            if results: return "\n".join([f"Source: {r['title']} - {r['body']}" for r in results])
    except: return ""
    return ""

def generate_video_robust(prompt):
    models = ["guoyww/AnimateDiff", "cerspense/zeroscope_v2_576w"]
    headers = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}
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
    name = st.text_input("Operator Name")
    password = st.text_input("Master Key", type="password")
    if st.button("Initialize Alpha"):
        if password == "Hasith12378":
            st.session_state.user_full_name = name or "Hasith"
            st.session_state.logged_in = True
            st.rerun()
        else: st.error("Access Denied")
    st.stop()

# -----------------------
# 7. Sidebar & Payment
# -----------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluent/100/000000/artificial-intelligence.png", width=70)
    st.title("Alpha Control")
    can_gen_img, img_count, is_vip = check_user_access(st.session_state.user_full_name, "image")
    can_gen_voice, voice_count, _ = check_user_access(st.session_state.user_full_name, "voice")
    
    if is_vip:
        st.markdown('<div class="limit-box">💎 PREMIUM OPERATOR</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="limit-box">🖼 Photos: {img_count}/5</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="limit-box">🎙️ Voices: {voice_count}/6</div>', unsafe_allow_html=True)
    
    if not is_vip:
        pay_html = f"""
        <form method="post" action="https://sandbox.payhere.lk/pay/checkout">   
            <input type="hidden" name="merchant_id" value="1211149">
            <input type="hidden" name="return_url" value="https://alpha-ai.streamlit.app">
            <input type="hidden" name="cancel_url" value="https://alpha-ai.streamlit.app">
            <input type="hidden" name="notify_url" value="https://your-api.com/notify">  
            <input type="hidden" name="order_id" value="PREMIUM_{st.session_state.user_full_name}">
            <input type="hidden" name="items" value="Alpha Premium Upgrade">
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

    mode = st.radio("Intelligence Level", ["Normal", "Pro", "Ultra"])
    web_search_on = st.checkbox("Web Search", value=False)
    voice_on = st.checkbox("Voice Output", value=True)
    if st.button("Log Out"):
        st.session_state.logged_in = False
        st.rerun()

st.markdown(f'<div class="premium-banner">⚡ ALPHA AI ULTIMATE | Created by Hasith</div>', unsafe_allow_html=True)

# -----------------------
# 8. AI Multimodal Labs (Original Labs + New Super Features)
# -----------------------
tab_img, tab_vid, tab_voice, tab_evo, tab_gest, tab_map = st.tabs([
    "🖼 Image Lab", "🎬 Cinema Lab", "🎙️ Voice Studio", "🧬 DNA Evolution", "🖐️ Gestures", "🧠 Neural Map"
])

with tab_img:
    st.markdown('<div class="lab-box">', unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])
    img_p = col1.text_input("Describe your vision:", key="cloud_img_prompt")
    art_style = col2.selectbox("Art Style:", ["Cartoon Style", "Comic Book", "Anime Style", "Ultra Realistic"])
    style_config = {
        "Cartoon Style": {"model": "@cf/lykon/dreamshaper-8-lcm", "prefix": "3d render, pixar style, cartoon, "},
        "Comic Book": {"model": "@cf/lykon/dreamshaper-8-lcm", "prefix": "comic book style, bold lines, illustration, "},
        "Anime Style": {"model": "@cf/lykon/dreamshaper-8-lcm", "prefix": "anime style, studio ghibli, 2d, "},
        "Ultra Realistic": {"model": "@cf/bytedance/stable-diffusion-xl-lightning", "prefix": "photorealistic, 8k, realistic, highly detailed, "}
    }
    image_display = st.empty()
    if st.button("Generate Masterpiece 🖌️"):  
        if img_p:  
            can_gen, current_count, is_premium = check_user_access(st.session_state.user_full_name, "image")
            if can_gen:
                with st.spinner(f"Alpha is crafting your {art_style}..."):  
                    try:
                        cfg = style_config[art_style]
                        API_URL = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/{cfg['model']}"
                        headers = {"Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}"}
                        payload = {"prompt": cfg['prefix'] + img_p, "negative_prompt": "blurry, low quality, distorted, bad anatomy"}
                        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
                        if response.status_code == 200:
                            img_data = response.content
                            st.session_state.generated_image = {"data": img_data, "caption": f"Alpha Gen: {art_style}"}
                            if not is_premium: update_usage(st.session_state.user_full_name, current_count, "image")
                        else: st.error(f"Cloudflare Error: {response.status_code}")
                    except Exception as e: st.error(f"Process Error: {e}")
            else: st.error("🚫 Daily free limit (5/5) reached! Upgrade to Premium.")
    
    if st.session_state.generated_image:
        with image_display.container():
            st.image(st.session_state.generated_image["data"], use_container_width=True, caption=st.session_state.generated_image["caption"])
            st.download_button("Download Image 📥", st.session_state.generated_image["data"], "alpha_gen.png", mime="image/png")
    st.markdown('</div>', unsafe_allow_html=True)

with tab_vid:
    st.markdown('<div class="lab-box">', unsafe_allow_html=True)
    v_col1, v_col2 = st.columns([3, 1])
    vid_p = v_col1.text_input("Describe video scene:", key="vid_prompt")
    if v_col2.button("Generate Video"):
        if vid_p:
            with st.spinner("Alpha is directing... 🎬"):
                vid_data = generate_video_robust(vid_p)
                if vid_data: st.video(vid_data)
                else: st.error("Cinema Lab is currently busy.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab_voice:
    st.markdown('<div class="lab-box">', unsafe_allow_html=True)
    st.subheader("🎙️ Alpha Voice Studio")
    v_text = st.text_area("කථා කිරීමට අවශ්‍ය දේ මෙහි ලියන්න:", height=100)
    # (Original Voice Studio Logic preserved)
    lang_options = {"Sinhala (සිංහල)": "si", "English": "en", "Hindi": "hi", "Tamil": "ta"}
    selected_lang = st.selectbox("Select Language:", list(lang_options.keys()))
    if st.button("Speak Now 🔊"):
        if v_text:
            can_v, v_current, is_p = check_user_access(st.session_state.user_full_name, "voice")
            if can_v:
                with st.spinner("Alpha is preparing voice..."):
                    tts = gTTS(text=v_text, lang=lang_options[selected_lang])
                    fp = io.BytesIO()
                    tts.write_to_fp(fp)
                    st.session_state.generated_audio = fp.getvalue()
                    if not is_p: update_usage(st.session_state.user_full_name, v_current, "voice")
    if st.session_state.generated_audio: st.audio(st.session_state.generated_audio)
    st.markdown('</div>', unsafe_allow_html=True)

# --- NEW FEATURE: DNA EVOLUTION (Protected by hasith78) ---
with tab_evo:
    st.markdown('<div class="lab-box">', unsafe_allow_html=True)
    st.header("🧬 DNA Evolution Engine (Pro)")
    evo_pass = st.text_input("Creator Key", type="password", key="dna_key")
    if evo_pass == "hasith78":
        evo_req = st.text_area("වෙනස් විය යුතු ආකාරය පවසන්න:")
        if st.button("Execute DNA Evolution ⚡"):
            with st.spinner("Pro Reasoning Model විකාශනය ආරම්භ කරයි..."):
                current_code = open(__file__, "r").read()
                completion = groq_client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[{"role": "user", "content": f"Rewrite this entire code to add: {evo_req}. Return only python code:\n{current_code}"}],
                    reasoning_effort="pro"
                )
                with open(__file__, "w", encoding="utf-8") as f: f.write(completion.choices[0].message.content)
                st.success("DNA Updated! Refreshing...")
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- NEW FEATURE: GESTURE CONTROL ---
with tab_gest:
    st.markdown('<div class="lab-box">', unsafe_allow_html=True)
    st.header("🖐️ Gesture Hub")
    cam_run = st.checkbox("Open Sensor Feed")
    if cam_run:
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands()
        cap = cv2.VideoCapture(0)
        st_frame = st.empty()
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret: break
            frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
            if hands.process(frame).multi_hand_landmarks: st.info("Hand Active")
            st_frame.image(frame)
            if not cam_run: break
        cap.release()
    st.markdown('</div>', unsafe_allow_html=True)

# --- NEW FEATURE: NEURAL MAP ---
with tab_map:
    st.markdown('<div class="lab-box">', unsafe_allow_html=True)
    st.header("🧠 Knowledge Graph")
    nodes = [Node(id="Alpha", label="Alpha Core", size=25, color="#FFD700"), Node(id="Hasith", label="Creator", size=20)]
    agraph(nodes=nodes, edges=[Edge(source="Hasith", target="Alpha")], config=Config(width=700, height=400))
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# 9. Hybrid Chat
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
            sys_msg = f"Your name is Alpha AI. Developed by Hasith from Bandarawela Central College. Context: {search_context}"
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

st.markdown("---")
st.caption("Alpha AI Project | Bandarawela Central College | Created by Hasith")
