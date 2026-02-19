import streamlit as st

st.title("Hello Streamlit 🚀")
st.subheader("Hi, I am abdullah")
st.text("How are you?")
st.write("UV diye run hocche!")

lag = st.selectbox("You favrourit language : ", ['c/c++', 'python', 'java', 'javascript'])

st.write(f"You choose {lag}. Good choice")

if lag == 'c/c++':
  st.success("Mother of Programming Language")
elif lag == 'python':
  st.success("Easy Syntax")
elif lag == 'java':
  st.success("Good for security")
else:
  st.success("Good for MERN")


name  = st.checkbox("Male")
year = st.checkbox("Female")

if name:
  male_name = st.radio("Male Name : ",['masum', 'noman', 'shafi'])
  st.write(f"You choose : ", male_name)
if year:
  female_name = st.radio("Female Name : ", ["Fatema", "Ayesha", "Mariyam"])
  st.write("You choose : ", female_name)

# st.subheader(f"{male_name} and {female_name} are cuple")
