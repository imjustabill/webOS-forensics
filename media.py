import os, hashlib
print "<h1>Media Partition</h1>"
for root, dirs, files in os.walk("/mnt/media"):
	print "Directory:  ",root
	print "<ul>"
	for i in files:
		print "<li><a href=\""+root+"/"+i+"\">"+i+"</a>"
                file=open(root+"/"+i, 'rb').read()
                print "&nbsp&nbsp&nbsp&nbsp&nbsp MD5: "+ hashlib.md5(file).hexdigest(),"<br>"
		print "</li>"
	print "</ul>"
