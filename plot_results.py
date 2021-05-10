import numpy as np
from numpy import genfromtxt as gent
import matplotlib.pyplot as plt
import mpl_toolkits.basemap as bm
import iris

def main(xstart,xend,ystart,yend):
 mnth = ['01','02','03','04','05','06','07','08','09','10','11','12']
 mnthname = ['January','February','March','April','May','June','July','August','September','October','November','December']
 for mn in mnth:
        plt.figure(figsize = (5,8))
        dummy_fle = iris.load_cube('/nfs/a277/IMPALA/data/25km/a05216/a05216_A1hr_mean_ay488_25km_199905010030-199905302330.nc')
        xysmallslice = iris.Constraint(latitude = lambda cell: float(ystart) <= cell <= float(yend), longitude = lambda cell: float(xstart) <= cell <= float(xend))
        dummy_fle = dummy_fle.extract(xysmallslice)
	lons = dummy_fle.coord('longitude').points
	lats = dummy_fle.coord('latitude').points
	plt.clf()
	cc_50 = gent('CP4_CC_50th_percentile_15m_temperatures_month_'+str(mn)+'_'+str(xstart)+'_'+str(xend)+'_'+str(ystart)+'_'+str(yend)+'.csv', delimiter = ',')
	fc_50 = gent('CP4_FC_50th_percentile_15m_temperatures_month_'+str(mn)+'_'+str(xstart)+'_'+str(xend)+'_'+str(ystart)+'_'+str(yend)+'.csv', delimiter = ',')
	levels_cp = np.arange(13,40,1.5)
	plt.subplot(4,2,1)
        m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
        m.drawcountries(linewidth = 1)
        m.drawcoastlines(linewidth = 2)
	cd = plt.contourf(lons, lats, cc_50-273.14, levels_cp, extend = 'min',cmap = plt.get_cmap('spectral'))
	cb = plt.colorbar(cd, orientation = 'vertical')
	cb.set_label('CP4-A CC ($^\circ$C)')
	plt.title('(a)', x = 0.01, fontsize = 10)
	plt.subplot(4,2,3)
        m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
        m.drawcountries(linewidth = 1)
        m.drawcoastlines(linewidth = 2)
	cd = plt.contourf(lons, lats, fc_50-273.14, levels_cp,extend = 'min', cmap = plt.get_cmap('spectral'))
	cb = plt.colorbar(cd, orientation = 'vertical')
	cb.set_label('CP4-A FC ($^\circ$C)')
	plt.title('(c)', x = 0.01, fontsize = 10)

	plt.subplot(4,2,7)
	CP_percentile = gent('CP4_FC_50th_percentile_relative_to_CC_15m_temp_month_'+str(mn)+'_'+str(xstart)+'_'+str(xend)+'_'+str(ystart)+'_'+str(yend)+'.csv' ,delimiter = ',')
        pallette = plt.get_cmap('Set1')
        pallette.set_over('w')
        pallette.set_under('b')
        levels_percentile = [50,75,80,85,90,95,99.9]
	#levels_percentile = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
        m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
        m.drawcountries(linewidth = 1)
        m.drawcoastlines(linewidth = 2)
	cd = plt.contourf(lons, lats, CP_percentile, levels_percentile,extend = 'both', cmap = pallette)
	cb = plt.colorbar(cd, orientation = 'vertical')
	cb.set_label('CP4-A FC 50th \n percentile position')
	plt.title('(g)', x = 0.01, fontsize = 10)







	pcc_50 = gent('param_CC_50th_percentile_15m_temp_month_'+str(mn)+'_'+str(xstart)+'_'+str(xend)+'_'+str(ystart)+'_'+str(yend)+'.csv', delimiter = ',')
	pfc_50 = gent('param_FC_50th_percentile_15m_temp_month_'+str(mn)+'_'+str(xstart)+'_'+str(xend)+'_'+str(ystart)+'_'+str(yend)+'.csv', delimiter = ',')
	levels_cp = np.arange(13,40,1.5)
	plt.subplot(4,2,2)
        m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
        m.drawcountries(linewidth = 1)
        m.drawcoastlines(linewidth = 2)
	cd = plt.contourf(lons, lats, pcc_50-273.14, levels_cp, extend = 'min',cmap = plt.get_cmap('spectral'))
	cb = plt.colorbar(cd, orientation = 'vertical')
	cb.set_label('P25 CC ($^\circ$C)')
	plt.title('(b)', x = 0.01, fontsize = 10)
	plt.subplot(4,2,4)
        m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
        m.drawcountries(linewidth = 1)
        m.drawcoastlines(linewidth = 2)
	cd = plt.contourf(lons, lats, pfc_50-273.14, levels_cp,extend = 'min', cmap = plt.get_cmap('spectral'))
	cb = plt.colorbar(cd, orientation = 'vertical')
	cb.set_label('P25 FC ($^\circ$C)')
	plt.title('(d)', x = 0.01, fontsize = 10)

