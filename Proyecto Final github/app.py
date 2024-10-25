import streamlit as st
import pandas as pd  
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df_perfumes = pd.read_csv("final_df2.csv")


# Estilos personalizados para el fondo
st.markdown(
    """
    <style>
    .stApp {
        background-color: #8ffaed;  /* Fondo color salmón */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Agregar un banner con imagen
st.image("OIP.jfif", use_column_width=True)



# Interfaz Streamlit
st.title("¿Cansado de tu perfume?")


perfume_seleccionado = st.selectbox("Selecciona tu perfume", df_perfumes['Name'])


if perfume_seleccionado:
    # Mostrar la imagen del perfume seleccionado
    perfume_info = df_perfumes[df_perfumes['Name'] == perfume_seleccionado].iloc[0]
    st.image(perfume_info['Image URL'], caption=perfume_seleccionado, width=150)

    cluster_seleccionado = df_perfumes[df_perfumes['Name'] == perfume_seleccionado]['cluster'].values[0]
    recomendaciones = df_perfumes[(df_perfumes['cluster'] == cluster_seleccionado) & (df_perfumes['Name'] != perfume_seleccionado)].head(5)
    st.header("Perfumes Que Deberias Probar")
    for index, perfume in recomendaciones.iterrows():
        st.write(f"- {perfume['Name']}")
        st.image(perfume['Image URL'], width=100) 
else:
    st.write("Selecciona un perfume para obtener recomendaciones.")



