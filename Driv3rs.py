from struct import unpack; from sys import argv

args = argv
usage = "\nUsage: python Driv3rs.py [input_file] [output_file]\n"

if len(args) < 3:
    print usage
    exit()
disk_img = args[1]
output_file = args[2]

def readUnpack(bytes, **options):
    if options.get("type") == 't':
        SOS = SOSfile.read(bytes)
        text_unpacked = unpack('%ss' % bytes, SOS)
        return ''.join(text_unpacked)

    if options.get("type") == 'b':
        SOS = SOSfile.read(bytes)
        offset_unpacked = unpack ('< H', SOS)
        return int('.'.join(str(x) for x in offset_unpacked))

    if options.get("type") == '1':
        SOS = SOSfile.read(bytes)
        offset_unpacked = unpack ('< B', SOS)
        return int(ord(SOS))

def nibblize(byte, **options):
    if options.get("direction") == 'high':
        return str(int(hex(byte >> 4), 0))
    if options.get("direction") == 'low':
        return str(int(hex(byte & 0x0F), 0))


dev_types ={273: 'Character Device, Write-Only, Formatter',
            321: 'Character Device, Write-Only, RS232 Printer',         # dictionary for types and subtypes
            577: 'Character Device, Write-Only, Silentype',
            833: 'Character Device, Write-Only, Parallel Printer',
            323: 'Character Device, Write-Only, Sound Port',
            353: 'Character Device, Read-Write, System Console',
            354: 'Character Device, Read-Write, Graphics Screen',
            355: 'Character Device, Read-Write, Onboard RS232',
            356: 'Character Device, Read-Write, Parallel Card',
            481: 'Block Device, Disk ///',
            721: 'Block Device, PROFile',
            4337: 'Block Device, CFFA3000'}

mfgs =     {17491: 'David Schmidt'}                                     # dictionary for manufacturers

SOSfile = open(disk_img, 'rb')                                  # open file to interrogate
filetype = readUnpack(8, type = 't')                                    # read first eight bytes and stick returned text into filetype

if filetype == 'SOS DRVR':                                              # is filetype 'SOS DRVR'??
    print "This is a proper SOS.DRIVER file."                           # output, this is a proper file
    print "Filetype is: %s." % (filetype)                               # output filetype found.
else:                                                                   # otherwise....
    print "Filetype is: %s." % (filetype)                               # output what was found
    print "This is not a proper SOS.DRIVER file"                        # ouput, this is not a proper SOS file
    exit()                                                              # nothing to be done, exit script


rel_offset = readUnpack(2, type = 'b')                                  # read two bytes after SOS DRVR to establish first rel_offset value
print "The first relative offset value is", rel_offset, hex(rel_offset) # print out for debug
drivers = 0                                                             # this is to keep a running total of drivers.
drivers_list=[]                                                         # initialize a list to hold dictionaries.

loop = True                                                             # set True for major driver loop
while loop :                                                            # establish loop to find major drivers
    driver = {}                                                         # initialize a dictionary to hold each major driver
    SOSfile.seek(rel_offset,1)                                          # jump past comment
    atell = SOSfile.tell()
    driver['comment_start'] = SOSfile.tell()                           # add new driver location to driver dictionary
    rel_offset = readUnpack(2, type = 'b')                              # grab next two bytes to set up jump and to see if we're at the end of drivers
    atell = SOSfile.tell()
    if rel_offset == 0xFFFF:                                            # if we encounter FFFF, no more drivers and
        loop = False                                                    # set loop to False; no more drivers
    else :                                                              # otherwise....
        drivers_list.append(driver)                                     # append a new list entry
        SOSfile.seek(rel_offset,1)                                      # jump (1 of 2) distance found in previous 2 bytes read
        atell = SOSfile.tell()
        rel_offset = readUnpack(2, type = 'b')                          # read 2 bytes to set up next jump
        atell = SOSfile.tell()
        SOSfile.seek(rel_offset,1)                                      # jump (2 of 2) distance found in previous two bytes
        atell = SOSfile.tell()
        rel_offset = readUnpack(2, type = 'b')                          # we're now at the comment_len of a new major driver; read two bytes for length
        atell = SOSfile.tell()

