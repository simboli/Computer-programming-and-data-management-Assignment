import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

# *********************************
# FUNCTIONS
# *********************************
# Functions to load data
def load_data_EU27_emissions():
    data_EU27_emissions = pd.read_csv('02.Transformed data/01.EU27_emissions.csv')  # 01.EU27_emissions.csv
    return data_EU27_emissions

def load_data_EU27_passengers():
    data_EU27_passengers = pd.read_csv('02.Transformed data/02.EU27_passengers.csv')  # 02.EU27_passengers.csv
    return data_EU27_passengers

def load_data_EU27_emissions_proCapita():
    data_EU27_emissions_proCapita = pd.read_csv('02.Transformed data/03.EU27_emissions_proCapita.csv')  # 03.EU27_emissions_proCapita
    return data_EU27_emissions_proCapita

def load_data_VFE():
    data_VFE = pd.read_csv('02.Transformed data/12.VFE.csv')  # 12.VFE
    return data_VFE

def load_data_VFE_climb_National():
    data_VFE_climb_National = pd.read_csv('02.Transformed data/12.1.VFE_climb_National.csv')  # 12.VFE
    return data_VFE_climb_National

def load_data_VFE_descent_National():
    data_VFE_descent_National = pd.read_csv('02.Transformed data/12.3.VFE_descent_National.csv')  # 12.VFE
    return data_VFE_descent_National

# Functions to viasualize data
def visualize_data(df, x_axis, y_axis):
    graph = alt.Chart(df).mark_circle(size=60).encode(
        x=x_axis,
        y=y_axis,
        color='Origin',
        tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
    ).interactive()

    st.write(graph)







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
    # Load data
    df_EU27_emissions = load_data_EU27_emissions()
    df_EU27_passengers = load_data_EU27_passengers()
    df_EU27_emissions_proCapita = load_data_EU27_emissions_proCapita()
    df_VFE = load_data_VFE()
    df_VFE_climb_National = load_data_VFE_climb_National()
    df_VFE_descent_National = load_data_VFE_descent_National()

    # Sidebar for navigation
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration", "Chart", "VFE", "Geo"])

    # Page selection
    if page == "Homepage":
        st.header("This is your data explorer.")
        st.write("Please select a page on the left.")
        st.write(df_EU27_passengers)
        data_visualization_page(df_EU27_emissions)
    elif page == "Exploration":
        st.title("Data Exploration")
        x_axis = st.selectbox("Choose a variable for the x-axis", df_EU27_emissions.columns, index=3)
        y_axis = st.selectbox("Choose a variable for the y-axis", df_EU27_emissions.columns, index=4)
        visualize_data(df_EU27_emissions, x_axis, y_axis)
    elif page == "Chart":  
        fixed_text_page()
    elif page == "VFE":
        st.title("Vertical flight efficiency")
        st.write("VFE over time")

        st.bar_chart(df_VFE_climb_National, x="PERIOD_ID", y="AVG_DIST_CLIMB", color="#FF0000")
        st.bar_chart(df_VFE_descent_National, x="PERIOD_ID", y="AVG_DIST_DESCENT", color="#FF0000")
        #st.line_chart(df_VFE, x="PERIOD_ID", y=["TOT_DELTA_CO2_KG_CLIMB_BELOW_10000", "NBR_CCO_FLIGHTS"], color=["#FF0000", "#0000FF"])
        #st.bar_chart(df_VFE, x="PERIOD_ID", y="TOT_DELTA_CO2_KG_CLIMB_BELOW_10000", color="#FF0000")
        
        st.write("Filtering example")
        
        selected_class = st.radio("Select Class", df_VFE_climb_National['YEAR'].unique())
        st.write("Selected Class:", selected_class)

        st.bar_chart(df_VFE_climb_National[df_VFE_climb_National.YEAR == selected_class], x="PERIOD_ID", y="AVG_DIST_CLIMB", color="#000080")
        st.bar_chart(df_VFE_descent_National[df_VFE_descent_National.YEAR == selected_class], x="PERIOD_ID", y="AVG_DIST_DESCENT", color="#000080")

        







# Run the app
if __name__ == "__main__":
    main()
