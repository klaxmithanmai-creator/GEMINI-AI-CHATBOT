import streamlit as st
from dotenv import load_dotenv
import os 
from google import genai
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
st.set_page_config(
    page_title = "Gemini AI Chatbot",
    layout = "centered"
)
st.title("Gemini AI Chatbot")
st.write("Ask Gemini anything!")
prompt = st.text_area(
    "Enter your prompt:",
    placeholder = "Explain Artificial Intelligence"
)
if st.button("Generate Response"):
    if prompt:
        with st.spinner("Gemini is thinking..."):
            response = client.models.generate_content(
                model ="gemini-3.5-flash-lite",
                contents = prompt
            )
        st.success("Response generated!")
        st.write(response.text)
    else:
        st.warning("please enter your prompt:")
        # Custom CSS
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f5f3ff, #eef4ff);
        color: #202040;
    }

    /* Main title */
    h1 {
        text-align: center;
        color: #5b3cc4;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .stApp p {
        font-size: 17px;
    }

    /* Text area */
    textarea {
        background-color: #ffffff !important;
        color: #222222 !important;
        border: 2px solid #d8cef8 !important;
        border-radius: 15px !important;
        padding: 15px !important;
        font-size: 16px !important;
    }

    textarea:focus {
        border: 2px solid #7c5ce6 !important;
        box-shadow: 0 0 10px rgba(124, 92, 230, 0.25) !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #6c4dd9, #8b6de8);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 20px;
        font-size: 17px;
        font-weight: 600;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #5838c4, #7654d8);
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(91, 60, 196, 0.25);
    }

    /* Success message */
    .stSuccess {
        border-radius: 12px;
    }

    /* Warning message */
    .stWarning {
        border-radius: 12px;
    }

    /* Center content width */
    .block-container {
        max-width: 800px;
        padding-top: 3rem;
    }

</style>
""", unsafe_allow_html=True)