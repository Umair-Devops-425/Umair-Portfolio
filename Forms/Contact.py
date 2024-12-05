import re
import streamlit as st
import requests

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZmMDYzNzA0MzM1MjZjNTUzNzUxMzUi_pc"

def is_valid_email(email):
    #email varification using Regex
    email_patter = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_patter, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Full name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not WEBHOOK_URL:
                st.error(
                    "Email Service is not set up. PLease Try agin Later.",
                    icon="✉️"
                )
                st.stop()

        if not name:
            st.error("Please Provide Your name")
            st.stop()

        if not email:
            st.error("Please provide your email address.",icon="✉️")            

        if not is_valid_email(email):
            st.error("Please provide a valid email address.", icon="✉️")
            st.stop()

        if not message:
            st.error("Please Provide a messag.", icon="💬")
            st.stop()

        data = {"Email":email, "name":name, "message":message}
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
            st.success("Your Meessage has been sent successfully!", icon="😊")
        else:
            st.error("There is something error", icon="😱")           