from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.7, model_name="text-davinci-003", openai_api_key="your_openai_api_key_here")

template = PromptTemplate.from_template(
    "Generate a {writing_style} job description for a {experience_level} {job_title} at {company_name}. \
     The job involves {brief_description}. The candidate should have the following skills: {desired_skills}."
)

def generate_with_langchain(job_title, company_name, brief_description, desired_skills, experience_level, writing_style):
    prompt = template.format(
        job_title=job_title,
        company_name=company_name,
        brief_description=brief_description,
        desired_skills=desired_skills,
        experience_level=experience_level,
        writing_style=writing_style
    )
    return llm(prompt)
