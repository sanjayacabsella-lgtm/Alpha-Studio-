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

# -----------------------
# 3. Session State Init
# -----------------------
if "messages" not in st.session_state: st.session_state.messages=[]
if "logged_in" not in st.session_state: st.session_state.logged_in=False
if "user_full_name" not in st.session_state: st.session_state.user_full_name=None

# -----------------------
# 4. Helper Functions (DNA Evolution with Pro Model)
# -----------------------
def dna_evolution_engine(user_req):
    """Pro Model එක භාවිතයෙන් DNA Evolution සිදු කරන ශ්‍රිතය"""
    current_code = open(__file__, "r").read()
    
    # ඔබ ඉල්ලූ විශේෂිත Pro Reasoning Model එක
    completion = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": f"Rewrite this entire Streamlit app code to include this feature: {user_req}. Return only the raw python code. No explanations:\n{current_code}"
            }
        ],
        temperature=1,
        max_completion_tokens=8192,
        top_p=1,
        reasoning_effort="pro", # Pro reasoning enabled
        stream=False 
    )
    return completion.choices[0].message.content

# -----------------------
# 5. UI & Logic
# -----------------------
if not st.session_state.logged_in:
    st.markdown('<h1 style="text-align:center;">⚡ ALPHA AI SYSTEM ACCESS</h1>', unsafe_allow_html=True)
    name = st.text_input("Operator Name")
    password = st.text_input("Master Key", type="password")
    if st.button("Initialize"):
        if password == "Hasith12378":
            st.session_state.user_full_name = name or "Hasith"
            st.session_state.logged_in = True
            st.rerun()
        else: st.error("Access Denied")
    st.stop()

tabs = st.tabs(["💬 Chat", "🧬 Evolution", "🖐️ Gestures", "🧠 Neural Map"])

# --- FEATURE: DNA EVOLUTION (With Creator Password Protection) ---
with tabs[1]:
    st.header("🧬 DNA Evolution Engine (Pro Mode)")
    st.info("මෙම පද්ධතිය වෙනස් කළ හැක්කේ නිර්මාණකරුට (Hasith) පමණි.")
    
    creator_key = st.text_input("Creator Authorization Key", type="password", key="evo_key")
    
    if creator_key == "hasith78":
        evo_input = st.text_area("Alpha හට ඇතුළත් විය යුතු නව පද්ධති වෙනස්කම් පවසන්න:")
        if st.button("Execute DNA Evolution ⚡"):
            if evo_input:
                with st.spinner("Pro Reasoning Model එක මගින් පද්ධතිය විකාශනය කරමින් පවතී..."):
                    try:
                        new_code = dna_evolution_engine(evo_input)
                        with open(__file__, "w", encoding="utf-8") as f:
                            f.write(new_code)
                        st.success("Evolution සාර්ථකයි! පද්ධතිය නැවත ආරම්භ වේ...")
                        time.sleep(2)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Evolution Error: {e}")
    else:
        if creator_key:
            st.error("වැරදි Authorization Key එකක්. ඔබට මෙම පද්ධතිය වෙනස් කළ නොහැක.")

# (අනෙකුත් Tabs - Chat, Gestures, Neural Map පවතින විදියටම ඇතුළත් වේ)
with tabs[0]:
    st.write(f"Welcome, {st.session_state.user_full_name}")
    # Chat logic here...

with tabs[2]:
    st.write("Gesture Control පද්ධතිය මෙතැනින් ක්‍රියාත්මක කරන්න...")

with tabs[3]:
    st.write("Neural Map දත්ත මෙතැනින් පෙන්වයි...")

st.markdown("---")
st.caption("Alpha AI Project | Created by Hasith")
