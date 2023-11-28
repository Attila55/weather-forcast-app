import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, subheader
st.title("Weather forecast for next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")

# Directly coded data for test

# def get_data(days):
#     dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
#     temperatures = [10, 11, 15]
#     temperatures = [days * i for i in temperatures]
#     return dates, temperatures
#
# d, t = get_data(days)
try:
    if place:
        # Get the temperature/sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperature = [dicti["main"]["temp"] / 10 for dicti in filtered_data]
            dates = [dicti["dt_txt"] for dicti in filtered_data]
            # Create a temperature plut
            figure = px.line(x=dates, y=temperature,
                             labels={"x": "Date", "y": "Temperature(C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dicti["weather"][0]["main"] for dicti in filtered_data]
            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png",
                      }
            # list comprehension
            image_paths = [images[conditions]for conditions in sky_conditions]
            st.image(image_paths, width=115)
except KeyError:
    st.title("There is no city like that")
