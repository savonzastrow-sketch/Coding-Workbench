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
            {"title": "🏷️ Basic Greeting", "label": "Enter your name:", "code": "output = f'Hi {x}!'"},
            {"title": "🔠 Uppercase", "label": "Enter text:", "code": "output = x.upper()"}
        ]
    },
    {
        "category_name": "🔢 Math",
        "logic_id": "math_cat",
        "content": [
            {"title": "🌡️ Celsius to F", "label": "Enter Celsius:", "code": "output = f'{9/5 * float(x) + 32} °F'"},
            {"title": "🧪 Eval Lab", "label": "Enter expression:", "code": "output = eval(x)"}
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
