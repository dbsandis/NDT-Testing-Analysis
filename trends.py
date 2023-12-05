#trend.py
def show_trends(df):

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import streamlit as st

    # Function to create a dataset for a given trend
    def create_trend_data(dates, trend_type):
        num_points = len(dates) * 5
        elevation = np.tile(np.linspace(20, 80, 5), len(dates))

        if trend_type == "increasing":
            reading = np.linspace(150, 300, num_points) + np.random.normal(0, 10, num_points)
        elif trend_type == "decreasing":
            reading = np.linspace(300, 150, num_points) + np.random.normal(0, 10, num_points)
        else:  # sharp increase
            reading = np.concatenate([
                np.linspace(150, 175, num_points // 3),
                np.linspace(175, 300, num_points // 3),
                np.linspace(300, 175, num_points // 3)
            ]) + np.random.normal(0, 10, num_points)

        return pd.DataFrame({
            'Date': np.repeat(dates, 5),
            'Elevation': elevation,
            'Reading': reading,
            'Tube': f't{np.random.randint(20, 30)}'  # Random tube number for illustration
        })


    # Streamlit app layout
    filtered_df = []

    # HTML to center the title
    centered_title_html = """
        <h1 style="text-align: center;">Trend Line Analysis of Data</h1>
        """

    # Render the centered title using markdown
    st.markdown(centered_title_html, unsafe_allow_html=True)

    # Sidebar filters
    selected_elevation = st.sidebar.selectbox("Select Elevation", options=df['Elevation'].unique())
    selected_tube = st.sidebar.selectbox("Select Tube", options=df['Tube'].unique())


    filtered_df = df[(df['Elevation'] == selected_elevation) & 
                 (df['Tube'] == selected_tube)]
    
    # Ensure 'Reading' is numeric
    filtered_df['Reading'] = pd.to_numeric(filtered_df['Reading'], errors='coerce')

    # Convert dates to ordinal for regression
    filtered_df['Date_ordinal'] = pd.to_datetime(filtered_df['Date']).apply(lambda date: date.toordinal())

    # Perform linear regression
    slope, intercept = np.polyfit(filtered_df['Date_ordinal'], filtered_df['Reading'], 1)

    # Create a best fit line
    best_fit_line = (slope * filtered_df['Date_ordinal']) + intercept

    # Plotting the trend line with Seaborn
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=filtered_df, x="Date", y="Reading", hue="Elevation", marker="o")

    # Add the best fit line
    plt.plot(filtered_df['Date'], best_fit_line, color='red', label='Best Fit Line')

    plt.title(f"Trend Line by Date for Elevation: {selected_elevation}, Tube: {selected_tube}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    # Displaying the plot in Streamlit
    st.pyplot(plt)


    # HTML content
    html_content = """
    <p>To trend UT data mathematically, the readings from the current and previous inspections are plotted on a thickness versus time diagram (see Figure 1). The results of trending UT data fall into three broad categories.<p>
    <p>The first category is, as depicted in (Figures 1), the UT readings show the tube wall is thinning. <p>
    <p>The second category is as depicted in (Figures 2)). Here, the UT readings for a test point suggest that the tube is getting thicker but within acceptable UT measuring accuracies.<p> 
    <p>The third category is as depicted in (Figures 3), where the UT readings suggest that the tube wall is getting significantly thicker. In these instances, the readings vary more considerably than the expected accuracies. </p>
    <p>Currently, it is crucial to mention significant differences in the expectations for the accuracy and consistency of UT data. <p>
    <p><b><i>note:<i> Best Fit Line with Streamlit does not show if data is missing</b><p>
    """

    # Using markdown to render HTML content
    st.markdown(html_content, unsafe_allow_html=True)

    # Generating dates from 2005 to 2023
    dates = pd.date_range(start="2005-01-01", end="2023-01-01", freq='Y')


    # Creating the datasets for each trend type
    df_increasing = create_trend_data(dates, "increasing")
    df_decreasing = create_trend_data(dates, "decreasing")
    df_sharp_increase = create_trend_data(dates, "sharp increase")


    col1, col2, col3 = st.columns(3)

    with col1:

        fig1, ax1 = plt.subplots()

        # Assuming ax2_df is your DataFrame filtered to show a decreasing trend
        sns.lineplot(data=df_decreasing, x="Date", y="Reading", hue="Elevation", marker="o")
        ax1.set_title("Figure 1")
        ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
        fig1.tight_layout()

        # Displaying the plot in Streamlit
        st.pyplot(fig1)


    with col2:

        fig2, ax2 = plt.subplots()

        # Plotting the trend line with Seaborn
        sns.lineplot(data=df_increasing, x="Date", y="Reading", hue="Elevation", marker="o", ax=ax2)

        # Additional plot formatting...
        ax2.set_title(f"Figure 2")
        ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
        fig2.tight_layout()

        # Displaying the plot in Streamlit
        st.pyplot(fig2)


    
    with col3:  # Assuming you have defined col3
        fig3, ax3 = plt.subplots()

        # Assuming ax3_df is your DataFrame filtered to show a sharp increase in the mid-section
        sns.lineplot(data=df_sharp_increase, x="Date", y="Reading", hue="Elevation", marker="o")
        ax3.set_title("Figure 3")
        ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45)
        fig3.tight_layout()

        # Displaying the plot in Streamlit
        st.pyplot(fig3)
