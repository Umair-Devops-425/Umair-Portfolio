import streamlit as st

from Forms.Contact import contact_form

# Contact_Function

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# Section1
col1, col2 = st.columns(2,gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/A2.png",width=230)
with col2:
    st.title("Mohd Umair", anchor=False)
    st.write(
        "DevOps Aspirint, Highly skilled Junior DevOps Engineer"
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()

        
#---Education-- 
st.write("\n")
st.subheader("Education", anchor=False)
st.write(
    """
    - Diploma In Engineering, Jamia Millia Islamia, New Delhi.
    - B.Tech, Bhopal Institute of Technology and Science, Bhopal.
    """
)

#---Skills--
st.write("\n")
st.subheader("Technical Skills")
st.write(
    """
    - Technology : DevOps.
    - Programming Language : Python, Angular, C.
    - Data Structure : Basic in DSA.
    """
)