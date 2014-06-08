import sqlite3,os, time

conn = sqlite3.connect("/mnt/var/luna/data/dbdata/PalmDatabase.db3")
c = conn.cursor()

# get all messages
print "<h2>Call Logs</h2><br>"
for name, number, type, start, length in c.execute('''
SELECT displayName,
        number,
        type,
        startTime,
        duration
FROM com_palm_superlog_Superlog

ORDER BY startTime    
'''):
	if type == 'incoming':
		print "From: "	
	elif type == 'outgoing':
		print "To: "	
	else: 
		print "Missed call from:  "	
	print name, "<br>"
	print "Number: ", number, "<br>"
	print "Start Time: ", time.strftime("%m/%d/%Y %H:%M:%S",time.localtime(int(start)/1000))
	print "<br>"
	print "Duration: ", int(length)/60000, " mins, ", int(length)%60000/1000, " secs<br>"
	print "<hr>"
