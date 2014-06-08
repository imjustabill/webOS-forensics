WebOS Forensics
===============

Some forensic analysis tools for Palm/HP WebOS. I haven't used these for a few years, but publising them in case someone finds them useful. 

### Requirements
* A WebOS Phone
* Linux environment
* WebOS SDK
* sleuthkit package, for searching slack space
* pv package, for providing a progress bar while creating images
* Python 2.6 or greater

To use, run image.sh to create images, then run run.sh to generate report. Run unmount.sh to unmount images when finished. If you wish to mount the images without creating a report, just run mount.sh

### Known Issues
* Timestamps stored on the phone are assumed to be from the same time zone as the host computer.
* Forwarded emails, replies, and emails with more than one recipient may show up multiple times.
* May have trouble handling Unicode characters in some fields.
