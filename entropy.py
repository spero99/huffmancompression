import os
import sys
import math

from Tools.scripts.objgraph import ignore


def calculateEntropy(path):
    filename, file_extension = os.path.splitext(path)

    with open(path, 'rb',) as file:

        binary_data = file.read()
        file.close()
        fileSize = len(list(binary_data))


    # calculate the frequency of each byte value in the file
    freqList = []
    for b in range(256):
        ctr = 0
        for byte in binary_data:
            if byte == b:
                ctr += 1
        freqList.append(float(ctr) / fileSize)


    # Shannon entropy
    ent = 0.0
    for freq in freqList:
        if freq > 0:
            ent = ent + freq * math.log(freq, 2)
    ent = -ent
    return ent
