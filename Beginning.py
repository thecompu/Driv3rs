from struct import unpack

#Is File a SOS DRIVER file?
SOSfile = open('SOSCFFA.DRIVER', 'rb')
SOS = SOSfile.read(10)
filetype, offset = unpack('< 8s H', SOS)
print "Filetype is: %s. Offset is: %04x" % (filetype, offset)

#Seek to first driver
SOSfile.seek(offset,1)
SOS = SOSfile.read(2) # Read two bytes
marker = unpack('< H', SOS)
if marker == \x0000 :

SOSfile.close()
