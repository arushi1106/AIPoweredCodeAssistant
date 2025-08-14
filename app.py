import streamlit as st
from openai import OpenAI
import re

# Set your OpenAI API key
client = OpenAI(api_key= "")

# Prompt template
def create_prompt(code_snippet):
    return f"""
You are a security auditor. Analyze the following C code and determine whether it contains any security vulnerabilities (such as buffer overflow, memory leaks, use-after-free, or unsafe pointer manipulation). If yes, explain what they are. If not, state it's safe.

Code:
{code_snippet}

Answer with one of the following:
- 'VULNERABLE' and the reason
- 'SAFE' and why
"""

# Query GPT-4
def analyze_code(code):
    prompt = create_prompt(code)
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        completion = response.choices[0].message.content
    except Exception as e:
        return "ERROR", str(e)

    # Extract label
    match = re.search(r"\b(SAFE|VULNERABLE)\b", completion.upper())
    label = match.group(1) if match else "UNKNOWN"
    return label, completion

# Streamlit UI
st.set_page_config(page_title="Code Security Auditor", layout="wide")

st.title("AI-Powered Code Vulnerability Auditor")
st.markdown("Paste a C/C++ function and get AI-generated security assessment.")

code_input = st.text_area("Paste your C/C++ code here", height=300)

if st.button("Analyze"):
    if code_input.strip():
        with st.spinner("Analyzing with GPT-4..."):
            label, explanation = analyze_code(code_input)

        st.subheader(f"Prediction: {label}")
        st.code(explanation)

        st.download_button(
            label="Download Explanation",
            data=explanation,
            file_name="vulnerability_analysis.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please paste some code before clicking Analyze.")
