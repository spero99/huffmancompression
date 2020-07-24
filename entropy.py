import os
import sys
import math





def calculateEntropy(path):
    filename, file_extension = os.path.splitext(path)

    with open(path, 'r+') as file:
        byteArr = map(ord, file.read())
        file.close()
        fileSize = len(byteArr)
        print ('File size in bytes:')
        print (fileSize)


    # calculate the frequency of each byte value in the file
    freqList = []
    for b in range(256):
        ctr = 0
        for byte in byteArr:
            if byte == b:
                ctr += 1
        freqList.append(float(ctr) / fileSize)
    # print 'Frequencies of each byte-character:'
    # print freqList
    # print

    # Shannon entropy
    ent = 0.0
    for freq in freqList:
        if freq > 0:
            ent = ent + freq * math.log(freq, 2)
    ent = -ent
    print ('Shannon entropy (min bits per byte-character):')
    print (ent)
    return ent