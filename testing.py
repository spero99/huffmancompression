import filecmp

from hammtest import hammingCodes, hammingCorrection

h = hammingCodes('uncompressedFile')

j = hammingCorrection('2encrypted.bin')

print(filecmp.cmp('uncompressedFile', '4decrypted.txt'))
