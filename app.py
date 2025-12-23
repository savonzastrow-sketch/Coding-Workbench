import streamlit as st

# --- UI CONFIG & MOBILE-FIRST STYLING ---
st.set_page_config(layout="centered", page_title="Python Workbench")

st.markdown("""
    <style>
    /* Oversized Tab Navigation (36px) */
    button[data-baseweb="tab"] {
        font-size: 36px !important;
        font-weight: bold !important;
    }
    /* Clean Flexbox Rows for Output */
    .output-container {
        display: flex;
        justify-content:间-between;
        align-items: center;
        padding: 10px;
        background-color: #f0f2f6;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- WORKBENCH CONTENT (Your Library) ---
# You can add new snippets here via the GitHub UI
lessons = [
    {
        "title": "🏷️ Variables",
        "code": "result = f'Hello {user_input}!'",
        "logic_id": "vars"
    },
    {
        "title": "🔢 Math",
        "code": "result = float(user_input) * 10",
        "logic_id": "math"
    }
]

# --- MAIN APP VIEW ---
st.title("🚀 Python Workbench")

# Create tabs dynamically from our 'lessons' list
tab_list = st.tabs([l["title"] for l in lessons])

for i, tab in enumerate(tab_list):
    with tab:
        lesson = lessons[i]
        
        # 1. INPUT SECTION
        st.subheader("📥 Input")
        user_val = st.text_input("Enter test data:", key=f"in_{lesson['logic_id']}")
        
        # 2. OUTPUT SECTION
        st.subheader("📤 Output")
        if user_val:
            try:
                # Logic execution based on the logic_id
                if lesson['logic_id'] == "vars":
                    output = f"Hello {user_val}!"
                elif lesson['logic_id'] == "math":
                    output = float(user_val) * 10
                
                st.success(f"**Result:** {output}")
            except Exception as e:
                st.error(f"Error executing logic: {e}")
        else:
            st.info("Waiting for input...")

        # 3. DISPLAY CODE SECTION
        st.divider()
        st.subheader("📜 The Code")
        st.code(lesson['code'], language='python')
