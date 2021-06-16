# Driv3rs.py
### A script to help catalog SOS.DRIVER files.

## Usage:
`$python Driv3rs.py [SOS_DRIVER_FILE] [output_file.csv]`

## Description and Philosophy:

**Driv3rs.py** is a Python 2.7 script written for Apple /// fans. The Apple /// was one of the first computers to introduce the concept of device drivers, small modules that installed into an operating system to run either built-in hardware, internally installed cards, or devices attached to the computer externally. Over the course of the few years of the Apple ///'s existence, hardware manufacturers built devices and wrote device drivers to support those devices (e.g. Apple's ProFile hard drive, the CFFA3000, etc.). However, the Apple /// simply didn't achieve as much prominence as the Apple II-series. Therefore, many drivers remain buried on imaged disks scattered on the Internet and elsewhere.

Driv3rs.py hopes to help that situation. Given a SOS.DRIVER file properly exported from an imaged Apple /// disk, Driv3rs.py can produce a Comma Separated Values (CSV) file. This CSV contains a whole host of stats including device name, commentary, manufacturer, as well as other potentially useful pieces of information.

When using an Apple ///, users would run a utility called the System Configuration Program (SCP) to install and uninstall drivers. A manufacturer, such as Apple Computer, would provide a driver on floppy. The user would then add the supplied driver to a configuration via the SCP. Finally, the user would instruct the SCP to create a new Sophisticated Operating System (SOS) bootable floppy with the new driver installed into a SOS.DRIVER file. Once booted from that floppy, the driver would then support the installed hardware.

Driv3rs.py works by opening the SOS.DRIVER file and then walking the Device Information Block (DIB) for every driver found within. The information gathered closely parallels the outlined DIB published in Apple's "Apple /// SOS Device Driver Writer's Guide." All information is eventually stored in the output CSV file.

## Requirements:

* Imaged Apple /// disk
* SOS.DRIVER files to be searched
* A utility like AppleCommander to manage files on imaged disks.
* Java, if required for your third party utility.

## Suggested Workflow:

1. Acquire an imaged Apple /// floppy disk.
2. Use AppleCommander's CLI functions to export the SOS.DRIVER file from the imaged disk. (See notes below on AppleCommander usage.)
3. Rename the exported SOS.DRIVER file to something that will clue you into where the SOS.DRIVER file came from.
4. Place the SOS.DRIVER file in same directory as Driv3rs.py.
5. Run the script according to the Usage section above.

A CSV file will be generated with driver information found inside the SOS.DRIVER file.

(**Note:** If the CSV already exists, Driv3rs.py will append the new SOS.DRIVER file's contents to the existing CSV file. This is handy if you're processing multiple SOS.DRIVER files.)

## Notes about AppleCommander:

AppleCommander is a utility written in Java for Apple II users. It allows manipulation of many different types of Apple II-based imaged floppy disks, including disks formatted in DOS 3.2, 3.3 and ProDOS. Apple's Sophisticated Operating System (SOS) is ProDOS's predecessor. Therefore, AppleCommander's ProDOS features can be used to easily export files from SOS disks.

Because AppleCommander is written in Java, you must have Java on your workstation in order to use it. AppleCommander's command-line functions work fine in Java 8. However, AppleCommander's GUI requires the 32-bit version of Java 6 which is very old at this date, vulnerable to security issues and hard to obtain. In short, we recommended using AppleCommander's command-line features in Java 8 rather than installing Java 6.

Here's the suggested command-line to enter when exporting using AppleCommander.

`$java -jar AppleCommander-1.3.5.13-ac.jar -g [ImagedDisk.dsk] [SOS.DRIVER] [ExportedFilename]`

## Notes about other utilities:

There are many disk-manipulation utilities for modern computers that can work to export files from imaged Apple /// disks. AppleCommander is one. You can also use CiderPress.

## Contributions
You can make contributions to the script by either registering at Github and sending Pull Requests, or you can contact the authors on Twitter, @ultramagnus_tcv and @16kRam. We are most interested in updates to the internal dictionary of manufacturers. 

## Special Thanks
My continued appreciation goes to 16KRam and to the crew of the Drop III Inches Podcast.

## Links:
AppleCommander: (https://applecommander.github.io/)

Java: (https://www.java.com/en/download/)

CiderPress for Windows: (http://a2ciderpress.com/)

CiderPress for WINE (Linux and Mac OS X): (http://retrocomputingaustralia.com/rca-downloads/)

Drop III Inches Podcast (http://drop-iii-inches.com/)
