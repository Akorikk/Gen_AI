import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini 
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file,get_file 
import google.generativeai as genai
import time
from pathlib import path
import tempfile

from dotenv import load_dotenv
load_dotenv()
import os 

API_KEY=os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

st.set_page_config(
    page_title="Multimodel AI Agent Video Summarizer",
    layout="wide"
)    

st.title("Phidata Multimodal AI Agent")
st.header("Powered by Gemini 2.0 Flash Exp")

@st.cache_resource
def initialize_agent():
    return Agent(
        name="Video AI Summarizer",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True,
    )

multimodel_Agent=initialize_agent()

video_file = st.file_uploader(
    "Upload a video file", type=["mp4","mov","avi"], help="Upload a video for AI analysis"
)

if video_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_vide:
        temp_vide.write(video_file.read())
        video_path = temp_vide.name

    st.video(video_path, fromat="video/mp4", start_time=0)

    user_query = st.text_area(
        
    )  
