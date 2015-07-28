import struct
import binascii
SOSfile = open('SOSCFFA.DRIVER', 'rb')
try:
        SOS = SOSfile.read()
finally:
        SOSfile.close()

# encode file as hexadecimal
SOSHex = SOS.encode('hex_codec')
print SOSHex[0x10:0x14]
SOSstruct = struct.unpack('< f', SOS[0x10:0x14])
print SOSstruct
