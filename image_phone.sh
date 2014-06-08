if [ ! -d images/ ]
then 
	mkdir images
fi

novacom run file://bin/dd if=/dev/mapper/store-root | pv -p -s 450000k > images/root.dd
md5sum root.dd >> image_hashes.txt

novacom run file://bin/dd if=/dev/mapper/store-var | pv -p -s  250000k > images/var.dd
md5sum var.dd >> image_hashes.txt

novacom run file://bin/dd if=/dev/mapper/store-log | pv -p -s 40000k > images/log.dd
md5sum log.dd >> image_hashes.txt

novacom run file://bin/dd if=/dev/mapper/store-media | pv -p -s 7010000k > images/media.dd
md5sum media.dd >> image_hashes.txt

novacom run file://bin/dd if=/dev/mapper/store-swap | pv -p -s 135000k > images/swap.dd
md5sum swap.dd >> image_hashes.txt

novacom run file://bin/dd if=/dev/mapper/control | pv -p -s 480000k > images/control.dd
md5sum control.dd >> image_hashes.txt

novacom run file://bin/dd if=/dev/mapper/store-update | pv -p -s 58000k > images/update.dd
md5sum update.dd >> image_hashes.txt


echo "List of hashes available in image_hashes.txt"
