import sqlite3, os, time

conn = sqlite3.connect("/mnt/var/luna/data/dbdata/PalmDatabase.db3")
c = conn.cursor()

c.execute("""
SELECT DISTINCT address, com_palm_pim_FolderEntry.displayName, summary,  textCacheKey, previewText, timeStamp  FROM com_palm_pim_FolderEntry 
    JOIN com_palm_pim_Recipient 
      ON (com_palm_pim_FolderEntry.id = com_palm_pim_Recipient.com_palm_pim_FolderEntry_id) 
      WHERE textCacheKey != ''  
      ORDER BY timeStamp
""")


rows = c.fetchall()
x = 1
for row in rows:
	#find the file 
	fileLoc = os.popen("find /mnt/var/luna/data/emails/ -name " + row[3]).read()
		
        print "#",x, "<br>from: ", row[1].encode("utf-8"), "<br>address: ",row[0].encode("utf-8"), "<br>subject:", row[2].encode("utf-8"), "<br>"
	#get rid of the last 3 digits to get the proper timestamp
	print "Date: ", time.strftime("%m/%d/%Y %H:%M:%S",time.localtime(row[5]/1000)), "<br>"
	print "Summary: ", row[4].encode("utf-8")
	print "<br><a href = \"", fileLoc, "\">Full Text</a>"
	print "<br><br>"
        x = x +1

