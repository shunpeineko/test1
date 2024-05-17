import streamlit as st
import pandas as pd
import time

st.title("streamlit Tutorial")

input_num = st.number_input("Input a number", value=0)
result = input_num ** 2

st.write("Result: ", result)

if "fnumD" not in st.session_state: 
    st.session_state.fnumD = { 0:" ", 1:" ", 2:" "}
if "fcolD" not in st.session_state: 
    st.session_state.fcolD = { 0:" ", 1:" ", 2:" "}
if "fseaD" not in st.session_state: 
    st.session_state.fseaD = { 0:" ", 1:" ", 2:" "}
if "faniD" not in st.session_state: 
    st.session_state.faniD = { 0:" ", 1:" ", 2:" "}

option0 = st.radio(
    "Who are you?",
    [0,1,2]
    )

option = st.radio(
    "Which number do you like best?", 
    ["1", "2", "3","4","5","6","7","8","9","10"]
)


st.write(f"You like {option}. OK?")

option2 = st.multiselect(
    "What are your favorite colors",
    ["Green","Yellow","Red","Blue","Black","Brown","Pink",
     "Purple","Lightgreen","Lightblue","White","orange"]
    )

option3 = st.multiselect(
    "What are your facorite seasons",
    ["spring","summer","fall(autumn)","winter"]
    )

option4 = st.multiselect(
    "What are your facorite animals",
    ["dog","cat","sparrow","monkey","turtle","snake",
     "hamster","mouse","lizard","frog","pig","horse","caw",
     "zebra","pigeon","beetle","butterfly","rabbit",
     "elephant","giraffe","penguin","seal","killer whale",
     "whale","dolphin","gorilla","tiger","hippopotamus",
     "kappa","lion","hedgehog","people","panda",
     "shoebill stork","flamingo","squirrel","koala",
     "shimaenaga","sheep","capybara","alpaca","kangaroo",
     "goat","raccoon","deer","reindeer","beer","polar beer",
     ]
    )


if st.button("確定"):
    st.session_state.fnumD[option0] = option
    st.session_state.fcolD[option0] = f"{option2}"
    st.session_state.fseaD[option0] = f"{option3}"
    st.session_state.faniD[option0] = f"{option4}"
    
    df = pd.DataFrame({
        "name": ["Shunpei","Satoko","Norihisa"] ,
        "favorite number": [st.session_state.fnumD[i] for i in range(3) ],
        "favorite colors": [st.session_state.fcolD[i] for i in range(3) ],
        "favorite seasons": [st.session_state.fseaD[i] for i in range(3) ],
        "favorite animals": [st.session_state.faniD[i] for i in range(3) ],
        "gender": ["male", "female","male"]
    })
    st.dataframe(df)

value = st.slider("Select a value", 0, 10000, 5000)
input_num2 = st.number_input("Input a number2", value=0)
ans = value ** input_num2
if st.button("start"):
    with st.spinner("I am thinking..."):
        time.sleep(3)
        st.write(f"Oh! {value}**{input_num2}={ans}!")
if st.button("Say hello"):
    st.write("Hello World!")
if st.checkbox("Show/Hide"):
    st.write("Happy nyannko!nyannko!!")

import numpy as np
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

def plot_graph():
    x = np.linspace(-7, 7, 100)
    y = np.sin(x)
    plt.plot(x, y)
    st.pyplot()

if st.button('Plot graph'):
    plot_graph()
