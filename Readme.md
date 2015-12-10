#Driv3rs.py
###A script to help catalog SOS.DRIVER files.

##Usage:
`$python Driv3rs.py [SOS_DRIVER_FILE] [output_file.csv]`

##Description:

**Driv3rs.py** is a Python script written for Apple /// fans. The Apple /// was one of the first computers to introduce the concept of device drivers, small programs that allowed a user to interact with hardware on-board, internally installed, or attached to the computer externally. Over the course of the few years of the Apple ///'s existence, hardware manufacturers built devices and wrote device drivers to support those devices. However, the Apple /// simply didn't achieve as much prominence as the Apple II-series. Therefore, a lot of drivers remain either undiscovered or long-forgotten.

Driv3rs.py hopes to help that situation. Given an SOS.DRIVER file properly exported from an imaged Apple /// disk, Driv3rs.py can produce a Comma Separated Values (CSV) file. This CSV contains a whole host of information including device name, commentary, manufacturer, among many other potentially useful pieces of information.

When using an Apple ///, users would run a utility called the System Configuration Program (SCP) to install and uninstall drivers. Once the user chose all the needed drivers, the user would create a new bootable floppy disk. This disk contained the files necessary to boot Apple's Sophisticated Operating System (SOS) and the companion SOS.DRIVER file. From that driver file, all the needed drivers would load into memory upon boot.

Driv3rs.py works by opening the SOS.DRIVER file and then walks the Device Information Block (DIB) for every driver found within. The information gathered closely parallels the outlined DIB published in Apple's "Apple /// SOS Device Driver Writer's Guide." All information is eventually stored in the output CSV file.

##Requirements:

* Imaged Apple /// disk
* SOS.DRIVER files to be searched
* AppleCommander
* Java for AppleCommander (Java 6 if you want to use AppleCommander's GUI).

##Suggested Workflow:

1. Acquire an imaged Apple /// floppy disk.
2. Use AppleCommander's CLI functions to export the SOS.DRIVER file from the imaged disk. (See notes below on AppleCommander usage.)
3. Rename the exported SOS.DRIVER file to something that will clue you into where the SOS.DRIVER file came from.
4. Place the SOS.DRIVER file in same directory as Driv3rs.py.
5. Run the script according to the Usage section above.

Depending upon the name you chose for the output file, a CSV file will be generated with driver information found inside the SOS.DRIVER file.

(**Note:** If you choose the output name of a CSV file that already exists, Driv3rs.py will append the new SOS.DRIVER file's contents to the existing CSV file. This is handy if you're processing multiple SOS.DRIVER files.)

##Notes about AppleCommander:

AppleCommander is a utility written in Java for Apple II users. It allows manipulation of many different types of Apple II-based imaged floppy disks, including disks formatted in DOS 3.2, 3.3 and ProDOS. Apple's Sophisticated Operating System (SOS) is ProDOS's predecessor. Therefore, AppleCommander ProDOS features can be used to easily export files from SOS disks.

Because AppleCommander is written in Java, you must have Java on your workstation in order to use it. AppleCommander's command-line functions work fine in Java 8. However, AppleCommander's GUI requires the 32-bit version of Java 6 which is very old at this date and is vulnerable to security issues. In short, we recommended using AppleCommander's command-line features in Java 8 rather than installing Java 6.

Here's the suggested command-line to enter when exporting using AppleCommander.

`$java -jar AppleCommander-1.3.5.13-ac.jar -g [ImagedDisk.dsk] [SOS.DRIVER] [ExportedFilename]`

##Links:
AppleCommander: (http://applecommander.sourceforge.net/)

Java: (https://www.java.com/en/download/)
