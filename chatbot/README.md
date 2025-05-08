# Project Overview

This project demonstrates how to build an AI chatbot using Groq and OpenAI . The chatbot leverages APIs for natural language processing and provides users with tailored financial advice. Follow the steps below to set up and run the project.

# Setup Instructions: Create Virtual Environment

1. Set Up a Virtual Environment
2. Create a virtual environment to isolate your dependencies:


**For Windows**

python -m venv venv

venv\Scripts\activate

**For macOS/Linux**

python3 -m venv venv
source venv/bin/activate

# Install Required Dependencies

Install the required Python packages listed in requirements.txt:

pip install -r requirements.txt


# Create a .env File

Create a .env file in the root directory of the project and add your OpenAI and Groq API keys:

OPENAI_API_KEY=your_openai_api_key_here

GROQ_API_KEY=your_groq_api_key_here

