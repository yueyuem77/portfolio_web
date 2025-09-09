from pathlib import Path

import streamlit as st
from streamlit_timeline import timeline
from PIL import Image

import os

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "YueyueMin_resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Yueyue Min"
PAGE_ICON = ":wave:"
NAME = "Yueyue Min"
DESCRIPTION = """
Full-Stack Data Scientist transforming complex data into business-ready AI solutions across forecasting, NLP, and visualization.
"""
EMAIL = "ym2980@columbia.edu"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/yueyuemin/",
    "GitHub": "https://github.com/yueyuem77/portfolio"
}
PROJECTS = {
    "📰 NBERT-Powered News Sentiment Explorer - Sentiment Analysis of New York Times Articles": "https://github.com/yueyuem77/NYT_Sentiment_AI",
    "🐿️ R Shiny App - Interactive Wildlife Habitat Dataviz Dashboard": "https://elenazz.shinyapps.io/squirrel_pj2/",
    "☕️ Tableau Dashboard: Coffee Shop Sales Report": "https://github.com/yueyuem77/portfolio",
    "🏠 HouseHunting Recommender - AI-powered Custom House Recommendation App that do data-driven decision making": "https://github.com/yueyuem77/portfolio",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# Initialize dark mode in session state
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False


# --- DARK MODE TOGGLE ---
with st.sidebar:
    st.markdown("### Theme Settings")
    dark_mode = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode)
    if dark_mode != st.session_state.dark_mode:
        st.session_state.dark_mode = dark_mode
        st.rerun()

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    css_content = f.read()
    
# Add dynamic dark mode CSS
dark_mode_css = f"""
<style>
{css_content}
/* Dynamic dark mode styles */
.stApp {{
    background-color: {'#0e1117' if st.session_state.dark_mode else '#ffffff'};
    color: {'#fafafa' if st.session_state.dark_mode else '#262730'};
}}

.stSidebar {{
    background-color: {'#1e1e1e' if st.session_state.dark_mode else '#f0f2f6'};
}}

.stMarkdown, .stText {{
    color: {'#fafafa' if st.session_state.dark_mode else '#262730'};
}}

.stSubheader {{
    color: {'#fafafa' if st.session_state.dark_mode else '#262730'};
}}

.stTitle {{
    color: {'#fafafa' if st.session_state.dark_mode else '#262730'};
}}
</style>
"""

st.markdown(dark_mode_css, unsafe_allow_html=True)

if os.path.exists(resume_file):
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
else:
    st.error("Resume file not found. Please upload it or check the path.")
    

profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

         
# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
    - ✔️ Built end-to-end data pipelines and ML applications, with experience in NLP, forecasting, and dashboarding 
    - ✔️ Proficient in Python, SQL, and R, with strong command of statistical modeling and real-world data analysis 
    - ✔️ Delivered impactful insights across education, finance, and logistics domains through automation and visualization 
    - ✔️ Excellent team collaborator with a proactive mindset and a passion for solving complex data problems 
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    ''' 
 - 👩‍💻 **Programming**: Python (Pandas, NumPy, Scikit-learn), SQL, R, MATLAB
 - 📊 **Data Visualization**: Tableau, Excel, Plotly, Seaborn, Matplotlib
 - 📚 **Modeling Techniques**: Linear/Logistic Regression, Random Forest, Clustering, Forecasting, A/B Testing
 - 🗄️ **Databases & Cloud**: MySQL, MongoDB, Databricks, AWS
''')
st.write("")
st.write("")
st.write("")
st.write("")


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Scientist Lead  | GradeMate**")
st.write("09/2024 - 05/2025")
st.write(
    """
- ► Designed and deployed scalable ML models using LLaMA 3 and Python to automate grading and feedback workflows,
reducing manual grading variance and increasing efficiency for educators
- ► Led a team of 4 analysts to engineered a time-aware scoring algorithm incorporating A/B testing and time series dynamics to adapt to teacher
grading styles and student learning behavior
- ► Design ML pipelines with Databricks and Python, automating model deployment and reducing latency in result feedback loops by 40%.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Business Intelligence Analyst | ADEL**")
st.write("04/2023 - 08/2024")
st.write(
    """
- ► Built forecasting models using XGBoost to analyze financial trends and regional demand signals, used SQL to extract
and structure time-series data, supporting improved inventory planning and pricing strategies across Southeast Asia.
- ►Automated analytics workflows with pandas to replace manual reporting, reducing turnaround time for market
performance insights and improving executive alignment.
- ►Developed KPI dashboards in Power BI translating operational and revenue data into actionable metrics, driving better
allocation decisions during monthly strategy reviews.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Machine Learning Engineer Intern | SF Technology**")
st.write("05/2021 - 09/2021")
st.write(
    """
- ► Enhanced warehouse automation by refining object detection models with TensorFlow and augmenting edge-case images using OpenCV, reducing misclassifications by 10%.
- ►Designed modular data pipelines with validation and feature tracking layers, enabling model reusability across lighting and warehouse layouts.
- ►Conducted anomaly detection on route tracking data using statistical control charts, identifying inefficiencies and supporting rerouting process redesign.

"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Timeline ---
st.write('\n')
st.subheader("DS TIMELINE")
st.write("---")

with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()

    timeline(data, height=500)