# Non-Destructive-Testing-Analytics

create virtual environment with requirement.txt
and execute with 
    streamlit run app.py

### Streamlit App Link

https://ndt-testing-analysis.streamlit.app/

### Introduction

A little history:  
I pulled sample data from an application TCRI developed in the early nineties. As that application called Techinical DataBase Systems (TDS) was developed to help ensure PaperMills Ultrasonic Data Inspections had accurate information to guide them in making sound maintenance decisions.  Such as when tubes should be replaced, or how is their operating environment was impacting tubes.

### Data/Operation Abstraction Design:

TCRI (Tom Ridgeway) provided the actual application to be installed on my machine, so I could extract the sample data.

That samples were in an archaic format (developed in 1984), so it had to be massaged, cleansed and reformatted so data could be interpret. I used Python to extract, melt and format the data.

Once the data was correctly formatted I then loaded same into this streamlit app and proceeded to produce several pages/columns. Several years of data were loaded, including images, mill locations in the US.

### Future Work:

With more time and development, the complete TDS could be incorporated within streamlit, along with additional coding.  I chose only to show what Steamlit capabilities were.  I created heatmaps for each inspection, created Wear trends along with a static wear image. The map was included to also show that Tableau would allow you to drill down to a specific location and show that mills data. 

And as I stated, a lot more can be developed within the app to provide a more complleted picture/story of Ultrasonic (UT) inspections at paper mills.

## Note:
 
Streamlit is powerful, but I found a developer loses control of actual presentation, and is a good tool / aid but a complete stand-alone application (APP) may require a lower level code such as Objective-C (C#), or C++.
