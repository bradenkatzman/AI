import time
import DataPrepAndNormalization as prep_norm
import GradientDescent as gd
import Predict


if __name__ == '__main__':
	print "start"
	start_time = time.time()

	filename = 'girls_age_weight_height_2_8.csv'

	# load the data into a matrix
	data = prep_norm.load(filename)

	# compute the means and standard deviations of each feature
	featureStats = prep_norm.mean_stdev(data[0])

	# print the statistics
	prep_norm.printFeatureStats(featureStats)

	# scale the data
	scaled = prep_norm.scale(data[0], featureStats)

	# plot the risk function
	gd.plotRisk(50, scaled, data[1], len(data[1]))

	beta = gd.gradient(scaled, data[1], [0,0,0], 0.05, 1500, len(data[1]))

	print 'Beta = ' + repr(beta)

	nscale = prep_norm.scale([[0], [5], [20]], featureStats)

	pred = Predict.predict(beta, nscale[0][0], nscale[1][0])

	print "The height of a 5-year old girl weighting 20 kilos is: " + repr(pred)

	beta = prep_norm.norm(data[0], data[1])
	
	print "The Beta obtained with normal equation is:"
	
	print beta
	
	pred = Predict.predict(beta, nscale[0][0], nscale[1][0])
	
	print "The height of a 5-year old girl weighting 20 kilos is using normal equation is: " + repr(pred)


	print "\ntotal program execution = {t} seconds".format(t=(time.time()-start_time))
	print "exiting...\n"