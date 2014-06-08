import sqlite3,os, time

conn = sqlite3.connect("/mnt/var/palm/data/file_.usr.palm.applications.com.palm.app.browser_0/0000000000000004.db")
c = conn.cursor()

print "<h2>Bookmarks</h2>"
for url, title, date, vcount, lastVisit in c.execute('''
SELECT url, title, date, visitCount, lastVisited
 FROM bookmarks '''):
	print "Title: ", title, "<br>"
	print "URL: <a href=\""+url+"\">"+url+"</a>"+"<br>"
	print "Date: ", time.strftime("%m/%d/%Y %H:%M:%S",time.localtime(date/1000)), "<br>"
	print "Visit Count: ", vcount, "<br>"
	print "Last Visited: ", time.strftime("%m/%d/%Y %H:%M:%S",time.localtime(lastVisit/1000)) , "<br>"
	print "<hr>"


print "<h2>History</h2>"
for date, url, title in c.execute('''
SELECT date, url, title FROM history
'''):
	print "Title: "
	if title != None:
		print title.encode("utf-8")
	print  "<br>"
	print "URL: <a href=\""+url+"\">"+url+"</a>"+"<br>"
	print "Date: ", time.strftime("%m/%d/%Y %H:%M:%S",time.localtime(date/1000)) , "<br>"
	print "<hr>"
