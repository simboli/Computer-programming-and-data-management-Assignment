import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data
def load_data():
    data = pd.read_csv('02.Transformed data/01.EU27_emissions.csv')  # Replace 'your_file.csv' with your CSV file path
    return data

# Page for Data Visualization
def data_visualization_page(df):
    st.title("CSV Data Exploration")

    # Display a data table (adjust the number of rows to display as needed)
    if st.checkbox('Show Raw Data'):
        st.subheader('Raw Data')
        st.write(df.head())

    # Filter options
    selected_columns = st.multiselect('Select Columns to Display', df.columns)
    df_filtered = df[selected_columns] if selected_columns else df

    # Display filtered data table
    st.subheader('Filtered Data')
    st.write(df_filtered)

    # Plotting options (can be expanded with more plot types)
    plot_types = st.selectbox("Choose a type of plot", 
                              ["None", "Line Plot", "Bar Plot", "Histogram"])
    
    if plot_types != "None":
        st.subheader(f'{plot_types}')
        if plot_types == "Line Plot":
            st.line_chart(df_filtered)
        elif plot_types == "Bar Plot":
            st.bar_chart(df_filtered)
        elif plot_types == "Histogram":
            column_to_plot = st.selectbox("Choose a column to plot", df_filtered.columns)
            plt.figure(figsize=(10, 4))
            sns.histplot(df_filtered[column_to_plot])
            st.pyplot(plt)

# Page with fixed text
def fixed_text_page():
    st.title("Information Page")
    st.write("""
        This is a fixed text page. You can put any information here.
        For example, details about the data, how to use the app, 
        or any other relevant information.
    """)

# Main app function
def main():
    # Sidebar for navigation
    st.sidebar.title("Navigation this")
    pages = ["Data Visualization", "Fixed Text Page"]
    selected_page = st.sidebar.radio("Select a page:", pages)

    # Load data
    df = load_data()

    # Page selection
    if selected_page == "Data Visualization":
        data_visualization_page(df)
    elif selected_page == "Fixed Text Page":
        fixed_text_page()

# Run the app
if __name__ == "__main__":
    main()
