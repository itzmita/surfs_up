# surfs_up
# Learning SQL Lite
## Project Overview
### Purpose
The purpose of this assignment is to help W. Avy, a famous surfer and investor analyse the weather data for Oahu, Hawaii which will help him make a decision about opening a and icecream and surf shop. The island weather varies a lot, so W. Ivy wants to understand the weather history and patterns in the area where he would want to open the shop. He wants a correct balance of warm and humid climate for his shop to flourish  round the year. The data provided for the analysis had 7 years of weather data from 2010 to 2017. W. Avy wants to focus on specifically June and December weather. As these 2 months are 6 months apart, analyzing these 2 months will give him a better idea for the whole year. 

#### Resources
  Software:

    SQLlite
    SQL
    Jupyter Notebook
    Flask Web Server
    Python
    Jupyter Notebook
    matplotlib
    sqlalchemy
    numpy
    Pandas
    

### Results

#### Deliverable 1 and 2
First we did the temperature observations (tobs) for the month of June.
	• There are 1700 data point for the month of June and 1517 for the month of December
	• The average temp of June is 75F and December is 71F which is not much less. 
	• This shows that around the year the temperature is pretty much consistent. It's not too cold in the month of December which is ideal for the surf and icecream shop

![image](https://user-images.githubusercontent.com/3753839/171982493-92a5be95-2c28-4feb-9dd3-7f1948bef7a2.png)

![image](https://user-images.githubusercontent.com/3753839/171982497-c6cbd8ee-92dd-4f34-ba4e-cc0964de99b7.png)


Above are snapshots showing June and December temperature Statistics


Additional queries for the Precipitation for June and December:
The below is a snapshot of statistics of Precipitation data for the month of June and December months.
• Average rainfall in the month of December (0.21) is more than June (0.13)
• December has maximum rainfall of 6.42 inches whereas June has 4.43 inches. 
• December is showing to be decently warm and humid which is again an ideal climate for W Avy to open his shop.
  
  ![image](https://user-images.githubusercontent.com/3753839/171982500-f45c55d9-39f3-4f80-8bd2-d574164fe0dc.png)

![image](https://user-images.githubusercontent.com/3753839/171982505-7e963f73-f9ad-4419-9341-87bf9719272c.png)





### Summary
The queries above shows the weather data is consistent across the year.
But to visualize the data here are 2 charts
This box and whiskers chart depicts the temperature quite steady year around and there are very few outliers. 
![image](https://user-images.githubusercontent.com/3753839/171982433-dedd89bf-08bb-411c-9c36-4718c7c359d3.png)



_Snapshot for Box and Whisker plot June and December Temperature Statistics_

The second box and whiskers chart shows the statistics of rainfall for the months of June and December and it has some outliers as well which tells that for some of the years the rainfall may be a bit higher in December.

![image](https://user-images.githubusercontent.com/3753839/171982435-77debeb6-cc0c-486a-9703-5411e8803eb8.png)

_Snapshot of Box and Whisker plot showing June and December Precipitation Statistics_

Though the rainfall seems to be higher, if we combine with the temperature statics, it shows that June and December months are almost similar and quite quite warm and near ideal for a surf shop to be opened.  

