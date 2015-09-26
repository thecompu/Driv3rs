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

(edit: Yes, there is. if element in tuple)

I played further with the function. I am still not able to get it to work, but I am feeling a little more comfortable with the idea.

9/12/2015

After reading little pieces about functions throughout the week and playing with tutorials, I have a function that will take a number of bytes as an argument, read those bytes, unpack into little-endian as hexadecimal, then return the resultant tuple as an integer. Right now, this function only handles two bytes which is what we need for the jumps. Later, I'll try to figure out what to do for strings which requires a different unpack procedure. It may work better as its own function or part of the same. I don't know.

The function is called inside a while loop that indefinitely executes until the encountered two-byte value is FFFF.

It's working... more or less.

9/26/2015

Life sucks. Fucking anxiety. Fucking depression.

Anyway, I cleaned up a lot of the code and I also implemented a counter for the number of drivers encountered.

Later, I implemented creating nested dictionaries based upon how many drivers were encountered. I don't know if this type of creation will work as I go back through the drivers to get information on the drivers themselves, but I think it's a good start.

Current sample run:

IN: python 3Slurp.py
OUT: This is a proper SOS file.
Filetype is: SOS DRVR.
The first offset value is 0x522
Total drivers encountered:  4
{'Driver_3': {'Offset': '0x2ea'}, 'Driver_2': {'Offset': '0xeac'}, 'Driver_1': {'Offset': '0x4a4'}, 'Driver_4': {'Offset': '0xf86'}}

I'll want to wind up with something like this (formatted for easier reading)

{
  'Driver_1' :
  {
    'Offset' : '0x4a4',
    'Name' : 'CONSOLE',
    etc...
  }
}
