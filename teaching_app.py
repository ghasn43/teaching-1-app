import streamlit as st
import arabic_reshaper

# --- Arabic Helper ---
def ar(text: str) -> str:
    """Reshape Arabic letters for proper connection."""
    return arabic_reshaper.reshape(text)

# --- Lesson Content ---
lessons = {
    "Fruits": {
        "words": [
            ("Apple", "تفاحة"),
            ("Banana", "موز"),
            ("Orange", "برتقال"),
        ],
        "practice": {
            "question": "اكتب الكلمة العربية لكلمة Apple:",
            "answer": "تفاحة"
        },
        "story": {
            "question": "Ali goes to the market. He wants to buy a 🍎. What does he ask?",
            "choices": ["أعطني تفاحة", "أعطني كتاب"],
            "answer": "أعطني تفاحة"
        }
    }
}

# --- Streamlit UI ---
st.set_page_config(page_title="Teaching App", page_icon="📚", layout="centered")
st.title("📚 Teaching App")

# Sidebar: choose lesson
lesson_name = st.sidebar.selectbox("Choose Lesson", list(lessons.keys()))
lesson = lessons[lesson_name]

# --- Teaching Section ---
st.subheader("👩‍🏫 Teaching")
for eng, arabic in lesson["words"]:
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write(eng)             # English on the left
    with col2:
        st.write(ar(arabic))      # Arabic on the right (properly connected)

# --- Practice Section ---
st.subheader("✍️ Practice")
st.write(ar(lesson["practice"]["question"]))
answer = st.text_input("", "")
if answer:
    if answer.strip() == lesson["practice"]["answer"]:
        st.success(ar("✅ صحيح! أحسنت"))
    else:
        st.error(ar("❌ خطأ، حاول مرة أخرى"))

# --- Story Mode ---
st.subheader("📖 Story Mode")
st.write(lesson["story"]["question"])
choices = [ar(c) for c in lesson["story"]["choices"]]
choice = st.radio("اختر الإجابة:", choices, key="story")
if st.button("Submit Answer"):
    if choice == ar(lesson["story"]["answer"]):
        st.success(ar("إجابة صحيحة ✅"))
    else:
        st.error(ar("إجابة خاطئة ❌"))
