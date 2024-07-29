import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("AQI Value Prediction Models")

# Function to determine status based on AQI value
def get_status(aqi_value):
    if aqi_value <= 50:
        return "Good"
    elif aqi_value <= 100:
        return "Moderate"
    elif aqi_value <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi_value <= 200:
        return "Unhealthy"
    elif aqi_value <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

# Historical Data Visualization
def display_historical_data():
    st.header("Historical AQI Data")
    data = {
        "Date": pd.date_range(start='1/1/2024', periods=100),
        "AQI Value": np.random.randint(0, 500, size=100)
    }
    df = pd.DataFrame(data)
    
    # Enhanced visualization using seaborn and matplotlib
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Date', y='AQI Value', marker='o', color='b')
    plt.title("Historical AQI Values Over Time")
    plt.xlabel("Date")
    plt.ylabel("AQI Value")
    plt.xticks(rotation=45)
    st.pyplot(plt)

# Predict AQI Status
def predict_aqi_status():
    st.subheader("Predict AQI Status")
    aqi_value = st.number_input("Enter AQI Value", min_value=0.0, max_value=500.0, step=0.1)
    if st.button("Predict AQI Status"):
        status = get_status(aqi_value)
        st.success(f"The AQI status is: {status}")

# Model Comparison and Rating
model_ratings = {"Nakul_AQI": [], "AQI_Navya": [], "Nishith_AQI2": []}

def compare_models():
    st.header("Model Comparison")
    model_comparison = {
        "Model": ["Nakul_AQI", "AQI_Navya", "Nishith_AQI2"],
        "RMSE": [0.019, 0.045, 0.025],
        "MSE": [0.00037, 0.002, 0.00060]
    }
    comparison_df = pd.DataFrame(model_comparison)
    st.write(comparison_df)

    # Visualize Model Performance with Altair
    st.subheader("Model Performance Visualization")
    rmse_chart = alt.Chart(comparison_df).mark_bar().encode(
        x='Model',
        y='RMSE',
        color='Model'
    ).properties(title="Root Mean Squared Error (RMSE)")
    st.altair_chart(rmse_chart, use_container_width=True)

    mse_chart = alt.Chart(comparison_df).mark_bar().encode(
        x='Model',
        y='MSE',
        color='Model'
    ).properties(title="Mean Squared Error (MSE)")
    st.altair_chart(mse_chart, use_container_width=True)

    # Rating Section
    st.subheader("Rate the Models")
    selected_model = st.selectbox('Select a model to rate', model_comparison["Model"])
    rating = st.slider(f"Rate {selected_model} (1 to 5)", 1, 5)
    if st.button("Submit Rating"):
        model_ratings[selected_model].append(rating)
        st.success(f"Rating submitted: {rating}")

    # Display average ratings
    st.subheader("Average Ratings")
    for model, ratings in model_ratings.items():
        if ratings:
            average_rating = sum(ratings) / len(ratings)
            st.write(f"{model}: {average_rating:.2f}")

# Feedback Section
def feedback_section():
    st.header("Help us Improve")
    name = st.text_input("Enter your name: ")
    date = st.date_input("Select a date: ")
    feedback = st.text_area("Feedback:", "")
    if st.button("Submit Feedback"):
        st.success("Feedback Submitted Successfully!")

# Main function
def main():
    display_historical_data()
    predict_aqi_status()
    compare_models()
    feedback_section()

# Section for adding a new model
st.sidebar.header('Add a New Model')
model_name = st.sidebar.text_input('Enter the name of model')
github_link = "https://github.com/DLShrankhala/DevelopingVariousLSTMModelForTimeSeriesForecasting-ai-25"
if model_name:
    st.sidebar.write(f'please visit the following GitHub repository to add a new model:')
    st.sidebar.markdown(f'''
        <a href="{github_link}" target="_blank">
            <button style="background-color: #4CAF50; border: none; color: white; padding: 15px 32px;
            text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px;
            cursor: pointer;">Go to GitHub Repository</button>
        </a>
    ''', unsafe_allow_html=True)

# Run the main function
if __name__== "__main__":
    main()