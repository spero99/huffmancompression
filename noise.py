import os
import random

class Noisy:
    def __init__(self, path):
        self.path

    def volume_it_up(self):
        filename, file_extension = os.path.splitext(self.path)
        output = filename + "_withNoise" + ".bin"

        with open(self.path, 'r+')as file, open(output, 'wb') as output:
            file = file.read()
            for byte in file:
                random_byte = random.getrandbits(8)
                noised