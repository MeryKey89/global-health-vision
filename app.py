import subprocess
import sys

# Instalación automática de librerías
subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai", "pillow"])

import streamlit as st
import google.generativeai as genai
from PIL import Image

st.title("🏥 Diagnóstico IA: Análisis Clínico")

# Configuración de la IA
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    modelo = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Configura tu GOOGLE_API_KEY en los Secrets.")
    st.stop()

archivo = st.file_uploader("Sube radiografía", type=["jpg", "png"])
if archivo:
    img = Image.open(archivo)
    st.image(img)
    if st.button('Analizar con IA'):
        with st.spinner('Analizando...'):
            respuesta = modelo.generate_content(["Actúa como radiólogo. Analiza esta imagen:", img])
            st.info(respuesta.text)
