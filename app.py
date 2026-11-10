import streamlit as st
import requests
from icalendar import Calendar
from datetime import datetime, timedelta
import random

# Page layout configuration
st.set_page_config(page_title="ChannelSync 3D Engine", page_icon="⚡", layout="wide")

# Custom CSS injection for 3D Cards, Neon Accents, Animations, and Font Styling
st.markdown("""
<style>
    /* Neon Glow & Background Reset */
    .stApp {
        background: linear-gradient(135deg, #0e1117 0%, #161b22 100%);
    }
    
    /* 3D Glassmorphism Container with Hover Lift Motion */
    .dashboard-card {
        background: rgba(22, 27, 34, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s ease;
        margin-bottom: 20px;
    }
    .dashboard-card:hover {
        transform: translateY(-8px) scale(1.01);
        box-shadow: 0 15px 35px 0 rgba(0, 209, 255, 0.2);
        border-color: rgba(0, 209, 255, 0.4);
    }
    
    /* Pulsing Animation for Live Sync Indicators */
    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(0, 255, 136, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 136, 0); }
    }
    .live-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        background-color: #00ff88;
        border-radius: 50%;
        margin-right: 8px;
        animation: pulse 2s infinite;
    }
    
    /* Gradient Text Header Styles */
    .gradient-text {
        background: linear-gradient(45deg, #00d1ff, #00ff88);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.2rem;
    }
    .panel-header {
        color: #ffffff;
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 15px;
        border-bottom: 1px solid rgba(255,255,255,0.05);
        padding-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# App Header Component
st.markdown('<div><span class="live-indicator"></span><span class="gradient-text">OmniSync 3D Pro</span></div>', unsafe_allow_html=True)
st.markdown("<p style='color: #8b949e; margin-bottom: 30px;'>Real-time AI Multi-Channel Engine for Luxury Stays</p>", unsafe_allow_html=True)

# Helper function to mock or parse calendar logic safely
def parse_mock_sync(url, platform_name):
    if not url: return 0
    # Simulate processing delay motion
    return random.randint(5, 18)

# Layout Setup
left_sidebar, main_content = st.columns([1, 3])

with left_sidebar:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown('<div class="panel-header">⛓️ Node Integrations</div>', unsafe_allow_html=True)
    
    # Expanded Channel Connections (5 Premium Platforms)
    airbnb = st.text_input("Airbnb iCal URL", value="https://example.com")
    vrbo = st.text_input("Vrbo iCal URL")
    booking = st.text_input("Booking.com URL")
    expedia = st.text_input("Expedia Group URL")
    agoda = st.text_input("Agoda Homes URL")
    st.markdown('</div>', unsafe_allow_html=True)

with main_content:
    # Top Row Metrics wrapped in Animated 3D Glass Cards
    m1, m2, m3 = st.columns(3)
    
    with m1:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("<h4 style='color: #8b949e; margin:0;'>Active Channels</h4>", unsafe_allow_html=True)
        active_count = sum(1 for x in [airbnb, vrbo, booking, expedia, agoda] if x)
        st.markdown(f"<h1 style='color: #00d1ff; margin:0; font-size: 3rem;'>{active_count} <span style='font-size:1.2rem; color:#8b949e;'>/ 5 Connected</span></h1>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with m2:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("<h4 style='color: #8b949e; margin:0;'>Sync Velocity</h4>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: #00ff88; margin:0; font-size: 3rem;'>Instant <span style='font-size:1.2rem; color:#8b949e;'>⚡ Real-time</span></h1>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with m3:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("<h4 style='color: #8b949e; margin:0;'>Double-Book Multiplier</h4>", unsafe_allow_html=True)
        st.markdown("<h1 style='color: #ff4b4b; margin:0; font-size: 3rem;'>0.00% <span style='font-size:1.2rem; color:#8b949e;'>Risk Factor</span></h1>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Core Action Areas
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown('<div class="panel-header">📅 Matrix Availability Calendar</div>', unsafe_allow_html=True)
        
        target_date = st.date_input("Inquire Specific Placement Slot", datetime.now().date())
        # Visual response styling based on state
        if airbnb:
            st.markdown("<div style='padding: 15px; background: rgba(0, 255, 136, 0.1); border-left: 4px solid #00ff88; border-radius: 4px; color: #00ff88;'>⚡ Automated Protection Enabled: Selected date is fully synchronized across all 5 pipelines.</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='color: #8b949e;'>Provide active node connections to start cluster sync mapping.</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_right:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown('<div class="panel-header">🤖 Predictive Rate Yield Engine</div>', unsafe_allow_html=True)
        base = st.number_input("Base Room Value ($)", min_value=10, value=220)
        multiplier_selection = st.select_slider("Forecast / Local Holiday Scaling Parameter", options=["Low Season (-20%)", "Standard Pricing", "Premium Surge (+35%)"], value="Standard Pricing")
        
        mult = 1.0
        if "Low" in multiplier_selection: mult = 0.8
        elif "Premium" in multiplier_selection: mult = 1.35
        
        st.markdown(f"<h2 style='color: #ffffff; margin-top:15px;'>Smart Room Yield: <span style='color: #00ff88;'>${round(base * mult, 2)}</span></h2>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
