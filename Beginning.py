import struct
import binascii
SOSfile = open('SOSCFFA.DRIVER', 'rb')
try:
        SOS = SOSfile.read()
finally:
        SOSfile.close()

#Slice two bytes
SOSSlice = SOS[0x10:0x11]
SOSstruct = struct.unpack('< H', SOSSlice[0])
