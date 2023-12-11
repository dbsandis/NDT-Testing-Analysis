def show_intro():
    import streamlit as st
    # Streamlit app layout

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
