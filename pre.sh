
# image disks
#novacom run file://bin/dd if=/dev/mapper/store-root | pv -p -s 450000k > root.dd
#novacom run file://bin/dd if=/dev/mapper/store-var | pv -p -s 	250000k > var.dd
#novacom run file://bin/dd if=/dev/mapper/store-log | pv -p -s 40000k > log.dd
#novacom run file://bin/dd if=/dev/mapper/store-media | pv -p -s 7010000k > media.dd
#novacom run file://bin/dd if=/dev/mapper/store-swap | pv -p -s 135000k > swap.dd
#novacom run file://bin/dd if=/dev/mapper/control | pv -p -s 480000k > control.dd



# run find stuff in contacts DB

################# emails/ims
# run python file


#browser stuff

#any other apps to look at



############## context file stuff

# find a line that has timestamp: XXX, latituide: XXX, logitude: XXX
line=`img_cat ../../var.dd | grep "\"timestamp\": [0-9]\+\.[0-9]\+, \"latitude\": -\?[0-9]\+\.[0-9]\+, \"longitude\": -\?[0-9]\+\.[0-9]\+" --binary-file="text"`

# get the timestamp
time=`echo $line | sed 's/{ \"errorCode\": [0-9]\+, \"timestamp\": \([0-9]\+\).*/\1/'`

#the trailing 3 digits are extra...dunno what they're for...ms perhaps??
realtime=`echo $time | awk '{ print substr( $0, 0, length($0) - 2 ) }'`

# print the date
date -d "UTC 1970-01-01 $realtime secs"


# get the lat/long, output the link
echo $line | sed 's/{ \"errorCode\": [0-9]\+, \"timestamp\": [0-9]\+\.[0-9]\+, \"latitude\": \(-\?[0-9]\+\.[0-9]\+\), \"longitude\": \(-\?[0-9]\+\.[0-9]\+\).*/<a href=\"http:\/\/maps.google.com\/maps?q=\1,++\2\">Map<\/a>/'
