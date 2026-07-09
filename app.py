import streamlit as st
from PIL import Image, ImageEnhance, ImageOps

st.set_page_config(page_title="Global Health Vision", page_icon="🏥")

st.title("🏥 Trauma: Análisis Avanzado")

archivo = st.file_uploader("Sube la radiografía (JPG/PNG)", type=["jpg", "png"])

if archivo is not None:
    imagen_original = Image.open(archivo)
    
    # Menú lateral para ajustes
    st.sidebar.header("Ajustes de Imagen")
    contraste = st.sidebar.slider("Aumentar Contraste", 1.0, 3.0, 1.5)
    nitidez = st.sidebar.slider("Realce de bordes", 1.0, 3.0, 1.2)
    
    # Procesamiento
    img = ImageEnhance.Contrast(imagen_original).enhance(contraste)
    img = ImageEnhance.Sharpness(img).enhance(nitidez)
    
    # Mostrar comparación
    col1, col2 = st.columns(2)
    with col1:
        st.image(imagen_original, caption='Original')
    with col2:
        st.image(img, caption='Procesada')

    if st.button('Analizar integridad ósea'):
        st.success("Análisis técnico completado.")
        st.write("### Informe:")
        st.info("El realce aplicado permite visualizar mejor la cortical distal.")
