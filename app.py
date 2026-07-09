import streamlit as st

st.set_page_config(page_title="Global Health Vision", layout="centered")

st.title("🏥 Global Health Vision")
st.subheader("Plataforma de Diagnóstico Asistido")

st.write("Bienvenida, Mery. Esta es tu plataforma profesional.")

st.info("Selecciona el módulo de diagnóstico para comenzar:")

modulo = st.radio("Especialidad:", ["Traumatología", "Tórax", "Neurología"])

if st.button("Acceder al módulo"):
    st.write(f"Has seleccionado: {modulo}")
    st.warning("Próximamente: Integración con IA para análisis de imágenes.")
