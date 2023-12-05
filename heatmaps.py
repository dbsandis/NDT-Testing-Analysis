def show_heatmaps(df):
    import streamlit as st
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    import numpy as np


    # Streamlit app layout

    # HTML to center the title
    centered_title_html = """
        <h1 style="text-align: center;">Heatmap of Wear Pattern in Recovery Boilers</h1>
        """

    # Render the centered title using markdown
    st.markdown(centered_title_html, unsafe_allow_html=True)



    st.markdown("""
    Heatmaps are an invaluable tool in visualizing wear patterns, particularly in fields such as maintenance and inspection. Here are the top five points that highlight their effectiveness:

    1. **Visual Overview of Data**: Heatmaps offer a concise, visual summary of complex wear data, enabling quick identification of patterns and problematic areas.
    2. **Highlighting Problem Areas**: They effectively highlight regions with significant wear through color differentiation, aiding in the rapid identification of areas needing maintenance.
    3. **Comparative Analysis**: Ideal for comparing wear patterns over time or across datasets, heatmaps assist in tracking changes and evaluating maintenance effectiveness.
    4. **Easy Interpretation**: The intuitive, color-coded design of heatmaps ensures that they are easily interpretable by various audiences, including those without technical expertise.
    5. **Guiding Maintenance Decisions**: By providing a clear depiction of wear distribution, heatmaps are instrumental in guiding crucial maintenance decisions and resource allocation.
    """)

    # # Select Year for Inspection
    # year = st.selectbox('Select Year for Inspection', options=df['Date'].unique())
    
    # # Filter data based on selected year
    # filtered_df = df[df['Date'] == year]

    # # Group by Elevation and Tube, and average the Reading values for duplicates
    # grouped_df = filtered_df.groupby(['Elevation', 'Tube']).Reading.mean().reset_index()

    # # Pivot the data for the heatmap
    # heatmap_data = grouped_df.pivot(index="Elevation", columns="Tube", values="Reading")


    # Extract unique years and sort them in reverse order
    unique_years = sorted(df['Date'].dt.year.unique(), reverse=True)

    # Use the unique, sorted years in the select box
    year = st.selectbox('Select Year for Inspection', options=unique_years)

    # Filter data based on selected year
    # Ensure you're comparing the year part of the 'Date' column
    filtered_df = df[df['Date'].dt.year == year]

    # Group by Elevation and Tube, and average the Reading values for duplicates
    grouped_df = filtered_df.groupby(['Elevation', 'Tube']).Reading.mean().reset_index()

    # Pivot the data for the heatmap
    heatmap_data = grouped_df.pivot(index="Elevation", columns="Tube", values="Reading")


    # Create a custom color map
    n_bins = 32
    colors = sns.color_palette("coolwarm", n_bins)
    cmap = mcolors.ListedColormap(colors)

    # Define a normalization from 141 to 300 (values for the colormap)
    norm = mcolors.Normalize(vmin=141, vmax=300)

    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(heatmap_data, cmap=cmap, norm=norm)

    # Color values below 141 in red
    for text in plt.gca().texts:
        if float(text.get_text()) < 141:
            text.set_color('red')

    st.pyplot(plt)
