# Lab2

## Current Fleet Histogram and Scatterplot

In the first part of the lab assignment an example code for pliting caterplits and histograms was given. This program was used as a base and then modified to create a histogram and a scatterplot of the currentfleet and the pruposed fleet. 

The data of the file vehicles.cvs is read using the following function:

	df = pd.read_csv('./vehicles.csv')

Then the data obtained is used to create the following scaterplot
![logo](./scaterplot.png?raw=true)

After the data was divided ino two sets in which not available data is ignored using the dropna funtions from the pandas library. The functions used in the program are shown below.

	df0 = df.dropna(subset=['Current fleet'], how='any')
	df1 = df.dropna(subset=['New Fleet'], how='any')
	
Then the mean, median, varianze, standar deviation and the median absolute deviation of each set are calculated. This are the results:

	Current Fleet
	Mean: 20.144578
	Median: 19.000000
	Var: 40.983113
	std: 6.401805
	MAD: 4.000000

	New Fleet
	Mean: 30.481013
	Median: 32.000000
	Var: 36.831918
	std: 6.068931
	MAD: 4.000000

Next, the histogram of the data is made.
![logo](./histogram.png?raw=true)

## Bootstrap

Finally the bootstrap of the current fleet and the new fleet was calculated and graphed using the sample code found in the file bootstrap.py
The following images contain the results.

Bootstrap confidence of the current fleet
![logo](./bootstrap_confidence_Currentfleet.png?raw=true)

Bootstrap confidence of the new fleet
![logo](./bootstrap_confidence_Newfleet.png?raw=true)




