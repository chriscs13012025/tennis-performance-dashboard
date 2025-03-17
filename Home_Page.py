import streamlit as st

# Set up the homepage
st.title("Christophe Clement's Web App")
st.subheader("CS 1301 - Intro to Computing")

st.write("Welcome to my multi-page Streamlit app! Use the sidebar to navigate between pages.")

# Describe the available pages
st.write("### Pages:")
st.write("1. **Portfolio**: Showcases my projects and experiences.")
st.write("2. **Data Visualization**: Interactive charts and graphs.")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Portfolio", "Data Visualization"])

if page == "Portfolio":
    import Portfolio  # Make sure Portfolio.py exists and is implemented
    Portfolio.show()
elif page == "Data Visualization":
    import PhaseII  # Make sure PhaseII.py is implemented
    PhaseII.show()
