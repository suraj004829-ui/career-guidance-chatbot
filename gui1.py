import streamlit as st
from crew_setup import run_crew

# PAGE CONFIG
st.set_page_config(
    page_title="Career Guidance Bot",
    page_icon="🎯",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background-color: #0E1117;
}

.block-container {
    padding-top: 2rem;
}

.stTextArea textarea {
    background-color: #1E1E1E;
    color: white;
    border-radius: 15px;
    padding: 15px;
    font-size: 17px;
    border: 1px solid #333;
}

.stButton button {
    width: 100%;
    background: linear-gradient(90deg,#10A37F,#0D8C6D);
    color: white;
    border-radius: 12px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton button:hover {
    background: linear-gradient(90deg,#0D8C6D,#10A37F);
    color: white;
}

.metric-card {
    background: linear-gradient(135deg,#1F2937,#111827);
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    border: 1px solid #333;
}

.metric-title {
    color: #9CA3AF;
    font-size: 16px;
    margin-top: 10px;
}

.metric-value {
    color: white;
    font-size: 30px;
    font-weight: bold;
}

.card {
    background-color: #161B22;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #333;
    margin-top: 20px;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("🚀 Career Guidance Bot")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### ⚡ Technologies Used

- CrewAI  
- LangChain  
- Groq API  
- Streamlit  
""")

st.sidebar.markdown("---")

st.sidebar.info("""
Enter your skills and interests to get:

✅ Career Suggestions  
✅ Certifications  
✅ Roadmaps  
✅ Courses  
✅ Job Preparation Tips  
""")

# MAIN TITLE
st.title("🎯 AI Career Guidance Dashboard")

st.markdown("""
Get personalized:

- 📚 Courses  
- 🎓 Certifications  
- 💼 Career Paths  
- 🛣️ Learning Roadmaps  
- 🤖 AI Guidance  
""")

st.markdown("---")

# USER INPUT
user_input = st.text_area(
    "✍️ Enter your skills, interests and goals:",
    height=180,
    placeholder="Example:\nPython\nDSA\nAI\nWeb Development"
)

# BUTTON
if st.button("🚀 Generate Career Guidance"):

    if user_input.strip() == "":
        st.warning("Please enter your skills.")
    else:

        with st.spinner("🤖 AI Agents are analyzing your profile..."):

            # RUN CREW
            result = run_crew(user_input)

            # GET CLEAN OUTPUT
            try:
                final_output = result.raw
            except:
                final_output = str(result)

            # SUCCESS MESSAGE
            st.success("✅ Career Guidance Generated Successfully!")

            st.markdown("---")

            # COUNTS
            course_count = final_output.lower().count("course")
            cert_count = final_output.lower().count("certification")
            career_count = final_output.lower().count("career")
            roadmap_count = final_output.lower().count("phase")

            # METRIC CARDS
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size:40px;">📚</div>
                    <div class="metric-value">{course_count}</div>
                    <div class="metric-title">Courses</div>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size:40px;">🎓</div>
                    <div class="metric-value">{cert_count}</div>
                    <div class="metric-title">Certifications</div>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size:40px;">💼</div>
                    <div class="metric-value">{career_count}</div>
                    <div class="metric-title">Careers</div>
                </div>
                """, unsafe_allow_html=True)

            with col4:
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size:40px;">🛣️</div>
                    <div class="metric-value">{roadmap_count}</div>
                    <div class="metric-title">Roadmap</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # TABS
            tab1, tab2 = st.tabs(["📋 Full Report", "📥 Download"])

            # FULL REPORT TAB
            with tab1:

                st.markdown('<div class="card">', unsafe_allow_html=True)

                st.markdown(final_output)

                st.markdown('</div>', unsafe_allow_html=True)

            # DOWNLOAD TAB
            with tab2:

                st.download_button(
                    label="📥 Download Career Report",
                    data=final_output,
                    file_name="career_report.txt",
                    mime="text/plain"
                )

# FOOTER
st.markdown("""
<div class="footer">
Built with CrewAI + LangChain + Groq API
</div>
""", unsafe_allow_html=True)