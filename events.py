import sqlite3,os, time

conn = sqlite3.connect("/mnt/var/luna/data/dbdata/PalmDatabase.db3")
c = conn.cursor()

# get all messages
print "<h2>Events</h2><br>"
for start, end, rrule, subject, location, note in c.execute('''
SELECT startTimeStamp,
	endTimeStamp,
	rrule,
	subject,
	location,
	note

FROM com_palm_pim_CalendarEvent
	
    ORDER BY startTimeStamp'''):

	print "Start Time: ", time.strftime("%m/%d/%Y %H:%M:%S",time.localtime(start/1000))
	print "<br>"
	print "End Time: ", time.strftime("%m/%d/%Y %H:%M:%S",time.localtime(end/1000))
	print "<br>"
	if rrule != None:
		print "Repeats: "
		print rrule
	print "<br>"
	print "Subject: "
	if subject != None:
		print subject
	print "<br>"
	print "Location: "
	if location != None:
		print location
	print "<br>"
	print "Note: "
	if note != None:
		print note.encode("utf-8")
	print "<br>"
	print "<hr>"
