import CP4_cc_csv_maker
import CP4_fc_csv_maker
import param_cc_csv_maker
import param_fc_csv_maker
import CP4_where_is_fc_percentile_csv_maker
import param_where_is_fc_percentile_csv_maker
import plot_results
import numpy as np
from numpy import genfromtxt as gent

def main():
	xmin = float(raw_input("Please enter the western most longitude (for 20W type 340) - "))
	xmax = float(raw_input("Please enter the eastern most longitude (for 20W type 340) - "))
	ymin = float(raw_input("Please enter the southern most latitude (for 10S type -10) - "))
	ymax = float(raw_input("Please enter the northern most latitude (for 10S type -10) - "))
	pressure_yes_no = 'n'
	pressure_yes_no = str(raw_input("Are you using pressure level data? (Type Y or y for yes) - "))
	if pressure_yes_no == 'Y' or pressure_yes_no == 'y':
		pressure_level = int(raw_input("Please enter the desired pressure level in hPa -"))
	else:
		pressure_level = -500
	variable_STASH = str(raw_input("Please enter the stash code for the target variable (e.g. f30201 for u winds on pressure level) - "))
	variable_long_name = str(raw_input("Please enter the variable name for plots and csv files - "))
	measure = str(raw_input("Please enter MAX, MEAN, MIN, or SUM depending on the daily measure you wish to calculate -")
	percentile = float(raw_input("Please enter the percentile in each climate you want to compare (e.g. 50th percentile) -")

# For now, the code will go through every month. Possible to change this so that a specific month or season can be selected by people,
# however for now, this loop is hard coded

	mnth = ['01','02','03','04','05','06','07','08','09','10','11','12']
	mnthname = ['January','February','March','April','May','June','July','August','September','October','November','December']
	for m in mnth:
		print(m)


# So, let us start by considering single level metrics (the more common metrics we start with		
		if pressure_level == -500:


# So, for plotting we will need 6 arrays with model data inside them, as well as the latitudes and longitudes. 
# Latitudes and longitudes will be saved in the CP4_cc_array code, so try this one first.
			try:
				CP4_cc_array = gent('CP4_CC_month_'+str(m)+'_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', delimiter = ',')
				CP4_lons = gent("CP4_longitudes_"+str(xmin)+"_"+str(xmax)+".csv", delimiter = ',')
				CP4_lats = gent("CP4_latitudes_"+str(xmin)+"_"+str(xmax)+".csv", delimiter = ',')
			except IOError:
				CP4_cc_csv_maker.main(xmin,xmax,ymin,ymax,m,pressure_yes_no,pressure_level,variable_STASH,measure,percentile)
				CP4_cc_array = gent('CP4_CC_month_'+str(m)+'_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', delimiter = ',')
				CP4_lons = gent("CP4_longitudes_"+str(xmin)+"_"+str(xmax)+".csv", delimiter = ',')
				CP4_lats = gent("CP4_latitudes_"+str(xmin)+"_"+str(xmax)+".csv", delimiter = ',')


# CP4-A future climate data
			try:
				CP4_fc_array = gent('CP4_FC_month_'+str(m)+'_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', delimiter = ',')
			except IOError:
				CP4_fc_csv_maker.main(xmin,xmax,ymin,ymax,m,pressure_yes_no,pressure_level,variable_STASH,measure,percentile)
				CP4_fc_array = gent('CP4_FC_month_'+str(m)+'_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', delimiter = ',')


# Now the CP4-A where is current climate percentile relative to future climate
			try:
				CP4_fc_where_array = gent('CP4_month_'+str(m)+'where_is_FC_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', delimiter = ',')
			except IOError:
				CP4_where_is_fc_percentile_csv_maker.main(xmin,xmax,ymin,ymax,m,pressure_yes_no,pressure_level,variable_STASH,measure,percentile)
				CP4_fc_where_array = gent('CP4_month_'+str(m)+'where_is_FC_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', delimiter = ',')



# Okay fantastic. So that is the CP4-A data sorted
# Now we want to have a look at getting the P25 data in

			try:
				P25_cc_array = gent('P25_CC_month_'+str(m)+'_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', delimiter = ',')
				P25_lons = gent("P25_longitudes_"+str(xmin)+"_"+str(xmax)+".csv", delimiter = ',')
				P25_lats = gent("P25_latitudes_"+str(xmin)+"_"+str(xmax)+".csv", delimiter = ',')
			except IOError:
				param_cc_csv_maker.main(xmin,xmax,ymin,ymax,m,pressure_yes_no,pressure_level,variable_STASH,measure,percentile)
				P25_cc_array = gent('P25_CC_month_'+str(m)+'_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', delimiter = ',')
				P25_lons = gent("P25_longitudes_"+str(xmin)+"_"+str(xmax)+".csv", delimiter = ',')
				P25_lats = gent("P25_latitudes_"+str(xmin)+"_"+str(xmax)+".csv", delimiter = ',')


# P25 future climate data

			try:
				P25_fc_array = gent('P25_FC_month_'+str(m)+'_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', delimiter = ',')
			except IOError:
				param_fc_csv_maker.main(xmin,xmax,ymin,ymax,m,pressure_yes_no,pressure_level,variable_STASH,measure,percentile)
				P25_fc_array = gent('P25_FC_month_'+str(m)+'_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', delimiter = ',')



# P25 where is the future percentile compared to current climate data

			try:
				P25_fc_where_array = gent('P25_month_'+str(m)+'where_is_FC_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', delimiter = ',')
			except IOError:
				param_where_is_fc_percentile_csv_maker.main(xmin,xmax,ymin,ymax,m,pressure_yes_no,pressure_level,variable_STASH,measure,percentile)
				P25_fc_where_array = gent('P25_month_'+str(m)+'where_is_FC_'+str(percentile)+'th_percentile_'+str(variable_STASH)+'_single_level_daily_'+str(measure)+'_lon_'+str(xmin)+'_'+str(xmax)+'_lat_'+str(ymin)+'_'+str(ymax)+'.csv', delimiter = ',')


# okay, that is the six files we need, now let us plot. Might be easier to have this in the code right now.

			plt.figure(figsize = (5,8))
			plt.subplot(4,2,1)
			levels = np.linspace(np.percentile(CP4_cc_array,10), np.percentile(CP4_cc_array,90),10)
			m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
			m.drawcountries(linewidth = 1)
			m.drawcoastlines(linewidth = 2)
			cd = plt.contourf(CP4_lons, CP4_lats, CP4_cc_array, levels, extend = 'both',cmap = plt.get_cmap('spectral'))
			cb = plt.colorbar(cd, orientation = 'vertical')
			cb.set_label('CP4-A CC')
			plt.title('(a)', x = 0.01, fontsize = 10)
			plt.subplot(4,2,3)
			levels = np.linspace(np.percentile(CP4_fc_array,10), np.percentile(CP4_fc_array,90),10)
			m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
			m.drawcountries(linewidth = 1)
			m.drawcoastlines(linewidth = 2)
			cd = plt.contourf(CP4_lons, CP4_lats, CP4_fc_array, levels,extend = 'both', cmap = plt.get_cmap('spectral'))
			cb = plt.colorbar(cd, orientation = 'vertical')
			cb.set_label('CP4-A FC')
			plt.title('(c)', x = 0.01, fontsize = 10)

			plt.subplot(4,2,2)
			levels = np.linspace(np.percentile(P25_cc_array,10), np.percentile(P25_cc_array,90),10)
			m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
			m.drawcountries(linewidth = 1)
			m.drawcoastlines(linewidth = 2)
			cd = plt.contourf(P25_lons, P25_lats, P25_cc_array, levels, extend = 'both',cmap = plt.get_cmap('spectral'))
			cb = plt.colorbar(cd, orientation = 'vertical')
			cb.set_label('P25 CC')
			plt.title('(b)', x = 0.01, fontsize = 10)
			plt.subplot(4,2,4)
			levels = np.linspace(np.percentile(P25_fc_array,10), np.percentile(P25_fc_array,90),10)
			m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
			m.drawcountries(linewidth = 1)
			m.drawcoastlines(linewidth = 2)
			cd = plt.contourf(P25_lons, P25_lats, P25_fc_array, levels,extend = 'both', cmap = plt.get_cmap('spectral'))
			cb = plt.colorbar(cd, orientation = 'vertical')
			cb.set_label('P25 FC')
			plt.title('(d)', x = 0.01, fontsize = 10)


# dIFFERENCE BETWEEN cc AND fc
			plt.subplot(4,2,5)
			diff_cp = CP4_fc_array - CP4_cc_array
			levels_diff = np.linspace(np.percentile(diff_cp,10), np.percentile(diff_cp,90), 10)
			m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
			m.drawcountries(linewidth = 1)
			m.drawcoastlines(linewidth = 2)
			cd = plt.contourf(CP4_lons, CP4_lats, diff_cp, levels_diff,extend = 'both', cmap = plt.get_cmap('spectral'))
			cb = plt.colorbar(cd, orientation = 'vertical')
			cb.set_label('CP4-A FC - CC')
			plt.title('(e)', x = 0.01, fontsize = 10)


			plt.subplot(4,2,6)
			diff_param = P25_fc_array - P25_cc_array
			m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
			m.drawcountries(linewidth = 1)
			m.drawcoastlines(linewidth = 2)
			cd = plt.contourf(P25_lons, P25_lats, diff_param, levels_diff,extend = 'both', cmap = plt.get_cmap('spectral'))
			cb = plt.colorbar(cd, orientation = 'vertical')
			cb.set_label('P25 FC - CC')
			plt.title('(f)', x = 0.01, fontsize = 10)

# now for the location plots


			plt.subplot(4,2,7)
			pallette = plt.get_cmap('Set1')
			pallette.set_over('w')
			pallette.set_under('b')
			levels_percentile = [50,75,80,85,90,95,99.9]
			m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
			m.drawcountries(linewidth = 1)
			m.drawcoastlines(linewidth = 2)
			cd = plt.contourf(CP4_lons, CP4_lats, CP4_fc_where_array, levels_percentile,extend = 'both', cmap = pallette)
			cb = plt.colorbar(cd, orientation = 'vertical')
			cb.set_label('CP4-A FC 50th \n percentile position')
			plt.title('(g)', x = 0.01, fontsize = 10)

			plt.subplot(4,2,8)
			m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
			m.drawcountries(linewidth = 1)
			m.drawcoastlines(linewidth = 2)
			cd = plt.contourf(P25_lons, P25_lats, P25_fc_where_array, levels_percentile,extend = 'both', cmap = pallette)
			cb = plt.colorbar(cd, orientation = 'vertical')
			cb.set_label('P25 FC 50th \n percentile position')
			plt.title('(g)', x = 0.01, fontsize = 10)
			plt.suptitle(str(mnthname[int(mn)-1])+' comparison')
			plt.subplots_adjust(wspace = 0.5)
# Needs pressure level adding
			plt.savefig(str(mnthname[int(mn)-1])+'_'+str(variable_STASH)+'_comparisons_'+str(xstart)+'_'+str(xend)+'_'+str(ystart)+'_'+str(yend)+'.png', bbox_inches = 'tight')



if "__name__" == "__main__":
	main()
