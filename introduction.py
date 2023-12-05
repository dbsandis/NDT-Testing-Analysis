def show_intro():
    import streamlit as st
    # Streamlit app layout

    # HTML content
    html_content = """
    <h2 style="text-align: center;">
            VISUAL ANALYTICS FINAL PROJECT
    </h2>
    <p style="text-align: center;"><i>"A description on how I developed my story"</i></p>

    <p style="text-align: center;"><i>"Daryl Sanders"</i></p>

    <p style="text-align: center;"><b>A little history:</b></p>

    <p>I pulled sample data from an application TCRI developed in the early nineties. As that application called Technical Database Systems (TDS) was developed to help ensure PaperMills Ultrasonic Data Inspections had accurate information to guide them in making sound maintenance decisions. Such as when tubes should be replaced, or how is their operating environment was impacting tubes.</p>

    <p>TCRI (Tom Ridgeway) provided the actual application to be installed on my machine, so I could extract the sample data.</p>

    <p>Those samples were in an archaic format (developed in 1984), so it had to be massaged, cleansed and reformatted so my app could interpret. I used Python to extract, melt and format the data.</p>

    <p>Once the data was correctly formatted I then loaded same into a dataframe and proceeded to produce several sheets. Several years of data were loaded, including images, mill locations in the US.</p>

    <p>With more time and development, the complete TDS could be incorporated within the app, along with additional coding. I chose only to show what Tableau capabilities were. I created heatmaps for each inspection, created Wear trends along with a static wear image. The map was included to also show that Streamlit would allow you to drill down to a specific location and show that mill's data.</p>

    <p>And as I stated, a lot more can be developed within the app to provide a more completed picture/story of Ultrasonic (UT) inspections at paper mills.</p>
    """

    # Using markdown to render HTML content
    st.markdown(html_content, unsafe_allow_html=True)

    ## add image

    ## describe image


        