#if directories dont exist, create them
if [ ! -d /mnt/root ]
then
	mkdir /mnt/root
fi

if [ ! -d /mnt/log ]
then
	mkdir /mnt/log 
fi

if [ ! -d /mnt/media ]
then
	mkdir /mnt/media 
fi

if [ ! -d /mnt/var ]
then
	mkdir /mnt/var
fi

if [ ! -d /mnt/control ]
then
	mkdir /mnt/control
fi

if [ ! -d /mnt/update ]
then
	mkdir /mnt/update
fi

# mount the images read-only
mount -o ro,loop images/log.dd /mnt/log 
mount -o ro,loop images/media.dd /mnt/media
mount -o ro,loop images/root.dd /mnt/root
mount -o ro,loop images/var.dd /mnt/var
mount -o ro,loop images/control.dd /mnt/control 
mount -o ro,loop images/update.dd /mnt/update
