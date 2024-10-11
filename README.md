# AI-Powered Job Description Generator

This project is a **Streamlit** application that uses **OpenAI's GPT-3.5-turbo** model to generate dynamic job descriptions based on user inputs. It allows users to select a department, job title, and desired skills, and provides fields for company name, job description, and experience level. The generated job description is tailored to these inputs using the OpenAI API.

## Features
- **Department and Job Title Selection**: Choose from different departments like Engineering, Data Science, Product, Design, and Marketing, with predefined job titles in each.
- **Auto-populated Skills**: Each job title has a list of recommended skills, which can be selected or customized by the user.
- **Dynamic Job Description Generation**: Generates a comprehensive job description based on inputs like job title, skills, company name, experience level, and job description.
- **User-friendly Interface**: Built with Streamlit, featuring a clean, intuitive UI with animations for a smooth user experience.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Key Setup](#api-key-setup)
- [Technologies Used](#technologies-used)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To run this project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/job-description-generator.git
cd job-description-generator
# generatedAIJD

** 2. Use your OpenAI API Key**

Get an API key from [OpenAI](https://beta.openai.com/signup/). In `app.py`, replace `YOUR_OPENAI_API_KEY` with your actual API key:

```python
openai.api_key = "YOUR_OPENAI_API_KEY"
```

Alternatively, you can set the API key as an environment variable:
```bash
export OPENAI_API_KEY="your-api-key"
```

### 3. Install Dependencies

Make sure Python 3.7 or above is installed. Then install the necessary Python libraries:
```bash
pip install streamlit openai
```

### 4. Run the Application

To start the Streamlit application:
```bash
streamlit run app.py
```

## Usage

1. **Select a Department**: Choose from the available departments:
    - Engineering
    - Data Science
    - Product
    - Design & Marketing

2. **Select a Job Title**: After selecting a department, choose a job title from the list.

3. **Select Desired Skills**: Choose up to 7 skills for the selected job title. The app will suggest a set of skills based on the selected title.

4. **Provide Company Name**: Enter the company name where the position is being offered.

5. **Write a Brief Job Description**: Enter a job description (between 100 and 2000 characters). The app will track the character count.

6. **Select Experience Level**: Choose the required experience level for the role (Entry-Level, Mid-Level, Senior).

7. **Generate the Job Description**: Click the "Generate Job Description" button to generate the job description based on your inputs.

## Project Structure

```plaintext
├── app.py              # Main application code
├── README.md           # Documentation file
└── requirements.txt    # Project dependencies (optional, for deployment)
```

### Key Components:
- **app.py**: The main Python script that contains the Streamlit application logic, including user inputs, API interaction, and job description generation.
- **README.md**: The file you're currently reading, which provides detailed instructions and information about the project.

## Technologies Used

- **Python**: The primary language used to develop the application.
- **Streamlit**: A Python library for building simple and interactive web applications.
- **OpenAI GPT-3.5-turbo**: Used to generate job descriptions dynamically based on user inputs.
- **HTML & CSS**: Used for styling and custom animations in the Streamlit app.
