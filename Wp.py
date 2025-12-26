import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Finance & Research Portfolio",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS (STRICT, PROFESSIONAL)
# -------------------------------------------------
st.markdown("""
<style>
html, body, [class*="css"]  {
    background-color: #121524;
    color: #9DACCC;
    font-family: "Inter", sans-serif;
}

h1, h2, h3 {
    color: #C0C9DB;
    font-weight: 600;
}

.section {
    margin-top: 40px;
}

.card {
    background-color: #384C65;
    padding: 28px;
    border-radius: 14px;
    margin-bottom: 28px;
}

.label {
    font-size: 14px;
    color: #9DACCC;
    margin-bottom: 6px;
}

input {
    background-color: #121524 !important;
    color: #C0C9DB !important;
}

.stButton button {
    background-color: #485F88;
    color: #121524;
    border-radius: 8px;
    padding: 8px 18px;
    font-weight: 600;
    border: none;
}

.stButton button:hover {
    background-color: #C0C9DB;
    color: #121524;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown("<h1>Finance & Research Portfolio</h1>", unsafe_allow_html=True)
st.markdown(
    "<p>Selected analytical applications and macro-financial research prototypes.</p>",
    unsafe_allow_html=True
)

# -------------------------------------------------
# PROJECT SECTION
# -------------------------------------------------
st.markdown("<div class='section'><h2>Project Portfolio</h2></div>", unsafe_allow_html=True)

# ------------------- PROJECT 1 -------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h3>ARIMA Forecasting Application</h3>", unsafe_allow_html=True)
st.markdown(
    "<p>Time-series forecasting model for economic and financial indicators using ARIMA methodology.</p>",
    unsafe_allow_html=True
)

arima_link = st.text_input(
    "Streamlit Application Link",
    placeholder="https://your-arima-app.streamlit.app",
    key="arima"
)

if arima_link:
    st.markdown(f"[Open Application]({arima_link})")

st.markdown("</div>", unsafe_allow_html=True)

# ------------------- PROJECT 2 -------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h3>Macro News Indicator Application</h3>", unsafe_allow_html=True)
st.markdown(
    "<p>Macro sentiment and news-based indicator to assess economic and market-level signals.</p>",
    unsafe_allow_html=True
)

macro_link = st.text_input(
    "Streamlit Application Link",
    placeholder="https://your-macro-news-app.streamlit.app",
    key="macro"
)

if macro_link:
    st.markdown(f"[Open Application]({macro_link})")

st.markdown("</div>", unsafe_allow_html=True)

# ------------------- PROJECT 3 -------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h3>Asset Allocation Application</h3>", unsafe_allow_html=True)
st.markdown(
    "<p>Portfolio allocation model demonstrating risk-return optimisation across asset classes.</p>",
    unsafe_allow_html=True
)

asset_link = st.text_input(
    "Streamlit Application Link",
    placeholder="https://your-asset-allocation-app.streamlit.app",
    key="asset"
)

if asset_link:
    st.markdown(f"[Open Application]({asset_link})")

st.markdown("</div>", unsafe_allow_html=True)
