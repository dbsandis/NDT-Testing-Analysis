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
        <h1 style="text-align: center;">Ultrasonic Data Visualization</h1>
        """
    # Render the centered title using markdown
    st.markdown(centered_title_html, unsafe_allow_html=True)

    # HTML to center the additional description
    second_line_html = """
        <p style="text-align: center;">App provides Visual Analysis<br>
        of ultrasonic data using<br>
        histograms, trends & heatmaps.</p>
        """
    st.markdown(second_line_html, unsafe_allow_html=True)

    st.write()

    # Sidebar for navigation
    st.sidebar.title('Navigation')

    # Tooltips also support markdown
    radio_markdown = '''
        \n"**Introduction:** Overview of the project."
        \n"**Histograms:** Explore data distributions."
        \n"**Trends:** Analyze data trends over time."
        \n"**Heatmaps:** Visualize data density and patterns."
        '''.strip()
    

    # Adding radio buttons
    page = st.sidebar.radio('Select a Page:', ['Introduction', 'Histograms', 'Trends', 'Heatmaps'], help=radio_markdown)

    # # Descriptions for each page
    # st.sidebar.markdown("**Introduction:** Overview of the project.")
    # st.sidebar.markdown("**Histograms:** Explore data distributions.")
    # st.sidebar.markdown("**Trends:** Analyze data trends over time.")
    # st.sidebar.markdown("**Heatmaps:** Visualize data density and patterns.")
    # # Function to load data with caching

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
