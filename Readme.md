# Python-III-Git
A Python Script to open Apple III DSK files, export SOS.DRIVER, and catalog what drivers are installed.

Work History

8/1/2015 -- Approx.
Initial Commit

8/26/2015
Goals Defined:

1. Obtain the name of the .dsk image from the command-line (like: python my_script.py my_disk_image.dsk)

2. For each driver:
    a. File offset
    b. List the name of the driver
    c. Whether it's char or block device
    d. Manufacturer id
    e. Version number

	3. Print it all on one line in a file, delimited with commas

Example:

$ python sos.extract.py -disk "my_disk_image.dsk" -driver [SOS.DRIVER] -output [diskname.csv]

0530,FMT_D1,BLOCK,01,1.1

096e,FMT_D2,BLOCK,01,1.1

0990,FMT_D3,BLOCK,01,1.1

09B2,FMT_D4,BLOCK,01,1.1

0a00,SILENTYPE,CHAR,01,4.0c

0b00,DMP,CHAR,01,1.0

0c00,CONSOLE,CHAR,01,1.0

8/26/2015
Problems to solve (in no particular order):

1. How to write to a file.

2. How to seek to an offset. Can that be done in HEX?

3. How best to approach? Should we run through the file multiple times, marking names and offsets then returning to grab data? Or is one-time best?

4. Can anything be turned into functions?

9/7/2015

Completely removed the prompts as they were a pain during troubleshooting.

Attempted to create a function that will:
1. Take the 2-byte offset found in the file and unpack it then,
2. Convert the resultant tuple into an integer.

I am having trouble with the return portion. I don't really know how to do it. Will continue to play.

Implemented a (very) rudimentary IF/ELSE that checks the first eight bytes of the driver file to see if "SOS DRVR" exist. If not, the script ends. If so, we will continue. This entailed unpacking the data as string-data, converting the resultant tuple into an str, then checking what's there. I did verify via HEX edit that if the string is not "SOS DRVR," the else will be taken.

Is there a way to run the IF/ELSE against the contents of the tuple? It would save my having to convert from tuple to str. 
