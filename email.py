import sqlite3, os, time, hashlib

conn = sqlite3.connect("/mnt/var/luna/data/dbdata/PalmDatabase.db3")
c = conn.cursor()
d = conn.cursor()


print "<h2>Emails</h2><br>"

#TODO: use a for loop here!!
c.execute("""
SELECT DISTINCT com_palm_pim_FolderEntry.id, address, com_palm_pim_FolderEntry.displayName, summary,  textCacheKey, previewText, timeStamp  FROM com_palm_pim_FolderEntry 
    JOIN com_palm_pim_Recipient 
      ON (com_palm_pim_FolderEntry.id = com_palm_pim_Recipient.com_palm_pim_FolderEntry_id) 
      WHERE textCacheKey != ''  
      ORDER BY timeStamp
""")


rows = c.fetchall()
x = 1
for row in rows:

	#find the file 
	fileLoc = os.popen("find /mnt/var/luna/data/emails/ -name " + row[4]).read()
	print "#",x, "<br>from: ", row[2].encode("utf-8"), "<br>address: ",row[1].encode("utf-8"), "<br>subject:", row[3].encode("utf-8"), "<br>"
	#get rid of the last 3 digits to get the proper timestamp
	print "Date: ", time.strftime("%m/%d/%Y %H:%M:%S",time.localtime(row[6]/1000)), "<br>"
	print "Summary: ", row[5].encode("utf-8"), "<br>"
	for displayName, uri in	d.execute("""
		SELECT displayName, uri  
		FROM com_palm_pim_Part 
		WHERE com_palm_pim_FolderEntry_id = """ + str(row[0]) + """
		AND uri != ''"""):
			file=open('/mnt/'+uri, 'rb').read()
			print "Attachment: <a href=\"/mnt"+uri+"\">",displayName,"</a>"
			print "&nbsp&nbsp&nbsp&nbsp&nbsp MD5: "+ hashlib.md5(file).hexdigest(),"<br>"




	print "<a href = \"", fileLoc, "\">Full Text</a>"
	print "<br><hr>"
        x = x +1

