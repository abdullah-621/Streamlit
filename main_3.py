import streamlit as st

st.title("Chai APP")

col1, col2 = st.columns(2)

with col1:
  st.header("Masla chai")
  st.image("https://images.pexels.com/photos/14654380/pexels-photo-14654380.jpeg", width=200)
  vote1 = st.button("Vote masala chai")

with col2:
  st.header("Adrak")
  st.image("https://images.pexels.com/photos/5974071/pexels-photo-5974071.jpeg", width=200)
  vote2 = st.button("Vote Adrak chai")

if vote1:
  st.success("Thanks for voting masala chai ")
if vote2:
  st.success("Thanks for voting Adrak chai")

# todo : SideBar

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Select your chai " ,["Option","Masala Chai", "Adrak Chai", "Kesar Chai"])

st.write(f"Hello {name} ! Thanks for you chossing 🥰")

with st.expander("Show Chai Making Instruction"):
  st.write("""
  1. Boil water with tea leaves
  2. Add milk and spices
  3. Serve hot
""")
  
st.markdown(f"## Hello {name} Welcome to Chai App")
st.markdown('> Blockquote')


casual, formal = st.columns(2)

def Casual_Pic():
  with open("masum_casual.jpg", "rb") as f:
    pic_casual = f.read()
  with casual:
    st.markdown("## Abdullah Al Masum")
    st.image(pic_casual, width=200)
    st.markdown('> A motivated CSE student aiming to build a career in AI and Machine Learning. Skilled in C++, Python, and Data Structures & Algorithms with strong problem-solving ability. Interested in working on real-world projects and continuously improving technical skills.')

def Formal_pic():
  with open("masum_formal.png", "rb") as f:
    pic_fromal = f.read()
  with formal:
    st.markdown("## Abdullah Al Masum")
    st.image(pic_fromal, width=200)
    st.markdown('> A motivated CSE student aiming to build a career in AI and Machine Learning. Skilled in C++, Python, and Data Structures & Algorithms with strong problem-solving ability. Interested in working on real-world projects and continuously improving technical skills.')


# if vote1:
#   Casual_Pic()
# if vote2:
#   Formal_pic()

if tea == "Masala Chai" :
  Casual_Pic()
elif tea == "Adrak Chai":
  Formal_pic()
else:
  st.error("No One here 😒")

