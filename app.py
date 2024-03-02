import streamlit as st


st.set_page_config(page_title="python web",layout="wide")

with st.container():
     st.title("Hi,I am Babu Natarajan")
st.subheader("front end developer")

st.write("I As a fresher, l am looking for a good platform to start my career. although l don't have any work experience if l get chance l will enhance my ability & skills and l hope. I am a Friendly Person and a Creative Thinker. It's all about me.")
st.write("[linkedin](www.linkedin.com/in/-babu-natarajan-43-)")


with st.container():
 st.write("---")
 left_column,right_column=st.columns(2)
 with left_column:
    st.header("skills")
    st.write("##")
    st.write("Python")
    st.write("Front end development")
    st.write("Git & GitHub")
    

with st.container():
 st.write("---")
 st.header("PROJECT")
 st.write("##")
 st.write("Website using Python and Streamlit")
 st.write("Website using Python and Streamlit")

with st.container():
 st.write("---")
 st.header("Certifications ")
 st.write("##")
 st.subheader("udemy")
 st.write(" Web Development Bootcamp")
 st.subheader("Nptel")
 st.write(" Sustainable Power Generation Systems")







with st.container():
 st.write("---")
 st.header("contact ")
 st.write("##")
 st.subheader("Gmail")
st.write("babunatarajan43@gmail.com")
contact_from="""
<form action="https://formsubmit.co/#" method="POST">
     <input type="text" name="name" placeholder="Your name "equired>
     <input type="email" name="email" placeholder="Your email "required>
     <textaera name="message" placeholder="Your message here "required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column,right_column=st.columns(2)
with left_column:
   st.markdown(contact_from,unsafe_allow_html=True)
   with right_column:
      st.empty()