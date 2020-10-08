from hammtest import encode, correct
from huffman import HuffmanCoding
from hamming import hamming_encode, hamming_correct
from noise import Noisy
from pathlib import Path
from scipy.stats import entropy
from entropy import calculateEntropy
from correction import encode_hamming, detect_error

path = "uncompressedFile"

h = HuffmanCoding(path)
output_path = h.compress()

#encode('1compressed.bin') #hammtest
#encode_hamming('1compressed.bin') #correction
hamming_encode('1compressed.bin')

#addnoise = Noisy('2encrypted.bin')
#addnoise.volume_it_up('2encrypted.bin')

#correct('2encrypted.bin')
#detect_error('2encrypted.bin')
hamming_correct('2encrypted.bin')

#detect_error('3noise.bin')

decompressed = h.decompress('4decrypted.bin')


print("*** file info  ***")
print("BEFORE COMPRESSION : File length = " + str(Path(path).stat().st_size))
print('BEFORE COMPRESSION : Entropy =' + str(calculateEntropy(path)))

print("AFTER COMPRESSION : File length : " + str(Path('1compressed.bin').stat().st_size))
print('AFTER COMPRESSION : Entropy  :' + str(calculateEntropy('1compressed.bin')))

print("AFTER ENCRYPTION : File length : " + str(Path('2encrypted.bin').stat().st_size))
print('AFTER ENCRYPTION : Entropy  :' + str(calculateEntropy('2encrypted.bin')))

print("AFTER DECRYPTION : File length : " + str(Path('4decrypted.bin').stat().st_size))
print('AFTER DECRYPTION : Entropy  :' + str(calculateEntropy('4decrypted.bin')))

print("AFTER DECOMPRESSION: File length :" + str(Path('5decompressed.txt').stat().st_size))
print('AFTER DECOMPRESSION: Entropy:' + str(calculateEntropy('5decompressed.txt')))
