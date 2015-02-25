#!usr/bin/python3

import sys
import shutil

def main(argv):
	# argv[1] = input file, argv[2] = output file
	srcFile = argv[1]
	destFile = argv[2]
	
	# Clone xml file & import it
	shutil.copyfile(srcFile, destFile)
	import xml.etree.ElementTree as ET
	tree = ET.parse(destFile)
	root = tree.getroot()
	
	# Iterate over all points of the corpus
	for point in root:
		bottomHz = float(point.find('BOTTOM_HZ').text)
		topHz = float(point.find('TOP_HZ').text)
		fEnd = float(point.find('F0_END').text)
		fStart = float(point.find('F0_START').text)
		
		# Check if fStart & fEnd are between Hz boundaries
		if((fStart < bottomHz) or (fStart > topHz) or (fEnd < bottomHz) or (fEnd > topHz)):
				root.remove(point)
	
	tree.write(destFile)
	
if __name__ == "__main__":
	main(sys.argv)
