import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(
    page_title="Mi App Completa",
    page_icon="📂",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("🔍 Mi Aplicación Streamlit Completa")
st.write("Una aplicación con múltiples funcionalidades y componentes interactivos")

# Barra lateral para navegación
st.sidebar.title("📊 Navegación")
app_mode = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["🏠 Inicio", "📈 Análisis de Datos", "📊 Visualizaciones", "🧮 Calculadora", "ℹ️ Acerca de"]
)

# Sección de Inicio
if app_mode == "🏠 Inicio":
    st.header("Bienvenido a la aplicación")
    st.write("""
    Esta es una aplicación completa de Streamlit que incluye:
    - Análisis de datos
    - Visualizaciones interactivas
    - Herramientas de cálculo
    - Y mucho más...
    """)
    
    # Crear datos de ejemplo
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Usuarios", "1,234", "+123")
    
    with col2:
        st.metric("Ingresos", "$45,678", "+12%")
    
    with col3:
        st.metric("Tasa de Conversión", "23.5%", "-2%")

# Sección de Análisis de Datos
elif app_mode == "📈 Análisis de Datos":
    st.header("Análisis de Datos")
    
    # Cargar o crear datos
    uploaded_file = st.file_uploader("Sube un archivo CSV", type=['csv'])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        # Datos de ejemplo
        data = {
            'Fecha': pd.date_range(start='2024-01-01', periods=100, freq='D'),
            'Ventas': np.random.randint(100, 1000, 100),
            'Clientes': np.random.randint(10, 200, 100),
            'Producto': np.random.choice(['A', 'B', 'C', 'D'], 100)
        }
        df = pd.DataFrame(data)
    
    # Mostrar datos
    st.subheader("Vista previa de los datos")
    st.dataframe(df.head(), use_container_width=True)
    
    # Estadísticas
    st.subheader("Estadísticas descriptivas")
    st.write(df.describe())
    
    # Filtros
    st.subheader("Filtros")
    col1, col2 = st.columns(2)
    
    with col1:
        if 'Producto' in df.columns:
            productos = st.multiselect(
                "Selecciona productos:",
                options=df['Producto'].unique(),
                default=df['Producto'].unique()[:2]
            )
            if productos:
                df = df[df['Producto'].isin(productos)]
    
    with col2:
        if 'Ventas' in df.columns:
            ventas_min, ventas_max = st.slider(
                "Rango de ventas:",
                min_value=int(df['Ventas'].min()),
                max_value=int(df['Ventas'].max()),
                value=(int(df['Ventas'].min()), int(df['Ventas'].max()))
            )
            df = df[(df['Ventas'] >= ventas_min) & (df['Ventas'] <= ventas_max)]

# Sección de Visualizaciones
elif app_mode == "📊 Visualizaciones":
    st.header("Visualizaciones Interactivas")
    
    # Crear datos para gráficos
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Matplotlib")
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Seno', color='blue')
        ax.plot(x, y2, label='Coseno', color='red')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
    
    with col2:
        st.subheader("Plotly")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='Seno'))
        fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='Coseno'))
        fig.update_layout(
            title='Gráfico interactivo',
            xaxis_title='X',
            yaxis_title='Y'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Gráfico de barras con Seaborn
    st.subheader("Seaborn - Gráfico de barras")
    data = pd.DataFrame({
        'Categoría': ['A', 'B', 'C', 'D', 'E'],
        'Valores': np.random.randint(10, 100, 5)
    })
    
    fig, ax = plt.subplots()
    sns.barplot(data=data, x='Categoría', y='Valores', ax=ax, palette='viridis')
    ax.set_title('Distribución por categoría')
    st.pyplot(fig)

# Sección de Calculadora
elif app_mode == "🧮 Calculadora":
    st.header("Calculadora")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        num1 = st.number_input("Número 1", value=0.0)
    
    with col2:
        operation = st.selectbox(
            "Operación",
            ["Suma", "Resta", "Multiplicación", "División", "Potencia"]
        )
    
    with col3:
        num2 = st.number_input("Número 2", value=0.0)
    
    # Realizar cálculo
    result = None
    if operation == "Suma":
        result = num1 + num2
    elif operation == "Resta":
        result = num1 - num2
    elif operation == "Multiplicación":
        result = num1 * num2
    elif operation == "División":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("No se puede dividir por cero")
    elif operation == "Potencia":
        result = num1 ** num2
    
    if result is not None:
        st.success(f"**Resultado:** {result}")
    
    # Calculadora científica adicional
    st.subheader("Funciones científicas")
    col1, col2 = st.columns(2)
    
    with col1:
        angle = st.slider("Ángulo (grados)", 0, 360, 45)
        st.write(f"Sen({angle}°) = {np.sin(np.radians(angle)):.4f}")
        st.write(f"Cos({angle}°) = {np.cos(np.radians(angle)):.4f}")
    
    with col2:
        exp_input = st.number_input("Número para exponencial", value=1.0)
        st.write(f"exp({exp_input}) = {np.exp(exp_input):.4f}")
        st.write(f"log({exp_input}) = {np.log(exp_input) if exp_input > 0 else 'Indefinido'}")

# Sección Acerca de
elif app_mode == "ℹ️ Acerca de":
    st.header("Acerca de esta aplicación")
    
    st.write("""
    ## Mi Aplicación Streamlit Completa
    
    **Versión:** 1.0.0
    
    **Descripción:**
    Esta es una aplicación demostrativa creada con Streamlit que muestra
    diversas funcionalidades y componentes disponibles en la biblioteca.
    
    **Características incluidas:**
    1. Análisis de datos con pandas
    2. Visualizaciones con Matplotlib, Seaborn y Plotly
    3. Componentes interactivos
    4. Calculadora básica y científica
    
    **Tecnologías utilizadas:**
    - Python 3.x
    - Streamlit
    - Pandas, NumPy
    - Matplotlib, Seaborn, Plotly
    """)
    
    st.info("""
    💡 **Consejo:** Para ejecutar esta aplicación, usa el comando:
    ```
    streamlit run app.py
    ```
    """)

# Pie de página
st.sidebar.markdown("---")
st.sidebar.info("© 2024 Mi App Completa. Todos los derechos reservados.")
