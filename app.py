import streamlit as st
import requests
from icalendar import Calendar
from datetime import datetime, timedelta

st.set_page_config(page_title="Sync Engine", page_icon="⚡", layout="wide")
st.title("⚡ Live Rental Sync Engine & Dynamic Pricing")

# 1. Input Fields for Real Platform Links
st.sidebar.header("🔗 Connect Your Rental Channels")
airbnb_url = st.sidebar.text_input("Airbnb iCal URL", placeholder="https://airbnb.com...")
vrbo_url = st.sidebar.text_input("Vrbo iCal URL", placeholder="https://vrbo.com...")

def fetch_booked_dates(url):
    if not url: return []
    try:
        response = requests.get(url, timeout=10)
        cal = Calendar.from_ical(response.content)
        dates = []
        for component in cal.walk():
            if component.name == "VEVENT":
                start = component.get('dtstart').dt
                end = component.get('dtend').dt
                # Handle both datetime and date formats
                if isinstance(start, datetime): start = start.date()
                if isinstance(end, datetime): end = end.date()
                
                # Loop through all days of the reservation
                curr = start
                while curr < end:
                    dates.append(curr.strftime("%Y-%m-%d"))
                    curr += timedelta(days=1)
        return dates
    except Exception as e:
        st.sidebar.error(f"Error syncing link: {str(e)[:50]}")
        return []

# 2. Process Live Calendar Sync
all_booked_dates = set()
if airbnb_url:
    all_booked_dates.update(fetch_booked_dates(airbnb_url))
if vrbo_url:
    all_booked_dates.update(fetch_booked_dates(vrbo_url))

# 3. Main Dashboard UI
col1, col2 = st.columns(2)

with col1:
    st.subheader("📅 Centralized Real-Time Calendar")
    st.write(f"**Total Blocked Days Across Channels:** {len(all_booked_dates)}")
    
    # Render a date picker highlighting blocked dates
    target_date = st.date_input("Check Availability Date", datetime.now().date())
    if target_date.strftime("%Y-%m-%d") in all_booked_dates:
        st.error("❌ Blocked: Double-Booking Risk Auto-Prevented!")
    else:
        st.success("✅ Available to Book Across All Channels")

with col2:
    st.subheader("🤖 AI Dynamic Pricing Engine")
    base_price = st.number_input("Base Nightly Rate ($)", min_value=50, max_value=2000, value=250)
    weather_factor = st.selectbox("Forecast Impact", ["Sunny/Perfect Weekend (+20%)", "Standard Season (0%)", "Stormy/Rainy Outlook (-15%)"])
    
    # Calculate price based on live logic
    multiplier = 1.0
    if "Perfect" in weather_factor: multiplier = 1.20
    elif "Stormy" in weather_factor: multiplier = 0.85
    
    final_price = round(base_price * multiplier, 2)
    st.metric(label="Suggested Smart Rate", value=f"${final_price}", delta=f"{round((multiplier-1)*100)}% adjustment")
