import streamlit as st
from datetime import date

st.title("Make chai for you 🥰")

btn = st.button("Make chai")
masala = bool
if btn:
  masala = st.checkbox("Add masala")

if masala:
  Tea_base = st.selectbox("Whice one is your favourit ?",["Milk🐮", "Water🫗", "Lemon🍋"])
  st.success(f"You choose {Tea_base}")

flavour = st.radio("Choose your flavour !", ["lemon", 'tulsi', 'orange', 'chocolate'])
if flavour:
  st.write(f"You choose {flavour}")

suger = st.slider("Sugar label (spoon)", 0,5, 3)
st.success(f"Suger label {suger}")

# st.chat_input
# st.date_input
# st.text_input
# st.time_input
# st.audio_input
# st.camera_input
# st.number_input
# st.datetime_input

cups = st.number_input("How many cups:", min_value=1, max_value=10)
st.success(f"{cups} cups of chai")

name = st.text_input("Enter your name : ")
st.success(f"Welcome ! {name} sir in our Resturant")

dob = st.date_input("Select your BOD", min_value=date(2000, 1,1), max_value=date(2050, 1,5))
st.success(f"Your BOD is : {dob}")

chat = st.chat_input("Enter your chat : ",)
if chat:
  st.success(f"Your chat is : {chat}")

camera = st.camera_input("Enter you pic : ")
# if camera is not None:
#     st.write("This is you : ")
#     st.image(camera)

if camera is not None:
  with open("masum.png", "wb") as f:
    f.write(camera.getbuffer())

  st.success("Image save successfully!")
  st.text("This is you : ")
  st.image(camera)



audio = st.audio_input("Record your voice : ")
# if audio is not None:
#    st.write("This is your voice : ")
#    st.audio(audio)

if audio is not None:
  with open("masum.mp4", "wb") as f:
    f.write(audio.getbuffer())
  
  st.success("Audio save successfully !")
  st.write("This is you voice : ")
  st.audio(audio)



