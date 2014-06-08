import sqlite3,os, time

conn = sqlite3.connect("/mnt/var/luna/data/dbdata/PalmDatabase.db3")
c = conn.cursor()
d = conn.cursor()

# get all messages

print "<h2>Contacts</h2><br>"
for first, middle, last, picLoc, picLocBig, display, id in c.execute('''
	SELECT  com_palm_pim_Person.firstName,
	        com_palm_pim_Person.middleName,  
        	com_palm_pim_Person.lastName,  
	        com_palm_pim_Person.pictureLoc,  
	        com_palm_pim_Person.pictureLocBig,  
	        com_palm_pim_Person.displayText,
	        com_palm_pim_Person.id
	FROM com_palm_pim_Person
	'''):
	
	if picLocBig != '':
		print "<img src = \"/mnt/" + picLocBig + "\"><br>"
	elif picLoc != '':
		print "<img src = \"/mnt/" + picLoc + "\"><br>"
		
	print "Name: "
	if first != None:
		print first, " "
	if middle != None:
		print middle, " "
	if last != None:	
		print last
	print "<br>"
	print "Display Name: ",
	if display != None:
		print display
	print "<br>"
	print "<ul>"
	for cDisplay, cFirst, cMiddle, cLast, cPicLoc, cType, cValue, cService,cStatus in d.execute('''
		Select  com_palm_pim_Contact.displayText,
			com_palm_pim_Contact.firstName,
			com_palm_pim_Contact.middleName,
			com_palm_pim_Contact.lastName,
			com_palm_pim_Contact.pictureLoc,
			com_palm_pim_ContactPoint.type,
			com_palm_pim_ContactPoint.value,
			com_palm_pim_ContactPoint.serviceName,
			com_palm_pim_Contact.status

		FROM com_palm_pim_Contact 
		JOIN com_palm_pim_ContactPoint
		ON com_palm_pim_Contact.id = com_palm_pim_ContactPoint.com_palm_pim_Contact_ContactPts_id
		WHERE com_palm_pim_Contact.com_palm_pim_Person_id = ''' + str(id)):
		print "<li>"

		if cPicLoc != '':
			print "<img src = \"/mnt/" + cPicLoc + "\"><br>"
		print "Name: "
		if cFirst != None:
			print cFirst, " "
		if cMiddle != None:
			print cMiddle, " "
		if cLast != None:	
			print cLast
		print "<br>"
		if display != None:
			print "Display Name: ", cDisplay, "<br>"

		if cType == "EMAIL":
			print " Address: "
		elif cType == "PHONE":
			print " Number: "
		elif cType == "IM":
			print " ",cService, " Screen Name: "
		print cValue, "<br>"

		if cStatus != None:
			print "Status: ", cStatus.encode("utf-8"), "<br>"
				

		print "</li>"
	print "</ul>"
	print "<hr>"

