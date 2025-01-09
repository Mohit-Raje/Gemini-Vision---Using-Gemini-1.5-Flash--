import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Set the page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Gemini Image Demo")


# Sidebar for API key input
st.sidebar.title("API Key Input")
API_KEY = st.sidebar.text_input("Enter Gemini API Key", type="password")

# Set the API key as an environment variable
os.environ['GOOGLE_API_KEY'] = API_KEY

# Configure the Generative AI model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Define the response function
def response(input, img):
    if input != "":
        result = model.generate_content([input, img])
    else:
        result = model.generate_content(img)
    return result.text

# Main application content
st.header("Image-to-Text Translator")
input_text = st.text_input("Input Prompt:", key="input")

uploaded_image = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
image = ""
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image")

submit = st.button("Tell me about Image")

if submit:
    if API_KEY:
        try:
            result = response(input_text, image)
            st.subheader("The Response is:")
            st.write(result)
        except Exception as e:
            st.error(f"Error generating response: {e}")
    else:
        st.error("Please enter a valid API Key in the sidebar.")


st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: black;
            color: white;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
            z-index: 100;
        }
        .footer a {
            color: white;
            text-decoration: none;
        }
        .footer img {
            width: 30px;
            vertical-align: middle;
            margin-left: 10px;
        }
    </style>
    <div class="footer">
        <strong>Trademark © 2025 Mohit Raje</strong>
        <a href="https://github.com/Mohit-Raje" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
