from huffman import Compressing
from noise import Noisy
from pathlib import Path

path = "uncompressedFile"


# prints string size of uncompressed file
print("file length before compression")
print(Path('uncompressedFile').stat().st_size)

h = Compressing(path)

# compress file on path
output_path = h.compress()

# prints string size of compressed file
print("file length after compression")
print(Path('uncompressedFile.bin').stat().st_size)



# encrypt file on path
#encoded_path = " "
# add noise on file
#Noisy.volume_it_up(encoded_path)
# decrypt

# decompress

# correct

h.decompress(output_path)



# before and after length ,entropy ,test 2 times  calculate errors