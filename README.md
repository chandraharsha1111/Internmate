# 📄 InternMate – AI-Powered Internship & Career Planning Assistant

## 1. Team Information

- **Team Name:**Aivana
- **Team Members & Roles:**
  - **Chandra Harsha** – Team Lead & UX Designer  
  - **Varshini** – AI Engineer  
  - **Sofia** – Frontend Developer  
  - **likitha** – Documentation & Testing

### Individual Contributions:

- **Chandra Harsha:** Led team coordination, designed user journey and interface flow, oversaw deployment, and managed user feedback collection.
- **Varshini:** Implemented AI integration, built prompt templates for internship recommendation and resume generation, handled API calls.
- **Sofia:** Developed and styled the Streamlit frontend, including input forms, layout, responsiveness, and Hugging Face deployment.
- **likitha:** Created detailed documentation (`README.md`, `REPORT.md`), organized code structure, conducted manual and user testing, collected and compiled feedback.

---

## 1.2 Application Overview

- **Application Name:** InternMate  
- **Use Case & Problem Solved:**  
  Many students face confusion and lack of personalized guidance while searching for internships or preparing job documents. InternMate solves this by:
  - Recommending internships based on stream, skills, and interests
  - Automatically generating tailored resumes and cover letters
  - Suggesting short-term learning goals to upskill for desired opportunities

- **Target Users:**  
  Undergraduate students, freshers, and job-seekers aged 18–25

- **Key Features:**
  -  Personalized internship suggestions
  -  AI-generated resumes and cover letters
  -  Skill roadmap for career development
  -  Simple, intuitive interface built with Streamlit

- **Motivation:**  
  We wanted to create a solution that simplifies the internship discovery and preparation process. As students ourselves, we understood the struggle and aimed to solve it using AI and open-source tools.

---

## 1.3 AI Integration Details

- **AI Model/Technique Used:**
  - **Model:** GPT-3.5 / LLM from Hugging Face Inference API (e.g., `google/flan-t5-xl` or OpenAI API)
  - **Technique:** Prompt-based generation with persona conditioning (Career Mentor Role)

- **Model Link:** <!-- TODO: Add your Hugging Face model card or API if used -->

- **How AI Powers the App:**
  - Generates personalized internship recommendations based on user input
  - Auto-writes resumes using structured prompt templates
  - Suggests 3-step skill paths for any selected domain

- **Prompt Engineering Strategy:**
  - Each LLM call includes a defined "role" (career advisor)
  - Prompts include:
    - Field of study
    - Skills
    - Career goals
  - Output structured as bullet points, markdown-friendly for Streamlit display

  **Example Prompt:**
  > "You are a career mentor. A 3rd-year Computer Science student wants internships in Machine Learning. Suggest 5 current roles with companies and generate a 3-bullet resume summary."

---

## 1.4 Technical Architecture & Development

- **Architecture Diagram:**  
  ![Architecture](https://sdmntprnorthcentralus.oaiusercontent.com/files/00000000-cc54-622f-a1cc-739b1a2bd803/raw?se=2025-06-10T03%3A51%3A46Z&sp=r&sv=2024-08-04&sr=b&scid=7f68cb14-7656-5a2f-b977-d657f2eac292&skoid=add8ee7d-5fc7-451e-b06e-a82b2276cf62&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-06-09T12%3A32%3A51Z&ske=2025-06-10T12%3A32%3A51Z&sks=b&skv=2024-08-04&sig=96WBaVTNWx9iH%2BxTZ/4mb33R1u2KqDcSWgsbXP8lOr4%3D)


- **Technology Stack:**
  - Python
  - Streamlit
  - Hugging Face Inference API / OpenAI
  - Pandas
  - Markdown for formatting output
  - Google Forms (for feedback collection)

- **Challenges & Solutions:**
  1. **Formatting AI outputs** – Solved using prompt constraints and markdown rendering in Streamlit.
  2. **User confusion during first use** – Added sample inputs and help instructions.
  3. **Model inconsistency** – Mitigated with templated and few-shot prompt examples.

- **Open-Source Licensing:**
  - **License:** MIT License  
  - **Reason:** Allows wide reuse, modification, and distribution with minimal restrictions. Suitable for educational and open-source collaboration.

---

## 1.5 User Testing & Feedback

- **Methodology:**
  We collected feedback via a Google Form and direct outreach. Users included college students, recent grads, and working professionals. None were part of the internship program.

- **Summary of Feedback:**
  | Category | User Feedback |
  |----------|----------------|
  | Usability | Easy to navigate; appreciated simple UI |
  | AI Accuracy | Resume and roadmap generation were very relevant |
  | Criticisms | Wanted ability to filter internships by city/type |
  | Suggestions | Add real-time internship listings and resume export to PDF |

- **Total Users Surveyed:** 12 (external to internship program)

- **Insights & Iterations:**
  - We enhanced input clarity with examples.
  - We improved prompt consistency to avoid hallucinated job data.
  - We plan to add PDF export and city-based filtering post-submission.

---

## 1.6 Future Roadmap & User Adoption Plan

### 🛠 Future Roadmap (Post-Submission)

- **Phase 1 (Weeks 1–2):**
  - Fix bugs
  - Resume layout improvements
  - Minor UI polishing

- **Phase 2 (Weeks 3–4):**
  - Add filtering by location/remote/full-time
  - Resume export to PDF feature

- **Phase 3 (Weeks 5–6):**
  - Integrate real-time APIs for internship listings
  - Enable user profile save/log-in
  - Open contributions via GitHub

---

### 📈 User Adoption Plan

- **Target Audience:**  
  College students aged 18–25, mostly active on LinkedIn, Telegram study groups, GitHub, and Reddit forums like `r/IndiaStudents`.

- **Compelling Value Proposition:**  
  One-stop tool to discover internships, build resumes, and track skill paths — in a single session.

- **Strategic Promotion:**
  - Share app in student Discord servers, Reddit threads
  - Write a short blog post (Medium/Hashnode) + LinkedIn post
  - Submit to Streamlit Community Showcase

- **Frictionless Onboarding:**
  - One-screen input → instant output
  - Sample inputs shown on startup
  - Feedback form integrated into sidebar

- **Feedback & Iteration Loop:**
  - Add embedded Google Form
  - Create public roadmap/issues section on GitHub
  - Encourage community suggestions

- **Open-Source Engagement:**
  - CONTRIBUTING.md with clear PR instructions
  - Invite ideas for new domains (e.g., Govt jobs, Research Internships)
  - Allow feedback via form + email + GitHub Issues

---

## 2. Code Repository

**Code Repository Link:** [https://code.swecha.org/YourRepoLinkHere](https://code.swecha.org/YourRepoLinkHere)  
<!-- TODO: Replace with actual repo link -->

---

## 3. Live Application

**Hugging Face Space:**  
[https://huggingface.co/spaces/chandraharsha/Internmate](https://huggingface.co/spaces/chandraharsha/Internmate)  


---

## 4. Demo Video

**Video Link:**  
[https://drive.google.com/YourVideoLink](https://drive.google.com/YourVideoLink)  
<!-- TODO: Replace with actual YouTube or Drive link -->

---

