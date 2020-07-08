import huffman

path = ""
calling = huffman(path)

output_path = calling.compress()


calling.decompress(output_path)