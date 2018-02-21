import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 


def boostrap(statistic_func, iterations, data):
	samples  = np.random.choice(data,replace = True, size = [iterations, len(data)])
	#print samples.shape
	data_mean = data.mean()
	vals = []
	for sample in samples:
		sta = statistic_func(sample)
		#print sta
		vals.append(sta)
	b = np.array(vals)
	#print b
	lower, upper = np.percentile(b, [2.5, 97.5])
	return data_mean,lower, upper


# def permutation(statistic, error):


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	print((df.columns))
	sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	sns_plot.savefig("scaterplot.png",bbox_inches='tight')
	sns_plot.savefig("scaterplot.pdf",bbox_inches='tight')
	

	df0 = df.dropna(subset=['Current fleet'], how='any')
	df1 = df.dropna(subset=['New Fleet'], how='any')
	
	print (df0)
	print (df1)
	
	data0 = df0.values.T[0]
	print ("Current Fleet")
	print((("Mean: %f")%(np.mean(data0))))
	print((("Median: %f")%(np.median(data0))))
	print((("Var: %f")%(np.var(data0))))
	print((("std: %f")%(np.std(data0))))
	print((("MAD: %f")%(mad(data0))))

	data1 = df1.values.T[1]
	print ("New Fleet")
	print((("Mean: %f")%(np.mean(data1))))
	print((("Median: %f")%(np.median(data1))))
	print((("Var: %f")%(np.var(data1))))
	print((("std: %f")%(np.std(data1))))
	print((("MAD: %f")%(mad(data1))))

	plt.clf()
	sns_plot2 = sns.distplot(data1, bins=20, kde=False, rug=True).get_figure()

	axes = plt.gca()
	axes.set_xlabel('Current Fleet') 
	axes.set_ylabel('Proposed fleeet')

	sns_plot2.savefig("histogram.png",bbox_inches='tight')
	sns_plot2.savefig("histogram.pdf",bbox_inches='tight')



	#Bootstrap

	#Current fleet boot

	boots = []
	for i in range(100,100000,1000):
		boot = boostrap(np.mean, i, data0)
		boots.append([i,boot[0], "mean"])
		boots.append([i,boot[1], "lower"])
		boots.append([i,boot[2], "upper"])
	
	df_boot = pd.DataFrame(boots,  columns=['Boostrap Iterations','Mean',"Value"])
	sns_plot = sns.lmplot(df_boot.columns[0],df_boot.columns[1], data=df_boot, fit_reg=False,  hue="Value")




	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,100000)

	sns_plot.savefig("bootstrap_confidence_Currentfleet.png",bbox_inches='tight')
	sns_plot.savefig("bootstrap_confidence_Currentfleet.pdf",bbox_inches='tight')
	
	#New fleet boot

	boots = []
	for i in range(100,100000,1000):
		boot = boostrap(np.mean, i, data1)
		boots.append([i,boot[0], "mean"])
		boots.append([i,boot[1], "lower"])
		boots.append([i,boot[2], "upper"])


	df_boot = pd.DataFrame(boots,  columns=['Boostrap Iterations','Mean',"Value"])
	sns_plot = sns.lmplot(df_boot.columns[0],df_boot.columns[1], data=df_boot, fit_reg=False,  hue="Value")




	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,100000)

	sns_plot.savefig("bootstrap_confidence_Newfleet.png",bbox_inches='tight')
	sns_plot.savefig("bootstrap_confidence_newflet.pdf",bbox_inches='tight')




	
