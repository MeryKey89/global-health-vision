import streamlit as st
import google.generativeai as genai
from PIL import Image

st.title("🏥 Diagnóstico IA")

# Intentamos cargar la API
api_key = st.secrets.get("GOOGLE_API_KEY")
if not api_key:
    st.error("No se encuentra la API KEY. Por favor, revisa tus Secrets en Streamlit.")
else:
    genai.configure(api_key=api_key)
    modelo = genai.GenerativeModel('gemini-1.5-flash')

    archivo = st.file_uploader("Sube radiografía", type=["jpg", "png"])
    if archivo:
        img = Image.open(archivo)
        st.image(img)
        if st.button('Analizar'):
            respuesta = modelo.generate_content(["Actúa como radiólogo. Analiza esta imagen:", img])
            st.info(respuesta.text)
