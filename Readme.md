# Final Project: Real Estate study and Predictive Model | Marco Ayora Arsic

Link for streamlit:

## Introduction

In this project i will be showing how based on a dataset about the real estate market in Barcelona i have been able to train a predictive model based on 2023 data, as well as visualization done with Tableau and all presented through Streamlit. 

## Data Source 

The Data was obtained through a Real Estate Agency, due to this reason the data won't be published on Github. In the Dataset it is observable the prices of the properties and many characteristics of the properties.

## Methodology

I firstly explored the dataset with pandas. Once i knew the properties of the dataset i proceeded to clean it in order to have only relative data and create two different datasets one that i used for Tableau and the other to train the model. After seeing how time consuming is to try so many regression models to see which fits the best i decided to use h20 which allows to see between all the best combinations of regression models. After having finished the predictive model and making it work in python, i did all the necessary Visualizations on tableau with the help of some geojsons from Barcelona to create geographical visualizations.

## Overview

This project is divided into two different sections. On one hand the predictive model which can be effective for personal use as well as used by companies. In the other hand the insightful visualizations done with Tableau that show in an interactive way how Barcelona's Market is distributed. To present all the work done it is visible through my streamlit which link is at the beginning of this ReadMe file.

## Tableau analysis

Taking a look at the Tableau documents there are in The streamlit we first find Two maps of Barcelona One divided by Districts and the other divided by neighborhoods. The color intensity shows the average price of a property in that specific zone, and the circles the average meter square.

In the second Tableau visualization we have other sort of graphs, firstly at the left 3 positive correlations between the price and mt/square, Quantity of bedrooms, quantity of bathrooms. Finnally in the left the average price based on the build type and typolgy of the property.


## Improvements

This project is a combination of of tools on how based on real current data i created a predictive model that can be used on the market. It is true that due to the limitation of data provided the model couldn't be actually used for real-life practice as it lacks data. Even though beeing trained with more than 30,000 properties from barcelona some of this properties lacked a diversity on prices as well as in carachteristics meaning that the dataset used does not fully represent Barcelona's Real Estate Market causing the malfunctionality in the predictive model depending on how it is used.

## Conclusion

In conclusion, this project provides a thorough examination of Barcelona's real estate market through a dual approach of predictive modeling and interactive visualizations. Utilizing a dataset sourced from a Real Estate Agency, I meticulously cleaned and partitioned the data for Tableau visualizations and predictive model training. The use of H2O streamlined the model development process, yet the resultant predictive model faced limitations stemming from the dataset's insufficient diversity in property prices and characteristics. The Tableau visualizations, accessible through Streamlit, offer valuable insights into Barcelona's market distribution, displaying average property prices and square meter values across districts and neighborhoods. Despite the acknowledged constraints, this project serves as a commendable showcase of integrating various tools for real estate data analysis, emphasizing the need for data inclusivity to enhance the model's practical applicability in capturing the complexities of the market.

## Source links:

Barcelona geojsons = https://github.com/martgnz/bcn-geodata