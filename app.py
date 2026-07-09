import streamlit as st
from PIL import Image

st.set_page_config(page_title="Global Health Vision", page_icon="🏥")

st.title("🏥 Global Health Vision: Trauma")
st.subheader("Análisis de Radiografía - Módulo de Urgencias")

# Subida de archivo
archivo = st.file_uploader("Sube la radiografía (JPG/PNG)", type=["jpg", "png"])

if archivo is not None:
    imagen = Image.open(archivo)
    st.image(imagen, caption='Imagen en estudio', use_column_width=True)
    
    if st.button('Analizar fractura'):
        with st.spinner('Evaluando integridad ósea...'):
            # Aquí simulamos el análisis técnico
            st.success("Análisis realizado con éxito")
            st.write("### Informe Preliminar:")
            st.info("- **Hallazgo:** Se observa discontinuidad en la cortical del radio distal.")
            st.warning("- **Sugerencia:** Valorar proyección lateral para confirmar angulación.")

st.divider()
st.caption("Sistema de apoyo al diagnóstico - Mery © 2026")
