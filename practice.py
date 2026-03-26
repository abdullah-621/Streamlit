import streamlit as st

st.write("My name is masum")
st.title("Hello world!")
st.subheader("How are you")

lag = st.selectbox("My favourit language : ", ['c', 'c++', 'java', 'python'])

if lag == 'c':
  st.success("Mother of PL")
elif lag == 'python':
  st.success("Easy Syntex")
elif lag == 'java':
  st.success("Good for security")


male_name = st.checkbox("Male")
female_name = st.checkbox("Female")


if male_name:
  name = st.radio("Male Name : ", ['Masum', 'Noman', 'Shafi'])

  st.success(f"Hello {name}")
if female_name:
  name = st.radio("Female Name : ", ["Fatema", "Ayesha", "Mariyam"])
  st.success(f"Hello {name}")


num = st.slider("Your lavel : ", 0,5,1)

text = st.text_input("Enter your name :")
text1 = st.text_area("Enter your name :")
text2 = st.chat_input("Enter your name :")
st.success(text)
st.success(text1)
st.success(text2)

col1, col2, col3 = st.columns(3)

with col1:
  st.header("Masum")
  masum = st.button("vate for masum")

with col2:
  st.header("Noman")
  noman = st.button("vate for noman")

with col3:
  st.header("Ashik")
  ashik = st.button("vate for ashik")

if masum:
  st.subheader("Hi Masum")

if noman:
  st.subheader("Hi Noman")

if ashik:
  st.subheader("Hi Ashik")


name = st.sidebar.text_input("Enter your name")

tea = st.sidebar.selectbox("Select your chai " ,["Option","Masala Chai", "Adrak Chai", "Kesar Chai"])