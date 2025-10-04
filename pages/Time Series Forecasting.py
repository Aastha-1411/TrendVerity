import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

st.set_page_config(page_title="Time Series Analysis")

st.markdown("# Time Series Analysis")
# File upload
uploaded_file = st.file_uploader("Upload your time series CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Raw Data Preview:", df.head())

    # Let user select columns for date and value
    cols = df.columns.tolist()
    date_col = st.selectbox("Select date column", cols)
    value_col = st.selectbox("Select value column", cols)
    df = df[[date_col, value_col]].rename(columns={date_col: "ds", value_col: "y"})
    df["ds"] = pd.to_datetime(df["ds"])

    # Fit Prophet
    model = Prophet()
    model.fit(df)

    # Future dataframe
    future = model.make_future_dataframe(periods=12, freq="M")
    forecast = model.predict(future)

    # Plot forecast
    fig1 = model.plot(forecast)
    st.pyplot(fig1, clear_figure=True)

    # Plot components
    fig2 = model.plot_components(forecast)
    st.pyplot(fig2, clear_figure=True)