import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="My Complete App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title
st.title("🚀 My Complete Streamlit App")
st.write("An app with multiple functionalities and interactive components")

# Sidebar for navigation
st.sidebar.title("📱 Navigation")
app_mode = st.sidebar.selectbox(
    "Select a section:",
    ["Home", "Data Analysis", "Visualizations", "Calculator", "About"]
)

# Home Section
if app_mode == "Home":
    st.header("Welcome to the App")
    st.write("""
    This is a complete application built with Streamlit.
    
    **Features:**
    - 📊 Data analysis and visualization
    - 📈 Interactive charts
    - 🧮 Calculator tools
    - ⚙️ Customizable settings
    
    Use the sidebar to navigate between sections.
    """)
    
    # Quick metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Users", "1,234", "+123")
    with col2:
        st.metric("Satisfaction", "4.5/5.0", "+0.2")
    with col3:
        st.metric("Active Now", "57", "-3")

# Data Analysis Section
elif app_mode == "Data Analysis":
    st.header("📊 Data Analysis")
    
    # Generate sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=100, freq='D'),
        'Sales': np.random.normal(1000, 200, 100).cumsum() + 5000,
        'Customers': np.random.randint(50, 200, 100),
        'Rating': np.random.uniform(3.5, 5.0, 100),
        'Category': np.random.choice(['A', 'B', 'C', 'D'], 100)
    })
    
    # Show data
    st.subheader("Sample Data")
    st.dataframe(data.head(10))
    
    # Statistics
    st.subheader("Statistics")
    st.write(data.describe())

# Visualizations Section
elif app_mode == "Visualizations":
    st.header("📈 Visualizations")
    
    # Generate data
    np.random.seed(42)
    x = np.arange(50)
    y = np.random.randn(50).cumsum()
    
    # Matplotlib chart
    st.subheader("Matplotlib Chart")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x, y, color='blue', linewidth=2)
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.set_title('Sample Time Series')
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    
    # Interactive chart with Plotly
    st.subheader("Interactive Plotly Chart")
    
    # Create sample data
    categories = ['A', 'B', 'C', 'D']
    values = np.random.randint(10, 100, 4)
    
    fig_plotly = go.Figure(data=[
        go.Bar(x=categories, y=values, marker_color=['red', 'green', 'blue', 'purple'])
    ])
    
    fig_plotly.update_layout(
        title="Sales by Category",
        xaxis_title="Category",
        yaxis_title="Sales",
        template="plotly_white"
    )
    
    st.plotly_chart(fig_plotly, use_container_width=True)

# Calculator Section
elif app_mode == "Calculator":
    st.header("🧮 Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Basic Calculator")
        num1 = st.number_input("First number", value=0.0)
        num2 = st.number_input("Second number", value=0.0)
        
        operation = st.selectbox(
            "Operation",
            ["Addition", "Subtraction", "Multiplication", "Division"]
        )
        
        if st.button("Calculate"):
            if operation == "Addition":
                result = num1 + num2
            elif operation == "Subtraction":
                result = num1 - num2
            elif operation == "Multiplication":
                result = num1 * num2
            elif operation == "Division":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            
            st.success(f"Result: {result}")
    
    with col2:
        st.subheader("Password Generator")
        length = st.slider("Password length", 6, 20, 12)
        
        if st.button("Generate Password"):
            import random
            import string
            
            characters = string.ascii_letters + string.digits + "!@#$%^&*"
            password = ''.join(random.choice(characters) for _ in range(length))
            st.code(password, language="text")

# About Section
else:
    st.header("ℹ️ About")
    
    st.write("""
    ## About This App
    
    This application was created to demonstrate the capabilities of Streamlit.
    
    **Technologies used:**
    - Streamlit for the web interface
    - Pandas for data manipulation
    - NumPy for numerical operations
    - Matplotlib and Plotly for visualizations
    
    **Features:**
    - Interactive data visualization
    - Real-time calculations
    - Responsive design
    - User-friendly interface
    
    This app is deployed on Streamlit Cloud and is accessible to everyone.
    """)
    
    # Contact info
    with st.expander("Contact Information"):
        st.write("""
        - **Email:** example@email.com
        - **GitHub:** github.com/username
        - **Created on:** January 2024
        """)
    
    # App info
    st.info(f"App last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Footer
st.divider()
st.caption("© 2024 - My Streamlit App | Built with ❤️ using Streamlit")
