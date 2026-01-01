import streamlit as st

# --- UI CONFIG & MOBILE-FIRST STYLING ---
st.set_page_config(layout="centered", page_title="Python Workbench")

st.markdown("""
    <style>
    /* Oversized Tab Navigation (36px) for mobile-first thumb navigation */
    button[data-baseweb="tab"] {
        font-size: 36px !important;
        font-weight: bold !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- WORKBENCH CONTENT (Your Library) ---
# 'code' is now the ONLY place you need to write your logic.
# Use 'x' to represent the user's input value.
lessons = [
    {
        "title": "🏷️ Variables",
        "code": "output = f'Hi {x}!'",
        "logic_id": "vars",
        "label": "Enter your name:"
    },
    {
        "title": "🔢 Math",
        "code": "output = f'In Fahrenheit that is {9/5 * float(x) + 32}'",
        "logic_id": "math",
        "label": "Enter temperature in Celsius:"
    },
    {
        "title": "🧪 Eval Lab",
        "code": "output = eval(x)",
        "logic_id": "eval",
        "label": "Enter any Python expression (e.g. 10 + 5):"
    }
]

# --- MAIN APP VIEW ---
st.title("🚀 Python Workbench")

# Create tabs dynamically from our 'lessons' list
tab_names = [l["title"] for l in lessons]
tab_list = st.tabs(tab_names)

for i, tab in enumerate(tab_list):
    with tab:
        lesson = lessons[i]
        
        # 1. INPUT SECTION
        st.subheader("📥 Input")
        user_val = st.text_input(lesson['label'], key=f"in_{lesson['logic_id']}")
        
        # 2. OUTPUT SECTION
        st.subheader("📤 Output")
        if user_val:
            try:
                # Setup the environment for the code to run
                # We map 'x' to the user's input
                local_vars = {'x': user_val, 'float': float, 'eval': eval}
                
                # Execute the code string from the dictionary
                exec(lesson['code'], {}, local_vars)
                
                # Retrieve the 'output' variable defined inside the code string
                st.success(f"**Result:** {local_vars.get('output', 'No output defined')}")
                
            except Exception as e:
                st.error(f"Error executing logic: {e}")
        else:
            st.info("Waiting for input...")

        # 3. DISPLAY CODE SECTION
        # This now pulls from the exact same string used in the execution above
        st.divider()
        st.subheader("📜 The Code")
        st.code(lesson['code'], language='python')
