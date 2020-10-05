from huffman import HuffmanCoding
from noise import Noisy
from pathlib import Path
from scipy.stats import entropy
from entropy import calculateEntropy
from correction import encode_hamming, detect_error

path = "uncompressedFile"



# prints info of uncompressed file
print("*****file info***********:")
print("BEFORE COMPRESSION : File length = " + str(Path('uncompressedFile').stat().st_size))
print('BEFORE COMPRESSION : Entropy =' + str(calculateEntropy('uncompressedFile')))
print("***************************")

# compress file on path
h = HuffmanCoding(path)
output_path = h.compress()

print("***************************")

# prints info of compressed file
print("*** After compression ***")
print("AFTER COMPRESSION : File length : " + str(Path('1compressed.bin').stat().st_size))
print('AFTER COMPRESSION : Entropy  :' + str(calculateEntropy('1compressed.bin')))

print("***************************")

# encrypt file on path
print("encrypting")
encode_hamming('1compressed.bin')
print('encryption complete')
print("***************************")

# add noise on file
print("simulating noise")
#addnoise = Noisy('2encrypted.bin')
#addnoise.volume_it_up('2encrypted.bin')
print('noise added')
print("***************************")

# correction
#print('decrypting file with noise')
#detect_error('3noise.bin.bin')
print('decrypting file without noise')
detect_error('2encrypted.bin')

print("***************************")

# decompress
print("decompressing")
decompressed = h.decompress('4decrypted.bin')

print("*** file info after decompressing ***")
print("file length after decompression: " + str(Path('4decompressed.txt').stat().st_size))
print('Entropy of compressed file is :' + str(calculateEntropy('4decompressed.txt')))


# before and after length ,entropy ,test 2 times  calculate errors