import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ContractLens",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown("""
<style>

/* ---------- GLOBAL ---------- */

.stApp {
    background-color: #F6F9FD;
}

[data-testid="stHeader"] {
    background-color: #F6F9FD;
}

.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
    padding-bottom: 3rem;
}

h1, h2, h3, p {
    font-family: Arial, sans-serif;
}


/* ---------- SIDEBAR ---------- */

[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid #E4EAF2;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 2rem;
    padding-left: 1.5rem;
    padding-right: 1.5rem;
}

[data-testid="stSidebar"] * {
    color: #172033;
}

.logo-title {
    font-size: 22px;
    font-weight: 700;
    color: #172033 !important;
    margin-bottom: 4px;
}

.logo-subtitle {
    font-size: 14px;
    color: #94A3B8 !important;
    margin-bottom: 35px;
}


/* ---------- SIDEBAR NAV ---------- */

.nav-active {
    background-color: #EAF2FF;
    color: #2563EB !important;
    border-radius: 9px;
    padding: 11px 12px;
    font-weight: 700;
    margin-bottom: 5px;
}

.nav-item {
    color: #334155 !important;
    padding: 11px 12px;
    font-weight: 600;
    margin-bottom: 5px;
}


/* ---------- ADD CONTRACT BUTTON ---------- */

.add-contract-button {
    background-color: #2563EB;
    color: white !important;
    border-radius: 9px;
    padding: 12px;
    text-align: center;
    font-weight: 700;
    margin-top: 25px;
}


/* ---------- PAGE HEADER ---------- */

.page-title {
    font-size: 36px;
    font-weight: 750;
    color: #172033 !important;
    margin-bottom: 4px;
}

.page-subtitle {
    font-size: 15px;
    color: #7B8BA3 !important;
    margin-bottom: 28px;
}


/* ---------- METRIC CARDS ---------- */

.metric-card {
    background-color: #FFFFFF;
    border: 1px solid #DFE7F2;
    border-radius: 14px;
    padding: 20px;
    min-height: 115px;
}

.metric-top {
    display: flex;
    align-items: center;
    gap: 12px;
}

.metric-icon {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
}

.blue-icon {
    background-color: #EAF2FF;
}

.green-icon {
    background-color: #E8F8F1;
}

.purple-icon {
    background-color: #F2EBFF;
}

.metric-label {
    color: #64748B;
    font-size: 14px;
    font-weight: 600;
}

.metric-number {
    color: #172033;
    font-size: 30px;
    font-weight: 700;
    margin-top: 8px;
}


/* ---------- SECTION CARD ---------- */

.section-card {
    background-color: #FFFFFF;
    border: 1px solid #DFE7F2;
    border-radius: 14px;
    padding: 20px;
    margin-top: 22px;
}

.section-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 15px;
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #17345F !important;
}

.section-icon {
    margin-right: 8px;
}


/* ---------- ATTENTION CARDS ---------- */

.attention-card {
    border-radius: 11px;
    padding: 17px;
    border: 1px solid;
}

.attention-blue {
    background-color: #EFF6FF;
    border-color: #BFDBFE;
}

.attention-yellow {
    background-color: #FFFBEB;
    border-color: #FDE68A;
}

.attention-title {
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 7px;
}

.attention-description {
    font-size: 13px;
    color: #64748B !important;
}


/* ---------- UPCOMING ROW ---------- */

.upcoming-row {
    display: flex;
    align-items: center;
    border: 1px solid #E5EBF3;
    border-radius: 10px;
    padding: 11px;
    margin-bottom: 8px;
    background-color: #FFFFFF;
}

.date-box {
    background-color: #EFF5FF;
    border-radius: 9px;
    width: 58px;
    min-width: 58px;
    padding: 7px 4px;
    text-align: center;
    margin-right: 15px;
}

.date-month {
    color: #2563EB;
    font-size: 11px;
    font-weight: 700;
}

.date-day {
    color: #17345F;
    font-size: 20px;
    font-weight: 700;
}

