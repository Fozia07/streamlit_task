import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
        .stTextInput, .stNumberInput, .stRadio {
            font-size: 18px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the calculator
st.title("🧮 Interactive Calculator")

# User input for numbers
num1 = st.number_input("🔢 Enter first number:", step=1.0, value=0.0)
num2 = st.number_input("🔢 Enter second number:", step=1.0, value=0.0)

# Select operation with radio buttons (more interactive than dropdown)
operation = st.radio("➕➖✖️➗ Select an operation:", ["Addition", "Subtraction", "Multiplication", "Division"], horizontal=True)

# Live Calculation
def calculate():
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        return num1 / num2 if num2 != 0 else "❌ Error: Division by zero!"

# Show result dynamically
result = calculate()

# Display result only if user changes inputs
if result != "❌ Error: Division by zero!":
    st.success(f"✅ **Result:** {result}")
else:
    st.error(result)