for i in range(0,len(drivers_list)):                                    # begin loop to grab information from DIB
    SOSfile.seek(drivers_list[i]['comment_start'],0)                    # reference SOF and seek to beginning of major driver
    comment_len = readUnpack(2, type = 'b')                             # grab comment length (2 bytes)
    drivers_list[i]['comment_len'] = comment_len                        # store comment length
    if comment_len != 0x0000:                                           # if comment length is not 0000
        comment_txt = readUnpack(comment_len, type = 't')               # comment_len bytes as text
        drivers_list[i]['comment_txt'] = comment_txt                    # place comment in dictionary
    else:                                                               # otherwise...
        drivers_list[i]['comment_txt'] = 'None'                         # else enter comment as nothing
    SOSfile.seek(2,1)                                                   # skip two bytes immediately following comment or 0000
    drivers_list[i]['dib_start'] = SOSfile.tell()
    link_ptr = readUnpack(2, type = 'b')                                # grab link pointer
    drivers_list[i]['link_ptr'] = link_ptr                              # store link pointer
    entry = readUnpack(2, type = 'b')                                   # grab entry field
    drivers_list[i]['entry'] = entry                                    # store entry field
    name_len = readUnpack(1, type = '1')                                # grab one byte for name length
    drivers_list[i]['name_len'] = name_len                              # store name length
    name = readUnpack(name_len, type = 't')                             # read name based on length
    drivers_list[i]['name'] = name                                      # store name
    SOSfile.seek(15 - name_len,1)                                       # skip past remainder of 15-byte long name field
    flag = readUnpack(1, type = '1')                                    # grab Flag byte
    if flag == 192:                                                     # is flag 0xc0?
        drivers_list[i]['flag'] = 'ACTIVE, Load on Boundary'            # yes, ACTIVE and load on boundary
    elif flag == 128:                                                   # is flag 0x80?
        drivers_list[i]['flag'] = 'ACTIVE'                              # insert Flag into dictionary with value ACTIVE
    else:                                                               # otherwise...
        drivers_list[i]['flag'] = 'INACTIVE'                            # insert Flag into dictionary with value INACTIVE
    slot_num = readUnpack(1, type = '1')                                # grab slot number
    if slot_num == 0:                                                   # check if device has no slot number...
        drivers_list[i]['slot_num'] = 'None'                            # ... and indicate so.
    else:                                                               # otherwise...
        drivers_list[i]['slot_num'] = slot_num                          # ... enter slot number into the dictionary
    unit = readUnpack(1, type = '1')                                    # get the unit byte
    drivers_list[i]['unit'] = unit                                      # store unit in dictionary
    dev_type = readUnpack(2, type ='b')
    try:
        drivers_list[i]['dev_type'] = dev_types[dev_type]               # insert device type into dictionary
    except:
        drivers_list[i]['dev_type'] = 'Unknown'
    SOSfile.seek(1,1)
    block_num = readUnpack(2, type = 'b')                               # get block_num
    if block_num != 0:                                                  # is block_num not zero?
        drivers_list[i]['block_num'] = block_num                        # yes, store retrieved block_num value
    else:                                                               # otherwise...
        drivers_list[i]['block_num'] = 'Character Device or Undefined'  # log field as char device or undefined
    mfg = readUnpack(2, type = 'b')                                     # read mfg bytes
    try:
        drivers_list[i]['mfg'] = mfgs[mfg]                              # try to match key and place in dictionary
    except:
        if 1 <= mfg <= 31:                                              # if exception, check if mfg is between 1 and 31
            drivers_list[i]['mfg'] = 'Apple Computer'                   # yes, this is Apple Computer
        else:
            drivers_list[i]['mfg'] = 'Unknown'                          # no, this is unknown. log as such
    ver_byte0 = readUnpack(1, type = '1')                               # start version field -- grab the V/v0 numbers | V = high-nibble, v0 = low-nibble
    ver_byte1 = readUnpack(1, type = '1')                               # grab the v1/Q numbers | v1 = high-nibble, Q = low-nibble
    V   = nibblize(ver_byte1, direction = 'high')                       # grab major version number as string
    v0  = nibblize(ver_byte1, direction = 'low')                        # grab first minor version number (v0) as string
    v1  = nibblize(ver_byte0, direction = 'high')                       # grab second minor version number (v1) as string
    Q   = nibblize(ver_byte0, direction = 'low')                        # grab qualifier number. We only care about A (Alpha), B (Beta), or E (Experimental)
    drivers_list[i]['version'] = V + '.' + v0 + v1 + Q                  # put version number into dictionary

for i in range(0,len(drivers_list)):                                    # begin search for how many devices a driver can support
    link_ptr = drivers_list[i]['link_ptr']                              # grab link_ptr in dictionary
    if link_ptr != 0x0000:                                              # is link_ptr not 0x0000?
        total_devs = 1                                                  # initialize devices count (initially 1)
        SOSfile.seek(drivers_list[i]['dib_start'],0)                    # seek to beginning of major driver from start of file
        SOSfile.seek(drivers_list[i]['link_ptr'],1)                     # seek to beginning of sub-DIB
        sub_loop = True                                                 # setup loop to run through sub-drivers
        while sub_loop:                                                 # begin loop to move only through sub-
            sub_link = readUnpack(2, type = 'b')                        # read link field of sub-driver
            if sub_link != 0x0000:                                      # if link field is not zero...
                total_devs = total_devs + 1                             # increment sub_drivers count
                SOSfile.seek(32,1)                                      # seek to next sub-DIB ($22 bytes minus link field)
            else:                                                       # else...
                sub_loop = False                                        # set inner loop to false                                               # set sub-driver loop to false
        drivers_list[i]['num_devices'] = total_devs                     # place total number in dictionary

print drivers_list[4]
SOSfile.close()
