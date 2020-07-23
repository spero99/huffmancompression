import os
import random
import bitarray

class Noisy:
    def __init__(self, path):
        self.path = path
        self.errorCounter = 0

    def volume_it_up(self, path):
        filename, file_extension = os.path.splitext(self.path)
        output = filename + "_withNoise" + ".bin"

        with open(self.path, 'r+')as file, open(output, 'wb') as output:
            file = file.read()
            for byte in file:
                random_byte = random.getrandbits(8)
                a = bytearray()
                a.extend(map(ord, str(random_byte)))
                b = bytearray()
                b.extend(map(ord, byte))
                noised_byte = a ^ b
                if noised_byte != byte:
                    self.errorCounter += 1
                output.write(noised_byte)
        return self.errorCounter