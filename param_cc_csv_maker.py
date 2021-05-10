import matplotlib.pyplot as plt
import glob
import numpy as np
from numpy import genfromtxt as gent
import iris
from iris.experimental.equalise_cubes import equalise_attributes
import iris.coord_categorisation

def main(xmin,xmax,ymin,ymax,m,pressure_yes_no,pressure_level,variable_STASH,measure,percentile):
	counter = 0
	for yyyy in range(1997,2007):
		holdrlist = iris.cube.CubeList([])
		flelist = glob.glob('/nfs/a277/IMPALA/data/25km/'+str(variable_STASH)+'/*'+str(yyyy)+str(m)+'010100-*.nc')
		flelist.sort()
		for fle in flelist:
			temp = iris.load_cube(fle)
			temp = temp[:-1,:,:].extract(xysmallslice)
                        if int(pressure_level) != -500:
                                pressure_slice = iris.Constraint(pressure_level = int(pressure_level))
                                temp = temp.extract(pressure_slice)
			lons = temp.coord('longitude').points
			lats = temp.coord('latitude').points
			iris.coord_categorisation.add_day_of_year(temp, 'time', name='day_of_year')
                        if measure.upper() == 'MAX':
                                temp = temp.aggregated_by('time', iris.analysis.MAX)
                        elif measure.upper() == 'MIN':
                                temp = temp.aggregated_by('time', iris.analysis.MIN)
                        elif measure.upper() == 'MEAN':
                                temp = temp.aggregated_by('time', iris.analysis.MEAN)
                        elif measure.upper() == 'SUM':
                                temp = temp.aggregated_by('time', iris.analysis.SUM)

			if "12010100-" in fle:
				temp = temp.data
			else:
				temp = temp[:-1,:,:].data
			if counter == 0:
				rainfall = temp
			else:
				rainfall = np.concatenate((rainfall,temp), axis = 0)
			counter = counter + 1
	rainfall = np.percentile(rainfall,float(percentile),axis = 0)
        if pressure_level != -500:
                np.savetxt('P25_CC_month_'+str(m)+'_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_'+str(pressure_level)+'hPa_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', rainfall, delimiter = ',')

        else:
                np.savetxt('P25_CC_month_'+str(m)+'_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', rainfall, delimiter = ',')

        np.savetxt("P25_longitudes_"+str(xmin)+"_"+str(xmax)+".csv", lons, delimiter = ',')
        np.savetxt("P25_latitudes_"+str(xmin)+"_"+str(xmax)+".csv", lats, delimiter = ',')





if "__name__" == "__main__":
	main(xstart,xend,ystart,yend,yyyy)
