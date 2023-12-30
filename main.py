import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Weather Forecast API")

place = st.text_input(label="Place: ")

query = st.selectbox(label="Forecast Type:", options=["Temperature","Sky"])

days = st.slider("Forecast Days: ", min_value=1,max_value=7)

st.subheader(f"{query} for {place} for the next {days} day(s)")

fig = px.line(x=["21", "22", "23"],
        y=["1", "14", "8"],
        labels={"x":"Dates","y":"Temperature"})
st.plotly_chart(fig)