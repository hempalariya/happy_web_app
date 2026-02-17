import streamlit as st
import plotly.express as px
import csv

st.title("In Search for happiness")
x_axis = st.selectbox("Select data for the x-axis",
                     ("GDP", "Happiness", "Generosity"))
y_axis = st.selectbox("Select data for the y-axis",
                      ("GDP", "Happiness", "Generosity"))

gdp = []
happiness = []
generosity = []

with open("happy.csv", "r") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        gdp.append(float(row["gdp"]))
        happiness.append(float(row["happiness"]))
        generosity.append(float(row["generosity"]))

match x_axis:
    case "GDP":
        x_array = gdp
    case "Happiness":
        x_array = happiness
    case "Generosity":
        x_array = generosity

match y_axis:
    case "GDP":
        y_array = gdp
    case "Happiness":
        y_array = happiness
    case "Generosity":
        y_array = generosity

st.subheader(f"{x_axis} and {y_axis}")

figure = px.scatter(x=x_array, y=y_array, labels={"x": f"{x_axis}", "y": f"{y_axis}", "label": f"{y_axis}"} )

st.plotly_chart(figure)
