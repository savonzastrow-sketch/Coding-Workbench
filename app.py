# --- WORKBENCH CONTENT (Your Library) ---
# Each item is a Category that will become a Tab.
# 'content' is a list of specific lessons for that category.
categories = [
    {
        "category_name": "📝 Strings",
        "logic_id": "strings",
        "content": [
            {
                "title": "🏷️ Basic Greeting",
                "label": "Enter your name:",
                "code": "output = f'Hi {x}!'"
            },
            {
                "title": "🔠 Uppercase",
                "label": "Enter text:",
                "code": "output = x.upper()"
            }
        ]
    },
    {
        "category_name": "🔢 Math",
        "logic_id": "math_cat",
        "content": [
            {
                "title": "🌡️ Celsius to F",
                "label": "Enter Celsius:",
                "code": "output = f'{9/5 * float(x) + 32} °F'"
            },
            {
                "title": "🍰 Area of Circle",
                "label": "Enter radius:",
                "code": "import math; output = math.pi * float(x)**2"
            }
        ]
    }
]

# --- MAIN APP VIEW ---
st.title("🚀 Python Workbench")

# 1. Create top-level tabs for Categories
tab_names = [c["category_name"] for c in categories]
tab_list = st.tabs(tab_names)

for i, tab in enumerate(tab_list):
    with tab:
        category = categories[i]
        
        # 2. Drop-down for specific lessons within this category
        lesson_titles = [item["title"] for item in category["content"]]
        selected_lesson_title = st.selectbox(
            "Choose a lesson:", 
            lesson_titles, 
            key=f"select_{category['logic_id']}"
        )
        
        # Find the specific lesson data based on the selection
        lesson = next(item for item in category["content"] if item["title"] == selected_lesson_title)
        
        # 3. INPUT / OUTPUT / CODE (Same logic as before)
        st.subheader("📥 Input")
        user_val = st.text_input(lesson['label'], key=f"in_{category['logic_id']}_{selected_lesson_title}")
        
        if user_val:
            try:
                local_vars = {'x': user_val, 'float': float, 'eval': eval}
                exec(lesson['code'], {}, local_vars)
                st.success(f"**Result:** {local_vars.get('output', 'No output defined')}")
            except Exception as e:
                st.error(f"Error: {e}")

        st.divider()
        st.subheader("📜 The Code")
        st.code(lesson['code'], language='python')
