import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import OneHotEncoder

def main():
    # title and description
    st.title("ML Project - Amazon Sales Prediction")
    st.write("This is a test Streamlit app for a machine learning project.")

    # load the data
    df = pd.read_csv("AmazonSalesData.csv")
    # dropping rows with missing qty and amount
    df = df.dropna(subset=["qty", "amount"])
    # dropping rows with zero qty and amount
    df = df[(df["qty"] > 0) & (df["amount"] > 0)]
    # clean the column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '_')
    # colums to keep
    cols_to_keep = ['qty', 'amount', 'category', 'size']
    df = df[cols_to_keep]
    # clean the data by converting the 'category' strings to lowercase and removing any empty spaces
    df['category'] = df['category'].str.lower().str.strip()
    # clean the 'size' column by converting the strings to uppercase, removing any empty spaces, and replacing 'FREE' with 'Free'
    df['size'] = df['size'].str.upper().str.strip().str.replace('FREE', 'Free')
    # one-hot encode the 'category' and 'size' columns
    df = pd.get_dummies(df, columns=['category', 'size'], drop_first=True)
    # split the data into features and target
    X = df.drop('amount', axis=1)
    y = df['amount']
    # split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # fit the model
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X_train, y_train)
    # make predictions
    y_pred = model.predict(X_test)
    # evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    st.write(f"Mean Squared Error: {mse}")
    st.write(f"R^2: {r2}")

    # display the results
    st.write("Here is the data:")
    st.df(df)

if __name__ == "__main__":
    main()