from huffman import Compressing
from noise import Noisy
from pathlib import Path
from scipy.stats import entropy
from entropy import calculateEntropy
from correction import encode_hamming, detect_error

path = "uncompressedFile"


# prints info of uncompressed file
print("file length before compression")
print(Path('uncompressedFile').stat().st_size)
print('Entropy of uncompressed file is :' + str(calculateEntropy('uncompressedFile')))

# compress file on path
h = Compressing(path)
output_path = h.compress()

# prints info of compressed file
print("file length after compression")
print(Path('uncompressedFile.bin').stat().st_size)
print('Entropy of compressed file is :' + str(calculateEntropy('uncompressedFile.bin')))


# encrypt file on path
encode_hamming('uncompressedFile.bin')
# add noise on file
Noisy.volume_it_up('uncompressedFile_ham_enc.txt')

# correct
detect_error('file_withNoise.txt')
# decompress
h.decompress('ham_enc_fix.txt')



# before and after length ,entropy ,test 2 times  calculate errors