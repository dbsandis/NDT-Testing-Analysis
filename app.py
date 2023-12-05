import streamlit as st
import pandas as pd
from histograms import show_histograms
from heatmaps import show_heatmaps
from introduction import show_intro
from trends import show_trends

# Load data function
#@st.cache
#def load_data():
#    return pd.read_csv('final_combined_file_path.csv', dtype={'Date': str})  # Ensure 'Date' is read as string
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)

    # Convert 'Date' to datetime for proper plotting
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    # Convert 'Reading' to numeric, coercing non-numeric values to NaN
    df['Reading'] = pd.to_numeric(df['Reading'], errors='coerce')
    return df

# Main app
def main():

    # HTML to center the title
    centered_title_html = """
        <h1 style="text-align: center;">Recovery Boiler Ultrasonic Data Visualization App</h1>
        """
    # Render the centered title using markdown
    st.markdown(centered_title_html, unsafe_allow_html=True)
    # Render the centered title using markdown
    st.markdown("""
    <p style="text-align: center;">
        This app provides visual analysis of ultrasonic data using histograms, trend & heatmaps.
    </p>
""", unsafe_allow_html=True)
    

    st.write()

    # Sidebar for navigation
    st.sidebar.title('Navigation')
    
    # Adding radio buttons
    page = st.sidebar.radio('Select a Page:', ['Introduction', 'Histograms', 'Trends', 'Heatmaps'])

    # Descriptions for each page
    st.sidebar.markdown("**Introduction:** Overview of the project.")
    st.sidebar.markdown("**Histograms:** Explore data distributions.")
    st.sidebar.markdown("**Trends:** Analyze data trends over time.")
    st.sidebar.markdown("**Heatmaps:** Visualize data density and patterns.")
    # Function to load data with caching

    # Path to the merged data
    file_path = 'final_combined_file_path.csv'
    data = load_data(file_path)
    

    # Page selection
    if page == 'Introduction':
        show_intro()
    elif page == 'Histograms':
        show_histograms(data)
    elif page == 'Heatmaps':
        show_heatmaps(data)
    elif page == 'Trends':
        show_trends(data)
    

if __name__ == "__main__":
    main()
