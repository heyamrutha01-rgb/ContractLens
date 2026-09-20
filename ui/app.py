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

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "analysis_state" not in st.session_state:
    st.session_state.analysis_state = "idle"

if "show_source" not in st.session_state:
    st.session_state.show_source = False

if "obligation_source" not in st.session_state:
    st.session_state.obligation_source = None

if "timeline_event" not in st.session_state:
    st.session_state.timeline_event = None

if "review_item" not in st.session_state:
    st.session_state.review_item = None

if "compare_result" not in st.session_state:
    st.session_state.compare_result = False

if "compare_source" not in st.session_state:
    st.session_state.compare_source = None

if "qa_messages" not in st.session_state:
    st.session_state.qa_messages = []

if "qa_source" not in st.session_state:
    st.session_state.qa_source = None

if "dashboard_source" not in st.session_state:
    st.session_state.dashboard_source = None

# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown("""
<style>

/* ---------- GLOBAL ---------- */

.stApp {
    background-color: #f3f6fa;
}

[data-testid="stHeader"] {
    background-color: #f3f6fa;
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
    color: #64748B !important;
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
    border: 1px solid #D9E2EF;
    border-radius: 14px;
    padding: 20px;
    margin-top: 22px;
    box-shadow: 0 2px 8px rgba(23, 32, 51, 0.04);
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
    border: 1px solid #C9D6E6;
    background-color: #FFFFFF;
    color: #2563EB !important;
    font-weight: 600;
    min-height: 38px;
}

/* ---------- SIDEBAR NAV BUTTON ---------- */

[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    border: none !important;
    background-color: transparent !important;
    color: #334155 !important;
    text-align: left !important;
    padding: 11px 12px !important;
    font-weight: 600 !important;
    min-height: 0 !important;
    border-radius: 9px !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #F3F6FA !important;
    border: none !important;
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

/* ---------- ADD CONTRACT UPLOAD ---------- */

.upload-section-label {
    font-size: 13px;
    font-weight: 700;
    color: #64748B;
    margin-top: 8px;
    margin-bottom: 10px;
    letter-spacing: 0.4px;
}

[data-testid="stFileUploader"] {
    max-width: 580px;
    margin: 0 auto;
}

[data-testid="stFileUploaderDropzone"] {
    background-color: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 8px !important;
    min-height: 130px !important;
}

[data-testid="stFileUploaderDropzoneInstructions"] {
    color: #64748B !important;
}

[data-testid="stFileUploaderDropzoneInstructions"] div {
    color: #64748B !important;
}

.upload-section-label {
    font-size: 13px;
    font-weight: 700;
    color: #64748B;
    margin-top: 18px;
    margin-bottom: 8px;
}

.related-label {
    margin-top: 24px;
}

.file-row {
    display: flex;
    align-items: center;
    gap: 10px;
    background: #FFFFFF;
    border: 1px solid #DFE7F2;
    border-radius: 8px;
    padding: 10px 14px;
    margin-top: 8px;
    color: #334155;
    font-size: 13px;
}

.file-check {
    margin-left: auto;
    color: #16A34A;
    font-weight: 700;
}

/* ---------- FILE UPLOAD BUTTON ---------- */

[data-testid="stFileUploader"] button {
    background-color: #2563EB !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}

[data-testid="stFileUploader"] button:hover {
    background-color: #1D4ED8 !important;
    color: #FFFFFF !important;
}

[data-testid="stFileUploaderDropzone"] {
    background-color: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 9px !important;
}

[data-testid="stFileUploaderDropzoneInstructions"] {
    color: #7B8BA3 !important;
}

.analysis-card {
    background: #FFFFFF;
    border: 1px solid #DFE7F2;
    border-radius: 12px;
    padding: 24px;
    margin-top: 25px;
    max-width: 620px;
}

.analysis-title {
    font-size: 18px;
    font-weight: 700;
    color: #172033;
    margin-bottom: 20px;
}

.analysis-step {
    color: #64748B;
    font-size: 14px;
    padding: 7px 0;
}

/* ---------- SEARCH INPUT ---------- */

[data-testid="stTextInput"] input {
    background-color: #FFFFFF !important;
    color: #172033 !important;
    border: 1px solid #D6E0ED !important;
    border-radius: 8px !important;
}

[data-testid="stTextInput"] input::placeholder {
    color: #94A3B8 !important;
}

[data-testid="stTextInput"] input:focus {
    border-color: #2563EB !important;
    box-shadow: 0 0 0 1px #2563EB !important;
}

/* ---------- SELECTBOXES ---------- */

[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #172033 !important;
    border: 1px solid #D6E0ED !important;
    border-radius: 8px !important;
}

[data-testid="stSelectbox"] svg {
    fill: #64748B !important;
    color: #64748B !important;
}

[data-testid="stSelectbox"] div[data-baseweb="select"] span {
    color: #172033 !important;
}

[data-testid="stSelectbox"] label {
    color: #64748B !important;
    font-weight: 600 !important;
}

/* ---------- POLISHED BUTTONS ---------- */

.stButton > button {
    border-radius: 8px !important;
    border: 1px solid #D6E0ED !important;
    background: #FFFFFF !important;
    color: #2563EB !important;
    font-weight: 600 !important;
    min-height: 38px !important;
    transition: all 0.15s ease;
}

.stButton > button:hover {
    border-color: #2563EB !important;
    background: #F8FBFF !important;
}


/* ---------- BORDERED STREAMLIT CONTAINERS ---------- */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #FFFFFF;
    border-color: #E2E8F0 !important;
    border-radius: 12px !important;
}


/* ---------- CONSISTENT BODY TEXT ---------- */

body {
    color: #172033;
}


/* ---------- SMALL SECTION LABEL ---------- */

.eyebrow {
    color: #64748B;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

.contract-name {
    color: #172033;
    font-size: 18px;
    font-weight: 700;
}

.contract-meta {
    color: #64748B;
    font-size: 13px;
    margin-top: 5px;
}

.contract-parties {
    color: #94A3B8;
    font-size: 13px;
    margin-top: 4px;
}


div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 12px !important;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    padding: 4px !important;
}

/* Obligation cards */
div[class*="st-key-obligation_card_"] {
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 14px !important;
    padding: 18px 20px !important;
    margin-bottom: 14px !important;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05) !important;
}

