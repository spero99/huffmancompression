import os
import random
import string
from pathlib import Path
import bitarray
import binascii


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


class Noisy:
    def __init__(self, path):
        self.path = path

    def volume_it_up(self, path):
        filename, file_extension = os.path.splitext(self.path)
        output = "file_withNoise" + ".txt"

        with open(self.path, 'r+')as file, open(output, 'wb') as output:
            file = file.read()
            file_length = Path(path).stat().st_size
            errorCounter = random.randint(1, file_length)
            print("while sending we got : " + str(errorCounter) + " errors")
            errors = random.sample(range(file_length), errorCounter)
            position = 0
            for byte in file:
                if position in errors:
                    random_byte = get_random_string(1)
                else:
                    random_byte = byte
                random_byte = random_byte.encode()
                output.write(random_byte)
                position += 1
        return errorCounter