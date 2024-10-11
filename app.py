import os
import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Predefined departments with job titles and corresponding skills
departments = {
    'Engineering': {
        'Software Engineer': ['Python', 'Java', 'C++', 'Agile Development', 'Version Control (Git)', 'Debugging', 'REST APIs', 'Cloud Computing', 'Unit Testing'],
        'DevOps Engineer': ['CI/CD Pipelines', 'Kubernetes', 'Docker', 'AWS', 'Linux', 'Networking', 'Automation', 'Scripting'],
        'QA Engineer': ['Test Automation', 'Selenium', 'Cucumber', 'Manual Testing', 'API Testing', 'Performance Testing'],
        'Backend Developer': ['Node.js', 'Ruby', 'Go', 'Microservices', 'Database Management', 'REST APIs'],
        'Frontend Developer': ['JavaScript', 'React', 'CSS', 'HTML', 'UI/UX Design', 'Responsive Design']
    },
    'Data Science': {
        'Data Scientist': ['Python', 'Machine Learning', 'Data Analysis', 'Statistics', 'SQL', 'Data Visualization', 'Big Data', 'TensorFlow', 'R'],
        'Data Engineer': ['ETL Pipelines', 'SQL', 'Apache Spark', 'Big Data', 'Python', 'Cloud Data Storage'],
        'ML Engineer': ['Machine Learning', 'Deep Learning', 'Python', 'TensorFlow', 'Model Deployment', 'Data Preprocessing'],
        'Data Analyst': ['Data Visualization', 'SQL', 'Python', 'Excel', 'Tableau', 'Power BI'],
        'AI Researcher': ['Neural Networks', 'Deep Learning', 'AI Ethics', 'NLP', 'Reinforcement Learning', 'Machine Learning']
    },
    'Product': {
        'Product Manager': ['Product Roadmap', 'Stakeholder Communication', 'Agile Methodology', 'Market Research', 'Feature Prioritization', 'Risk Management', 'UX/UI Knowledge'],
        'Business Analyst': ['Requirement Gathering', 'Stakeholder Communication', 'Data Analysis', 'Market Research', 'Process Improvement', 'Documentation'],
        'Scrum Master': ['Agile Methodologies', 'Sprint Planning', 'Team Management', 'Facilitation', 'Risk Management'],
        'Project Manager': ['Project Planning', 'Risk Management', 'Budgeting', 'Scheduling', 'Stakeholder Management', 'Resource Allocation'],
        'Program Manager': ['Strategic Planning', 'Resource Management', 'Risk Management', 'Cross-Functional Team Management', 'Budget Management']
    },
    'Design & Marketing': {
        'UX/UI Designer': ['Wireframing', 'Prototyping', 'User Research', 'Figma', 'Adobe XD', 'Interaction Design', 'Visual Design', 'Typography', 'Design Thinking'],
        'Graphic Designer': ['Photoshop', 'Illustrator', 'InDesign', 'Creative Suite', 'Typography', 'Branding', 'Visual Communication'],
        'Marketing Specialist': ['SEO', 'Content Strategy', 'Social Media Marketing', 'Email Campaigns', 'Google Analytics', 'Ad Campaign Management', 'Copywriting', 'PPC Campaigns'],
        'Social Media Manager': ['Content Creation', 'Branding', 'Community Management', 'Social Media Strategy', 'Analytics', 'Copywriting'],
        'Content Writer': ['SEO Writing', 'Content Strategy', 'Copywriting', 'Blog Writing', 'Editing', 'Social Media Content']
    }
}

# Add custom CSS and JavaScript for animations
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    .stApp {
        background-color: #8cd3ff;
        font-family: 'Poppins', sans-serif;
        color: #333333;
    }

    h1, h2, h3, h4, h5, h6 {
        color: black;
        animation: fadeIn 1s ease-in-out;
    }

    div.stSelectbox, div.stTextInput, div.stTextArea, div.stMultiselect, div.stButton {
        animation: fadeIn 1s ease-in-out forwards;
        background-color: #d9f1ff !important;
        border-radius: 5px;
        padding: 10px;
        margin: 10px 0;
    }

    div.stSelectbox { animation-delay: 0s; } 
    div.stMultiselect { animation-delay: 0s; } 
    div.stTextInput { animation-delay: 0s; } 
    div.stTextArea { animation-delay: 0s; } 
    div.stButton { animation-delay: 0s; }

    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    div.stButton button:hover {
        background-color: #0056b3;
        transform: scale(1.05);
    }

    .stSidebar p:nth-of-type(1) { animation-delay: 4s; }
    .stSidebar p:nth-of-type(2) { animation-delay: 4.5s; }
    
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("AI-Powered Job Description Generator")

# Department Dropdown
department = st.selectbox('Select Department:', ['Select a Department'] + list(departments.keys()))

# Job Title Dropdown based on selected department
if department != 'Select a Department':
    job_titles_in_department = list(departments[department].keys())
    job_title = st.selectbox('Select the Job Title:', ['Select the Job Title'] + job_titles_in_department)

    # Auto-populate Desired Skills based on selected Job Title
    if job_title != 'Select the Job Title':
        default_skills = departments[department][job_title]
        
        # Multiselect Dropdown for Desired Skills with a limit of 7 selections
        desired_skills = st.multiselect('Select desired skills (Max 7):', default_skills, max_selections=7)

# Company Name Input
company_name = st.text_input('Enter Company Name:')

# Brief Job Description
max_characters = 2000
brief_description = st.text_area('Provide a brief job description (100 to 2000 characters):')
description_char_count = len(brief_description)

# Display remaining characters
st.write(f"Characters remaining: {max_characters - description_char_count} / {max_characters}")

# Experience Level
experience_level = st.selectbox('Select Experience Level:', ['Entry-Level', 'Mid-Level', 'Senior'])

# Button to generate the job description
if st.button("Generate Job Description"):
    if not company_name or not brief_description or len(desired_skills) == 0:
        st.error("Please fill out all the required fields.")
    elif description_char_count < 100:
        st.error(f"Job description is too short. You have {description_char_count} characters. Please write at least 100 characters.")
    elif description_char_count > max_characters:
        st.error(f"Job description is too long. You have {description_char_count} characters. Please shorten it to {max_characters} characters or less.")
    else:
        # Function to generate the job description using OpenAI's API
        def generate_job_description(job_title, company_name, brief_description, desired_skills, experience_level):
            prompt = f"""
            Generate a detailed job description for a {job_title} at {company_name}. 
            The role should include the following skills: {', '.join(desired_skills)}.
            Experience Level: {experience_level}.
            Additional Information: {brief_description}.
            """
            try:
                response = openai.Completion.create(
                    engine="gpt-3.5-turbo",
                    prompt=prompt,
                    max_tokens=300
                )
                return response.choices[0].text.strip()
            except Exception as e:
                return f"Error: {str(e)}"

        # Generate the job description
        job_description = generate_job_description(job_title, company_name, brief_description, desired_skills, experience_level)
        
        # Display the generated job description
        st.subheader("Generated Job Description:")
        st.write(job_description)

# Add project details to the sidebar
st.sidebar.title("About")
st.sidebar.info("""
This app generates job descriptions based on user inputs like Job Title, Company Name, and Desired Skills. 
It uses OpenAI's API to create the description dynamically based on your inputs.
""")
