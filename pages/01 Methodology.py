import streamlit as st
import streamlit.components.v1 as components

def main():
    # Set page title and favicon
    st.set_page_config(
        page_title="Real Estate Project Methodology",
        page_icon="🏠",
        layout="wide"
    )

    # Page Title and Introduction
    st.title("Real Estate Exploration Methodology")
    st.write(
        "Welcome to the methodology page, providing an in-depth look into the approach for exploring the real estate market in Barcelona. "
        "Below are the detailed steps and methodologies employed to derive meaningful insights."
    )

    # Methodology Sections
    st.header("1. Data Collection 📊")
    st.write(
        "In this project, I had the privilege of working with a curated dataset provided by a private company in the business."
        "Due to privacy reasons any of the data sets will be published into GitHub"
    )

    st.header("2. Tableau Visualizations 🗺️")
    st.write(
        "Tableau was chosen for its unparalleled ability to transform data into interactive visualizations. "
        "The visualizations provide a panoramic view of Barcelona's real estate landscape, highlighting trends and patterns for informed decision-making."
        "Such as a company looking to invest on Real Estate or a family new to barcelona looking for a place to live"
    )

    st.header("3. Predictive Modeling 📈")
    st.write(
        "The predictive model, grounded in advanced analytics using h2o, which calculates the best combination of regression models possible. It estimates property prices based on a multitude of characteristics. "
        "Users can input specific features and receive insights into the potential market value, adding a forward-looking dimension to the exploration of Barcelona's real estate market."
    )

    st.header("4. User Interaction 🚀")
    st.write(
        "Designed with user interaction in mind, our project offers a seamless experience. "
        "Users can dynamically engage with visualizations, and harness the predictive model to make data-driven decisions in the dynamic Barcelona real estate landscape."
    )

    st.header("5. Challenges and Solutions 🛠️")
    st.write(
        "Throughout the project journey, I navigated challenges, from data complexities to model fine-tuning. "
        "My commitment to excellence resulted in innovative solutions, enriching the user experience and ensuring the robustness of my insights, ensuring the best results possible based on the data provided."
    )

    st.header("6. Future Enhancements 🚀")
    st.write(
        "This project is a living entity, open to continuous evolution. "
        "Future enhancements may include additional visualizations, expanded SQL query functionalities, or the integration of cutting-edge modeling techniques, all aimed at providing users with deeper insights and a richer exploration experience."
        "Any sort of data provided is welcome to improve and upgrade the model"
    )

    st.markdown(
        "### Conclusion\n"
        "My methodology combines advanced analytics, interactive visualizations, and tailored queries to offer users a comprehensive understanding of the dynamic Barcelona real estate market."
    )

if __name__ == "__main__":
    main()