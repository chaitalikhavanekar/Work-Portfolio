import streamlit as st

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="Finance & Research Portfolio",
    layout="wide"
)

# ------------------ CSS ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

html, body {
    background-color: #121524;
    color: #9DACCC;
    font-family: 'Inter', sans-serif;
}

h1, h2, h3 {
    color: #C0C9DB;
    font-weight: 600;
}

.hero {
    padding: 60px 0 40px 0;
}

.subtitle {
    max-width: 720px;
    line-height: 1.6;
    color: #9DACCC;
}

.disclaimer {
    font-size: 13px;
    color: #9DACCC;
    opacity: 0.8;
}

.card {
    background: linear-gradient(180deg, #384C65 0%, #2f4159 100%);
    border-radius: 16px;
    padding: 28px;
    height: 100%;
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}

.card-title {
    font-size: 20px;
    margin-bottom: 10px;
}

.card-desc {
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 18px;
}

.tag {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    background-color: #485F88;
    color: #121524;
    font-size: 12px;
    margin-right: 8px;
    margin-bottom: 12px;
}

.open-btn button {
    background-color: #C0C9DB;
    color: #121524;
    border-radius: 10px;
    padding: 10px 22px;
    font-weight: 600;
    border: none;
}

.open-btn button:hover {
    background-color: #9DACCC;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HERO ------------------
st.markdown("""
<div class="hero">
    <h1>Finance & Research Portfolio</h1>
    <p class="subtitle">
        A curated showcase of analytical products developed for macro-financial research,
        time-series modelling, and portfolio construction. These applications are academic
        and exploratory in nature and are not intended for trading or investment execution.
    </p>
    <p class="disclaimer">
        This portfolio is presented for research, learning, and analytical demonstration purposes only.
    </p>
</div>
""", unsafe_allow_html=True)

# ------------------ PROJECT GRID ------------------
st.markdown("## Analytical Products")

col1, col2, col3 = st.columns(3)

# ------------------ ARIMA ------------------
with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">ARIMA Forecasting</div>
        <div class="card-desc">
            Time-series forecasting framework for economic and financial indicators,
            focusing on trend, seasonality, and residual diagnostics.
        </div>
        <span class="tag">Time Series</span>
        <span class="tag">ARIMA</span>
        <span class="tag">Forecasting</span>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Product", key="arima"):
        st.session_state["view"] = "arima"

# ------------------ MACRO NEWS ------------------
with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">Macro News Indicator</div>
        <div class="card-desc">
            News and sentiment-based macro indicator designed to interpret
            economic signals across policy, inflation, and growth narratives.
        </div>
        <span class="tag">Macro</span>
        <span class="tag">Sentiment</span>
        <span class="tag">Indicators</span>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Product", key="macro"):
        st.session_state["view"] = "macro"

# ------------------ ASSET ALLOCATION ------------------
with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">Asset Allocation</div>
        <div class="card-desc">
            Portfolio construction prototype demonstrating allocation logic
            across asset classes using risk-return assumptions.
        </div>
        <span class="tag">Portfolio</span>
        <span class="tag">Allocation</span>
        <span class="tag">Risk</span>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Product", key="asset"):
        st.session_state["view"] = "asset"

# ------------------ EMBED VIEW ------------------
if "view" in st.session_state:
    st.divider()

    if st.session_state["view"] == "arima":
        st.markdown("### ARIMA Forecasting Application")
        st.components.v1.iframe(
            "https://YOUR-ARIMA-APP.streamlit.app",
            height=900,
            scrolling=True
        )

    if st.session_state["view"] == "macro":
        st.markdown("### Macro News Indicator Application")
        st.components.v1.iframe(
            "https://YOUR-MACRO-APP.streamlit.app",
            height=900,
            scrolling=True
        )

    if st.session_state["view"] == "asset":
        st.markdown("### Asset Allocation Application")
        st.components.v1.iframe(
            "https://YOUR-ASSET-APP.streamlit.app",
            height=900,
            scrolling=True
        )
