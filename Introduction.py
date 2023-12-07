import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs
import pandas as pd

#Function with html to align text on bothh sides
def justified_text(text):
    html_code = f"""
    <style>
        p {{
            text-align: justify;
            text-justify: inter-word;
        }}
    </style>
    <div>
        {text}
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)


st.set_page_config(
     page_title="BCN RS study",
     page_icon=":house:",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get help': "https://www.filmaffinity.com/es/film160882.html",
         'About': "*Ezequiel 25:17*. The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness. For he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy my brothers. And you will know I am the Lord when I lay my vengeance upon you."
     }
 )


st.title("Barcelona Real State Study")

st.header("IronHack final project")

#cover immage from image folder
cover = Image.open("Images/vistas_bcn.jpg")

st.image(cover, use_column_width=True)
# If I don`t use the "st.", NOTHING will be shown. Although it is useful for saving variables and calculate a bunch of stuff (really useful if you want to import functions and libraries or use Machine Learning in you code)
st.write(
    "This project is designed to empower users with a comprehensive understanding of the dynamic Real Estate market in Barcelona, Spain. Divided into three distinct components, it offers an insightful exploration of the city's property landscape.",
    font={'size': 25})

project_info = {
    "Title": "Real State Study",
    "Location": "Barcelona, Spain",
    "This project is powered by a combination of tools and technologies. Here are some of the key tools used": 
    "Python-Jupyter Notebooks-Git and GitHub-Tableau-h2o-Streamlit.",
    "Last update": " 07/12/2023",
    "Acknowledgments": "IronHack Team(Fernando Costa, Santiago Aguilar and Begoña Ripoll)",
}

Project_Overview = """
This multifaceted project delves into the intricate dynamics of the real estate market in Barcelona, Spain. 
Offering users a comprehensive understanding through three distinct components: Tableau visualizations, SQL queries, and a predictive modeling framework.
"""

# Columns: A way of splitting equally your text. You can have as much as you want
col1, col2 = st.columns(2)

# Left Column
col1.subheader("**General Information**")
for key, value in project_info.items():
    col1.write(f"**{key}:** {value}")

# Right column
col2.subheader("*Project Overview*")
col2.write(Project_Overview)