import sqlite3,os, time

conn = sqlite3.connect("/mnt/var/luna/data/dbdata/PalmDatabase.db3")
c = conn.cursor()

# get all messages

for text, first, last, status, address, timeStamp, flag in c.execute('''
 SELECT com_palm_pim_FolderEntry.messageText,
           com_palm_pim_Recipient.firstName,
           com_palm_pim_Recipient.lastName,
           com_palm_pim_FolderEntry.status,
           com_palm_pim_Recipient.address,
           com_palm_pim_FolderEntry.timeStamp,
           com_palm_pim_FolderEntry.flags
    FROM com_palm_pim_FolderEntry
    JOIN com_palm_pim_Recipient
      ON (com_palm_pim_FolderEntry.id = com_palm_pim_Recipient.com_palm_pim_FolderEntry_id)
    WHERE messageType = "SMS"
    ORDER BY com_palm_pim_FolderEntry.timeStamp'''):

	# no first/last name
	# look it up!
	if first == None and last == None:
		d = conn.cursor()
		d.execute('''
			SELECT firstName, lastName 
			FROM com_palm_pim_Contact 
			WHERE id = 
				(SELECT com_palm_pim_Contact_contactPts_id 
				FROM com_palm_pim_ContactPoint WHERE type = "PHONE"
				AND trailingDigits = ''' + address + ''' % 10000000 LIMIT 1)
			LIMIT 1''')
		row = d.fetchone()
		if row == None:
			first = "Unknown"
			last = "Unknown"
		else:
			first = row[0]
			last = row[1]

	#we sent it
	if  flag == 133:
		print "To: "
	#recieved
	else:
		print "From: "
	if first != "None" and first != "Unknown":
		print first, " "
	if last != None:
		print last

	print ", Phone: ", address
	print "<br>Date: ", time.strftime("%m/%d/%Y %H:%M:%S",time.localtime(timeStamp/1000))
	print "<br>Message: ", text
	print "<br><hr>"
