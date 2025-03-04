import streamlit as st
# streamlit run app.py


st.title("Streamlit for MLOps Demo")

st.header("Heading of Streamlit")

st.subheader("Sub-Heading of Streamlit")

st.text("This is an Example Text")

st.success("Success")
st.warning("Warning")
st.info("Information")
st.error("Error")

if st.checkbox("Select/Unselect"):
    st.text("User selected the checkbox")
else:
    st.text("User has not selected the checkbox")

state = st.radio("What is your favorite Color ?", 
("Red","Green","Yellow"))

if state == "Yellow":
    st.success("Thats my favorite color as well!")

occupation = st.selectbox("What do you do ?",
["Student","Vlogger","Engineer"])

st.text(f"selected option is {occupation}")

if st.button("Example Button"):
    st.error("You clicked it")

st.sidebar.header("Heading of sidebar")
st.sidebar.text("Created by Shreyash")