/* Contract cards */
div[class*="st-key-contract_card_"] {
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 14px !important;
    padding: 18px 20px !important;
    margin-bottom: 14px !important;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05) !important;
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

    if st.button("🏠  Dashboard", key="nav_dashboard"):
        st.session_state.page = "Dashboard"
        st.rerun()

    if st.button("📄  Contracts", key="nav_contracts"):
        st.session_state.page = "Contracts"
        st.rerun()

    if st.button("✓  Obligations", key="nav_obligations"):
        st.session_state.page = "Obligations"
        st.rerun()

    if st.button("◷  Timeline", key="nav_timeline"):
        st.session_state.page = "Timeline"
        st.rerun()

    if st.button("⚠  Review", key="nav_review"):
        st.session_state.page = "Review"
        st.rerun()

    if st.button("⇄  Compare", key="nav_compare"):
        st.session_state.page = "Compare"
        st.rerun()


    if st.button("✦  Ask AI", key="nav_ask_ai"):
        st.session_state.page = "Ask AI"
        st.rerun()

    st.markdown("---")

    if st.button("＋  Add Contract", key="add_contract"):
        st.session_state.page = "Add Contract"
        st.rerun()


# ============================================================
# MAIN CONTENT
# ============================================================

if st.session_state.page == "Add Contract":

    # --------------------------------------------------------
    # PAGE HEADER
    # --------------------------------------------------------

    st.markdown(
        '<div class="page-title">Add Contract</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">Upload your contract to extract obligations, deadlines, and important clauses.</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # ADD CONTRACT PAGE
    # --------------------------------------------------------

    if st.session_state.analysis_state == "idle":

        # PRIMARY CONTRACT
        st.markdown(
            '<div class="upload-section-label">Upload your primary contract</div>',
            unsafe_allow_html=True
        )

        primary_file = st.file_uploader(
            "Drag & drop your PDF here",
            type=["pdf"],
            key="primary_contract"
        )

        if primary_file:
            st.markdown(
                f"""
                <div class="file-row">
                    <span>□</span>
                    <span>{primary_file.name}</span>
                    <span class="file-check">✓</span>
                </div>
                """,
                unsafe_allow_html=True
            )

        # RELATED DOCUMENTS
        st.markdown(
            '<div class="upload-section-label related-label">Related documents (optional)</div>',
            unsafe_allow_html=True
        )

        related_files = st.file_uploader(
            "Add related document",
            type=["pdf"],
            key="related_documents",
            accept_multiple_files=True
        )

        if related_files:
            for file in related_files:
                st.markdown(
                    f"""
                    <div class="file-row">
                        <span>□</span>
                        <span>{file.name}</span>
                        <span class="file-check">✓</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # ----------------------------------------------------
        # ACTION BUTTONS
        # ----------------------------------------------------

        action_col1, action_col2, action_col3 = st.columns([5, 1, 1])

        with action_col2:
            if st.button("Cancel", key="cancel_contract"):
                st.session_state.page = "Dashboard"
                st.session_state.analysis_state = "idle"
                st.rerun()

        with action_col3:
            analyze = st.button(
                "Analyze",
                key="analyze_contract"
            )

        if analyze:

            if primary_file is None:

                st.warning(
                    "Please upload a primary contract first."
                )

            else:

                st.session_state.analysis_state = "processing"
                st.rerun()

    # --------------------------------------------------------
    # PROCESSING STATE
    # --------------------------------------------------------

    elif st.session_state.analysis_state == "processing":

        st.html(
            """
            <div class="analysis-card">

                <div class="analysis-title">
                    Analyzing your contract...
                </div>

                <div class="analysis-step">
                    ✓ &nbsp; Reading document
                </div>

                <div class="analysis-step">
                    ✓ &nbsp; Identifying parties
                </div>

                <div class="analysis-step">
                    ● &nbsp; Extracting obligations
                </div>

                <div class="analysis-step">
                    ○ &nbsp; Finding deadlines
                </div>

                <div class="analysis-step">
                    ○ &nbsp; Checking clauses
                </div>

            </div>
            """
        )

        st.write("")

        if st.button(
            "Continue",
            key="finish_analysis"
        ):

            st.session_state.analysis_state = "complete"
            st.rerun()

    # --------------------------------------------------------
    # ANALYSIS COMPLETE
    # --------------------------------------------------------

    elif st.session_state.analysis_state == "complete":

        st.html(
            """
            <div class="analysis-card">

                <div class="analysis-title">
                    ✓ Analysis complete
                </div>

                <div class="analysis-step">
                    <strong>Acme Master Agreement</strong>
                </div>

                <div class="analysis-step">
                    Acme Corp ↔ Vendor X
                </div>

                <div class="analysis-step">
                    Effective: Jan 1, 2026
                </div>

                <div class="analysis-step">
                    Expires: Dec 31, 2026
                </div>

                <div class="analysis-step">
                    14 obligations identified
                </div>

                <div class="analysis-step">
                    3 clauses require human review
                </div>

            </div>
            """
        )

        st.write("")

        complete_col1, complete_col2 = st.columns([5, 1])

        with complete_col2:

            if st.button(
                "View Contract",
                key="view_contract"
            ):

                st.session_state.page = "Contract Overview"
                st.session_state.analysis_state = "idle"
                st.rerun()

# ============================================================
# CONTRACTS
# ============================================================

elif st.session_state.page == "Contracts":

    st.markdown(
        '<div class="page-title">Contracts</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">View and manage your uploaded contracts.</div>',
        unsafe_allow_html=True
    )

    # Search
    search = st.text_input(
        "Search contracts",
        placeholder="Search contracts...",
        key="contract_search"
    )

    st.write()

    contracts = [
        {
            "name": "Acme Master Agreement",
            "type": "Service Agreement",
            "parties": "Acme Corp ↔ Vendor X",
            "status": "Active",
        },
        {
            "name": "XYZ Vendor Agreement",
            "type": "Vendor Agreement",
            "parties": "XYZ Corp ↔ Acme Corp",
            "status": "Active",
        },
    ]

    search_term = search.strip().lower()

    filtered_contracts = []

    for contract in contracts:
        search_text = (
            contract["name"] + " " +
            contract["type"] + " " +
            contract["parties"]
        ).lower()

        if search_term in search_text:
            filtered_contracts.append(contract)


    for contract in filtered_contracts:

        with st.container(
            key=f"contract_card_{contract['name']}"
        ):

            col1, col2 = st.columns([6, 1])

            with col1:

                st.markdown(
                    f"""
                    <div style="
                        color:#172033;
                        font-size:17px;
                        font-weight:700;
                    ">
                        {contract["name"]}
                    </div>

                    <div style="
                        color:#64748B;
                        font-size:13px;
                        margin-top:5px;
                    ">
                        {contract["type"]}
                    </div>

                    <div style="
                        color:#64748B;
                        font-size:13px;
                        margin-top:4px;
                    ">
                        {contract["parties"]}
                    </div>

                    <div style="
                        display:inline-block;
                        background:#E8F8F1;
                        color:#15803D;
                        padding:4px 9px;
                        border-radius:20px;
                        font-size:11px;
                        font-weight:700;
                        margin-top:10px;
                    ">
                        {contract["status"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:

                if st.button(
                    "Open →",
                    key=f"open_{contract['name']}"
                ):
                    st.session_state.page = "Contract Overview"
                    st.rerun()


# ============================================================
# OBLIGATIONS
# ============================================================

elif st.session_state.page == "Obligations":

    st.markdown(
        '<div class="page-title">Obligations</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">Track what each party is responsible for.</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    st.markdown(
        """
        <div style="
            color:#64748B;
            font-size:14px;
            margin-bottom:22px;
        ">
            <strong style="color:#172033;">14 obligations</strong>
            &nbsp;·&nbsp;
            <strong style="color:#172033;">3 due soon</strong>
            &nbsp;·&nbsp;
            <strong style="color:#172033;">2 overdue</strong>
            &nbsp;·&nbsp;
            <strong style="color:#172033;">9 ongoing</strong>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # FILTERS
    # --------------------------------------------------------

    filter_col1, filter_col2, filter_col3 = st.columns(3)

    with filter_col1:
        contract_filter = st.selectbox(
            "Contract",
            ["All contracts", "Acme Master Agreement", "XYZ Vendor Agreement"],
            key="obligation_contract_filter"
        )

    with filter_col2:
        party_filter = st.selectbox(
            "Responsible party",
            ["All parties", "Acme Corp", "Vendor X", "XYZ Corp"],
            key="obligation_party_filter"
        )

    with filter_col3:
        status_filter = st.selectbox(
            "Status",
            ["All status", "Upcoming", "Due Soon", "Overdue", "Ongoing"],
            key="obligation_status_filter"
        )

    st.write("")

    # --------------------------------------------------------
    # MOCK OBLIGATIONS
    # --------------------------------------------------------

    obligations = [
        {
            "obligation": "Maintain 99.9% service uptime",
            "party": "Vendor X",
            "timing": "Continuous",
            "status": "Ongoing",
            "contract": "Acme Master Agreement",
            "section": "§7.2 — Service Levels",
            "page": "Page 14",
        },
        {
            "obligation": "Submit monthly usage report",
            "party": "Acme Corp",
            "timing": "Due 5th every month",
            "status": "Due Soon",
            "contract": "Acme Master Agreement",
            "section": "§9.1 — Reporting",
            "page": "Page 16",
        },
        {
            "obligation": "Provide incident response within 24 hours",
            "party": "Vendor X",
            "timing": "Within 24 hours of an incident",
            "status": "Ongoing",
            "contract": "Acme Master Agreement",
            "section": "§8.3 — Incident Response",
            "page": "Page 15",
        },
        {
            "obligation": "Pay outstanding invoice",
            "party": "XYZ Corp",
            "timing": "Due Sep 20, 2026",
            "status": "Overdue",
            "contract": "XYZ Vendor Agreement",
            "section": "§6.1 — Payment Terms",
            "page": "Page 9",
        },
    ]

    # --------------------------------------------------------
    # FILTER + DISPLAY
    # --------------------------------------------------------

    for item in obligations:

        if (
            contract_filter != "All contracts"
            and item["contract"] != contract_filter
        ):
            continue

        if (
            party_filter != "All parties"
            and item["party"] != party_filter
        ):
            continue

        if (
            status_filter != "All status"
            and item["status"] != status_filter
        ):
            continue

        with st.container(
            key=f"obligation_card_{item['obligation']}"
        ):

            col1, col2 = st.columns([5, 1])

            with col1:

                st.markdown(
                    f"""
                    <div style="
                        color:#172033;
                        font-size:16px;
                        font-weight:700;
                    ">
                        {item["obligation"]}
                    </div>

                    <div style="
                        color:#64748B;
                        font-size:13px;
                        margin-top:7px;
                    ">
                        {item["party"]} · {item["timing"]}
                    </div>

                    <div style="
                        color:#94A3B8;
                        font-size:12px;
                        margin-top:5px;
                    ">
                        {item["contract"]}
                    </div>

                    <div style="
                        display:inline-block;
                        background:{
                            '#EFF6FF' if item['status'] == 'Ongoing'
                            else '#FFF7ED' if item['status'] == 'Due Soon'
                            else '#FEF2F2' if item['status'] == 'Overdue'
                            else '#F1F5F9'
                        };
                        color:{
                            '#2563EB' if item['status'] == 'Ongoing'
                            else '#C2410C' if item['status'] == 'Due Soon'
                            else '#B91C1C' if item['status'] == 'Overdue'
                            else '#475569'
                        };
                        padding:4px 9px;
                        border-radius:20px;
                        font-size:11px;
                        font-weight:700;
                        margin-top:10px;
                    ">
                        {item["status"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:

                if st.button(
                    "View Source",
                    key=f"obligation_source_{item['obligation']}"
                ):
                    st.session_state.obligation_source = item
                    st.rerun()

    # --------------------------------------------------------
    # SOURCE
    # --------------------------------------------------------

    if st.session_state.get("obligation_source") is not None:

        source = st.session_state.obligation_source

        st.html(
    f"""
    <div style="
        background:#FFFFFF;
        border:1px solid #DFE7F2;
        border-radius:12px;
        padding:20px;
        margin-top:20px;
    ">
        <div style="
            color:#2563EB;
            font-size:12px;
            font-weight:700;
        ">
            SOURCE
        </div>

        <div style="
            color:#172033;
            font-size:15px;
            font-weight:700;
            margin-top:6px;
        ">
            {source["contract"]}
        </div>

        <div style="
            color:#64748B;
            font-size:12px;
            margin-top:5px;
        ">
            {source["section"]} · {source["page"]}
        </div>

        <div style="
            color:#475569;
            font-size:14px;
            line-height:1.7;
            margin-top:15px;
        ">
            Supporting clause for:
            <strong>{source["obligation"]}</strong>
        </div>
    </div>
    """
)

        if st.button("Close Source", key="close_obligation_source"):
            del st.session_state.obligation_source
            st.rerun()

# ============================================================
# TIMELINE
# ============================================================

elif st.session_state.page == "Timeline":

    st.markdown(
        '<div class="page-title">Timeline</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">See upcoming contractual deadlines and important events.</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # FILTERS
    # --------------------------------------------------------

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:
        timeline_contract = st.selectbox(
            "Contract",
            [
                "All contracts",
                "Acme Master Agreement",
                "XYZ Vendor Agreement"
            ],
            key="timeline_contract_filter"
        )

    with filter_col2:
        timeline_period = st.selectbox(
            "Period",
            [
                "This month",
                "Next 3 months",
                "All upcoming"
            ],
            key="timeline_period_filter"
        )

    st.write("")

    # --------------------------------------------------------
    # MOCK TIMELINE DATA
    # --------------------------------------------------------

    timeline_events = [
        {
            "date": "Sep 20, 2026",
            "title": "Pay outstanding invoice",
            "party": "XYZ Corp",
            "contract": "XYZ Vendor Agreement",
            "status": "Overdue",
            "section": "§6.1 — Payment Terms",
            "page": "Page 9",
        },
        {
            "date": "Sep 22, 2026",
            "title": "Submit monthly usage report",
            "party": "Acme Corp",
            "contract": "Acme Master Agreement",
            "status": "Due Soon",
            "section": "§9.1 — Reporting",
            "page": "Page 16",
        },
        {
            "date": "Sep 28, 2026",
            "title": "Renewal notice deadline",
            "party": "Acme Corp / Vendor X",
            "contract": "Acme Master Agreement",
            "status": "Upcoming",
            "section": "§12.1 — Renewal",
            "page": "Page 18",
        },
        {
            "date": "Dec 31, 2026",
            "title": "Contract expiration",
            "party": "Acme Corp / Vendor X",
            "contract": "Acme Master Agreement",
            "status": "Upcoming",
            "section": "§12.1 — Renewal",
            "page": "Page 18",
        },
    ]

    # --------------------------------------------------------
    # UPCOMING
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="section-title" style="margin-top:10px;">
            UPCOMING
        </div>
        """,
        unsafe_allow_html=True
    )

    for event in timeline_events:

        if (
            timeline_contract != "All contracts"
            and event["contract"] != timeline_contract
        ):
            continue

        with st.container(border=True):

            col1, col2, col3 = st.columns([1.5, 5, 1])

            with col1:
                st.markdown(
                    f"""
                    <div style="
                        color:#17345F;
                        font-size:14px;
                        font-weight:700;
                        padding-top:5px;
                    ">
                        {event["date"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:
                st.markdown(
                    f"""
                    <div style="
                        color:#172033;
                        font-size:15px;
                        font-weight:700;
                    ">
                        {event["title"]}
                    </div>

                    <div style="
                        color:#64748B;
                        font-size:13px;
                        margin-top:5px;
                    ">
                        {event["party"]} · {event["contract"]}
                    </div>

                    <div style="
                        display:inline-block;
                        background:#F1F5F9;
                        color:#475569;
                        padding:4px 9px;
                        border-radius:20px;
                        font-size:11px;
                        font-weight:700;
                        margin-top:9px;
                    ">
                        {event["status"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col3:
                if st.button(
                    "View",
                    key=f"timeline_{event['title']}"
                ):
                    st.session_state.timeline_event = event
                    st.rerun()

    # --------------------------------------------------------
    # EVENT DETAILS
    # --------------------------------------------------------

    if st.session_state.timeline_event is not None:

        event = st.session_state.timeline_event

        st.html(
    f"""
    <div style="
        background:#FFFFFF;
        border:1px solid #DFE7F2;
        border-radius:12px;
        padding:20px;
        margin-top:20px;
    ">
        <div style="
            color:#2563EB;
            font-size:12px;
            font-weight:700;
        ">
            EVENT DETAILS
        </div>

        <div style="
            color:#172033;
            font-size:17px;
            font-weight:700;
            margin-top:8px;
        ">
            {event["title"]}
        </div>

        <div style="
            color:#64748B;
            font-size:13px;
            margin-top:7px;
        ">
            {event["date"]} · {event["status"]}
        </div>

        <div style="
            color:#64748B;
            font-size:13px;
            margin-top:5px;
        ">
            {event["party"]} · {event["contract"]}
        </div>

        <div style="
            color:#475569;
            font-size:13px;
            margin-top:15px;
        ">
            Source: {event["section"]} · {event["page"]}
        </div>
    </div>
    """
)

        if st.button("Close", key="close_timeline_event"):
            st.session_state.timeline_event = None
            st.rerun()


# ============================================================
# REVIEW
# ============================================================

elif st.session_state.page == "Review":

    st.markdown(
        '<div class="page-title">Review</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">Contract clauses that deserve human attention.</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    st.markdown(
        """
        <div style="
            color:#64748B;
            font-size:14px;
            margin-bottom:22px;
        ">
            <strong style="color:#172033;">3 clauses require attention</strong>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # FILTER
    # --------------------------------------------------------

    review_contract = st.selectbox(
        "Contract",
        [
            "All contracts",
            "Acme Master Agreement",
            "XYZ Vendor Agreement"
        ],
        key="review_contract_filter"
    )

    st.write("")

    # --------------------------------------------------------
    # MOCK REVIEW ITEMS
    # --------------------------------------------------------

    review_items = [
        {
            "title": "Termination clause",
            "contract": "Acme Master Agreement",
            "section": "§12.2 — Termination",
            "page": "Page 19",
            "reason": "Notice period requires human attention.",
            "source_text": "Either party may terminate this agreement by providing written notice at least sixty (60) days prior to termination."
        },
        {
            "title": "Payment penalty clause",
            "contract": "XYZ Vendor Agreement",
            "section": "§6.4 — Late Payment",
            "page": "Page 11",
            "reason": "Additional penalty applies after the payment deadline.",
            "source_text": "A late payment penalty may apply to amounts remaining unpaid after the applicable payment deadline."
        },
        {
            "title": "Auto-renewal clause",
            "contract": "Acme Master Agreement",
            "section": "§12.1 — Renewal",
            "page": "Page 18",
            "reason": "Automatic renewal requires advance notice.",
            "source_text": "The agreement shall automatically renew unless either party provides written notice of non-renewal at least sixty (60) days prior to expiration."
        },
    ]

    # --------------------------------------------------------
    # REVIEW CARDS
    # --------------------------------------------------------

    for item in review_items:

        if (
            review_contract != "All contracts"
            and item["contract"] != review_contract
        ):
            continue

        with st.container(border=True):

            col1, col2 = st.columns([5, 1])

            with col1:

                st.markdown(
                    f"""
                    <div style="
                        color:#172033;
                        font-size:16px;
                        font-weight:700;
                    ">
                        {item["title"]}
                    </div>

                    <div style="
                        color:#64748B;
                        font-size:13px;
                        margin-top:6px;
                    ">
                        {item["contract"]} · {item["section"]}
                    </div>

                    <div style="
                        color:#B45309;
                        font-size:13px;
                        margin-top:9px;
                    ">
                        Human review recommended
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:

                if st.button(
                    "View →",
                    key=f"review_view_{item['title']}"
                ):
                    st.session_state.review_item = item
                    st.rerun()

    # --------------------------------------------------------
    # REVIEW DETAILS
    # --------------------------------------------------------

    if st.session_state.review_item is not None:

        item = st.session_state.review_item

        st.html(
            f"""
            <div style="
                background:#FFFFFF;
                border:1px solid #DFE7F2;
                border-radius:12px;
                padding:20px;
                margin-top:20px;
            ">

                <div style="
                    color:#2563EB;
                    font-size:12px;
                    font-weight:700;
                ">
                    REVIEW DETAILS
                </div>

                <div style="
                    color:#172033;
                    font-size:17px;
                    font-weight:700;
                    margin-top:8px;
                ">
                    {item["title"]}
                </div>

                <div style="
                    color:#64748B;
                    font-size:13px;
                    margin-top:6px;
                ">
                    {item["contract"]} · {item["section"]} · {item["page"]}
                </div>

                <div style="
                    color:#172033;
                    font-size:14px;
                    font-weight:600;
                    margin-top:18px;
                ">
                    Why this needs attention
                </div>

                <div style="
                    color:#64748B;
                    font-size:14px;
                    line-height:1.6;
                    margin-top:6px;
                ">
                    {item["reason"]}
                </div>

                <div style="
                    color:#172033;
                    font-size:14px;
                    font-weight:600;
                    margin-top:18px;
                ">
                    Source
                </div>

                <div style="
                    color:#475569;
                    font-size:14px;
                    line-height:1.7;
                    margin-top:6px;
                ">
                    "{item["source_text"]}"
                </div>

            </div>
            """
        )

        if st.button("Close", key="close_review_item"):
            st.session_state.review_item = None
            st.rerun()

# ============================================================
# COMPARE
# ============================================================

elif st.session_state.page == "Compare":

    st.markdown(
        '<div class="page-title">Compare</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">Compare two versions of a contract and identify what changed.</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # CONTRACT SELECTOR
    # --------------------------------------------------------

    contract_compare = st.selectbox(
        "Contract",
        [
            "Acme Master Agreement",
            "XYZ Vendor Agreement"
        ],
        key="compare_contract"
    )

    st.write("")

    # --------------------------------------------------------
    # VERSION UPLOADS
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="upload-section-label">
                Version 1
            </div>
            """,
            unsafe_allow_html=True
        )

        version_1 = st.file_uploader(
            "Upload Version 1",
            type=["pdf"],
            key="compare_version_1"
        )

        if version_1:

            st.markdown(
                f"""
                <div class="file-row">
                    <span>□</span>
                    <span>{version_1.name}</span>
                    <span class="file-check">✓</span>
                </div>
                """,
                unsafe_allow_html=True
            )

    with col2:

        st.markdown(
            """
            <div class="upload-section-label">
                Version 2
            </div>
            """,
            unsafe_allow_html=True
        )

        version_2 = st.file_uploader(
            "Upload Version 2",
            type=["pdf"],
            key="compare_version_2"
        )

        if version_2:

            st.markdown(
                f"""
                <div class="file-row">
                    <span>□</span>
                    <span>{version_2.name}</span>
                    <span class="file-check">✓</span>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.write("")

    # --------------------------------------------------------
    # COMPARE BUTTON
    # --------------------------------------------------------

    if st.button("Compare", key="run_compare"):

        if version_1 is None or version_2 is None:

            st.warning(
                "Please upload both contract versions first."
            )

        else:

            st.session_state.compare_result = True
            st.session_state.compare_source = None
            st.rerun()

    # --------------------------------------------------------
    # COMPARISON RESULTS
    # --------------------------------------------------------

    if st.session_state.compare_result:

        st.markdown(
            """
            <div style="
                margin-top:30px;
                color:#172033;
                font-size:18px;
                font-weight:700;
            ">
                3 changes found
            </div>
            """,
            unsafe_allow_html=True
        )

        changes = [
            {
                "term": "Payment Terms",
                "old": "Net 45 days",
                "new": "Net 30 days",
                "explanation": "Payment is now due 15 days earlier.",
                "section": "§6.1 — Payment Terms",
            },
            {
                "term": "Termination Notice",
                "old": "30 days written notice",
                "new": "60 days written notice",
                "explanation": "The required notice period has increased.",
                "section": "§12.2 — Termination",
            },
            {
                "term": "Service Level",
                "old": "99.5% uptime",
                "new": "99.9% uptime",
                "explanation": "The required service uptime has increased.",
                "section": "§7.2 — Service Levels",
            },
        ]

        for index, change in enumerate(changes):

            with st.container(border=True):

                st.markdown(
                    f"""
                    <div style="
                        color:#172033;
                        font-size:16px;
                        font-weight:700;
                    ">
                        {change["term"]}
                    </div>

                    <div style="
                        color:#64748B;
                        font-size:12px;
                        margin-top:5px;
                    ">
                        {change["section"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                value_col1, value_col2 = st.columns(2)

                with value_col1:

                    st.html(
                        f"""
                        <div style="
                            background:#F8FAFC;
                            border:1px solid #E2E8F0;
                            border-radius:8px;
                            padding:13px;
                            margin-top:14px;
                        ">
                            <div style="
                                color:#94A3B8;
                                font-size:11px;
                                font-weight:700;
                            ">
                                VERSION 1
                            </div>

                            <div style="
                                color:#172033;
                                font-size:14px;
                                font-weight:600;
                                margin-top:6px;
                            ">
                                {change["old"]}
                            </div>
                        </div>
                        """
                    )

                with value_col2:

                    st.html(
                        f"""
                        <div style="
                            background:#F8FAFC;
                            border:1px solid #E2E8F0;
                            border-radius:8px;
                            padding:13px;
                            margin-top:14px;
                        ">
                            <div style="
                                color:#94A3B8;
                                font-size:11px;
                                font-weight:700;
                            ">
                                VERSION 2
                            </div>

                            <div style="
                                color:#172033;
                                font-size:14px;
                                font-weight:600;
                                margin-top:6px;
                            ">
                                {change["new"]}
                            </div>
                        </div>
                        """
                    )

                st.markdown(
                    f"""
                    <div style="
                        color:#64748B;
                        font-size:13px;
                        margin-top:12px;
                    ">
                        {change["explanation"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    "View Source",
                    key=f"compare_source_{index}"
                ):

                    st.session_state.compare_source = change
                    st.rerun()

        # ----------------------------------------------------
        # SOURCE
        # ----------------------------------------------------

        if st.session_state.compare_source is not None:

            source = st.session_state.compare_source

            st.html(
                f"""
                <div style="
                    background:#FFFFFF;
                    border:1px solid #DFE7F2;
                    border-radius:12px;
                    padding:20px;
                    margin-top:20px;
                ">

                    <div style="
                        color:#2563EB;
                        font-size:12px;
                        font-weight:700;
                    ">
                        SOURCE
                    </div>

                    <div style="
                        color:#172033;
                        font-size:15px;
                        font-weight:700;
                        margin-top:6px;
                    ">
                        {contract_compare}
                    </div>

                    <div style="
                        color:#64748B;
                        font-size:12px;
                        margin-top:5px;
                    ">
                        {source["section"]}
                    </div>

                    <div style="
                        color:#475569;
                        font-size:14px;
                        line-height:1.7;
                        margin-top:15px;
                    ">
                        Version 1: <strong>{source["old"]}</strong>
                        <br><br>
                        Version 2: <strong>{source["new"]}</strong>
                    </div>

                </div>
                """,
            )

            if st.button(
                "Close Source",
                key="close_compare_source"
            ):

                st.session_state.compare_source = None
                st.rerun()

# ============================================================
# ASK AI
# ============================================================

elif st.session_state.page == "Ask AI":

    st.markdown(
        '<div class="page-title">Ask AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">Ask questions about your contracts.</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # CONTRACT SELECTOR
    # --------------------------------------------------------

    contract_qa = st.selectbox(
        "Contract",
        [
            "Acme Master Agreement",
            "XYZ Vendor Agreement"
        ],
        key="qa_contract"
    )

    st.write("")

    # --------------------------------------------------------
    # EXAMPLE QUESTIONS
    # --------------------------------------------------------

    st.markdown(
        """
        <div style="
            color:#64748B;
            font-size:13px;
            font-weight:600;
            margin-bottom:10px;
        ">
            Try asking
        </div>
        """,
        unsafe_allow_html=True
    )

    example_col1, example_col2, example_col3 = st.columns(3)

    with example_col1:
        if st.button(
            "When does this contract expire?",
            key="qa_example_expiry"
        ):
            st.session_state.qa_messages.append(
                {
                    "role": "user",
                    "text": "When does this contract expire?"
                }
            )
            st.session_state.qa_messages.append(
                {
                    "role": "assistant",
                    "text": "The contract expires on December 31, 2026.",
                    "source": "§12.1 — Term · Page 18"
                }
            )
            st.rerun()

    with example_col2:
        if st.button(
            "What are the payment terms?",
            key="qa_example_payment"
        ):
            st.session_state.qa_messages.append(
                {
                    "role": "user",
                    "text": "What are the payment terms?"
                }
            )
            st.session_state.qa_messages.append(
                {
                    "role": "assistant",
                    "text": "Payment is due within 30 days of receiving an invoice.",
                    "source": "§6.1 — Payment Terms · Page 9"
                }
            )
            st.rerun()

    with example_col3:
        if st.button(
            "What must the vendor do?",
            key="qa_example_vendor"
        ):
            st.session_state.qa_messages.append(
                {
                    "role": "user",
                    "text": "What must the vendor do?"
                }
            )
            st.session_state.qa_messages.append(
                {
                    "role": "assistant",
                    "text": "The vendor must maintain the required service level and provide incident response within 24 hours.",
                    "source": "§7.2 — Service Levels · Page 14"
                }
            )
            st.rerun()

    st.write("")

    # --------------------------------------------------------
    # CONVERSATION
    # --------------------------------------------------------

    for index, message in enumerate(st.session_state.qa_messages):

        if message["role"] == "user":

            st.html(
                f"""
                <div style="
                    background:#EAF2FF;
                    border-radius:12px;
                    padding:13px 16px;
                    margin-top:14px;
                    margin-left:15%;
                    color:#172033;
                    font-size:14px;
                ">
                    <strong>You</strong>
                    <div style="margin-top:6px;">
                        {message["text"]}
                    </div>
                </div>
                """
            )

        else:

            st.html(
                f"""
                <div style="
                    background:#FFFFFF;
                    border:1px solid #DFE7F2;
                    border-radius:12px;
                    padding:16px;
                    margin-top:12px;
                    margin-right:10%;
                ">
                    <div style="
                        color:#2563EB;
                        font-size:12px;
                        font-weight:700;
                    ">
                        CONTRACTLENS
                    </div>

                    <div style="
                        color:#172033;
                        font-size:14px;
                        line-height:1.7;
                        margin-top:7px;
                    ">
                        {message["text"]}
                    </div>

                    <div style="
                        color:#64748B;
                        font-size:12px;
                        margin-top:12px;
                    ">
                        Source: {message["source"]}
                    </div>
                </div>
                """
            )

            if st.button(
                "View Source",
                key=f"qa_source_{index}"
            ):
                st.session_state.qa_source = message
                st.rerun()

    # --------------------------------------------------------
    # SOURCE
    # --------------------------------------------------------

    if st.session_state.qa_source is not None:

        source = st.session_state.qa_source

        st.html(
            f"""
            <div style="
                background:#FFFFFF;
                border:1px solid #DFE7F2;
                border-radius:12px;
                padding:20px;
                margin-top:20px;
            ">

                <div style="
                    color:#2563EB;
                    font-size:12px;
                    font-weight:700;
                ">
                    SOURCE
                </div>

                <div style="
                    color:#172033;
                    font-size:15px;
                    font-weight:700;
                    margin-top:6px;
                ">
                    {contract_qa}
                </div>

                <div style="
                    color:#64748B;
                    font-size:12px;
                    margin-top:5px;
                ">
                    {source["source"]}
                </div>

                <div style="
                    color:#475569;
                    font-size:14px;
                    line-height:1.7;
                    margin-top:15px;
                ">
                    Supporting contract content used for this answer.
                </div>

            </div>
            """
        )

        if st.button(
            "Close Source",
            key="close_qa_source"
        ):
            st.session_state.qa_source = None
            st.rerun()

    # --------------------------------------------------------
    # QUESTION INPUT
    # --------------------------------------------------------

    question = st.text_input(
        "Ask a question",
        placeholder="e.g. What are the vendor's obligations?",
        key="qa_question"
    )

    if st.button("Ask →", key="ask_question"):

        if question.strip():

            st.session_state.qa_messages.append(
                {
                    "role": "user",
                    "text": question
                }
            )

            # Mock answer for frontend testing
            st.session_state.qa_messages.append(
                {
                    "role": "assistant",
                    "text": "Based on the contract, the relevant obligation is described in the service and incident response provisions.",
                    "source": "§7.2 — Service Levels · Page 14"
                }
            )

            st.rerun()


# ============================================================
# CONTRACT OVERVIEW PLACEHOLDER
# ============================================================

elif st.session_state.page == "Contract Overview":

    # --------------------------------------------------------
    # BACK BUTTON
    # --------------------------------------------------------

    if st.button("←  Contracts", key="back_contracts"):
        st.session_state.page = "Contracts"
        st.rerun()

    st.markdown(
        '<div class="page-title">Acme Master Agreement</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">Service Agreement · Acme Corp ↔ Vendor X</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # CONTRACT HEADER
    # --------------------------------------------------------

    header_col1, header_col2 = st.columns([5, 1])

    with header_col1:
        st.markdown(
            """
            <div style="
                color:#64748B;
                font-size:13px;
                margin-top:5px;
            ">
                Contract status
                <span style="
                    background:#E8F8F1;
                    color:#15803D;
                    padding:5px 10px;
                    border-radius:20px;
                    font-size:11px;
                    font-weight:700;
                    margin-left:8px;
                ">
                    Active
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with header_col2:
        if st.button(
            "View Source",
            key="overview_source"
        ):
            st.session_state.show_source = True
            st.rerun()

    # --------------------------------------------------------
    # CONTRACT DETAILS
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="section-title" style="margin-top:30px;">
            CONTRACT DETAILS
        </div>
        """,
        unsafe_allow_html=True
    )

    detail_col1, detail_col2 = st.columns(2)

    with detail_col1:

        st.markdown(
            """
            <div class="metric-card" style="margin-bottom:15px;">
                <div class="metric-label">Parties</div>
                <div style="
                    color:#172033;
                    font-size:15px;
                    font-weight:600;
                    margin-top:8px;
                ">
                    Acme Corp ↔ Vendor X
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="metric-card" style="margin-bottom:15px;">
                <div class="metric-label">Effective Date</div>
                <div style="
                    color:#172033;
                    font-size:15px;
                    font-weight:600;
                    margin-top:8px;
                ">
                    Jan 1, 2026
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">Renewal</div>
                <div style="
                    color:#172033;
                    font-size:15px;
                    font-weight:600;
                    margin-top:8px;
                ">
                    Automatically renews annually
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with detail_col2:

        st.markdown(
            """
            <div class="metric-card" style="margin-bottom:15px;">
                <div class="metric-label">Contract Type</div>
                <div style="
                    color:#172033;
                    font-size:15px;
                    font-weight:600;
                    margin-top:8px;
                ">
                    Service Agreement
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="metric-card" style="margin-bottom:15px;">
                <div class="metric-label">Expiration Date</div>
                <div style="
                    color:#172033;
                    font-size:15px;
                    font-weight:600;
                    margin-top:8px;
                ">
                    Dec 31, 2026
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">Termination</div>
                <div style="
                    color:#172033;
                    font-size:15px;
                    font-weight:600;
                    margin-top:8px;
                ">
                    60 days written notice
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # SOURCE
    # --------------------------------------------------------

    if st.session_state.show_source:

        st.html(
            """
            <div style="
                background:#FFFFFF;
                border:1px solid #DFE7F2;
                border-radius:12px;
                padding:20px;
                margin-top:20px;
            ">
                <div style="
                    color:#2563EB;
                    font-size:12px;
                    font-weight:700;
                    margin-bottom:6px;
                ">
                    SOURCE
                </div>

                <div style="
                    color:#172033;
                    font-size:15px;
                    font-weight:700;
                ">
                    Acme Master Agreement
                </div>

                <div style="
                    color:#64748B;
                    font-size:12px;
                    margin-top:5px;
                ">
                    §12.1 — Renewal · Page 18
                </div>

                <div style="
                    color:#475569;
                    font-size:14px;
                    line-height:1.7;
                    margin-top:15px;
                ">
                    "The agreement shall automatically renew for successive
                    one-year periods unless either party provides written
                    notice of non-renewal at least sixty (60) days prior
                    to the expiration date."
                </div>
            </div>
            """,
        )

        if st.button("Close Source", key="close_overview_source"):
            st.session_state.show_source = False
            st.rerun()

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="section-title" style="margin-top:32px;">
            SUMMARY
        </div>

        <div style="
            background:#FFFFFF;
            border:1px solid #DFE7F2;
            border-radius:12px;
            padding:20px;
            color:#64748B;
            font-size:14px;
            line-height:1.7;
        ">
            This agreement governs the services provided by Vendor X
            to Acme Corp, including service levels, reporting obligations,
            payment terms, and termination conditions.
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # NEEDS ATTENTION
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="section-title" style="margin-top:32px;">
            NEEDS ATTENTION
        </div>
        """,
        unsafe_allow_html=True
    )

    attention_col1, attention_col2 = st.columns(2)

    with attention_col1:
        st.markdown(
            """
            <div class="attention-card yellow-card">
                <div class="attention-title">
                    3 clauses require attention
                </div>
                <div class="attention-text">
                    Review flagged contract sections.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with attention_col2:
        st.markdown(
            """
            <div class="attention-card blue-card">
                <div class="attention-title">
                    Renewal notice deadline
                </div>
                <div class="attention-text">
                    Sep 28, 2026
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    obligation_col1, obligation_col2 = st.columns([5, 1])

    with obligation_col1:
        st.markdown(
            """
            <div style="
                color:#64748B;
                font-size:14px;
                padding-top:10px;
            ">
                <strong style="color:#172033;">14 obligations</strong>
                identified in this contract.
            </div>
            """,
            unsafe_allow_html=True
        )

    with obligation_col2:
        if st.button(
            "View Obligations",
            key="overview_obligations"
        ):
            st.session_state.page = "Obligations"
            st.rerun()


# ============================================================
# DASHBOARD
# ============================================================

else:

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

if st.session_state.page == "Dashboard":
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


st.markdown(
    '<div style="height:18px;"></div>',
    unsafe_allow_html=True
)
# ============================================================
# NEEDS ATTENTION
# ============================================================

if st.session_state.page == "Dashboard":
    # ---------- NEEDS ATTENTION ----------
    st.markdown(
    """
    <div style="
        color:#172033;
        font-size:22px;
        font-weight:700;
        margin-top:10px;
        margin-bottom:18px;
    ">
        Needs Attention
    </div>
    """,
    unsafe_allow_html=True
)

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

    st.markdown(
    '<div style="height:24px;"></div>',
    unsafe_allow_html=True
)

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

        for index, item in enumerate(upcoming):

            if index > 0:
                st.markdown(
                    '<div style="height:14px;"></div>',
                    unsafe_allow_html=True
                )

            col1, col2, col3 = st.columns([1, 6, 1], vertical_alignment="center")

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
                if st.button(
                    "View",
                    key=f"upcoming_{item['title']}"
                ):
                    st.session_state.dashboard_source = item
                    st.rerun()

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

        for index, item in enumerate(reviews):

            if index > 0:
                st.markdown(
                    '<div style="height:14px;"></div>',
                    unsafe_allow_html=True
                )

            col1, col2 = st.columns([7, 1], vertical_alignment="center")
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
                if st.button(
                    "View",
                    key=f"review_{item['title']}"
                ):
                    st.session_state.dashboard_source = item
                    st.rerun()


    # ============================================================
# DASHBOARD SOURCE
# ============================================================

if st.session_state.dashboard_source is not None:

    source = st.session_state.dashboard_source

    st.html(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #DFE7F2;
            border-radius:12px;
            padding:20px;
            margin-top:20px;
        ">

            <div style="
                color:#2563EB;
                font-size:12px;
                font-weight:700;
            ">
                SOURCE
            </div>

            <div style="
                color:#172033;
                font-size:15px;
                font-weight:700;
                margin-top:6px;
            ">
                Acme Master Agreement
            </div>

            <div style="
                color:#64748B;
                font-size:12px;
                margin-top:5px;
            ">
                §12.1 — Renewal · Page 18
            </div>

            <div style="
                color:#475569;
                font-size:14px;
                line-height:1.7;
                margin-top:15px;
            ">
                Supporting contract content for:
                <strong>{source["title"]}</strong>
            </div>

        </div>
        """
    )

    if st.button(
        "Close Source",
        key="close_dashboard_source"
    ):
        st.session_state.dashboard_source = None
        st.rerun()
# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer-text">ContractLens helps teams understand and keep track of contractual commitments.</div>',
    unsafe_allow_html=True
)