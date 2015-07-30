from struct import unpack
import os

#Clear SCREEN
print("\033c");

# Ask for the DSK filename then open it
dskname = raw_input("Welcome to the Apple /// SOS.Driver.Slurper.\nAppleCommander _must_ exist in the same directory as this script.\n\nYou must have JAVA on your system. \n\nEnter CaSe-SeNsItIvE DSK filename: ")
if len(dskname) < 1 :
    print '\nSorry, you must enter a disk name.'
    exit()
else:
    try:
        dskopen = open(dskname) #Checks to see if DSK exists.
        sosdrivername = raw_input('\nEnter the name of the SOS driver file you wish exported [SOS.DRIVER]: ')
        if len(sosdrivername) < 1 :
            sosdrivername = 'SOS.DRIVER'
            print "DEBUG: Taking the default IF. sosdrivername is: " + sosdrivername
            os.popen("java -jar AppleCommander-1.3.5.13-ac.jar -g %s %s >%s.SOS.DRIVER" % (dskname, sosdrivername,dskname))
        else:
            print 'DEBUG: Taking the else...'
            os.popen("java -jar AppleCommander-1.3.5.13-ac.jar -g %s %s >%s.SOS.DRIVER" % (dskname, sosdrivername,dskname))
    except:
        print '\n\nI cannot find that disk file. Check path and/or name.\n\n'
        exit()
#Is File a SOS DRIVER file?
SOSfile = open('SOSCFFA.DRIVER', 'rb')
SOS = SOSfile.read(10)
filetype, offset = unpack('< 8s H', SOS)
print "Filetype is: %s. Offset is: %04x" % (filetype, offset)

#Seek to first driver
SOSfile.seek(offset,1)
SOS = SOSfile.read(2) # Read two bytes
marker = unpack('< H', SOS)
# if marker == \x0000 : #Saving for later...

SOSfile.close()
