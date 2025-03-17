import streamlit as st
import info
import pandas as pd


def about_me_section():
    st.header("About Me")
    st.write(info.about_me)
    st.write("---")

about_me_section()


def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Follow my journey on Instagram")
    instagram_link = f'<a href="{info.my_instagram_url}"><img src="{info.instagram_image_url}" alt="Instagram" width="65" height="65"></a>'
    st.sidebar.markdown(instagram_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)

links_section()


def tennis_career_section(tennis_data):
    st.header("🎾 Tennis Career")
    for achievement in tennis_data["achievements"]:
        st.write(f"- {achievement}")
    st.write("---")

tennis_career_section(info.tennis_data)


def education_section(education_data):
    st.header("🎓 Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Major:** {education_data['Major']}")
    st.write(f"**Expected Graduation:** {education_data['Graduation Date']}")
    st.write("---")

education_section(info.education_data)


def future_goals_section(future_goals):
    st.header("🚀 Future Goals")
    for goal in future_goals:
        st.write(f"- {goal}")
    st.write("---")

future_goals_section(info.future_goals)


def contact_section():
    st.header("📩 Contact Me")
    st.write(f"**Email:** {info.my_email_address}")
    st.write(f"**LinkedIn:** [{info.my_linkedin_url}]({info.my_linkedin_url})")
    st.write(f"**Instagram:** [{info.my_instagram_url}]({info.my_instagram_url})")
    st.write("---")

contact_section()



