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
    </style>
""", unsafe_allow_html=True)

# --- WORKBENCH CONTENT ---
categories = [
    {
        "category_name": "📝 Strings",
        "logic_id": "strings",
        "content": [
            {"title": "🏷️ Basic Greeting", "description": "This code demonstrates a simple text string", "label": "Enter your name:", "code": "output = f'Hi {x}!'"},
            {"title": "🔠 Uppercase", "description": "This code converts text to upper case", "label": "Enter text:", "code": "output = x.upper()"}
        ]
    },
    {
        "category_name": "🔢 Math",
        "logic_id": "math_cat",
        "content": [
            {"title": "🌡️ Celsius to F", "description": "This code converts an entered Celsius value to Fahrenheit.", "label": "Enter Celsius:", "code": "output = f'{9/5 * float(x) + 32} °F'"},
            {"title": "🧪 Eval Lab", "description": "This code runs simple python funtios", "label": "Enter expression:", "code": "output = eval(x)"},
            {"title": "2️⃣ x^2", "description": "This code calculates the square of a value 2", "label": "Enter a value:", "code": "output = f'The square of {x} is {float(x) * float(x)}.'"}
        ]
    }
]

st.title("🚀 Python Workbench")

tab_names = [c["category_name"] for c in categories]
tab_list = st.tabs(tab_names)

for i, tab in enumerate(tab_list):
    with tab:
        category = categories[i]
        lesson_titles = [item["title"] for item in category["content"]]
        selected_title = st.selectbox("Choose a lesson:", lesson_titles, key=f"sel_{category['logic_id']}")
        
        lesson = next(item for item in category["content"] if item["title"] == selected_title)

        # 1. DESCRIPTION SECTION
        if "description" in lesson:
            st.info(lesson["description"])
        
        # 2. INPUT SECTION
        user_val = st.text_input(lesson['label'], key=f"in_{category['logic_id']}_{selected_title}")
        
        if user_val:
            try:
                local_vars = {'x': user_val, 'float': float, 'eval': eval}
                exec(lesson['code'], {}, local_vars)
                st.success(f"**Result:** {local_vars.get('output', 'No output defined')}")
            except Exception as e:
                st.error(f"Error: {e}")

        st.divider()
        st.code(lesson['code'], language='python')
