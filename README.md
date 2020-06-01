# Elevation map to 3D sample object 
## Project :3D printed landscapes
Date: May 4, 2020
Bordeaux Université	 
Master Informatique 2019

Team members:
* Tran Quang Tung	(quangtung0276@yahoo.com)
* Nguyen Quoc Khanh (qkhanh2006@gmail.com)
* Nguyen Vu Anh Trung (kivanolai@gmail.com)

#Components:
##WhiteBox Tools
https://jblindsay.github.io/wbt_book/intro.html
WhiteboxTools is an advanced geospatial data analysis platform created by Prof. John Lindsay at the University of Guelph's Geomorphometry and Hydrogeomatics Research Group (GHRG). The project began in January 2017 and quickly evolved in terms of its analytical capabilities. The WhiteboxTools homepage contains more project information and the software download site.
###Example
Binary of whiteBox found in /whitebox/linux64/
cd /whitebox/linux64/
run analysis of data source ./whitebox_tools -r=lidar_info --cd="../data" -i=points.las --vlr --geokeys
