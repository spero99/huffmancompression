# huffman compression,hamming encoding for error checking(linear)
Python script that compress a text file with huffman algorithm,encrypts it and then adds noise(simulate transfer over web),corrects the mistakes ,decrypts and decompress the file(not completed)

Papadas Alexandros P17095
Karanasios Stathis P17041

Simulation of noise : get the length of the file ,random number between 1-length gives us how many errors we get in the transport,then we get random postitions from 1-length (errorCount)times ,in every positions we add a random character 