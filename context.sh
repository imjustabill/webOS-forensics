############## context file stuff 
  

echo "<h2>Saved Locations</h2><br>"
# find a line that has timestamp: XXX, latituide: XXX, logitude: XXX 
line=`img_cat images/var.dd | grep "\"timestamp\": [0-9]\+\.[0-9]\+, \"latitude\": -\?[0-9]\+\.[0-9]\+, \"longitude\": -\?[0-9]\+\.[0-9]\+" --binary-file="text"` 

if [ ! line = "" ]
then
	# get the timestamp 
	time=`echo $line | sed 's/{ \"errorCode\": [0-9]\+, \"timestamp\": \([0-9]\+\).*/\1/'` 
	    
	#the trailing 3 digits are extra...dunno what they're for...ms perhaps?? 
	realtime=`echo $time | awk '{ print substr( $0, 0, length($0) - 2 ) }'` 
	 
	# print the date 
	date -d "UTC 1970-01-01 $realtime secs" 
	   

	# get the lat/long, output the link 
	echo $line | sed 's/{ \"errorCode\": [0-9]\+, \"timestamp\": [0-9]\+\.[0-9]\+, \"latitude\": \(-\?[0-9]\+\.[0-9]\+\), \"longitude\": \(-\?[0-9]\+\.[0-9]\+\), \"horizAccuracy\": \(-\?[0-9]\+\).*/<br>Coordinates: \1,\2<br>Accuracy: \3 meters<br><a href=\"http:\/\/maps.google.com\/maps?q=\1,++\2\">Map<\/a><br>/'

fi

if [ ! -d rescued/ ]
then
	mkdir rescued
fi

#remove any leftover unzipped files
rm -f rescued/*

#look for any gzipped files (context files are sent to palm as .gz)
magicrescue -r /usr/share/magicrescue/recipes/gzip -d rescued/ images/var.dd > /dev/null 2>&1
#go through all of them 

# find a line that has timestamp: XXX, latituide: XXX, logitude: XXX 
line=`cat rescued/* | grep "\"timestamp\": [0-9]\+\.[0-9]\+, \"latitude\": -\?[0-9]\+\.[0-9]\+, \"longitude\": -\?[0-9]\+\.[0-9]\+" --binary-file="text"` 

if [ -n "$line" ]
then
	echo "<hr>"
	# get the timestamp 
	time=`echo $line | sed 's/{ \"errorCode\": [0-9]\+, \"timestamp\": \([0-9]\+\).*/\1/'` 
    
	#the trailing 3 digits are extra...dunno what they're for...ms perhaps?? 
	realtime=`echo $time | awk '{ print substr( $0, 0, length($0) - 2 ) }'` 
	 
	# print the date 
	date -d "UTC 1970-01-01 $realtime secs" 

	# get the lat/long, output the link 
	echo $line | sed 's/{ \"errorCode\": [0-9]\+, \"timestamp\": [0-9]\+\.[0-9]\+, \"latitude\": \(-\?[0-9]\+\.[0-9]\+\), \"longitude\": \(-\?[0-9]\+\.[0-9]\+\), \"horizAccuracy\": \(-\?[0-9]\+\).*/<br>Coordinates: \1,\2<br>Accuracy: \3 meters<br><a href=\"http:\/\/maps.google.com\/maps?q=\1,++\2\">Map<\/a><br>/'
fi

#remove unzipped files
rm -f rescued/*
