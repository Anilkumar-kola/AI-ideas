import streamlit as st
from PIL import Image
import requests
import os
import asyncio
import edge_tts
import openai
from io import BytesIO

# ========== CONFIG ==========
openai.api_key = os.getenv("OPENAI_API_KEY")  # or replace with your API key string

# ========== FUNCTIONS ==========

def generate_pixar_image(prompt, save_path):
    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    img = Image.open(BytesIO(requests.get(image_url).content))
    img.save(save_path)
    return save_path

def generate_voice(text, voice_name, filename="output.mp3"):
    async def _generate():
        communicate = edge_tts.Communicate(text, voice_name)
        await communicate.save(filename)
    asyncio.run(_generate())
    return filename

# ========== UI ==========

st.set_page_config(page_title="3D Pixar Avatar Generator", layout="centered")
st.title("🧒 Pixar-Style Avatar with Voice")

image_prompt = st.text_input("🎨 Describe your Pixar-style image:", "A cute 3D Pixar-style school girl with large eyes")
voice_prompt = st.text_input("🗣️ What should the avatar say?:", "Hi, I’m your animated assistant!")

voice_options = [
    "en-US-KidNeural", "en-US-JennyNeural", "en-GB-RyanNeural", "en-US-AriaNeural",
    "en-US-GuyNeural", "en-US-LisaNeural", "en-US-ChristopherNeural"
]
voice_choice = st.selectbox("🎮 Select Voice: ", voice_options, index=0)

if st.button("🚀 Generate Avatar"):
    with st.spinner("Generating image..."):
        image_path = os.path.join("temp", "avatar.jpg")
        os.makedirs("temp", exist_ok=True)
        generate_pixar_image(image_prompt, image_path)

    st.image(image_path, caption="🧒 Generated Pixar-style Avatar", use_column_width=True)

    with st.spinner("Generating voice..."):
        audio_path = generate_voice(voice_prompt, voice_choice)
        st.audio(audio_path, format="audio/mp3")

    st.success("✅ Done!")
