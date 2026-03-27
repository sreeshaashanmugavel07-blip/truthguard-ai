import streamlit as st
import os
from predict import predict
from astar import get_keywords
from minimax import stability_check
from factcheck import ai_fact_check 

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="TruthGuard", page_icon="🛡️", layout="centered")

# ==========================================
# 🎨 PROFESSIONAL CSS
# ==========================================
st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(-45deg, #a1c4fd, #c2e9fb, #ff9a9e, #fecfef, #a18cd1, #fbc2eb);
        background-size: 400% 400%;
        animation: aurora 15s ease infinite;
        background-attachment: fixed;
    }

    @keyframes aurora {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .glowing-header {
        font-size: 3.5rem !important;
        font-family: 'Copperplate', fantasy;
        font-weight: 900;
        text-align: center;
        margin: 0px;
        background: linear-gradient(135deg, #1e3a8a 0%, #f63b3b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .status-bar-fake {
        background: rgba(220, 38, 38, 0.9);
        color: white;
        padding: 12px 25px;
        border-radius: 12px;
        text-align: center;
        border-left: 8px solid #7f1d1d;
        font-weight: bold;
        margin-bottom: 20px;
    }

    .status-bar-real {
        background: rgba(22, 163, 74, 0.9);
        color: white;
        padding: 12px 25px;
        border-radius: 12px;
        text-align: center;
        border-left: 8px solid #14532d;
        font-weight: bold;
        margin-bottom: 20px;
    }

    .metric-box {
        background: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        height: 140px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 12px !important;
        background: #1e293b !important;
        color: white !important;
        font-weight: 700 !important;
        border: none !important;
    }

    #MainMenu, footer, header {visibility: hidden;}

    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# 🛡️ HEADER
# ==========================================
st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)

logo_path = "logo.png"
if os.path.exists(logo_path):
    st.image(logo_path, width=120)

st.markdown('<p class="glowing-header">Truth Guard</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#1e293b; font-weight:700;'>AI-POWERED VERIFICATION</p>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# INPUT
# ==========================================
text = st.text_area("", height=180, placeholder="Paste content here...")

# ==========================================
# BUTTON ACTION
# ==========================================
if st.button("EXECUTE SCAN"):

    if not text:
        st.warning("⚠️ Please provide text.")
        st.stop()

    with st.spinner("Analyzing... ⏳"):

        # -------------------------------
        # GET RESULTS
        # -------------------------------
        label, conf = predict(text)
        keywords = get_keywords(text)
        stability_score = stability_check(text, keywords)
        explanation = ai_fact_check(text)

        # -------------------------------
        # 🧠 HYBRID DECISION
        # -------------------------------
        ai_lower = explanation.lower()

        if "true" in ai_lower or "correct" in ai_lower:
            final_label = "REAL"
        elif "false" in ai_lower or "incorrect" in ai_lower:
            final_label = "FAKE"
        else:
            final_label = label

        # -------------------------------
        # RESULT DISPLAY
        # -------------------------------
        if final_label == "FAKE":
            st.markdown(
                f'<div class="status-bar-fake">❌ RESULT: FAKE ({conf}% Confidence)</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="status-bar-real">✅ RESULT: REAL ({conf}% Confidence)</div>',
                unsafe_allow_html=True
            )

        # -------------------------------
        # TECHNICAL ANALYSIS
        # -------------------------------
        st.markdown("### 🔍 Technical Analysis")
        col1, col2 = st.columns(2)

        # A* Keywords
        col1.markdown(f"""
            <div class="metric-box">
                <p style="margin:0; font-weight:bold; color:#1e293b;">🔑 A* Indicators</p>
                <p style="font-size:0.85rem; color:#334155;">{keywords}</p>
            </div>
        """, unsafe_allow_html=True)

        # Minimax Stability
        stability_pct = max(0, min(100, round((1 - stability_score) * 100, 1)))
        stab_color = "#16a34a" if stability_score < 0.2 else "#dc2626"

        col2.markdown(f"""
            <div class="metric-box">
                <p style="margin:0; font-weight:bold; color:#1e293b;">🎯 Minimax Stability</p>
                <h2 style="color: {stab_color}; margin: 5px 0;">{stability_pct}%</h2>
                <p style="font-size:0.7rem; font-weight:bold;">ROBUSTNESS</p>
            </div>
        """, unsafe_allow_html=True)

        # -------------------------------
        # AI EXPLANATION
        # -------------------------------
        st.markdown("<br>", unsafe_allow_html=True)

        if final_label == "FAKE":
            st.markdown(
                f'<div class="status-bar-fake">🤖 {explanation}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="status-bar-real">🤖 {explanation}</div>',
                unsafe_allow_html=True
            )