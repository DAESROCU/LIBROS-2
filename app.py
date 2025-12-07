import streamlit as st
import matplotlib.pyplot as plt

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Tracker de Lectura", page_icon="📚")

st.title("📚 Tracker: Karamazov vs Roma")
st.write("Control de avance y nivelación de lectura.")

# --- 2. DATOS FIJOS DE LOS LIBROS ---
# Aquí están las páginas fijas que me diste
libro1_nombre = "Los Hermanos Karamazov"
libro1_total = 876

libro2_nombre = "Roma Soy Yo"
libro2_total = 746

# --- 3. ENTRADA DE DATOS ---
col1, col2 = st.columns(2)

with col1:
    st.info(f"**{libro1_nombre}**")
    st.caption(f"Total: {libro1_total} páginas")
    # max_value impide que pongas un número mayor al total del libro
    libro1_actual = st.number_input(
        "Pág. Actual (Karamazov)", 
        min_value=0, 
        max_value=libro1_total, 
        value=0,
        step=1
    )

with col2:
    st.info(f"**{libro2_nombre}**")
    st.caption(f"Total: {libro2_total} páginas")
    # max_value impide que pongas un número mayor al total del libro
    libro2_actual = st.number_input(
        "Pág. Actual (Roma)", 
        min_value=0, 
        max_value=libro2_total, 
        value=0,
        step=1
    )

# --- 4. BOTÓN Y CÁLCULOS ---
if st.button("Calcular Progreso 🚀", type="primary"):
    
    # Cálculos de porcentaje
    porcentaje1 = (libro1_actual / libro1_total) * 100
    porcentaje2 = (libro2_actual / libro2_total) * 100

    st.divider()
    
    # Mostrar porcentajes grandes
    m1, m2 = st.columns(2)
    m1.metric(label="Avance Karamazov", value=f"{porcentaje1:.2f}%")
    m2.metric(label="Avance Roma", value=f"{porcentaje2:.2f}%")

    # --- 5. LÓGICA DE NIVELACIÓN (REGLA DE 3) ---
    st.subheader("⚖️ Veredicto")
    
    if abs(porcentaje1 - porcentaje2) < 0.1:
        st.success("✅ ¡Estás perfectamente nivelado en ambos libros!")
    
    elif porcentaje1 > porcentaje2:
        # Karamazov va ganando, hay que leer Roma
        objetivo_paginas = (porcentaje1 * libro2_total) / 100
        paginas_faltantes = objetivo_paginas - libro2_actual
        
        st.warning(f"⚠️ **{libro2_nombre}** se está quedando atrás.")
        st.write(f"Para igualar el **{porcentaje1:.2f}%** de '{libro1_nombre}', debes leer:")
        st.info(f"➡️ Hasta la página **{int(objetivo_paginas)}** de **{libro2_nombre}**")
        st.caption(f"(Te faltan {int(paginas_faltantes)} páginas para nivelarte).")
        
    else:
        # Roma va ganando, hay que leer Karamazov
        objetivo_paginas = (porcentaje2 * libro1_total) / 100
        paginas_faltantes = objetivo_paginas - libro1_actual
        
        st.warning(f"⚠️ **{libro1_nombre}** se está quedando atrás.")
        st.write(f"Para igualar el **{porcentaje2:.2f}%** de '{libro2_nombre}', debes leer:")
        st.info(f"➡️ Hasta la página **{int(objetivo_paginas)}** de **{libro1_nombre}**")
        st.caption(f"(Te faltan {int(paginas_faltantes)} páginas para nivelarte).")

    # --- 6. GRÁFICOS ---
    st.subheader("📊 Gráficos Visuales")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
    # Colores: Verde para leído, Gris claro para lo que falta
    colors = ['#4CAF50', '#EEEEEE']
    
    # Gráfico 1 (Karamazov)
    ax1.pie([libro1_actual, libro1_total - libro1_actual], 
            labels=['Leído', 'Faltante'], 
            autopct='%1.0f%%', 
            startangle=90, 
            colors=colors,
            explode=(0.05, 0))
    ax1.set_title(f"Karamazov")

    # Gráfico 2 (Roma)
    ax2.pie([libro2_actual, libro2_total - libro2_actual], 
            labels=['Leído', 'Faltante'], 
            autopct='%1.0f%%', 
            startangle=90, 
            colors=colors,
            explode=(0.05, 0))
    ax2.set_title(f"Roma")
    
    # Mostrar gráfico en la app
    st.pyplot(fig)
