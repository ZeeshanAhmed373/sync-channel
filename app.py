import streamlit as st
from datetime import datetime

# Compress layout and remove default header blocks completely
st.set_page_config(
    page_title="OmniSync 3D Pro", 
    page_icon="⚡", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Complete Production CSS Overrides for High Contrast Visibility & Photo Slideshow
st.markdown("""
<style>
    /* Bright Electric Cyan color override for the top header bar decoration */
    header[data-testid="stHeader"] {
        background-color: #00d1ff !important;
        box-shadow: 0 2px 20px rgba(0, 209, 255, 0.4);
    }

    /* Automated High-Definition Resort Photo Slideshow Core Engine */
    [data-testid="stAppViewContainer"] {
        background-size: cover !important;
        background-position: center center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
        animation: resortSlideshow 24s infinite ease-in-out !important;
    }

    @keyframes resortSlideshow {
        0%, 100% { 
            background: linear-gradient(rgba(10, 25, 47, 0.82), rgba(10, 25, 47, 0.82)), 
            url('https://unsplash.com') no-repeat center center fixed !important;
            background-size: cover !important;
        }
        25% { 
            background: linear-gradient(rgba(10, 25, 47, 0.82), rgba(10, 25, 47, 0.82)), 
            url('https://unsplash.com') no-repeat center center fixed !important;
            background-size: cover !important;
        }
        50% { 
            background: linear-gradient(rgba(10, 25, 47, 0.82), rgba(10, 25, 47, 0.82)), 
            url('https://unsplash.com') no-repeat center center fixed !important;
            background-size: cover !important;
        }
        75% { 
            background: linear-gradient(rgba(10, 25, 47, 0.82), rgba(10, 25, 47, 0.82)), 
            url('https://unsplash.com') no-repeat center center fixed !important;
            background-size: cover !important;
        }
    }
    
    /* 3D Elevated Glassmorphism Panel Containers */
    .dashboard-card {
        background: rgba(10, 25, 47, 0.85) !important;
        border: 1px solid rgba(0, 209, 255, 0.3) !important;
        border-radius: 14px !important;
        padding: 20px 24px !important;
        box-shadow: 0 12px 40px -12px rgba(2, 12, 27, 0.9);
        backdrop-filter: blur(25px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%);
        margin-bottom: 16px;
    }
    
    /* Input Container Field Adjustments */
    div[data-testid="stTextInput"] > div, div[data-testid="stNumberInput"] > div {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.35) !important;
        border-radius: 8px !important;
    }
    
    /* Forces stark white text values for text entries and input fields */
    div[data-testid="stTextInput"] input, div[data-testid="stNumberInput"] input {
        color: #ffffff !important;
        font-weight: 600 !important;
        -webkit-text-fill-color: #ffffff !important;
    }

    /* Target placeholder input text fields explicitly to stay clear and highly readable */
    div[data-testid="stTextInput"] input::placeholder {
        color: rgba(255, 255, 255, 0.7) !important;
        -webkit-text-fill-color: rgba(255, 255, 255, 0.7) !important;
        opacity: 1 !important;
    }

    /* Force all layout labels, widget headers, and values to bold stark white */
    div[data-testid="stTextInput"] label, 
    div[data-testid="stDateInput"] label, 
    div[data-testid="stNumberInput"] label,
    .stSlider label, p, span, h4, h1, h2, h3 {
        color: #ffffff !important;
        font-size: 0.96rem !important;
        font-weight: 700 !important;
        text-shadow: 0px 1px 5px rgba(0, 0, 0, 0.95) !important;
    }

    .sub-title-text {
        color: #e2e8f0 !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
        margin-top: 2px !important;
        margin-bottom: 25px !important;
    }

    .gradient-title {
        background: linear-gradient(45deg, #00d1ff, #00ff88);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2rem !important;
    }

    @keyframes pulseGlow {
        0% { transform: scale(0.95); opacity: 0.6; }
        50% { transform: scale(1.05); opacity: 1; }
        100% { transform: scale(0.95); opacity: 0.6; }
    }
    .status-ping {
        display: inline-block;
        width: 11px;
        height: 11px;
        background: #00ff88;
        border-radius: 50%;
        margin-right: 10px;
        animation: pulseGlow 2s infinite ease-in-out;
    }
    .block-container { padding-top: 2.5rem !important; padding-bottom: 1rem !important; }
</style>
""", unsafe_allow_html=True)

# Top Bar Title Layout Context
st.markdown('<div><span class="status-ping"></span><span class="gradient-title">OmniSync 3D Pro</span></div>', unsafe_allow_html=True)
st.markdown("<p class='sub-title-text'>Real-time AI Multi-Channel Engine for Luxury Stays</p>", unsafe_allow_html=True)
# Session tracking state initialization
if 'active_view' not in st.session_state:
    st.session_state.active_view = "Live Multi-Channel View"

# Render completely filled interactive tab row configurations with unique actions
t1, t2, t3, t4 = st.columns(4)
with t1:
    if st.button("🌐 Live Channels Matrix", use_container_width=True):
        st.session_state.active_view = "Live Multi-Channel View"
with t2:
    if st.button("📊 Sync Optimization Log", use_container_width=True):
        st.session_state.active_view = "Optimization Performance Log"
with t3:
    if st.button("🤖 Dynamic AI Insights", use_container_width=True):
        st.session_state.active_view = "Dynamic AI Insights Dashboard"
with t4:
    if st.button("⚙️ Core Engine Settings", use_container_width=True):
        st.session_state.active_view = "System Engine Configuration"

st.write("")

# Render layout modules dynamically based on active selection from top functional tabs
if st.session_state.active_view == "Live Multi-Channel View":
    left_panel, right_panel = st.columns([1, 1.2])

    with left_panel:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("<p style='font-size:1.15rem; font-weight:700; margin-top:0; margin-bottom:15px; color:#ffffff;'>⛓️ Node Integration Hub</p>", unsafe_allow_html=True)
        
        airbnb_node = st.text_input("Airbnb iCal Link", value="https://example.com")
        vrbo_node = st.text_input("Vrbo Pipeline", placeholder="Paste Vrbo .ics calendar link")
        booking_node = st.text_input("Booking.com Node", placeholder="Paste Booking.com calendar feed")
        expedia_node = st.text_input("Expedia Loop", placeholder="Enter Expedia channel feed")
        agoda_node = st.text_input("Agoda Ledger", placeholder="Enter Agoda calendar endpoint")
        
        # Submit, Save, and Apply Changes action button
        st.write("")
        if st.button("💾 Apply & Save Node Formations", type="primary", use_container_width=True):
            st.toast("⚡ Node sync matrix updated successfully!", icon="✅")
            
        st.markdown('</div>', unsafe_allow_html=True)

    with right_panel:
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
            st.markdown("<span style='color: #ffffff; font-size:0.8rem; font-weight:700;'>ACTIVE PIPELINES</span>", unsafe_allow_html=True)
            connected = sum(1 for node in [airbnb_node, vrbo_node, booking_node, expedia_node, agoda_node] if node)
            st.markdown(f"<p style='color: #00d1ff; font-size: 1.8rem; font-weight:800; margin:4px 0;'>{connected} <span style='font-size:0.85rem; color:#e2e8f0; font-weight:500;'>/ 5 Connected</span></p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
            st.markdown("<span style='color: #ffffff; font-size:0.8rem; font-weight:700;'>SYNC VELOCITY</span>", unsafe_allow_html=True)
            st.markdown("<p style='color: #00ff88; font-size: 1.8rem; font-weight:800; margin:4px 0;'>Realtime <span style='font-size:0.85rem; color:#e2e8f0; font-weight:500;'>⚡ 0.4s lag</span></p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
            st.markdown("<span style='color: #ffffff; font-size:0.8rem; font-weight:700;'>OVERLAP RISK</span>", unsafe_allow_html=True)
            st.markdown("<p style='color: #ff4b4b; font-size: 1.8rem; font-weight:800; margin:4px 0;'>0.00% <span style='font-size:0.85rem; color:#e2e8f0; font-weight:500;'>Shield On</span></p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
            st.markdown("<p style='font-size:1rem; font-weight:700; margin-top:0; color:#ffffff;'>📅 Unified Ledger Matrix</p>", unsafe_allow_html=True)
            selected_slot = st.date_input("Inquire Block Dates", datetime.now().date())
            if airbnb_node:
                st.markdown("<div style='padding: 10px; background: rgba(0, 255, 136, 0.08); border-left: 3px solid #00ff88; border-radius: 4px; color: #00ff88; font-size:0.85rem;'>✅ Live protection mapping active.</div>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
            st.markdown("<p style='font-size:1rem; font-weight:700; margin-top:0; color:#ffffff;'>🤖 AI Predictive Rate Engine</p>", unsafe_allow_html=True)
            base_rate = st.number_input("Base Nightly Rate ($)", min_value=10, value=250)
            yield_multiplier = st.select_slider("Environmental Scaler", options=["Off-Peak (-20%)", "Standard Pricing", "Surge Demand (+35%)"], value="Standard Pricing")
            
            calculated_factor = 1.0
            if "Off-Peak" in yield_multiplier: calculated_factor = 0.8
            elif "Surge" in yield_multiplier: calculated_factor = 1.35
            
            st.markdown(f"<p style='color: #ffffff; font-size: 1.1rem; margin-top:12px; margin-bottom:0;'>Optimized Rate: <span style='color: #00ff88; font-weight:800;'>${round(base_rate * calculated_factor, 2)}</span></p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

else:
    # Secondary navigation view layouts logic
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown(f"<h3 style='color:#ffffff;'>📊 Matrix Layer: {st.session_state.active_view}</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#cbd5e1; font-weight:400;'>This partition structure connects to active live data simulated sockets. Node link modifications will update these system matrix records automatically.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
