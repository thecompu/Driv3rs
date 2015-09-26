from struct import unpack
import os

def readUnpackAndint(bytes):
    SOS = SOSfile.read(bytes)
    offset_unpacked = unpack ('< H', SOS)
    return int('.'.join(str(x) for x in offset_unpacked))

#Clear SCREEN
print("\033c");

#Is File a SOS DRIVER file?

SOSfile = open('SOSCFFA.DRIVER', 'rb')
SOS = SOSfile.read(8)
filetype = unpack('< 8s', SOS)

if 'SOS DRVR' in filetype:
    print "This is a proper SOS file."
    print "Filetype is: %s." % (filetype)
else:
    print "This is not a proper SOS file"


### At this point, we need the first offset to tell us where to jump to
### find the first actual driver.

# Read immediate two bytes after SOS DRVR to establish first offset value.
offset = readUnpackAndint(2)
print "The first offset value is", hex(offset)
drivers = 0 ## This is to keep a running total of drivers.
drivers_dict = dict() ## Intialize a dictionary to hold the drivers.

### Begin an indefinite loop that will come around until we
### encounter FF which indicates the last driver.

while offset != 65535 :
    SOSfile.seek(offset,1)
    ## print "DEBUG: This is our new position in the file: ", hex(SOSfile.tell())
    offset = readUnpackAndint(2)
    if offset == 0 : ## Check to see if we're at the beginning of a new driver.
        drivers = drivers + 1  ## And add to count of found drivers.
        offset = readUnpackAndint(2)
        drivers_dict ['Driver_'+str(drivers)] = dict([('Offset', hex(offset))])
##    print 'DEBUG: New offset is: ' , hex(offset)

SOSfile.close()
print 'Total drivers encountered: ', drivers
print drivers_dict
