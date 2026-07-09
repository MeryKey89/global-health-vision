import streamlit as st
# Intentamos importar, si no están, informamos al usuario
try:
    import google.generativeai as genai
    from PIL import Image
    librerias_ok = True
except ImportError:
    librerias_ok = False

st.title("🏥 Diagnóstico IA")

if not librerias_ok:
    st.error("Error: Las librerías necesarias no están instaladas.")
    st.write("Por favor, verifica tu archivo requirements.txt en GitHub.")
else:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    
    archivo = st.file_uploader("Sube radiografía", type=["jpg", "png"])
    if archivo:
        img = Image.open(archivo)
        st.image(img)
        if st.button('Analizar'):
            respuesta = modelo.generate_content(["Actúa como radiólogo. Analiza esta imagen:", img])
            st.info(respuesta.text)
