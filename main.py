import streamlit as st

st.header('Python Compiler') 

python_input = st.text_input('Type python code')
button_click = st.button('RUN 1 line code')

python_input2 = st.text_area('Type python code')
button_click2 = st.button('Run multiline code')

if button_click == True:
    with st.container():
        text = exec(python_input)
        st.markdown(text)

if button_click2 == True:
    with st.container():
        text = exec(python_input2)
        st.markdown(text)
