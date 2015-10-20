from struct import unpack
import os

def readUnpack(bytes, **options):
    if options.get("type") == 't':
        #print 'DEBUG: In t'
        SOS = SOSfile.read(bytes)
        text_unpacked = unpack('%ss' % bytes, SOS)
        return ''.join(text_unpacked)

    if options.get("type") == 'b':
        #print 'DEBUG: In b', bytes
        SOS = SOSfile.read(bytes)
        #print 'DEBUG: In b2', bytes, SOS
        offset_unpacked = unpack ('< H', SOS)
        #print 'DEBUG: In b3', bytes, SOS
        return int('.'.join(str(x) for x in offset_unpacked))

#Clear SCREEN
print("\033c");

#Is File a SOS DRIVER file?

SOSfile = open('SOSCFFA.DRIVER', 'rb')
filetype = readUnpack(8, type = 't')

if filetype == 'SOS DRVR':
    print "This is a proper SOS file."
    print "Filetype is: %s." % (filetype)
else:
    print "Filetype is: %s." % (filetype)
    print "This is not a proper SOS file"
    exit()

### At this point, we need the first offset to tell us where to jump to
### find the first actual driver.

# Read immediate two bytes after SOS DRVR to establish first rel_offset value.
rel_offset = readUnpack(2, type = 'b')
print "The first relative offset value is", rel_offset, hex(rel_offset)
print SOSfile.tell()
drivers = 0     ## This is to keep a running total of drivers.
drivers_list=[] ## Initialize a list to hold dictionaries.

### Begin an indefinite loop that will come around until we
### find all major drivers. FFFF means end of drivers.

loop = True
while loop :         ## as long as no FF FF are encountered
    driver = {}     ## Intialize a dictionary to hold vaules as we loop.
    SOSfile.seek(rel_offset,1)    ## jump to next location. a + 522 = 52c
    driver['location'] = SOSfile.tell() ## add to driver dictionary 52c
    rel_offset = readUnpack(2, type = 'b') ## 0000 comment length
    if rel_offset == 0xFFFF:
        loop = False
    else :
        drivers_list.append(driver) ## add to drivers_list list
        SOSfile.seek(rel_offset,1) ## 52e + 0000 = 52e
        rel_offset = readUnpack(2, type = 'b') # result: 4a4 pos: 530
        SOSfile.seek(rel_offset,1) # 530 + 4a4 = 9d4
        rel_offset = readUnpack(2, type = 'b') # be


#Loop to enter each driver to grab information from the DIB (Driver Information Block)

for i in range(0,len(drivers_list)):
    # print drivers_list[i], hex(drivers_list[i]['location'])
    SOSfile.seek(drivers_list[i]['location'],0)
    rel_offset = readUnpack(2, type = 'b') # will get comment length 0000
    drivers_list[i]['comment_len'] = rel_offset #store comment length
    if rel_offset != 0: #if comment length is not 0000
        comment_len = rel_offset # place length in comment_len var
        comment_txt = readUnpack(comment_len, type = 't') # comment_len bytes as text
        drivers_list[i]['comment_txt'] = comment_txt # place comment in dictionary
    else:
        drivers_list[i]['comment_txt'] = ''    # else enter comment as nothing
    SOSfile.seek(rel_offset,1) # go to link field
    lnk_pointer = readUnpack(2, type = 'b') # Grab distance to next DIB.
    SOSfile.seek(2,1) # Skip Entry field

print drivers_list

SOSfile.close()
