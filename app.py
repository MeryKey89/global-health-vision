import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuración de la IA
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
modelo = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="IA Diagnóstico Real", page_icon="🏥")
st.title("🏥 Diagnóstico IA: Análisis Clínico")

archivo = st.file_uploader("Sube la radiografía para análisis profesional", type=["jpg", "png"])

if archivo is not None:
    img = Image.open(archivo)
    st.image(img, caption='Radiografía cargada', use_column_width=True)
    
    if st.button('Analizar con IA (Gemini)'):
        with st.spinner('Analizando patrones radiológicos...'):
            prompt = "Actúa como un radiólogo experto. Analiza esta imagen, identifica hallazgos relevantes y proporciona un informe breve sobre posibles anomalías óseas o fracturas."
            respuesta = modelo.generate_content([prompt, img])
            
            st.write("### Informe del Análisis:")
            st.info(respuesta.text)
