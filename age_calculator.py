import streamlit as st
import datetime

today = datetime.date.today()

date_of_birth = st.date_input("Enter your dob : ", min_value=datetime.date(1900, 1, 1))

if date_of_birth:
  st.write("Your DOB is : ", date_of_birth)

  age = {
    "years" : today.year - date_of_birth.year,
    "months" : today.month - date_of_birth.month,
    "days" : today.day - date_of_birth.day
  }

  if age["days"] < 0:
        age["months"] -= 1
        # Add days of previous month
        prev_month = today.month - 1 or 12
        days_in_prev_month = (datetime.date(today.year, prev_month % 12 + 1, 1) - datetime.timedelta(days=1)).day
        age["days"] += days_in_prev_month

  if age["months"] < 0:
        age["years"] -= 1
        age["months"] += 12

st.subheader(f"Your age is : {age['years']} years {age['months']} months {age['days']} days" )


