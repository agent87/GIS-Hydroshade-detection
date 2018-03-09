#adf to tif file format converter
#the script converts a whole file
#requirements gdal, grass
#initial arguments
#for the output format just name your file, format suffic is not needed!

#importing needd modules
import os 
from sys import argv

#the initial variable given at the start of the script
#scriptname is the name of the script
#original_file is the name of the input folder to be converted
#new_filename is the given name of the tif file
try:
	scriptname,original_file, format_type, new_filename = argv
except ValueError:
	scriptname,original_file, new_filename = argv
	format_type = "GTiff"




#adding format suffix to the output file
new_file = new_filename + ".tif"


script_format = "gdal_translate {0} -of {1} {2}".format(original_file, format_type, new_file)
#executing the script
os.system(script_format)



