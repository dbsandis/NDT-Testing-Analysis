# Non-Destructive-Testing-Analytics

create virtual environment with requirement.txt
and execute with 
    streamlit run app.py


### Introduction

A little history:  
I pulled sample data from an application TCRI developed in the early nineties. As that application called Techinical DataBase Systems (TDS) was developed to help ensure PaperMills Ultrasonic Data Inspections had accurate information to guide them in making sound maintenance decisions.  Such as when tubes should be replaced, or how is their operating environment was impacting tubes.

* Find TCRI-TDS website here: http://www.tcri-tds.com/


### Data/Operation Abstraction Design:

TCRI (Tom Ridgeway) provided the actual application to be installed on my machine, so I could extract the sample data.

* Sample data included in this git was artificially created to allow simple presentation and to ensure privacy at papermills.

That samples were in an archaic format (developed in 1984), so it had to be massaged, cleansed and reformatted so data could be interpret. I used Python to extract, melt and format the data.  Data was originally created per paper mill, boiler, date, wall and elevation.  These were melted into a single csv file for multiple years to allow clean display.  Users can retrieve by date, elevation and reading easily to display visually the data.

Once the data was correctly formatted I then loaded same into this streamlit app and proceeded to produce several pages/columns. Several years of data were loaded, including images, mill locations in the US.

### Use Case:

As a junior engineer in a powerhouse, you are faced with the daunting task of analyzing a massive volume of Ultrasonic Testing (UT) data to assess the condition and predict the remaining lifespan of the Recovery boiler in your mill. Your desk is overwhelmed with a two-foot-high stack of 3-ring binders, encapsulating nine years of inspection data. This collection amounts to around 270,000 UT readings. Your primary objective is to devise a system for effectively displaying and trending this extensive data. The challenge lies in ensuring that your analysis accurately reflects the current state and rate of deterioration for each specific section of the boiler. The success of your approach is critical in making informed decisions about the boiler's maintenance and operational future.

### App Features

This app provides a simple cross-section view of visual analytics use with ultrasonic data used in non-destructive testing. This app uses several years of inspection date at a fictitious mill. Such data can be visuallize through trend charts, distribution charts and or heatmaps that can show changes over the course of the year on a given wall.

### Future Work:

With more time and development, the complete TDS could be incorporated within streamlit, along with additional coding.  I chose only to show what Steamlit capabilities were.  I created heatmaps for each inspection, created Wear trends along with a static wear image. The map was included to also show that Tableau would allow you to drill down to a specific location and show that mills data. 

And as I stated, a lot more can be developed within the app to provide a more complleted picture/story of Ultrasonic (UT) inspections at paper mills.

### Streamlit App Link

https://ndt-testing-analysis.streamlit.app/
