import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="IA Trauma Diagnostic", page_icon="🏥")
st.title("🏥 Diagnóstico IA: Trauma")

# Entrenamos un modelo simple en tiempo real
# (Simulamos características: Densidad, Bordes, Intensidad)
X_train = np.array([[10, 2, 80], [80, 70, 10], [15, 5, 75], [90, 80, 5]])
y_train = np.array([0, 1, 0, 1]) # 0: Sano, 1: Fractura
modelo = RandomForestClassifier().fit(X_train, y_train)

archivo = st.file_uploader("Sube una imagen para análisis", type=["jpg", "png"])

if archivo is not None:
    st.image(archivo, caption='Análisis en curso...', use_column_width=True)
    if st.button('Analizar con IA'):
        # Simulamos extracción de datos de la imagen
        datos_imagen = np.array([[np.random.randint(0, 100), np.random.randint(0, 100), np.random.randint(0, 100)]])
        prediccion = modelo.predict(datos_imagen)
        
        st.write("### Resultado del Modelo:")
        if prediccion[0] == 1:
            st.error("🚨 ALERTA: Patrón compatible con fractura.")
        else:
            st.success("✅ Diagnóstico: Tejido óseo íntegro.")
