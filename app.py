import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="IA Trauma Diagnostic", page_icon="🏥")

st.title("🏥 Trauma: Diagnóstico con IA")

# Simulador de modelo de IA (pre-entrenado)
def predecir_fractura(imagen):
    # Aquí es donde conectaremos el modelo real en el futuro
    # Por ahora, simulamos una lógica de análisis clínico
    probabilidad = np.random.randint(60, 99)
    if probabilidad > 80:
        return "Alta sospecha de fractura", probabilidad
    else:
        return "Baja sospecha / Tejido íntegro", probabilidad

archivo = st.file_uploader("Sube radiografía para diagnóstico IA", type=["jpg", "png"])

if archivo is not None:
    img = Image.open(archivo)
    st.image(img, caption='Imagen analizada', use_column_width=True)
    
    if st.button('Ejecutar Análisis IA'):
        with st.spinner('Procesando patrones óseos...'):
            resultado, conf = predecir_fractura(img)
            
            st.write("### Resultados del Modelo:")
            st.success(f"Diagnóstico: {resultado}")
            st.metric("Confianza de la IA", f"{conf}%")
            
            if conf > 80:
                st.error("Recomendación: Revisión urgente por especialista.")
            else:
                st.info("Recomendación: Hallazgos dentro de la normalidad.")
