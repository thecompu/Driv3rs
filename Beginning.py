import struct
import binascii
SOSfile = open('SOSCFFA.DRIVER', 'rb')
try:
        SOS = SOSfile.read()
finally:
        SOSfile.close()

SOSSlice = SOS.encode('hex_codec')[0x10:0x14]
print '0x' +  SOSSlice
SOSstruct = str(struct.pack('>2s', SOSSlice) [0])
print 'Packed: ' + SOSstruct
SOSunhexlify = binascii.unhexlify(SOSstruct)
print 'Unhexlified: ' + SOSunhexlify
