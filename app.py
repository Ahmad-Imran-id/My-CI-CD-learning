import streamlit as st

n=st.chat_input()

def square(n):
    return n**2

def cube(n):
    return n**3

def fifth_power(n):
    return n**5

st.title("Cube calculater")
st.write('Put in a number that you want the cube of')

n=st.number_input('ENter an integer',value=1,step=1)

st.write(f'square of {n} is {square(n)}')
st.write(f'cube of {n} is {cube(n)}')
st.write(f'fifth power of {n} is {fifth_power(n)}')