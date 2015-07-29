import struct
import binascii
SOSfile = open('SOSCFFA.DRIVER', 'rb')
try:
        SOS = SOSfile.read()
finally:
        SOSfile.close()

# encode file as hexadecimal
SOSHex = SOS.encode('hex_codec')

#Search for 0x2205 byte pair
print 'Searching for first bytepair...'
SOSfindbyte = SOSHex.find('2205')
print 'I found it.'

#Reorder for Little Endian
MSB = SOSHex[SOSfindbyte+2:SOSfindbyte+4]
LSB = SOSHex[SOSfindbyte:SOSfindbyte+2]

print "In File: " + LSB, MSB + "\nLittle Endian: " + MSB, LSB
