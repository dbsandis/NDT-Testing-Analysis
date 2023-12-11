# Load the merged data
#df = pd.read_csv('merged_data.csv', dtype={'Date': str})  # Ensure 'Date' is read as string

def show_histograms(df):
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    import numpy as np

    # Streamlit app layout
    # HTML to center the title
    centered_title_html = """
        <h1 style="text-align: center;">Histogram of wear pattern in Recovery Boilers</h1>
        """

    # Render the centered title using markdown
    st.markdown(centered_title_html, unsafe_allow_html=True)

    st.markdown("""
    Histograms are a fundamental tool in data visualization and analysis. Here are some key aspects of histograms:

    - **Visual Representation**: Histograms provide a visual representation of the frequency distribution of a dataset.
    - **Data Spread**: They allow you to quickly grasp how data points are spread across different ranges or bins, revealing the underlying distribution (e.g., normal, skewed, bimodal).
    - **Comparative Analysis**: Histograms are useful for comparing distributions between different groups or over time.
    - **Trend Identification**: They can reveal shifts in trends, differences in populations, or changes resulting from experimental conditions.
    - **Guiding Data Analysis**: Histograms can guide the direction of further data analysis.
    - **Data Transformation**: For instance, the observed distribution might suggest the need for data transformation, stratification, or the use of specific statistical models.
    """)
    
    # Extract unique years and sort them in reverse order
    unique_years = sorted(df['Date'].dt.year.unique(), reverse=True)

    # Use the unique, sorted years in the select box
    year = st.selectbox('Select Year for Inspection', options=unique_years)


    if st.checkbox('Show Distribution', value=True):

        # Filter data based on selected year
        # Ensure you're comparing the year part of the 'Date' column
        filtered_df = df[df['Date'].dt.year == year].copy()  # Create a copy to avoid SettingWithCopyWarning

        # Convert 'Reading' column to numeric, coercing errors to NaN
        #filtered_df["Reading"] = pd.to_numeric(filtered_df["Reading"], errors="coerce")
        filtered_df.loc[:, 'Reading'] = pd.to_numeric(filtered_df['Reading'], errors='coerce')

        # Further filter the dataframe for readings between 100 and 300
        # This time using .loc to avoid SettingWithCopyWarning
        filtered_df = filtered_df.loc[(filtered_df['Reading'] >= 100) & (filtered_df['Reading'] <= 300)]


        # Histogram settings
        st.sidebar.header('Histogram Settings')
        bin_size = st.sidebar.slider('Number of Bins', min_value=5, max_value=100, value=20)

        # Generate a colormap for the temperature scale (green-blue to yellow-orange)
        red = '#FF0000'
        # Create a colormap for the range with 32 colors
        yellow_orange = mcolors.to_rgba('orange')
        green_blue = mcolors.to_rgba('green')
        red = mcolors.to_rgba('red')
        colors = [yellow_orange,green_blue]  # Reversed order for warm to cool
        n_bins = 32  # We want 32 shades
        cmap = mcolors.LinearSegmentedColormap.from_list('custom_gradient', colors, N=n_bins)


        # Plot the histogram with only readings between 100 and 300
        fig, ax = plt.subplots()

        # Calculate the bins and get the bar patches
        n, bins, patches = ax.hist(filtered_df['Reading'], bins=bin_size, range=(100, 300))

        # Normalize the readings to the range of the colormap
        norm = plt.Normalize(100, 300)

        # Color code based on the value of the reading (x-value)
        for bin_left, bin_right, patch in zip(bins[:-1], bins[1:], patches):
            # Set the color for bins with values less than 141 to red
            if bin_left < 141:
                patch.set_facecolor(red)
            else:
                # Otherwise, use the colormap to assign a color based on the bin value
                patch.set_facecolor(cmap(norm(bin_left)))

        ax.set_title('Histogram of Readings (100 to 300)')
        ax.set_xlabel('Reading')
        ax.set_ylabel('Frequency')

        # Display the histogram
        st.pyplot(fig)

    if st.checkbox('Show Data'):

        # Display the filtered dataframe
        st.write(f"Displaying data for: {year}")
        st.dataframe(filtered_df)