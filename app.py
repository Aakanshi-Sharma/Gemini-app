import os
from PIL import Image
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")


def get_response_api(query, image):
    if query != "":
        response = model.generate_content([query, image])
    else:
        response = model.generate_content(image)
    return response.text


# -------------------UI------------------------
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini App")
input_text = st.text_input("Input Prompt: ", key="input", placeholder="Enter the text...")
uploaded_file = st.file_uploader("Choose an image.. ", type=["jpg", "png", "jpeg"])
image = ""
submit_button = st.button("Submit")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_column_width=True)

if submit_button:
    response_text = get_response_api(input_text, image)
    st.write(response_text)