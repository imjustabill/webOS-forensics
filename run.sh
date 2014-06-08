if [ "$(id -u)" != "0" ]; then
   echo "You need to be root!"
   exit 1
fi


echo "Script is starting"

echo "Removing old html files..."
rm -f *.html

echo "Unmounting any old images..."
sh unmount.sh

echo "Mounting images..."
sh mount.sh

echo "Extracting browser history..."
python browser.py > browser.html

echo "Extracting contacts..."
python contacts.py > contacts.html

echo "Extracting call log..."
python calls.py > calls.html

echo "Extracting emails..."
python email.py >  email.html

echo "Extracting calendar..."
python events.py > events.html

echo "Extracting IMs..."
python im.py > im.html

echo "Extracting SMSs..."
python sms.py > sms.html

echo "Extracting stored GPS locations..."
sh context.sh > context.html

echo "Generating list of files on media partition..."
python media.py > media.html

# remove old hashes file
rm -f report/hashes.txt 

md5sum  browser.html >> file_hashes.txt
md5sum  contacts.html >> file_hashes.txt
md5sum  email.html >> file_hashes.txt
md5sum  events.html >> file_hashes.txt
md5sum  im.html >> file_hashes.txt
md5sum  sms.html >> file_hashes.txt
md5sum  context.html >> file_hashes.txt
md5sum  calls.html >> file_hashes.txt
md5sum  media.html >> file_hashes.txt

echo "Generating report..."
echo "<html>
<h2>WebOS Forensics Report</h2>
Generated on " >> report.html
echo `date +"%x %r"` >> report.html
echo "<br><br>
<a href=\"browser.html\">Browser</a><br>
<a href=\"contacts.html\">Contacts</a><br>
<a href=\"calls.html\">Calls</a><br>
<a href=\"context.html\">Locations</a><br>
<a href=\"events.html\">Events</a><br>
<a href=\"email.html\">Email</a><br>
<a href=\"sms.html\">SMS</a><br>
<a href=\"im.html\">IMs</a><br>
<a href=\"media.html\">Media</a><br>
<br>
<a href=\"file_hashes.txt\">File hashes</a><br>
<a href=\"image_hashes.txt\">Image hashes</a><br>
</html>" >> report.html

echo "Finished!"
echo ""
echo "Please open report.html in your browser"
echo "See hashes.txt for hashes of created files"
