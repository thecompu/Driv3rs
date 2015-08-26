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