.upcoming-content {
    flex: 1;
}

.upcoming-title {
    color: #263B5A !important;
    font-size: 14px;
    font-weight: 700;
}

.upcoming-details {
    color: #94A3B8 !important;
    font-size: 12px;
    margin-top: 3px;
}


/* ---------- STATUS PILLS ---------- */

.status-pill {
    display: inline-block;
    border-radius: 20px;
    padding: 6px 12px;
    font-size: 11px;
    font-weight: 700;
    margin-right: 15px;
}

.status-due {
    background-color: #FFF0E8;
    color: #C2410C !important;
}

.status-upcoming {
    background-color: #EAF5FF;
    color: #2563EB !important;
}


/* ---------- REVIEW ROW ---------- */

.review-row {
    display: flex;
    align-items: center;
    border: 1px solid #E5EBF3;
    border-radius: 10px;
    padding: 13px;
    margin-bottom: 8px;
}

.review-icon {
    width: 38px;
    height: 38px;
    background-color: #EAF2FF;
    border-radius: 9px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 13px;
}

.review-content {
    flex: 1;
}

.review-title {
    color: #263B5A !important;
    font-size: 14px;
    font-weight: 700;
}

.review-details {
    color: #94A3B8 !important;
    font-size: 12px;
    margin-top: 4px;
}


/* ---------- VIEW BUTTON ---------- */

.stButton > button {
    border-radius: 8px;
    border: 1px solid #D6E0ED;
    background-color: #FFFFFF;
    color: #2563EB !important;
    font-weight: 600;
    min-height: 38px;
}

.stButton > button:hover {
    border-color: #2563EB;
    background-color: #F8FBFF;
}


/* ---------- FOOTER ---------- */

.footer-text {
    color: #8B9AB0 !important;
    font-size: 12px;
    margin-top: 25px;
}


/* ---------- ATTENTION CARDS ---------- */

.attention-card {
    border-radius: 12px;
    padding: 20px;
    min-height: 70px;
    border: 1px solid;
}

.blue-card {
    background-color: #EFF6FF;
    border-color: #BFDBFE;
}

.yellow-card {
    background-color: #FFFBEB;
    border-color: #FDE68A;
}

.attention-title {
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 10px;
}

.blue-card .attention-title {
    color: #1D4ED8;
}

.yellow-card .attention-title {
    color: #92400E;
}

.attention-text {
    font-size: 14px;
    color: #64748B;
}

.section-card {
    background: #FFFFFF;
    border: 1px solid #E3E8F0;
    border-radius: 12px;
    padding: 20px;
    margin-top: 12px;
    margin-bottom: 20px;
}

.section-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #172033;
    margin-bottom: 18px;
}

.section-icon {
    margin-right: 8px;
}

.upcoming-item {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 9px 0;
}

.upcoming-item strong {
    color: #172033;
}

.upcoming-item p,
.review-item {
    padding: 9px 0;
}

.review-item + .review-item {
    border-top: 1px solid #EEF1F5;
}

.date-box {
    width: 52px;
    min-width: 52px;
    text-align: center;
    padding: 7px 4px;
    background: #F6F8FC;
    border: 1px solid #E3E8F0;
    border-radius: 8px;
    color: #17345F;
}

.date-box strong {
    display: block;
    font-size: 1.15rem;
}

.date-box span {
    font-size: 0.7rem;
    color: #64748B;
}

.review-item {
    padding: 14px 0;
    border-top: 1px solid #EEF1F5;
}

.review-item strong {
    color: #172033;
}

