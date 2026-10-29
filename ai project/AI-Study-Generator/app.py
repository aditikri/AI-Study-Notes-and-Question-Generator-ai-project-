
import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load .env from this project's folder
load_dotenv(Path(__file__).with_name(".env"))

st.set_page_config(
    page_title="AI Study Generator",
    page_icon="📚",
    layout="centered"
)

st.title("📚 AI Study Notes & Question Generator")
st.write("Create simple study notes and practice questions with AI.")

api_key = os.getenv("GEMINI_API_KEY")

topic = st.text_input(
    "Enter your study topic",
    placeholder="e.g. Artificial Intelligence"
)

text = st.text_area(
    "Or paste your academic text (optional)",
    height=150,
    placeholder="Paste your notes or textbook content here..."
)

feature = st.selectbox(
    "Choose what you want to generate",
    ["Study Notes", "Practice Questions"]
)

if st.button("Generate", type="primary", use_container_width=True):

    source = text.strip() or topic.strip()

    if not source:
        st.warning("Please enter a topic or paste some text.")

    elif not api_key:
        st.error(
            "Gemini API key not found. Check the GEMINI_API_KEY "
            "entry in your project's .env file."
        )

    else:
        if feature == "Study Notes":
            prompt = f"""
            Create beginner-friendly study notes about:
            {source}

            Include:
            1. A simple introduction
            2. Important definitions
            3. Key concepts in bullet points
            4. Examples where useful
            5. A short revision summary

            Use clear English and readable headings.
            """

        else:
            prompt = f"""
            Create practice questions about:
            {source}

            Include:
            1. Five multiple-choice questions, each with four options
            2. The correct answer for each MCQ
            3. Five short-answer questions with answers

            Use simple English and format everything clearly.
            """

        try:
            client = genai.Client(api_key=api_key)

            with st.spinner("Generating your study material..."):
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

            result = response.text

            if result and result.strip():
                st.subheader("Generated Content")
                st.markdown(result)

                st.download_button(
                    label="Download as TXT",
                    data=result,
                    file_name="study_material.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            else:
                st.warning(
                    "No text was generated. Please try again."
                )

        except Exception as error:
            error_message = str(error)
            st.error("Content generation failed.")

            if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
                st.warning(
                    "The API quota or rate limit may have been reached. "
                    "Check your Gemini API usage and limits."
                )
            elif "401" in error_message or "403" in error_message:
                st.warning(
                    "Check whether your API key is valid and has access."
                )
            else:
                st.write("Error details:")
                st.code(error_message)
