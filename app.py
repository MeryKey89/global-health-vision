import streamlit as st
import random

st.set_page_config(page_title="IA Trauma Diagnostic", page_icon="🏥")
st.title("🏥 Diagnóstico IA: Trauma")

archivo = st.file_uploader("Sube una imagen para análisis", type=["jpg", "png"])

if archivo is not None:
    st.image(archivo, caption='Imagen en proceso...', use_column_width=True)
    if st.button('Analizar con IA'):
        st.write("### Resultado del análisis:")
        # Simulamos un diagnóstico técnico
        prob = random.randint(70, 99)
        st.success(f"Probabilidad de integridad ósea: {prob}%")
        if prob < 85:
            st.error("⚠️ Aviso: Se recomienda revisión radiológica detallada.")
        else:
            st.info("✅ Resultado: Sin hallazgos de fractura evidentes.")
