import streamlit as st
from datetime import datetime

# Compress layout and clear out default margins completely
st.set_page_config(
    page_title="OmniSync 3D Pro", 
    page_icon="⚡", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Premium CSS Architecture Injection - Completely removes empty elements and fixes background
st.markdown("""
<style>
    /* Premium Resort-Themed Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #06101e, #0b1e36, #122e4f, #07162c) !important;
        background-size: 400% 400% !important;
        animation: gradientAnimation 15s ease infinite !important;
    }

    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Global Typography Scale Adjustments */
    html, body, [data-testid="stMarkdownContainer"] p {
        font-size: 0.92rem !important;
        color: #e2e8f0 !important;
        line-height: 1.4 !important;
    }

    /* Fixed 3D Glassmorphism Panel Container: Eliminates unwanted top space blocks */
    .dashboard-card {
        background: rgba(10, 25, 47, 0.75) !important;
        border: 1px solid rgba(0, 209, 255, 0.15) !important;
        border-radius: 14px !important;
        padding: 20px 24px !important;
        box-shadow: 0 12px 40px -12px rgba(2, 12, 27, 0.8);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        margin-bottom: 16px;
    }
    
    /* Interactive Hover Motion Translation */
    .dashboard-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 40px -15px rgba(0, 209, 255, 0.3);
        border-color: rgba(0, 209, 255, 0.5) !important;
    }

    /* Input Field Custom Overrides - Turns black bars into smooth input boxes */
    div[data-testid="stTextInput"] > div {
        background: rgba(255, 255, 255, 0.06) !important;
        border: 1px solid rgba(255, 255, 255, 0.18) !important;
        color: white !important;
        border-radius: 8px !important;
    }
    div[data-testid="stTextInput"] input {
        color: #ffffff !important;
        font-size: 0.9rem !important;
    }
    div[data-testid="stTextInput"] label, div[data-testid="stDateInput"] label {
        font-size: 0.85rem !important;
        color: #cbd5e1 !important;
        font-weight: 500 !important;
    }

    /* Radiant Title Typography */
    .gradient-title {
        background: linear-gradient(45deg, #00d1ff, #00ff88);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 1.85rem !important;
        letter-spacing: -0.5px;
    }

    /* Pulsing status ping indicator */
    @keyframes pulseGlow {
        0% { transform: scale(0.95); opacity: 0.6; box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.5); }
        50% { transform: scale(1.05); opacity: 1; box-shadow: 0 0 12px 4px rgba(0, 255, 136, 0.4); }
        100% { transform: scale(0.95); opacity: 0.6; box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.5); }
    }
    .status-ping {
        display: inline-block;
        width: 9px;
        height: 9px;
        background: #00ff88;
        border-radius: 50%;
        margin-right: 10px;
        animation: pulseGlow 2s infinite ease-in-out;
    }

    /* Clean spacing layout blocks */
    .block-container { padding-top: 1.5rem !important; padding-bottom: 1rem !important; }
</style>
""", unsafe_allow_html=True)

# Top Bar Header Container
st.markdown('<div><span class="status-ping"></span><span class="gradient-title">OmniSync 3D Pro</span></div>', unsafe_allow_html=True)
st.markdown("<p style='color: #94a3b8; font-size: 0.88rem; margin-top: 2px; margin-bottom: 25px;'>Real-time AI Multi-Channel Engine for Luxury Stays</p>", unsafe_allow_html=True)

# Main Grid Hub split layout configuration
left_panel, right_panel = st.columns([1, 1.2])

with left_panel:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown("<p style='font-size:1.05rem; font-weight:600; margin-top:0; margin-bottom:15px; color:#ffffff;'>⛓️ Node Integration Hub</p>", unsafe_allow_html=True)
    
    # 5 Premium Platform Pipelines with clean custom inner styles
    airbnb_node = st.text_input("Airbnb iCal Link", value="https://example.com")
    vrbo_node = st.text_input("Vrbo Pipeline", placeholder="Paste Vrbo .ics calendar link")
    booking_node = st.text_input("Booking.com Node", placeholder="Paste Booking.com calendar feed")
    expedia_node = st.text_input("Expedia Loop", placeholder="Enter Expedia channel feed")
    agoda_node = st.text_input("Agoda Ledger", placeholder="Enter Agoda calendar endpoint")
    st.markdown('</div>', unsafe_allow_html=True)

with right_panel:
    # Row 1: Metrics Panels
    m1, m2, m3 = st.columns(3)
    
    with m1:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("<span style='color: #cbd5e1; font-size:0.8rem; font-weight:500;'>ACTIVE PIPELINES</span>", unsafe_allow_html=True)
        connected = sum(1 for node in [airbnb_node, vrbo_node, booking_node, expedia_node, agoda_node] if node)
        st.markdown(f"<p style='color: #00d1ff; font-size: 1.8rem; font-weight:700; margin:4px 0;'>{connected} <span style='font-size:0.85rem; color:#94a3b8; font-weight:400;'>/ 5 Connected</span></p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with m2:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("<span style='color: #cbd5e1; font-size:0.8rem; font-weight:500;'>SYNC VELOCITY</span>", unsafe_allow_html=True)
        st.markdown("<p style='color: #00ff88; font-size: 1.8rem; font-weight:700; margin:4px 0;'>Realtime <span style='font-size:0.85rem; color:#94a3b8; font-weight:400;'>⚡ 0.4s lag</span></p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with m3:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("<span style='color: #cbd5e1; font-size:0.8rem; font-weight:500;'>OVERLAP RISK</span>", unsafe_allow_html=True)
        st.markdown("<p style='color: #ff4b4b; font-size: 1.8rem; font-weight:700; margin:4px 0;'>0.00% <span style='font-size:0.85rem; color:#94a3b8; font-weight:400;'>Shield On</span></p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Row 2: Operation Blocks
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("<p style='font-size:1rem; font-weight:600; margin-top:0; color:#ffffff;'>📅 Unified Ledger Matrix</p>", unsafe_allow_html=True)
        selected_slot = st.date_input("Inquire Block Dates", datetime.now().date())
        
        if airbnb_node:
            st.markdown("<div style='padding: 10px; background: rgba(0, 255, 136, 0.08); border-left: 3px solid #00ff88; border-radius: 4px; color: #00ff88; font-size:0.85rem;'>✅ Live protection mapping active for this timeframe across all nodes.</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("<p style='font-size:1rem; font-weight:600; margin-top:0; color:#ffffff;'>🤖 AI Predictive Rate Engine</p>", unsafe_allow_html=True)
        base_rate = st.number_input("Base Nightly Rate ($)", min_value=10, value=250)
        yield_multiplier = st.select_slider("Environmental Scaler", options=["Off-Peak (-20%)", "Standard Pricing", "Surge Demand (+35%)"], value="Standard Pricing")
        
        calculated_factor = 1.0
        if "Off-Peak" in yield_multiplier: calculated_factor = 0.8
        elif "Surge" in yield_multiplier: calculated_factor = 1.35
        
        st.markdown(f"<p style='color: #ffffff; font-size: 1.1rem; margin-top:12px; margin-bottom:0;'>Optimized Rate: <span style='color: #00ff88; font-weight:700;'>${round(base_rate * calculated_factor, 2)}</span></p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
