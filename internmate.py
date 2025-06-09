import streamlit as st
import random

# Sample internship data
internships = {
    "AI": ["AI Intern @ TechNova", "ML Intern @ DataBridge", "NLP Intern @ LinguaTech"],
    "Web Development": ["Frontend Intern @ Webify", "Full-Stack Intern @ DevHive"],
    "Cybersecurity": ["Security Intern @ SecureX", "Network Intern @ CyberCore"]
}

# Resume summary generator
def generate_resume_summary(name, field, skills):
    return f"""
**Resume Summary for {name}**

A highly motivated {field} student with skills in {skills}.
Seeking an internship opportunity to apply theoretical knowledge to practical challenges,
contribute to innovative projects, and grow as a professional in the field of {field}.
"""

# Internship recommendation logic
def recommend_internships(field):
    return internships.get(field, ["No internships found for the selected field."])

# Streamlit app configuration
st.set_page_config(page_title="InternMate", page_icon="🎓", layout="centered")

# App title
st.title("🎓 InternMate – Your AI Internship & Resume Buddy")
st.markdown("Welcome to InternMate! Fill in your details to get personalized internship suggestions and a resume summary.")

# Input form
with st.form("user_form"):
    name = st.text_input("Your Name")
    field = st.selectbox("Choose your field of interest", list(internships.keys()))
    skills = st.text_area("List your skills (comma-separated)")
    submit = st.form_submit_button("Generate Suggestions & Resume")

# Output section
if submit:
    if not name or not skills:
        st.warning("Please fill in all the fields to get recommendations.")
    else:
        st.header("🔍 Recommended Internships")
        recommendations = recommend_internships(field)
        for job in recommendations:
            st.write(f"- {job}")

        st.header("📝 AI-Generated Resume Summary")
        resume_text = generate_resume_summary(name, field, skills)
        st.markdown(resume_text)

        st.success("✅ Done! You can now copy or save your results.")

# Footer
st.markdown("---")
st.info("Want to help improve InternMate? [Fill out our feedback form](https://forms.gle/your-google-form-link)")
