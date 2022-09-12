import streamlit as st
import os

st.header('Python Compiler') 

python_input = st.text_input('Type python code')
button_click = st.button('RUN 1 line code')

python_input2 = st.text_area('Type python code')
button_click2 = st.button('Run multiline code')

if button_click == True:
    with st.container():
        os.system('touch python1.py')
        os.system(f'echo {python_input} > python1.py')
        text = os.popen('python python1.py').read()
        st.markdown(text)

if button_click2 == True:
    with st.container():
        os.system('touch python2.py')
        os.system(f'echo {python_input2} > python2.py')
        text = os.popen('python python2.py').read()
        st.markdown(text)
