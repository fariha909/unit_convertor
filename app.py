import streamlit as st

st.set_page_config(page_title="Unit Convertor App")
st.title("UNIT CONVERTOR")
category = st.selectbox("Select Category",["Length","Weight"])

def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "feets": 3.28084
    }
    return value * conversion_factors[to_unit] / conversion_factors [from_unit]

def weight_convertor(value, from_unit, to_unit):
    conversion_factors = {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounces": 0.035274
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]
    
if category == "Length":
    units = ["meters","kilometers","miles","feet"]
    value =  st.number_input("Enter the Value")
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} is {result:.4f} {to_unit}")

elif category == "Weight":
    units = ["grams","kilograms","pounds","ounces"]
    value = st.number_input("Enter the Value")
    from_unit = st.selectbox("From unit", units)
    to_unit = st.selectbox("To unit", units)
    if st.button("Convert") :
        result = weight_convertor(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} is {result:.4f} {to_unit}")