.review-item span {
    display: inline-block;
    margin-top: 8px;
    font-size: 0.8rem;
    color: #B45309;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# MOCK DATA
# ============================================================

upcoming = [
    {
        "date": "Sep 22",
        "title": "Submit monthly usage report",
        "details": "Acme Corp · Acme Master Agreement",
        "status": "Due Soon",
    },
    {
        "date": "Sep 28",
        "title": "Renewal notice deadline",
        "details": "Acme Master Agreement",
        "status": "Upcoming",
    },
]

reviews = [
    {
        "title": "Termination clause",
        "contract": "Acme Master Agreement",
        "section": "§12.2 — Termination",
        "reason": "Notice period requires human attention.",
    },
    {
        "title": "Payment penalty clause",
        "contract": "XYZ Vendor Agreement",
        "section": "§6.4 — Late Payment",
        "reason": "Additional penalty applies after the payment deadline.",
    },
]


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="logo-title">📄 ContractLens</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="logo-subtitle">From contracts to commitments.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nav-active">🏠 &nbsp; Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nav-item">📄 &nbsp; Contracts</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nav-item">✓ &nbsp; Obligations</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nav-item">◷ &nbsp; Timeline</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nav-item">⚠ &nbsp; Review</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nav-item">⇄ &nbsp; Compare</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nav-item">✦ &nbsp; Ask AI</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        '<div class="add-contract-button">＋ &nbsp; Add Contract</div>',
        unsafe_allow_html=True
    )


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    '<div class="page-title">Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="page-subtitle">Your contracts, obligations, and upcoming deadlines.</div>',
    unsafe_allow_html=True
)


# ============================================================
# METRICS
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-top">
            <div class="metric-icon blue-icon">📅</div>
            <div class="metric-label">Due Soon</div>
        </div>
        <div class="metric-number">3</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-top">
            <div class="metric-icon green-icon">↻</div>
            <div class="metric-label">Renewals</div>
        </div>
        <div class="metric-number">2</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-top">
            <div class="metric-icon purple-icon">⚠</div>
            <div class="metric-label">Review</div>
        </div>
        <div class="metric-number">3</div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# NEEDS ATTENTION
# ============================================================

# ---------- NEEDS ATTENTION ----------
st.subheader("Needs Attention")

attention_col1, attention_col2 = st.columns(2)

with attention_col1:
    st.markdown(
        """
        <div class="attention-card blue-card">
            <div class="attention-title">3 obligations due soon</div>
            <div class="attention-text">The next deadline is Sep 22.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with attention_col2:
    st.markdown(
        """
        <div class="attention-card yellow-card">
            <div class="attention-title">3 clauses require attention</div>
            <div class="attention-text">Review flagged contract sections.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")


# ---------------- UPCOMING ----------------

with st.container(border=True):

    st.markdown(
        """
        <div class="section-title">
            <span class="section-icon">◉</span>
            Upcoming
        </div>
        """,
        unsafe_allow_html=True
    )

    for item in upcoming:

        col1, col2, col3 = st.columns([1, 6, 1])

        with col1:
            date_parts = item["date"].split()

            st.markdown(
                f"""
                <div class="date-box">
                    <div class="date-day">{date_parts[1]}</div>
                    <div class="date-month">{date_parts[0].upper()}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div style="padding-top:5px;">
                    <div class="upcoming-title">{item["title"]}</div>
                    <div class="upcoming-details">{item["details"]}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:
            st.button(
                "View",
                key=f"upcoming_{item['title']}"
            )

# ---------------- REVIEW ----------------

with st.container(border=True):

    st.markdown(
        """
        <div class="section-title">
            <span class="section-icon">⚠</span>
            Review
        </div>
        """,
        unsafe_allow_html=True
    )

    for item in reviews:

        col1, col2 = st.columns([5, 1])

        with col1:
            st.markdown(
                f"""
                <div class="review-content">
                    <div class="review-title">{item["title"]}</div>
                    <div class="review-details">
                        {item["contract"]} · {item["section"]}
                    </div>
                    <div style="
                        color:#B45309;
                        font-size:12px;
                        margin-top:7px;
                    ">
                        Human review recommended
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.button(
                "View",
                key=f"review_{item['title']}"
            )

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer-text">ContractLens helps teams understand and keep track of contractual commitments.</div>',
    unsafe_allow_html=True
)