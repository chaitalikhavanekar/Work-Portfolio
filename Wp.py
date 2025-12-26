import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Finance Research Portfolio",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
body {
    background-color: #121524;
    color: #C0C9DB;
}

.main {
    background-color: #121524;
}

h1, h2, h3 {
    color: #C0C9DB;
}

.card {
    background-color: #384C65;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
}

.button a {
    text-decoration: none;
    color: #121524;
    background-color: #485F88;
    padding: 10px 18px;
    border-radius: 10px;
    font-weight: 600;
}

.button a:hover {
    background-color: #9DACCC;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HERO SECTION ------------------
st.markdown("""
<h1>📊 Finance & Research Portfolio</h1>
<p>Analytical projects, market research, and data-driven insights.</p>
""", unsafe_allow_html=True)

st.divider()

# ------------------ PROJECTS ------------------
st.markdown("## 🚀 Featured Projects")

# ---- PROJECT 1 ----
st.markdown("""
<div class="card">
    <h3>Indian Startup Failure Analysis</h3>
    <p>
    Deep dive into why Indian startups fail using secondary data,
    unit economics, governance gaps, and market structure analysis.
    </p>
    <div class="button">
        <a href="https://your-streamlit-app-link" target="_blank">Live App</a>
        &nbsp;&nbsp;
        <a href="https://your-gamma-ppt-link" target="_blank">Research PPT</a>
        &nbsp;&nbsp;
        <a href="https://your-google-drive-pdf" target="_blank">Full Report</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---- PROJECT 2 ----
st.markdown("""
<div class="card">
    <h3>Working Capital Management – Indian Corporates</h3>
    <p>
    Research on post-COVID liquidity cycles, cash conversion,
    and financing patterns across Indian companies.
    </p>
    <div class="button">
        <a href="https://your-streamlit-app-link" target="_blank">Live Dashboard</a>
        &nbsp;&nbsp;
        <a href="https://your-gamma-ppt-link" target="_blank">Presentation</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.divider()
st.markdown("""
<p style="text-align:center; color:#9DACCC;">
Built with Streamlit | Finance • Research • Strategy
</p>
""", unsafe_allow_html=True)
