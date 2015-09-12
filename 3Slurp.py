from struct import unpack
import os

def tup2int(tup):
    return int('.' . join(str(x) for x in tup))

def tup2int():
    SOS = SOSfile.read(2)
    offset_unpacked = unpack ('< H', SOS)
    offset = int('.'.join(str(x) for x in offset_unpacked))
    print 'DEBUG: Inside function. Offset is:', hex(offset)
    return offset

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

def readUnpackAndint(bytes):
    SOS = SOSfile.read(bytes)
    offset_unpacked = unpack ('< H', SOS)
    return int('.'.join(str(x) for x in offset_unpacked))

### At this point, we need the first offset to tell us where to jump to
### find the first actual driver.

# Read immediate two bytes after SOS DRVR to establish first offset value.
offset = readUnpackAndint(2)
print "The first offset value is", hex(offset)

### Now we have the offset needed to jump to the first driver. Let's seek
### to that driver using the offset. This is our first jump.

SOSfile.seek(offset,1)
print "This is our new position in the file: ", hex(SOSfile.tell())
offset = readUnpackAndint(2)
print 'New offset is: ' , hex(offset)

### I will establish an indefinite loop that will come around until we
### encounter FF which indicates the last driver. For now, I am manually
### looping to check logic.

while offset != 65535 :
    SOSfile.seek(offset,1)
    print "This is our new position in the file: ", hex(SOSfile.tell())
    offset = readUnpackAndint(2)
    print 'New offset is: ' , hex(offset)

SOSfile.close()
