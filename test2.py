from huffman import HuffmanCoding
from correction import encode_hamming, detect_error
from hammtest import hammingCodes, hammingCorrection
import sys

print('encrypting')
encode_hamming('uncompressedFile')
print('decrypting')
detect_error('2encrypted.bin')




