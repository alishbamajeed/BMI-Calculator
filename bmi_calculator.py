import streamlit as st
import time

# App configuration
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# App title and description
st.title("🧮 BMI Calculator")
st.markdown("""
## Calculate your Body Mass Index (BMI)
Enter your weight and height below to find out your BMI and health status.
""")

# Calculator-style layout
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg):", min_value=1.0, format="%.2f")

with col2:
    height = st.number_input("Height (m):", min_value=0.1, format="%.2f")

# Calculate BMI if inputs are valid
if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.subheader("Your BMI is:")
    st.markdown(f"<h1 style='text-align: center; color: #4CAF50;'>{bmi:.2f}</h1>", unsafe_allow_html=True)

    # BMI Categories
    if bmi < 18.5:
        st.error("Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("Normal weight")
    elif 25 <= bmi < 29.9:
        st.warning("Overweight")
    else:
        st.error("Obesity")
else:
    st.info("Please enter valid weight and height.")

# Footer
st.markdown("""
---
**Built with ❤️ using Streamlit**
""")
