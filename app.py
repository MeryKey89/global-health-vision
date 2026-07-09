import os
# Forzamos la instalación de librerías necesarias
os.system("pip install google-generativeai pillow")

import streamlit as st
import google.generativeai as genai
from PIL import Image

st.title("🏥 Diagnóstico IA: Análisis Clínico")

# Intentamos cargar la API KEY
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    modelo = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Configura tu GOOGLE_API_KEY en los Secrets de Streamlit")
    st.stop()

archivo = st.file_uploader("Sube la radiografía", type=["jpg", "png"])
if archivo:
    img = Image.open(archivo)
    st.image(img)
    if st.button('Analizar con IA'):
        with st.spinner('Analizando...'):
            respuesta = modelo.generate_content(["Actúa como radiólogo experto. Analiza esta imagen:", img])
            st.info(respuesta.text)
