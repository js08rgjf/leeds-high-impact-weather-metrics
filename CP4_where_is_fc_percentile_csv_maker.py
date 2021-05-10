import matplotlib.pyplot as plt
import glob
import numpy as np
from numpy import genfromtxt as gent
import iris
from iris.experimental.equalise_cubes import equalise_attributes
import iris.coord_categorisation
import scipy.stats as stat

def main(xmin,xmax,ymin,ymax,m,pressure_yes_no,pressure_level,variable_STASH,measure,percentile):
	if pressure_level == -500:
		FC_data = gent('CP4_FC_month_'+str(m)+'_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_'+str(pressure_level)+'hPa_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', delimiter = ',')
	else:
		FC_data = gent('CP4_FC_month_'+str(m)+'_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', delimiter = ',')

############################################################################################################
#NOTE - The below lines exist as we are linearly regridding CP4-A data to 25 km horizontal resolution
#	
	dummy_fle = iris.load_cube('/nfs/a277/IMPALA/data/25km/a05216/a05216_A1hr_mean_ay488_25km_199905010030-199905302330.nc')
	xysmallslice = iris.Constraint(latitude = lambda cell: float(ystart) <= cell <= float(yend), longitude = lambda cell: float(xstart) <= cell <= float(xend))
	dummy_fle = dummy_fle.extract(xysmallslice)
##############################################################################################################
	counter = 0
	for yyyy in range(1997,2007):
		holdrlist = iris.cube.CubeList([])
		flelist = glob.glob('/nfs/a277/IMPALA/data/4km/'+str(variable_STASH)+'/*'+str(yyyy)+str(m)+'*-'+str(yyyy)+'*.nc')
		flelist.sort()
		for fle in flelist:
			temp = iris.load_cube(fle)
			temp = temp[:-2,:,:].extract(xysmallslice)
                        if int(pressure_level) != -500:
                                pressure_slice = iris.Constraint(pressure_level = int(pressure_level))
                                temp = temp.extract(pressure_slice)
			temp = temp.regrid(dummy_fle, iris.analysis.Linear())
                        if measure.upper() == 'MAX':
                                temp = temp.collapsed('time', iris.analysis.MAX)
                        elif measure.upper() == 'MIN':
                                temp = temp.collapsed('time', iris.analysis.MIN)
                        elif measure.upper() == 'MEAN':
                                temp = temp.collapsed('time', iris.analysis.MEAN)
                        elif measure.upper() == 'SUM':
                                temp = temp.collapsed('time', iris.analysis.SUM)
			temp = temp.data
                        if counter == 0:
                                rainfall = np.zeros((1,temp.shape[0],temp.shape[1]),float)
                                rainfall[0,:,:] = temp
                        else:
                                tempr = np.zeros((1,temp.shape[0],temp.shape[1]),float)
                                tempr[0,:,:] = temp
                                rainfall = np.concatenate((rainfall,tempr), axis = 0)
                        counter = counter + 1

        percents = np.zeros((rainfall.shape[1], rainfall.shape[2]),float)
        for y in range(0, percents.shape[0]):
                for x in range(0,percents.shape[1]):
                        a = rainfall[:,y,x]
                        percents[y,x] = stat.percentileofscore(a,FC_data[y,x],kind="rank")


	if pressure_level == -500:
		np.savetxt('CP4_month_'+str(m)+'where_is_FC_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', percents, delimiter = ',')

	else:
		np.savetxt('CP4_month_'+str(m)+'where_is_FC_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_'+str(pressure_level)+'hPa_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', percents, delimiter = ',')








if "__name__" == "__main__":
	main(xstart,xend,ystart,yend,yyyy)
