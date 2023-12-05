def show_intro():
    import streamlit as st
    # Streamlit app layout

    # HTML content
#     html_content = """
#     <h2 style="text-align: center;">
#             VISUAL ANALYTICS FINAL PROJECT
#     </h2>
#     <p style="text-align: center;"><i>"A description on how I developed my story"</i></p>

#     <p style="text-align: center;"><i>"Daryl Sanders"</i></p>

#     <p style="text-align: center;"><b>A little history:</b></p>

#     <p>I pulled sample data from an application TCRI developed in the early nineties. As that application called Technical Database Systems (TDS) was developed to help ensure PaperMills Ultrasonic Data Inspections had accurate information to guide them in making sound maintenance decisions. Such as when tubes should be replaced, or how is their operating environment was impacting tubes.</p>

#     <p>TCRI (Tom Ridgeway) provided the actual application to be installed on my machine, so I could extract the sample data.</p>

#     <p>Those samples were in an archaic format (developed in 1984), so it had to be massaged, cleansed and reformatted so my app could interpret. I used Python to extract, melt and format the data.</p>

#     <p>Once the data was correctly formatted I then loaded same into a dataframe and proceeded to produce several sheets. Several years of data were loaded, including images, mill locations in the US.</p>

#     <p>With more time and development, the complete TDS could be incorporated within the app, along with additional coding. I chose only to show what Tableau capabilities were. I created heatmaps for each inspection, created Wear trends along with a static wear image. The map was included to also show that Streamlit would allow you to drill down to a specific location and show that mill's data.</p>

#     <p>And as I stated, a lot more can be developed within the app to provide a more completed picture/story of Ultrasonic (UT) inspections at paper mills.</p>
#     """

#     # Using markdown to render HTML content
#     st.markdown(html_content, unsafe_allow_html=True)

    ## add image

    ## describe image

    # Assuming 'image_path' is the path to your image file
    image_path = 'PR-Boiler-Graphic-Babcock-Wilcox.png'

    # Creating two columns
    col1, col2 = st.columns([1, 2])  # Adjust the ratio as needed

    # In the first column, display the image
    with col1:
        st.image(image_path, caption='Boiler Cross-Section')

   # In the second column, display the text
    with col2:
        text = """
        ## The Problem
        Because of the potential for explosions and their devastating results, Industrial America uses Non-Destructive Testing (NDT) to inspect and monitor their critical equipment. With respect to the inspection of power generation boilers, Ultrasonic Thickness (UT) testing is commonly employed. Thousands of UT readings are gathered and analyzed in hopes of determining the current and predicted condition of each boiler. The ability to digest and analyze the vast amounts of UT data gathered each year has long been a goal of most boiler engineers.
        """
        st.markdown(text)

    text2 = """
        Imagine you are the junior engineer in the powerhouse and there upon your desk lies a two-foot-tall stack of 3-ring binders. The binders contain several thousand pages of UT data that represent nine years of inspections from the Recovery boiler at your mill. The number of UT readings in the stack is approximately 270,000. You are tasked with reviewing the data in hopes of predicting the remaining life of the boiler. In other words, you need a method of displaying and trending the data, such that your findings ACCURATELY represent the current condition and rate-of-change for any given boiler section.

        ## Key Metrics and Analyses to support my story

        - **Tube Wear Trends**: Visualize the average wear or deterioration of tubes over the years, such as mean wear rate or cumulative wear.
        - **Correlation Analysis**: Explore correlations between wear rates and various factors, such as operating conditions (black liquor spray on Front Wall).
        - **Predictive Models**: Develop predictive models that can estimate future wear or remaining tube lifespan based on historical data.
        - **Threshold Analysis**: Determine a critical wear threshold beyond which tube replacement is necessary.
        """
    st.markdown(text2)
