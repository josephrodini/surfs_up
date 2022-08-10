# surfs_up

SQLite with SQLAlchemy and Python

## Overview of the analysis

### Surf n' Shake

This project attempts to legitimize a hypothetical business for a surfing/ice cream shop in order to attract an investor, W. Avy. The investor wants to be assured that the weather in Oahu (the proposed location of the business) will be mild enough for the shop to remain open for most of the year. Specifically, he wants temperature data for the months of June and December, critical months of the year.

### Resources

- hawaii.sqlite data file
- Python, SQLAlchemy

## Results

### June Temperatures

The measurements table within the hawaii.sqlite file was filtered to find the temperature data from the month of June. These temperatures were then converted to a list, followed by a dataframe, and finally summary statistics were generated for the dataframe. See [June summary statistics](https://github.com/josephrodini/surfs_up/blob/main/Images/June_statistics.PNG).

### December Temperatures

The measurements table within the hawaii.sqlite file was filtered to find the temperature data from the month of December. These temperatures were then converted to a list, followed by a dataframe, and finally summary statistics were generated for the dataframe. See [December summary statistics](https://github.com/josephrodini/surfs_up/blob/main/Images/December_statistics.PNG).

### Three Major Findings

- The average temperature in June (74.94 degrees) is 3.9 degrees hotter than the average temperature in December (71.04 degrees).
- The range in temperatures in June was 21 degrees, compared to a larger range of 27 degrees for December.
- As one would expect due to the range statistic, temperatures are more dispersed in December, as indicated by a higher standard deviation (3.75) than the standard deviation for June (3.26).

## Summary

### Overall Findings

The temperature statistics indicate that the weather in June and December, around the low to mid 70s on average, is still hospitable for the operation of a surfing and ice cream shop. However, it may be that those months are too rainy for the shop to be successful.

### Two Additional Queries

In order to provide more information to the investor, we can run two more queries in order to get the precipitation data for June and December. The query for precipitation data for June would be: "june_precip = session.query(Measurement.date, Measurement.prcp).filter(extract('month',Measurement.date)==6).all()," and the one for December would be "dec_precip = session.query(Measurement.date, Measurement.prcp).filter(extract('month',Measurement.date)==12).all()."

### Limitations

There were no major limitations to the analyses as data was ample and complete. 