# dIFFERENCE BETWEEN cc AND fc
	plt.subplot(4,2,5)
	diff_cp = fc_50 - cc_50
	levels_diff = np.arange(4., 9.5, 0.5)
        m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
        m.drawcountries(linewidth = 1)
        m.drawcoastlines(linewidth = 2)
	cd = plt.contourf(lons, lats, diff_cp, levels_diff,extend = 'both', cmap = plt.get_cmap('spectral'))
	cb = plt.colorbar(cd, orientation = 'vertical')
	cb.set_label('CP4-A FC - CC ($^\circ$C)')
	plt.title('(e)', x = 0.01, fontsize = 10)


	plt.subplot(4,2,6)
	diff_param = pfc_50 - pcc_50
        m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
        m.drawcountries(linewidth = 1)
        m.drawcoastlines(linewidth = 2)
	cd = plt.contourf(lons, lats, diff_param, levels_diff,extend = 'both', cmap = plt.get_cmap('spectral'))
	cb = plt.colorbar(cd, orientation = 'vertical')
	cb.set_label('P25 FC - CC ($^\circ$C)')
	plt.title('(f)', x = 0.01, fontsize = 10)





	plt.subplot(4,2,8)
        pallette = plt.get_cmap('Set1')
        pallette.set_over('w')
        pallette.set_under('b')
        levels_percentile = [50,75,80,85,90,95,99.9]
	CP_percentile = gent('param_FC_50th_percentile_relative_to_CC_15m_temp_month_'+str(mn)+'_'+str(xstart)+'_'+str(xend)+'_'+str(ystart)+'_'+str(yend)+'.csv' ,delimiter = ',')
        m = bm.Basemap(projection='cyl',llcrnrlat = lats[0], urcrnrlat = lats[-1], llcrnrlon = lons[0], urcrnrlon = lons[-1],  resolution = 'l')
        m.drawcountries(linewidth = 1)
        m.drawcoastlines(linewidth = 2)
	cd = plt.contourf(lons, lats, CP_percentile, levels_percentile,extend = 'both', cmap = pallette)
	cb = plt.colorbar(cd, orientation = 'vertical')
#	cb.ax.set_xticklabels(levels_percentile[:],rotation = 90)
	cb.set_label('P25 FC 50th \n percentile position')
	plt.title('(h)', x = 0.01, fontsize = 10)
	plt.suptitle(str(mnthname[int(mn)-1])+' comparison')
        plt.subplots_adjust(wspace = 0.5)
        plt.savefig(str(mnthname[int(mn)-1])+'_Min_T_comparisons_'+str(xstart)+'_'+str(xend)+'_'+str(ystart)+'_'+str(yend)+'.png', bbox_inches = 'tight')








if "__name__" == "__main__":
	main(xstart,xend,ystart,yend)
