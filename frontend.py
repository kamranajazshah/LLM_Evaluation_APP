import streamlit as st
import requests

st.title("LLM Evaluation App")

api_url = "http://127.0.0.1:8000/evaluate"

input_text = st.text_input("User Input")
ai_output = st.text_input("AI Response")
actual_output = st.text_input("Actual Answer")

if st.button("Submit"):
    data = {
        "input": input_text,
        "ai_output": ai_output,
        "actual_output": actual_output
    }

    try:
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            result = response.json()
            st.subheader("Evaluation Scores")
            st.write(f"Factual: {result.get('factual')}")
            st.write(f"Coherence: {result.get('coherance')}")
            st.write(f"Relevance: {result.get('relevance')}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Request failed: {str(e)}")
