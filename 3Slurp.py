from struct import unpack
import os

def tup2int(offset):
    offset = unpack ('< H', SOS)
    return offset

#Clear SCREEN
print("\033c");

#Is File a SOS DRIVER file?

SOSfile = open('SOSCFFA.DRIVER', 'rb')
SOS = SOSfile.read(10)
filetype, offset = unpack('< 8s H', SOS)

if 'SOS DRVR' in filetype:
    print "This is a proper SOS file."
    print "Filetype is: %s. First offset is: %04x" % (filetype, offset)
else:
    print "This is not a proper SOS file"

#Seek to first driver
SOSfile.seek(offset,1)
SOS = SOSfile.read(2) # Read two bytes
marker = unpack('< H', SOS)
# if marker == \x0000 : #Saving for later...

SOSfile.close()
